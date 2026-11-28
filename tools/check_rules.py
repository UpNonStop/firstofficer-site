#!/usr/bin/env python3
"""The site's rule check: every page, held to the promise registry.

Run from the repo root:

    python3 tools/check_rules.py            # check this checkout
    python3 tools/check_rules.py --quiet    # failures and the verdict only
    python3 tools/check_rules.py --root DIR # check another checkout

It reads legal/promises.json and checks every page a reader can open:

  1. banned_claims    no page says what the registry bans
  2. required_lines   every content page carries the lines the registry requires
  3. glyphs           no em dash, en dash or horizontal bar anywhere a reader or a crawler reads
  4. exclamation      no exclamation point in copy
  5. hosts            nothing loads from or posts to a host that is not in site_hosts_allowed

Three outcomes, never two:

  exit 0  PASS        every rule was checked and held
  exit 1  FAIL        a page breaks a rule
  exit 2  CANNOT SEE  the registry or the pages could not be read. That is not a pass.

A known gap (known_gaps in the registry) is printed on every run and does not fail,
until its "until" is met and the entry is removed. A known gap that no longer matches
anything is stale and fails, so the list cannot rot.

What a reader can read: the visible text, and also the title, the meta descriptions,
alt text, aria labels, placeholders and structured data. The legal archive under
legal/ is what was published on its date and is never checked or changed.
"""
import argparse
import html
import json
import os
import re
import sys

PASS, FAIL, CANNOT_SEE = 0, 1, 2
GLYPHS = "—–―"  # em dash, en dash, horizontal bar
LOADS = re.compile(
    r"""<(script|iframe|img|link|form|source|video|audio|embed|object)\b[^>]*?\b(?:src|href|action|data)\s*=\s*["'](?:https?:)?//([^/"'\s>]+)""",
    re.I)
LINK_LOADS = re.compile(r"""rel\s*=\s*["']?[^"'>]*\b(?:stylesheet|preload|modulepreload|preconnect|dns-prefetch|icon|manifest)\b""", re.I)
CALLS = re.compile(
    r"""(?:\bfetch\s*\(|\bsendBeacon\s*\(|\.open\s*\(\s*["'](?:GET|POST|PUT|PATCH|DELETE)["']\s*,|\.src\s*=|\bimport\s*\(|\bnew\s+(?:WebSocket|EventSource)\s*\()\s*["'`]https?://([^/"'`\s?#]+)""")


class CannotSee(Exception):
    pass


def readable(raw):
    """Everything in a page that a reader or a crawler reads, as one string."""
    parts = []
    for m in re.finditer(r'(?is)<script[^>]*type\s*=\s*["\']application/ld\+json["\'][^>]*>(.*?)</script>', raw):
        parts.append(m.group(1))
    for m in re.finditer(r'(?is)<meta\b[^>]*\bcontent\s*=\s*"([^"]*)"', raw):
        parts.append(m.group(1))
    for m in re.finditer(r'(?is)\b(?:alt|title|aria-label|placeholder)\s*=\s*"([^"]*)"', raw):
        parts.append(m.group(1))
    body = re.sub(r"(?is)<(script|style|noscript|template)\b.*?</\1>", " ", raw)
    body = re.sub(r"(?s)<!--.*?-->", " ", body)
    body = re.sub(r"(?s)<[^>]+>", " ", body)
    parts.append(body)
    return re.sub(r"\s+", " ", html.unescape("   ".join(parts)))


def is_redirect_stub(raw):
    return re.search(r"""http-equiv\s*=\s*["']?refresh""", raw, re.I) is not None


def around(text, start, end, pad=50):
    return text[max(0, start - pad):end + pad].replace(" ", "|").strip()


def load(root):
    reg_path = os.path.join(root, "legal", "promises.json")
    try:
        with open(reg_path, encoding="utf-8") as f:
            reg = json.load(f)
    except (OSError, ValueError) as e:
        raise CannotSee(f"legal/promises.json could not be read: {e}")
    for key in ("banned_claims", "known_gaps", "site_hosts_allowed"):
        if not isinstance(reg.get(key), list):
            raise CannotSee(f"legal/promises.json has no list named {key}")
    pages = {}
    for d, sub, files in os.walk(root):
        rel_dir = os.path.relpath(d, root).replace(os.sep, "/")
        sub[:] = [s for s in sub if not s.startswith(".") and s not in ("node_modules", "recovered")]
        if rel_dir == "legal" or rel_dir.startswith("legal/"):
            continue  # the archive of what was published
        for name in files:
            if name.endswith(".html"):
                rel = name if rel_dir == "." else f"{rel_dir}/{name}"
                try:
                    with open(os.path.join(d, name), encoding="utf-8") as f:
                        pages[rel] = f.read()
                except (OSError, UnicodeDecodeError) as e:
                    raise CannotSee(f"{rel} could not be read: {e}")
    if not pages:
        raise CannotSee("no pages found. Run this from the repo root, or pass --root")
    scripts = {}
    assets = os.path.join(root, "assets")
    if os.path.isdir(assets):
        for name in sorted(os.listdir(assets)):
            if name.endswith(".js"):
                try:
                    with open(os.path.join(assets, name), encoding="utf-8") as f:
                        scripts[f"assets/{name}"] = f.read()
                except (OSError, UnicodeDecodeError) as e:
                    raise CannotSee(f"assets/{name} could not be read: {e}")
    return reg, pages, scripts


def check(root):
    """Return (fails, gaps, counts). Raises CannotSee."""
    reg, pages, scripts = load(root)
    text = {p: readable(raw) for p, raw in pages.items()}
    fails, gaps, counts = [], [], {}

    # known gaps, by the banned claim's id or its exact pattern
    known = {}
    for g in reg["known_gaps"]:
        key = g.get("id") or g.get("pattern")
        if not key or not g.get("file") or not g.get("until"):
            raise CannotSee(f"a known gap needs a file, an until, and an id or pattern: {g}")
        known[(g["file"], key)] = dict(g, seen=False)

    # 1. banned claims
    n = 0
    for b in reg["banned_claims"]:
        pat = b.get("pattern")
        if not pat:
            raise CannotSee(f"a banned claim has no pattern: {b}")
        try:
            rx = re.compile(pat, re.I)
        except re.error as e:
            raise CannotSee(f"banned claim pattern does not compile ({e}): {pat}")
        for p in sorted(text):
            m = rx.search(text[p])
            if not m:
                continue
            n += 1
            g = known.get((p, b.get("id"))) or known.get((p, pat))
            line = f"{p}: \"{around(text[p], m.start(), m.end())}\""
            if g:
                g["seen"] = True
                gaps.append(f"{line}\n      known gap until {g['until']}. Why it is banned: {b.get('why', '')}")
            else:
                fails.append(f"banned claim ({b.get('why', 'no reason given')})\n      {line}")
    counts["banned claims checked"] = len(reg["banned_claims"])
    for (f, key), g in sorted(known.items()):
        if not g["seen"]:
            fails.append(f"stale known gap: {f} no longer says it. Remove the entry from known_gaps ({key[:60]})")

    # 2. required lines, on every content page at the root
    not_content = {e["file"]: e.get("why", "") for e in reg.get("not_content_pages", [])}
    content = [p for p in sorted(pages) if "/" not in p and not is_redirect_stub(pages[p]) and p not in not_content]
    for r in reg.get("required_lines", []):
        want = re.sub(r"\s+", " ", r["text"])
        for p in content:
            if want not in text[p]:
                fails.append(f"required line missing ({r.get('why', '')})\n      {p}: \"{want[:90]}\"")
    counts["content pages"] = len(content)
    counts["required lines"] = len(reg.get("required_lines", []))

    # 3 and 4. glyphs and exclamation points
    for p in sorted(text):
        m = re.search(f"[{GLYPHS}]", text[p])
        if m:
            fails.append(f"dash glyph (use a period, a comma, a hyphen or the word to)\n      {p}: \"{around(text[p], m.start(), m.end())}\"")
        m = re.search(r"[A-Za-z]!", text[p])
        if m:
            fails.append(f"exclamation point in copy\n      {p}: \"{around(text[p], m.start(), m.end())}\"")

    # 5. hosts a page loads from or posts to
    allowed = {h.lower() for h in reg["site_hosts_allowed"]}
    seen_hosts = set()
    for p in sorted(pages):
        raw = pages[p]
        for m in LOADS.finditer(raw):
            if m.group(1).lower() == "link" and not LINK_LOADS.search(m.group(0)):
                continue  # a plain link out is navigation, not a load
            seen_hosts.add((m.group(2).lower(), p))
        for m in CALLS.finditer(raw):
            seen_hosts.add((m.group(1).lower(), p))
    for s in sorted(scripts):
        for m in CALLS.finditer(scripts[s]):
            seen_hosts.add((m.group(1).lower(), s))
    for h, where in sorted(seen_hosts):
        if h not in allowed:
            fails.append(f"outside host not in site_hosts_allowed (it goes into the Privacy Policy and the registry first)\n      {where}: {h}")
    counts["pages"] = len(pages)
    counts["hosts seen"] = len({h for h, _ in seen_hosts})
    return fails, gaps, counts


def main(argv=None):
    ap = argparse.ArgumentParser(description="Hold every page to the promise registry.")
    ap.add_argument("--root", default=".")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args(argv)
    try:
        fails, gaps, counts = check(a.root)
    except CannotSee as e:
        print(f"CANNOT SEE: {e}")
        print("VERDICT: CANNOT SEE. Nothing was checked, so nothing passed.")
        return CANNOT_SEE
    if not a.quiet:
        print("checked: " + ", ".join(f"{v} {k}" for k, v in counts.items()))
    for g in gaps:
        print("KNOWN GAP: " + g)
    for f in fails:
        print("FAIL: " + f)
    if fails:
        print(f"VERDICT: BLOCKED ({len(fails)} fail), {len(gaps)} known gap(s)")
        return FAIL
    print(f"VERDICT: PASS, {len(gaps)} known gap(s) still open")
    return PASS


if __name__ == "__main__":
    sys.exit(main())
