from parts import *
IND=['Agencies','Auto Repair','Cleaning','Consulting','Contractors','CPA Firms','Dental','E-Commerce','Fitness','HVAC','IT & MSP','Landscaping','Law Firms','Medical','Property Management','Real Estate','Restaurants','Salons','Trucking','Veterinary','Other']
opts_ind=''.join(f'<option>{i}</option>' for i in IND)
CHEV='<img src="img/fo-chevron-alpha.png" alt="" width="34" height="34">'

hero=f'''<section class="sx ps bkh" id="top">{ph(['e-phone','e-laptop','e-relax','e-coffee','i-desk','e-window','e-arrive'],'',6500)}<div class="w2"><div class="bk">
<div class="bkl">
{kk('The Found Money Call · Free, 20 minutes')}
<h1 data-rv>Twenty minutes, your way. <em>See what your spend missed.</em></h1>
<p class="lede" data-rv="2">We look at where your business card spend goes and what it already earns. If the math won't clear the fee, you get an honest no, in writing.</p>
<div class="chips" data-rv="3"><span class="chip2">No cost</span><span class="chip2">No card login needed</span><span class="chip2">No affiliate links</span><span class="chip2 pk">$550/month only if you say yes</span></div>
<div class="bkclock" data-rv="3" aria-hidden="true"><svg viewBox="0 0 120 120" width="104" height="104"><circle cx="60" cy="60" r="50" fill="none" stroke="#efe8dc" stroke-width="10"/><circle class="clk" cx="60" cy="60" r="50" fill="none" stroke="#FA1896" stroke-width="10" stroke-linecap="round" stroke-dasharray="104.7 314.2" transform="rotate(-90 60 60)"/><text x="60" y="64" text-anchor="middle" style="font:400 30px 'DM Serif Display'" fill="#141216">20</text><text x="60" y="82" text-anchor="middle" style="font:700 8px 'JetBrains Mono';letter-spacing:.14em" fill="#8d8794">MIN</text></svg>
<div><b>Same call, same honest answer.</b><span>Whichever way you reach us.</span></div></div>
</div>
<div class="gl console" id="console" data-rv="2">
<div class="steps"><div class="s on"><i>1</i><span>Reach us</span></div><div class="ln"><b></b></div><div class="s"><i>2</i><span>The call</span></div><div class="ln"><b></b></div><div class="s"><i>3</i><span>Your details</span></div></div>
<p class="q">How do you want to reach us?</p><p class="qs">Pick the one that fits your day. Same call, same honest answer.</p>
<div class="opts">
<button class="opt wa on" data-p="p-wa" aria-pressed="true"><span class="ic">💬</span><span><b>WhatsApp me</b><small>Message us, we reply in the thread.</small></span></button>
<button class="opt" data-p="p-em" aria-pressed="false"><span class="ic">✉️</span><span><b>Email me</b><small>Send a note, get a reply by email.</small></span></button>
<button class="opt" data-p="p-cb" aria-pressed="false"><span class="ic">📞</span><span><b>Call me back</b><small>Leave a number and a good time.</small></span></button>
<div class="opt osoon" aria-disabled="true"><span class="ic">📱</span><span><b>Text me</b><small>A plain text from your phone.</small></span><span class="soonb">Coming soon</span></div>
</div>
<div class="pane on" id="p-wa"><h4>Message us on WhatsApp.</h4><p>Opens WhatsApp with a short note already written, including anything you brought from the calculator. Edit it before you send.</p>
<div class="wapv"><div class="bub o">Hi, I'd like a Found Money Call. Industry: ___. Monthly card spend: about $___.</div><span>Preview of the note. You edit it before it sends.</span></div>
<a class="pill green" href="{WA}">💬 Open WhatsApp</a><p class="fine" style="margin-top:12px">WhatsApp is run by Meta, as listed in our <a href="privacy-policy.html">Privacy Policy</a>. Texting is coming soon.</p></div>
<div class="pane" id="p-em"><h4>Email me about the call.</h4><p>Four fields. We reply by email to set up the call.</p></div>
<div class="pane" id="p-cb"><h4>Call me back.</h4><p>Leave a number and a good time. We call the number you give, nothing else.</p></div>
<div class="bkrest" id="bkrest">
<div class="sdiv"><i>2</i><p class="q">How should we talk on the call?</p></div><p class="qs">Your choice. Both are the same 20 minutes.</p>
<div class="mode"><button class="opt on" data-m="phone"><span class="ic">📞</span><span><b>Phone call</b><small>We call the number you give.</small></span></button><button class="opt" data-m="meet"><span class="ic">🎥</span><span><b>Google Meet</b><small>A video link arrives with your calendar invite.</small></span></button></div>
<p class="mnote" data-m="phone">Phone it is. Add your number below.</p><p class="mnote" data-m="meet" style="display:none">Google Meet it is. The link comes in your calendar invite.</p>
<div class="sdiv"><i>3</i><p class="q">Tell us where to reach you</p></div><p class="qs">We reply within one business day to set the time.</p>
<form class="fg" id="bkf"><label>First name<input name="n" autocomplete="given-name" required></label><label>Business email<input name="e" type="email" autocomplete="email" required></label>
<label>Industry<select name="i"><option value="">Choose one</option>{opts_ind}</select></label>
<label id="phf">Mobile or office number<input name="p" type="tel" autocomplete="tel"></label>
<label class="full">Best time to call (your time zone)<select name="t"><option>Weekday morning</option><option>Weekday midday</option><option>Weekday afternoon</option><option>Anytime</option></select></label>
<label class="full">Anything we should look at? (optional)<textarea name="m" rows="3"></textarea></label>
<button class="pill pink full" type="submit">Send my request</button>
<p class="fine full">This opens your own email app with the request written out, so nothing is stored on this page. By sending it you agree to our <a href="terms-of-service.html">Terms &amp; Conditions</a> and <a href="privacy-policy.html">Privacy Policy</a>.</p></form>
</div></div>
<div class="gl person nug2 bkp" data-rv="4"><div class="ni">👤</div><div><b>Strategy within 24 hours</b><p>Your strategy is reviewed and fine-tuned by a person before it reaches you. Every redemption is booked by a person. Day-to-day answers are software-led, and a person steps in when needed.</p></div></div>
</div></div></section>'''

nxt=f'''<section class="sx ps" id="next">{ph(['e-window','e-arrive','d-kyoto','e-lobby'],'c c2')}{rail('02','What happens next')}<div class="w2">
<div style="text-align:center">{kk('After you send it')}</div>
<h2 class="h2x c" data-rv>Here's what <em>happens next.</em></h2>
<div class="btl" data-io>
<div class="tls" data-rv><div class="dot">💬</div><div><h4>Within one business day</h4><p>we reply on the channel you picked to set the time.</p></div></div>
<div class="tls" data-rv="2"><div class="dot">📞</div><div><h4>On the call</h4><p>we walk through where your card spend goes. Bring a rough monthly number, nothing else.</p></div></div>
<div class="tls p" data-rv="3"><div class="dot">✍️</div><div><h4>After the call</h4><p>you get a written answer: a yes at $550 a month, month to month, or an honest no.</p></div></div>
</div>
<div class="letter">
<div class="gl solid lt y" data-rv><span class="stamp">Yes · $550/mo</span><div class="hd">02 / The written answer</div><h4>A yes with the math behind it.</h4>
<div class="lbar"><span>Where your spend goes today</span><i style="--w:42%"></i></div><div class="lbar"><span>Where it should go</span><i class="pk" style="--w:86%"></i></div><div class="lbar"><span>Our fee, out first</span><i class="ink" style="--w:18%"></i></div>
<p class="fine" style="margin:14px 0 0">Illustrative layout of a written answer. Yours carries your own numbers.</p></div>
<div class="gl solid lt n" data-rv="2"><span class="stamp">Honest no</span><div class="hd">02 / The written answer</div><h4>Or an honest no if it won't clear the fee.</h4>
<div class="lbar"><span>What the routing adds</span><i class="g" style="--w:30%"></i></div><div class="lbar"><span>Our fee</span><i class="ink" style="--w:44%"></i></div>
<p style="margin:16px 0 0;font-size:15px">If the math won't clear the fee, you get an honest no, in writing.</p></div>
</div>
<p class="fine c" style="margin-top:22px">While you wait: <a href="field-notes.html">read the field notes</a>.</p>
</div></section>'''

ways=f'''<section class="sx ps" id="ways">{ph(['bg-02','d-lisbon','bg-07'],'r')}{rail('03','One desk')}<div class="w2"><div class="fwg">
<div><h2 class="h2x" data-rv>Four ways in. <em>One desk.</em></h2>
<svg class="conv" viewBox="0 0 420 300" role="img" aria-label="WhatsApp, email, a call back and text all lead to one desk" data-io>
<g class="cl4"><path d="M70 40 C220 40 220 150 330 150"/><path d="M70 113 C220 113 230 150 330 150"/><path d="M70 187 C220 187 230 150 330 150"/><path class="osoon" d="M70 260 C220 260 220 150 330 150"/></g>
<g class="nd"><circle cx="46" cy="40" r="24"/><text x="46" y="48" text-anchor="middle">💬</text><circle cx="46" cy="113" r="24"/><text x="46" y="121" text-anchor="middle">✉️</text><circle cx="46" cy="187" r="24"/><text x="46" y="195" text-anchor="middle">📞</text><circle class="osoon" cx="46" cy="260" r="24"/><text x="46" y="268" text-anchor="middle" opacity=".5">📱</text></g>
<circle cx="350" cy="150" r="46" fill="#fff" stroke="#FA1896" stroke-width="3"/><circle cx="350" cy="150" r="58" fill="none" stroke="rgba(250,24,150,.18)" stroke-width="10" class="pul"/>
<image href="img/fo-chevron-alpha.png" x="328" y="126" width="44" height="44"/>
</svg></div>
<div class="fw4">
<div class="gl fwc" data-rv><div class="n">01</div><h4>The call</h4><p>20 minutes on where your card spend goes and what it earns today.</p></div>
<div class="gl fwc" data-rv="2"><div class="n">02</div><h4>The written answer</h4><p>A yes with the math behind it, or an honest no if it won't clear the fee.</p></div>
<div class="gl fwc" data-rv="3"><div class="n">03</div><h4>Your decision</h4><p>Month to month, cancel anytime. Not ready? <a href="free-from-the-desk.html">Get the weekday note</a> instead.</p></div>
</div></div>
<a class="gl calcn" href="calculator.html" data-rv><span class="ni">🪙</span><span><b>Not sure it's worth 20 minutes?</b> Run your number on the <u>calculator</u> first and bring it with you.</span><svg width="120" height="64" viewBox="0 0 110 64" aria-hidden="true"><path d="M10 58a45 45 0 0 1 90 0" fill="none" stroke="#f3e3a6" stroke-width="11" stroke-linecap="round"/><path class="cg" d="M10 58a45 45 0 0 1 72-36" fill="none" stroke="#FA1896" stroke-width="11" stroke-linecap="round"/></svg></a>
<p class="fine" style="margin-top:26px;max-width:900px">First Officer is an educational tool, not a licensed financial advisor. Your strategy is reviewed and fine-tuned by a person before it reaches you. Every redemption is booked by a person. Day-to-day answers are software-led, and a person steps in when needed. Calculator figures you bring here are estimates, not a projection of your results. See our <a href="terms-of-service.html">Terms &amp; Conditions</a>.</p>
</div></section>'''

tail='''<script>(function(){var f=document.getElementById('bkf');if(!f)return;f.addEventListener('submit',function(e){e.preventDefault();var d=new FormData(f),cb=document.querySelector('#p-cb.on'),m=document.querySelector('.mode .opt.on');
var b='Name: '+d.get('n')+'\\nEmail: '+d.get('e')+'\\nIndustry: '+d.get('i')+'\\nCall by: '+(m?m.getAttribute('data-m'):'')+'\\nNumber: '+(d.get('p')||'')+'\\nBest time: '+d.get('t')+'\\n\\n'+(d.get('m')||'');
location.href='mailto:desk@upnonstop.com?subject='+encodeURIComponent((cb?'Callback request':'Found Money Call request')+' · '+d.get('n'))+'&body='+encodeURIComponent(b)})})();</script>'''
html=page('Book Your "Found Money" Call · First Officer', hero+nxt+ways, desc='The Found Money Call. Free, 20 minutes, your way.', src='book', tail=tail)
open('/workspace/fo-rebuild-v2/book.html','w').write(html); print(len(html))
