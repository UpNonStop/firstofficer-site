#!/usr/bin/env python3
"""
Make every page on firstofficer.upnonstop.com close the way the landing page does.

Audited live on 2026-09-09 across all 34 pages:

  11 pages already match index.html exactly.
  21 pages have NO Daily Redemption block at all: the 20 for-*.html industry
     pages plus strategist.html. On those, .ctab sits directly above .sitedir.
   2 pages, trust.html and terms-of-service.html, carry the block but their
     site directory is missing one link: "Do Not Sell My Info -> privacy.html".

This inserts the canonical block immediately before <div class="sitedir"> where
it is absent, and adds the missing directory link where that is the only fault.
The block is taken verbatim from index.html, including its own <style> and
<script>, so nothing is retyped or approximated.

It writes nothing unless --apply is passed. Default is a dry run.
"""
import os, re, sys, shutil, time

ROOT = os.path.expanduser("~/firstofficer-site")
APPLY = "--apply" in sys.argv

FOCAP = r"""<section class="focap" style="--phcap:url(&quot;img/fo-bali.jpg&quot;)" id="focap" aria-labelledby="focap-h">
  <div class="focap-in">
    <div class="focap-k">The Daily Redemption</div>
    <h2 class="focap-h" id="focap-h">One real redemption, every weekday.</h2>
    <p class="focap-s">The newsletter behind the desk: what the desk booked on request, what it cost in points, and what it would have cost in cash. Free, and you can leave whenever you like.</p>
    <form class="focap-f" id="focapForm" novalidate="">
      <input class="focap-i" id="focapEmail" type="email" required="" autocomplete="email" placeholder="you@yourbusiness.com" aria-label="Your email address">
      <button class="focap-b" type="submit">Get the newsletter</button>
    </form>
    <p class="focap-msg" id="focapMsg" role="status" aria-live="polite"></p>
  </div>
</section>
<style id="focapcss">
.focap{background:#fff;border-top:1px solid rgba(20,18,22,.07);border-bottom:1px solid rgba(20,18,22,.07);padding:64px 24px;}
.focap-in{max-width:640px;margin:0 auto;text-align:center;}
.focap-k{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:#FA1896;font-weight:700;}
.focap-h{font-weight:900;font-size:clamp(22px,3.2vw,30px);letter-spacing:-0.02em;margin-top:10px;color:#141216;}
.focap-s{color:#5b5566;font-size:14.5px;line-height:1.7;margin:12px auto 0;max-width:520px;}
.focap-f{display:flex;gap:10px;margin:22px auto 0;max-width:460px;}
.focap-i{flex:1;min-width:0;padding:14px 16px;border:1px solid rgba(20,18,22,.16);border-radius:999px;font:inherit;font-size:15px;color:#141216;background:#fff;}
.focap-i:focus{outline:none;border-color:#FA1896;box-shadow:0 0 0 3px rgba(250,24,150,.15);}
.focap-b{background:#FA1896;color:#fff;border:none;border-radius:999px;padding:14px 24px;font-weight:800;font-size:14.5px;cursor:pointer;white-space:nowrap;min-height:44px;}
.focap-b:disabled{opacity:.55;cursor:default;}
.focap-msg{min-height:20px;margin-top:12px;font-size:13.5px;font-weight:700;color:#FA1896;}
@media (max-width:560px){.focap-f{flex-direction:column;}.focap-b{width:100%;}}
</style>
<script id="focapjs">(function(){
  var f=document.getElementById('focapForm'); if(!f) return;
  var i=document.getElementById('focapEmail'), b=f.querySelector('.focap-b'), m=document.getElementById('focapMsg');
  f.addEventListener('submit', function(e){
    e.preventDefault();
    var v=(i.value||'').trim();
    if(!v || v.indexOf('@')<1){ m.textContent='Please enter a valid email address.'; i.focus(); return; }
    b.disabled=true; m.textContent='Sending...';
    fetch('https://www.upnonstop.com/members/api/send-magic-link/', {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({email:v, emailType:'signup', labels:['First Officer site'], name:''})
    }).then(function(r){
      if(r.ok){ f.style.display='none'; m.textContent='Check your inbox for the confirmation link.';
        if(typeof gtag==='function') gtag('event','newsletter_signup',{page_path:location.pathname}); }
      else { b.disabled=false; m.textContent='That did not go through. Try again in a moment.'; }
    }).catch(function(){ b.disabled=false; m.textContent='That did not go through. Try again in a moment.'; });
  });
})();</script>"""

MISSING_LINK = '<a href="privacy.html">Do Not Sell My Info</a>'
AFTER_LINK   = '<a href="privacy-policy.html">Privacy Policy</a>'

def main():
    if not os.path.isdir(ROOT):
        print("no repo at", ROOT); return 1
    files = sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))
    if not files:
        print("no html files in", ROOT); return 1

    backup = "/tmp/fo_site_" + time.strftime("%Y%m%d%H%M%S")
    added_focap, added_link, already, skipped = [], [], [], []

    for f in files:
        p = os.path.join(ROOT, f)
        s = open(p, encoding="utf-8", errors="replace").read()
        out = s

        # 1. the Daily Redemption block, where the page has none
        if 'class="focap"' not in out:
            if out.count('<div class="sitedir"') == 1:
                out = out.replace('<div class="sitedir"', FOCAP + "\n<div class=\"sitedir\"", 1)
                added_focap.append(f)
            else:
                skipped.append((f, "no single .sitedir anchor to insert before"))
                continue

        # 2. the directory link some pages lost
        if MISSING_LINK not in out and AFTER_LINK in out:
            out = out.replace(AFTER_LINK, AFTER_LINK + MISSING_LINK, 1)
            added_link.append(f)

        if out == s:
            already.append(f); continue

        if APPLY:
            os.makedirs(backup, exist_ok=True)
            shutil.copy2(p, backup)
            open(p + ".tmp", "w", encoding="utf-8").write(out)
            os.replace(p + ".tmp", p)

    print(("APPLIED" if APPLY else "DRY RUN, nothing written") + "\n")
    print(f"  {len(added_focap):>3} pages gained the Daily Redemption block")
    for f in added_focap: print("        ", f)
    print(f"  {len(added_link):>3} pages gained the missing directory link")
    for f in added_link: print("        ", f)
    print(f"  {len(already):>3} pages already correct")
    if skipped:
        print(f"  {len(skipped):>3} SKIPPED, look at these by hand")
        for f, why in skipped: print("        ", f, "-", why)
    if APPLY:
        print("\n  backup:", backup)
        print("  next:  cd ~/firstofficer-site && git diff --stat")
    else:
        print("\n  to write:  python3 " + os.path.basename(__file__) + " --apply")
    return 0

sys.exit(main())
