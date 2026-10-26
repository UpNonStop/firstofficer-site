import sys; import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fosite import *
# Freebies page: faithful port of free-from-the-desk.html (origin/home-v2-preview 30f25a1) into the v3 look.
# Copy is kept verbatim; see CHANGES.md for the short list of edits.
ICONS={'calc': '<svg viewBox="0 0 64 64" width="56" height="56" aria-hidden="true" fill="none" stroke="#141216" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><rect x="14" y="8" width="36" height="48" rx="7" fill="#FFE3F1"/><rect x="20" y="14" width="24" height="10" rx="2.5" fill="#fff"/><circle cx="24" cy="33" r="2.2" fill="#141216"/><circle cx="32" cy="33" r="2.2" fill="#141216"/><circle cx="40" cy="33" r="2.2" fill="#FA1896" stroke="#FA1896"/><circle cx="24" cy="42" r="2.2" fill="#141216"/><circle cx="32" cy="42" r="2.2" fill="#141216"/><rect x="38" y="39.5" width="4.5" height="10" rx="2.2" fill="#FA1896" stroke="#FA1896"/></svg>', 'mcc': '<svg viewBox="0 0 64 64" width="56" height="56" aria-hidden="true" fill="none" stroke="#141216" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><rect x="12" y="10" width="40" height="44" rx="6" fill="#E6F7EE"/><path d="M12 22 H52 M12 33 H52 M12 44 H52 M26 10 V54"/><path d="M17 16 h4" stroke="#FA1896"/></svg>', 'nug': '<svg viewBox="0 0 64 64" width="56" height="56" aria-hidden="true" fill="none" stroke="#141216" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M18 22 L32 10 L46 22 L40 50 L24 50 Z" fill="#F7D774"/><path d="M18 22 H46 M32 10 L28 22 L32 50 L36 22 Z"/><path d="M51 13 l2 -5 M54 18 l5 -1 M49 9 l-1 -4" stroke="#FA1896"/></svg>', 'nug2': '<svg viewBox="0 0 64 64" width="56" height="56" aria-hidden="true" fill="none" stroke="#141216" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M18 22 L32 10 L46 22 L40 50 L24 50 Z" fill="#F7D774"/><path d="M18 22 H46 M32 10 L28 22 L32 50 L36 22 Z"/><path d="M51 13 l2 -5 M54 18 l5 -1 M49 9 l-1 -4" stroke="#FA1896"/></svg>', 'chat': '<svg viewBox="0 0 64 64" width="56" height="56" aria-hidden="true" fill="none" stroke="#141216" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M10 16 a6 6 0 0 1 6-6 h28 a6 6 0 0 1 6 6 v16 a6 6 0 0 1-6 6 H26 l-10 9 v-9 h0 a6 6 0 0 1-6-6 Z" fill="#FFE3F1"/><path d="M20 20 h20 M20 28 h13"/><path d="M42 40 a6 6 0 0 1 6-6 h4 a4 4 0 0 1 4 4 v8 a4 4 0 0 1-4 4 v5 l-6-5 h-0 a4 4 0 0 1-4-4 Z" fill="#fff"/></svg>', 'chat2': '<svg viewBox="0 0 64 64" width="56" height="56" aria-hidden="true" fill="none" stroke="#141216" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M10 16 a6 6 0 0 1 6-6 h28 a6 6 0 0 1 6 6 v16 a6 6 0 0 1-6 6 H26 l-10 9 v-9 h0 a6 6 0 0 1-6-6 Z" fill="#FFE3F1"/><path d="M20 20 h20 M20 28 h13"/><path d="M42 40 a6 6 0 0 1 6-6 h4 a4 4 0 0 1 4 4 v8 a4 4 0 0 1-4 4 v5 l-6-5 h-0 a4 4 0 0 1-4-4 Z" fill="#fff"/></svg>', 'list': '<svg viewBox="0 0 64 64" width="56" height="56" aria-hidden="true" fill="none" stroke="#141216" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><rect x="14" y="8" width="36" height="48" rx="6" fill="#FFF6DA"/><rect x="24" y="5" width="16" height="8" rx="3" fill="#fff"/><path d="M21 25 l3 3 l6-6 M21 37 l3 3 l6-6" stroke="#FA1896"/><path d="M35 26 h9 M35 38 h9 M21 48 h23"/></svg>'}
IC={k:v.replace('width="56" height="56"','width="44" height="44"') for k,v in ICONS.items()}
def src(t): return f'<span class="pill" style="--c:var(--gold2)">{t}</span>'
def ex(t='Example'): return f'<span class="pill" style="--c:var(--ink3)">{t}</span>'

def dk(id_,ty,ind,ic,time,h,love,chips,inside,gold=False):
    return f'''<article class="card dk{" gold" if gold else ""}" id="{id_}" data-ty="{ty}" data-ind="{ind}" data-rv>
<div class="dk-top"><span class="ic">{IC[ic]}</span><span class="cap">{time}</span></div>
<span class="lab{" gold" if gold else ""}">{ty}</span><h3 class="h3">{h}</h3><p>{love}</p>
<div class="dchips">{chips}</div>
<details><summary class="grab">Grab it <span aria-hidden="true">&rarr;</span></summary><div class="inside">{inside}</div></details>
</article>'''

CODES=[('5211','Lumber and Building Materials'),('5200','Home Supply Warehouse'),('5039','Construction Materials (NEC)'),('5072','Hardware, Equipment and Supplies'),('5074','Plumbing and Heating Equipment'),('5065','Electrical Parts and Equipment'),('7394','Equipment, Tool, Furniture Rental'),('7513','Truck and Utility Trailer Rental'),('5172','Petroleum and Petroleum Products'),('5542','Automated Fuel Dispensers')]
tbl='<table class="codes"><thead><tr><th>Code</th><th>Visa\'s name for it</th></tr></thead><tbody>'+''.join(f'<tr><td>{c}</td><td>{n}</td></tr>' for c,n in CODES)+'</tbody></table>'

cards=''.join([
dk('mcc','Cheat sheet','contractors hvac','mcc','2 min read','The trade-supplier code sheet',
 'Ten codes that decide what your lumber, parts and fuel spend actually earns. Tape it above the desk.',
 src('Source: Visa MDSM'),
 tbl+'<p class="fine">Source: Visa Merchant Data Standards Manual. Each store\'s code is set by its processor, so your statement is the final word.</p>'),
dk('nug-contractors','Golden Nugget pack','contractors','nug','3 min read','Contractors: 5 Golden Nuggets',
 'The stuff I see on contractor statements that nobody mentions, like the 2x4 that codes three ways.',
 src('Visa, IRS')+ex('1 Example'),
 '<ol class="nl">'
 f'<li><b>The same 2x4 can code three ways.</b> Lumber yard 5211, home supply warehouse 5200, materials distributor 5039. Rewards follow the code, not the item. {src("Visa MDSM")}</li>'
 f'<li><b>Paying a sub by card moves their 1099.</b> The IRS says card payments go on Form 1099-K from the payment settlement entity, not on your 1099-NEC. Ask your preparer. {src("IRS i1099mec")}</li>'
 f'<li><b>Bulk fuel at the yard isn\'t "gas."</b> Delivered bulk fuel is 5172. The pump is 5542. {src("Visa MDSM")}</li>'
 f'<li><b>Rentals are their own category.</b> Equipment rental 7394, truck and trailer rental 7513. {src("Visa MDSM")}</li>'
 f'<li><b>Time the big materials buy to the draw.</b> Bought the day after your statement closes, it isn\'t due until the next statement\'s due date. Your dates will differ. {ex()}</li></ol>'
 '<p class="fine"><a href="for-contractors.html">See the full contractors page &rarr;</a></p>',gold=True),
dk('nug-hvac','Golden Nugget pack','hvac','nug2','3 min read','HVAC: 4 Golden Nuggets',
 'Refrigerant rules, parts-house codes and paying installers by card. Written for the shop, not the textbook.',
 src('Visa, IRS, EPA')+ex('1 Example'),
 '<ol class="nl">'
 f'<li><b>Refrigerant is sold to certified techs only.</b> Under 40 CFR 82.154(c), the buyer must be certified or employ a certified technician and show proof. Who holds the card at the counter matters. {src("EPA, 40 CFR 82.154")}</li>'
 f'<li><b>Your parts house and your electrical supplier code differently.</b> Plumbing and heating is 5074. Electrical parts is 5065. {src("Visa MDSM")}</li>'
 f'<li><b>Paying installers by card?</b> Same 1099-K rule as above. {src("IRS i1099mec")}</li>'
 f'<li><b>Equipment buys bunch up before peak season.</b> That\'s when timing your statement cycle matters most. {ex()}</li></ol>',gold=True),
dk('supplier','Script','contractors hvac all','chat','60-second read','5 questions for your supplier',
 'Read them at the counter. Most reps have never been asked, and the answers are worth knowing.',
 src('Coding: Visa MDSM'),
 '<ol class="nl q"><li>"What category does your card terminal run under? Can you check the merchant code on your processor statement?"</li><li>"Do you add a surcharge for cards? Is it the same at every location and for every card type?"</li><li>"Is there a different price for paying by bank transfer, or for net terms?"</li><li>"Does your online ordering run through the same terminal as the counter?"</li><li>"Can my receipts show the item lines, not just a total?"</li></ol>'
 '<p class="fine">The questions are ours. Merchant codes are defined in the Visa Merchant Data Standards Manual.</p>'),
dk('preparer','Script','contractors hvac all','chat2','1 min read','The 1099 line for your preparer',
 'One sentence that can save a back-and-forth in March.',
 src('Source: IRS'),
 '<p>The one line to read your preparer:</p><blockquote class="note">"When I pay a contractor by card, the IRS says it\'s reported on Form 1099-K by the payment settlement entity, not on my 1099-NEC. Does that change what we file this year?"</blockquote>'
 '<p class="fine">Source: IRS Instructions for Forms 1099-MISC and 1099-NEC. General information, not tax advice.</p>'),
dk('yearend','Checklist','all','list','5 minutes','Year-end card checklist',
 'Seven things to look at before December 31, so January starts with no surprises.',
 ex(),
 '<ol class="nl ticks"><li>Pull every card statement for the year into one folder.</li><li>Check which suppliers you paid by card and which by transfer.</li><li>List the contractors you paid by card. That\'s the 1099 question for your preparer.</li><li>Note every annual fee and its renewal month.</li><li>Write down each points balance and when it expires.</li><li>Find the biggest purchases you know are coming next quarter.</li><li>Check your statement close dates before those purchases.</li></ol>'
 '<p class="fine">An example checklist, not tax or financial advice.</p>'),
])

IND_F=[('all','any business'),('contractors','contracting business'),('hvac','HVAC shop')]
TY_F=[('all','everything'),('Golden Nugget pack','the nuggets'),('Cheat sheet','a cheat sheet'),('Script','what to say'),('Checklist','a checklist')]
def pick(lbl,k,opts,more=''):
    b=''.join(f'<button type="button" class="chip{" on" if i==0 else ""}" data-k="{k}" data-v="{v}" aria-pressed="{"true" if i==0 else "false"}">{t}</button>' for i,(v,t) in enumerate(opts))
    return f'<div class="picker"><span class="lab">{lbl}</span><div class="chiprow">{b}{more}</div></div>'

hero=f'''<section class="sec ffd" id="fftop" style="padding-top:28px">{ph(['i-desk','e-coffee','e-laptop','e-tablet'],6500)}<div class="wrap"><div class="split">
<div class="head" data-rv style="margin-bottom:0"><span class="lab gold">Free From the Desk</span><h1 class="h1">Everything I'd tell you <em>over coffee.</em></h1>
<p class="lede">Most owners put serious money on cards every month, and nobody ever sits them down and explains how it actually works. So here it is: the codes, the questions, the notes we keep for each trade. Free. <span class="hlm">No email. No catch.</span></p>
<div class="sig"><span class="av" aria-hidden="true">O</span><span><b>Ohad</b><small>Founder, UpNonStop</small></span></div></div>
<a class="card hero feat" href="calculator.html" data-rv>
<div class="dk-top"><span class="lab gold">Start here</span><span class="pill" style="--c:var(--ink3)">Estimate</span></div>
<span class="ic big">{ICONS['calc']}</span>
<h2 class="h3">The Found Money Calculator</h2>
<p>Put in what you spend in a normal month. See what it could be worth, with every assumption shown so you can argue with it.</p>
<span class="cap">takes 60 seconds</span>
<span class="btn">Run my numbers &rarr;</span>
</a>
</div>
<!-- Photo: Elena Leya (@foodistika), https://unsplash.com/photos/56J8143b7PU (Unsplash License) -->
<figure class="ptile deskphoto" data-rv><div class="im"><picture><source srcset="img/ind/desk.webp" type="image/webp"><img src="img/ind/desk.jpg" width="1200" height="744" alt="A notebook, pen and cup of coffee on a white desk" loading="lazy"></picture></div>
<figcaption class="cp"><b>Pull up a chair. Coffee's on me.</b><span class="cap">Photo: <a href="https://unsplash.com/photos/56J8143b7PU" rel="noopener">Elena Leya</a> / Unsplash</span></figcaption></figure>
</div></section>'''

desk=f'''<section class="sec ffd" id="industries">{ph(['e-tablet','i-desk','e-coffee'])}<div class="wrap">
{head('The desk, by trade','Pick your trade. <em>Take whatever helps.</em>',labc='gold')}
<div class="filters card" data-rv aria-label="Filter">
{pick('I run a','ind',IND_F,'<a class="chip more" href="#ftind">more trades coming</a>')}
{pick('and I want','ty',TY_F)}
</div>
<div class="dkgrid">{cards}</div>
</div></section>'''

end=f'''<section class="sec ffd" id="endnote">{ph(['e-coffee','e-window','e-relax'])}<div class="wrap">
<div class="card hero endnote" data-rv><span class="lab gold">From Ohad</span>
<p class="big">That's the desk. Take whatever helps. If you'd rather we just do it for you, that's what <a href="book.html">The Found Money Call</a> is: 20 minutes, and if the math says no, I'll tell&nbsp;you&nbsp;no.</p>
<div class="sig"><span class="av" aria-hidden="true">O</span><span><b>Ohad</b><small>Founder, UpNonStop</small></span></div>
<div class="btns"><a class="btn" href="book.html?from=freebies">Book Your "Found Money" Call</a></div></div>
<p class="method" data-rv><b>Plainly:</b> First Officer is an educational tool, not a licensed financial advisor. Nothing here is financial, tax or legal advice. Every number is sourced or labeled Example, and your results will be different. Rules change, so check with your issuer or program before you act. No affiliate links, and no money from any bank or program. Nobody pays us to send you anywhere. <a href="terms-of-service.html"><i>Terms &amp; Conditions</i></a></p>
<p class="method">Point valuations are estimates based on common redemption benchmarks. Actual value depends on how and when you redeem.</p>
</div></section>'''

JS='''<script>(function(){var f={ind:'all',ty:'all'};document.querySelectorAll('.ffd .picker button').forEach(function(b){b.addEventListener('click',function(){f[b.dataset.k]=b.dataset.v;document.querySelectorAll('.ffd .picker button[data-k="'+b.dataset.k+'"]').forEach(function(x){var on=x===b;x.classList.toggle('on',on);x.setAttribute('aria-pressed',on?'true':'false')});document.querySelectorAll('.dk').forEach(function(c){var i=c.dataset.ind.split(' ');var ok=(f.ind=='all'||i.indexOf(f.ind)>-1||i.indexOf('all')>-1)&&(f.ty=='all'||c.dataset.ty==f.ty);c.hidden=!ok})})})})();</script>
<script>(function(){if(location.host!=='htmlpreview.github.io')return;var m=location.search.match(/github\\.com\\/([^\\/]+)\\/([^\\/]+)\\/blob\\/([^\\/]+)\\/(.*\\/)?[^\\/]*$/);if(!m)return;var b='https://cdn.jsdelivr.net/gh/'+m[1]+'/'+m[2]+'@'+m[3]+'/'+(m[4]||'');document.querySelectorAll('.deskphoto source[srcset^="img/"]').forEach(function(s){s.srcset=b+s.getAttribute('srcset')});document.querySelectorAll('.deskphoto img[src^="img/"]').forEach(function(i){i.src=b+i.getAttribute('src')});})();</script>'''

page('free-from-the-desk.html','Free From the Desk · First Officer by UpNonStop',hero+desk+end,
     desc="Everything I'd tell you over coffee: merchant codes, supplier questions, the 1099 line for your preparer and a year-end checklist. Free. No email. No catch.",
     src='freebies',tail=JS)
