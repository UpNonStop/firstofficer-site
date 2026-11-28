#!/usr/bin/env python3
"""Fixtures for tools/check_rules.py. Run from the repo root:

    python3 tools/test_check_rules.py

Each test builds a tiny site in a temp folder and proves the check sees one thing:
a pass, each kind of fail, a known gap, a stale gap, and the three ways it cannot see.
"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_rules  # noqa: E402

FOOT = "Every owner shown is a fictional example. An educational tool, not a licensed financial advisor."
REG = {
    "banned_claims": [
        {"pattern": "completely separated", "why": "database rules, not infrastructure separation"},
        {"id": "outcome", "pattern": r"(?<!no )\bguaranteed savings", "why": "no promised outcome"},
    ],
    "known_gaps": [],
    "site_hosts_allowed": ["example.supabase.co"],
    "required_lines": [{"text": FOOT, "why": "the footer disclaimer"}],
    "not_content_pages": [{"file": "app.html", "why": "the app's shell"}],
}


def page(body, head=""):
    return f"<!doctype html><html><head><title>T</title>{head}</head><body>{body}<footer>{FOOT}</footer></body></html>"


class Site:
    def __init__(self, pages, reg=None, scripts=None, raw_registry=None):
        self.dir = tempfile.TemporaryDirectory()
        root = self.dir.name
        os.makedirs(os.path.join(root, "legal"))
        if raw_registry is not None:
            with open(os.path.join(root, "legal", "promises.json"), "w", encoding="utf-8") as f:
                f.write(raw_registry)
        elif reg is not False:
            with open(os.path.join(root, "legal", "promises.json"), "w", encoding="utf-8") as f:
                json.dump(reg or REG, f)
        for name, text in pages.items():
            full = os.path.join(root, name)
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "w", encoding="utf-8") as f:
                f.write(text)
        for name, text in (scripts or {}).items():
            os.makedirs(os.path.join(root, "assets"), exist_ok=True)
            with open(os.path.join(root, "assets", name), "w", encoding="utf-8") as f:
                f.write(text)
        self.root = root

    def run(self):
        return check_rules.main(["--root", self.root, "--quiet"])

    def fails(self):
        return check_rules.check(self.root)[0]


class TheCheck(unittest.TestCase):
    def test_a_clean_site_passes(self):
        self.assertEqual(Site({"index.html": page("<p>Estimates, never a promise.</p>")}).run(), check_rules.PASS)

    def test_a_banned_claim_fails(self):
        s = Site({"index.html": page("<p>Your data is completely separated.</p>")})
        self.assertEqual(s.run(), check_rules.FAIL)
        self.assertIn("banned claim", s.fails()[0])

    def test_a_banned_claim_in_a_meta_description_fails(self):
        s = Site({"index.html": page("<p>Fine.</p>", '<meta name="description" content="Guaranteed savings for owners">')})
        self.assertEqual(s.run(), check_rules.FAIL)

    def test_saying_it_is_not_guaranteed_passes(self):
        self.assertEqual(Site({"index.html": page("<p>No guaranteed savings.</p>")}).run(), check_rules.PASS)

    def test_a_known_gap_is_reported_and_does_not_fail(self):
        reg = dict(REG, known_gaps=[{"file": "terms.html", "pattern": "completely separated", "until": "the next Terms version", "why": "x"}])
        s = Site({"terms.html": page("<p>Completely separated at the infrastructure level.</p>")}, reg)
        fails, gaps, _ = check_rules.check(s.root)
        self.assertEqual((len(fails), len(gaps)), (0, 1))
        self.assertEqual(s.run(), check_rules.PASS)

    def test_a_known_gap_by_id(self):
        reg = dict(REG, known_gaps=[{"file": "old.html", "id": "outcome", "until": "it is rewritten", "why": "x"}])
        self.assertEqual(Site({"old.html": page("<p>Guaranteed savings.</p>")}, reg).run(), check_rules.PASS)

    def test_a_known_gap_covers_only_its_own_page(self):
        reg = dict(REG, known_gaps=[{"file": "terms.html", "pattern": "completely separated", "until": "later", "why": "x"}])
        s = Site({"terms.html": page("<p>Completely separated.</p>"), "index.html": page("<p>Completely separated.</p>")}, reg)
        self.assertEqual(s.run(), check_rules.FAIL)

    def test_a_stale_known_gap_fails(self):
        reg = dict(REG, known_gaps=[{"file": "terms.html", "pattern": "completely separated", "until": "later", "why": "x"}])
        s = Site({"terms.html": page("<p>Database rules keep clients apart.</p>")}, reg)
        self.assertEqual(s.run(), check_rules.FAIL)
        self.assertIn("stale known gap", s.fails()[0])

    def test_a_missing_required_line_fails(self):
        s = Site({"index.html": "<html><head><title>T</title></head><body><p>No footer here.</p></body></html>"})
        self.assertEqual(s.run(), check_rules.FAIL)
        self.assertIn("required line missing", s.fails()[0])

    def test_a_redirect_stub_and_a_listed_shell_need_no_footer(self):
        stub = '<html><head><meta http-equiv="refresh" content="0; url=index.html"></head><body>Moved</body></html>'
        shell = "<html><head><title>App</title></head><body><div id=app></div></body></html>"
        self.assertEqual(Site({"index.html": page("<p>Ok.</p>"), "old.html": stub, "app.html": shell}).run(), check_rules.PASS)

    def test_the_legal_archive_is_never_checked(self):
        s = Site({"index.html": page("<p>Ok.</p>"), "legal/terms/2026-01-01.html": "<p>Completely separated — guaranteed savings!</p>"})
        self.assertEqual(s.run(), check_rules.PASS)

    def test_a_dash_glyph_fails_even_in_alt_text(self):
        s = Site({"index.html": page('<img src="/a.png" alt="Earn – burn">')})
        self.assertEqual(s.run(), check_rules.FAIL)
        self.assertIn("dash glyph", s.fails()[0])

    def test_an_exclamation_point_fails(self):
        self.assertEqual(Site({"index.html": page("<p>Welcome aboard!</p>")}).run(), check_rules.FAIL)

    def test_an_exclamation_point_inside_a_script_is_code_not_copy(self):
        self.assertEqual(Site({"index.html": page("<script>if(a!==b){x=!y}</script><p>Ok.</p>")}).run(), check_rules.PASS)

    def test_an_outside_script_host_fails(self):
        s = Site({"index.html": page('<script src="https://cdn.tracker.example/t.js"></script>')})
        self.assertEqual(s.run(), check_rules.FAIL)
        self.assertIn("outside host", s.fails()[0])

    def test_an_allowed_host_and_a_plain_link_out_pass(self):
        body = '<script src="https://example.supabase.co/x.js"></script><a href="https://wa.me/15551234567">Message</a>'
        self.assertEqual(Site({"index.html": page(body)}).run(), check_rules.PASS)

    def test_a_fetch_to_an_outside_host_in_a_script_file_fails(self):
        s = Site({"index.html": page("<p>Ok.</p>")}, scripts={"send.js": "fetch('https://collector.example/in', {method:'POST'})"})
        self.assertEqual(s.run(), check_rules.FAIL)

    def test_no_registry_is_cannot_see(self):
        self.assertEqual(Site({"index.html": page("<p>Ok.</p>")}, reg=False).run(), check_rules.CANNOT_SEE)

    def test_a_broken_registry_is_cannot_see(self):
        self.assertEqual(Site({"index.html": page("<p>Ok.</p>")}, raw_registry="{not json").run(), check_rules.CANNOT_SEE)

    def test_a_pattern_that_does_not_compile_is_cannot_see(self):
        reg = dict(REG, banned_claims=[{"pattern": "(unclosed", "why": "x"}])
        self.assertEqual(Site({"index.html": page("<p>Ok.</p>")}, reg).run(), check_rules.CANNOT_SEE)

    def test_no_pages_is_cannot_see(self):
        self.assertEqual(Site({}).run(), check_rules.CANNOT_SEE)


if __name__ == "__main__":
    unittest.main(verbosity=1)
