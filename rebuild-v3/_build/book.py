import sys; sys.path.insert(0,'/workspace/fo-rebuild-v3/_build')
from fosite import *
IND=['Agencies','Auto Repair','Cleaning','Consulting','Contractors','CPA Firms','Dental','E-Commerce','Fitness','HVAC','IT & MSP','Landscaping','Law Firms','Medical','Property Management','Real Estate','Restaurants','Salons','Trucking','Veterinary','Other']
opts_ind=''.join(f'<option>{i}</option>' for i in IND)
def door(ic,t,s,p=None,on=False,soon=False,m=None):
    if soon: return f'<div class="door soon" aria-disabled="true"><span class="ic">{ic}</span><span class="bd"><b>{t}</b><small>{s}</small></span><span class="pill" style="--c:var(--gold2)">Coming soon</span></div>'
    a=f' data-p="{p}"' if p else f' data-m="{m}"'
    return f'<button type="button" class="door{" on" if on else ""}"{a} aria-pressed="{str(on).lower()}"><span class="ic">{ic}</span><span class="bd"><b>{t}</b><small>{s}</small></span><span class="rd"></span></button>'
def qh(n,q,qs): return f'<div style="margin:22px 0 12px"><span class="lab gold">Step {n}</span><h3 class="h3" style="margin-top:4px">{q}</h3><p class="sub" style="margin-top:4px;font-size:14px">{qs}</p></div>'

hero=f'''<section class="sec" id="book" style="padding-top:28px">{ph(['e-phone','e-laptop','e-relax','e-coffee','i-desk','e-window','e-arrive'],6500)}<div class="wrap"><div class="split">
<div>
<div class="head" data-rv><span class="lab gold">The Found Money Call · Free, 20 minutes</span><h1 class="h1">Twenty minutes, your way. <em>See what your spend missed.</em></h1>
<p class="lede">We look at where your business card spend goes and what it already earns. If the math won't clear the fee, you get an honest no, in writing.</p></div>
<div class="chips" data-rv><span class="chip">No cost</span><span class="chip">No card login needed</span><span class="chip">No affiliate links</span><span class="chip on">$550/month only if you say yes</span></div>
<div class="card" style="margin-top:14px;display:flex;gap:14px;align-items:center" data-rv><span class="num s tn" style="flex:none">20<small>min</small></span><div><b style="display:block;font-size:15px">Same call, same honest answer.</b><span class="sub" style="margin:0;font-size:14px">Whichever way you reach us.</span></div></div>
</div>
<div><div class="card hero bookcard" id="console" data-rv>
<div class="bkh"><span class="bkm"><img src="img/fo-chevron-transparent-v2.png" alt=""></span><span class="bd"><b>The Found Money Call</b><small>Free · 20 minutes · your way</small></span><span class="pill" style="--c:var(--green)">Open</span></div>
<div style="display:flex;justify-content:space-between;align-items:center;margin:16px 0 10px"><span class="lab">Your request</span><span class="cap" id="stepl" style="margin:0">Step 1 of 3</span></div>
<div class="steps" style="--n:3"><i class="on"></i><i></i><i></i></div>
<div class="steps" style="--n:3;margin-bottom:0"><span class="cap" style="margin:0">Reach us</span><span class="cap" style="margin:0">The call</span><span class="cap" style="margin:0">Your details</span></div>
<h2 class="h3" style="font-size:22px;margin-top:18px">How do you want to reach us?</h2><p class="sub" style="margin:4px 0 14px;font-size:14px">Pick the one that fits your day. Same call, same honest answer.</p>
{door('💬','WhatsApp me','Message us, we reply in the thread.',p='p-wa',on=True)}
{door('✉️','Email me','Send a note, get a reply by email.',p='p-em')}
{door('📞','Call me back','Leave a number and a good time.',p='p-cb')}
{door('📱','Text me','A plain text from your phone.',soon=True)}
<div class="pane on" id="p-wa" style="margin-top:16px"><h4 class="h3" style="font-size:17px">Message us on WhatsApp.</h4><p style="margin-top:4px">Opens WhatsApp with a short note already written, including anything you brought from the calculator. Edit it before you send.</p>
<div class="note" style="margin:12px 0;display:block"><div class="bub out" style="margin:0 0 8px auto;max-width:92%">Hi, I'd like a Found Money Call. Industry: ___. Monthly card spend: about $___.</div><span class="cap" style="margin:0">Preview of the note. You edit it before it sends.</span></div>
<a class="btn wa" href="{WA}">💬 Open WhatsApp</a><p class="cap" style="margin-top:10px">WhatsApp is run by Meta, as listed in our <a href="privacy-policy.html">Privacy Policy</a>. Texting is coming soon.</p></div>
<div class="pane" id="p-em" style="margin-top:16px"><h4 class="h3" style="font-size:17px">Email me about the call.</h4><p style="margin-top:4px">Four fields. We reply by email to set up the call.</p></div>
<div class="pane" id="p-cb" style="margin-top:16px"><h4 class="h3" style="font-size:17px">Call me back.</h4><p style="margin-top:4px">Leave a number and a good time. We call the number you give, nothing else.</p></div>
<div class="div" style="margin-top:20px"></div>
{qh(2,'How should we talk on the call?','Your choice. Both are the same 20 minutes.')}
<div class="mode">{door('📞','Phone call','We call the number you give.',m='phone',on=True)}{door('🎥','Google Meet','A video link arrives with your calendar invite.',m='meet')}</div>
<p class="mnote cap" data-m="phone" style="margin-top:10px">Phone it is. Add your number below.</p><p class="mnote cap" data-m="meet" style="display:none;margin-top:10px">Google Meet it is. The link comes in your calendar invite.</p>
{qh(3,'Tell us where to reach you','We reply within one business day to set the time.')}
<form id="bkf"><label class="fld">First name<input name="n" autocomplete="given-name" required></label><label class="fld">Business email<input name="e" type="email" autocomplete="email" required></label>
<label class="fld">Industry<select name="i"><option value="">Choose one</option>{opts_ind}</select></label>
<label class="fld" id="phf">Mobile or office number<input name="p" type="tel" autocomplete="tel"></label>
<label class="fld">Best time to call (your time zone)<select name="t"><option>Weekday morning</option><option>Weekday midday</option><option>Weekday afternoon</option><option>Anytime</option></select></label>
<label class="fld">Anything we should look at? (optional)<textarea name="m" rows="3"></textarea></label>
<button class="btn" type="submit" style="margin-top:16px">Send my request</button>
<p class="cap" style="margin-top:10px">This opens your own email app with the request written out, so nothing is stored on this page. By sending it you agree to our <a href="terms-of-service.html">Terms &amp; Conditions</a> and <a href="privacy-policy.html">Privacy Policy</a>.</p></form>
</div>
<div class="tip" style="--c:var(--gold2);margin-top:12px" data-rv><div class="tt">👤 Strategy within 24 hours</div><p>Your strategy is reviewed and fine-tuned by a person before it reaches you. Every redemption is booked by a person. Day-to-day answers are software-led, and a person steps in when needed.</p></div>
</div></div></div></section>'''

nxt=f'''<section class="sec" id="next">{ph(['e-window','e-arrive','d-kyoto','e-lobby'])}<div class="wrap">
{head('After you send it',"Here's what <em>happens next.</em>")}
<div class="split"><div class="card hero" data-rv><span class="lab">How we get you there</span><div style="margin-top:14px">
{tl([('now','Within one business day','we reply on the channel you picked to set the time.','💬'),('','On the call','we walk through where your card spend goes. Bring a rough monthly number, nothing else.','📞'),('','After the call','you get a written answer: a yes at $550 a month, month to month, or an honest no.','✍️')])}</div></div>
<div class="stack">
<div class="card top" style="--c:var(--earn)" data-rv><div style="display:flex;justify-content:space-between;align-items:center"><span class="lab">02 / The written answer</span><span class="pill" style="--c:var(--green)">Yes · $550/mo</span></div><h4 class="h3" style="margin-top:8px">A yes with the math behind it.</h4>
<div class="rows" style="margin-top:6px">{row('Where your spend goes today','',c='var(--ink3)',extra=meter(42,'var(--ink3)'))}{row('Where it should go','',c='var(--earn)',extra=meter(86,'var(--earn)',.15))}{row('Our fee, out first','',c='var(--ink2)',extra=meter(18,'var(--ink2)',.3))}</div>
<p class="cap" style="margin-top:8px">Illustrative layout of a written answer. Yours carries your own numbers.</p></div>
<div class="card" data-rv><div style="display:flex;justify-content:space-between;align-items:center"><span class="lab">02 / The written answer</span><span class="pill">Honest no</span></div><h4 class="h3" style="margin-top:8px">Or an honest no if it won't clear the fee.</h4>
<div class="rows" style="margin-top:6px">{row('What the routing adds','',c='var(--earn)',extra=meter(30,'var(--earn)'))}{row('Our fee','',c='var(--ink2)',extra=meter(44,'var(--ink2)',.15))}</div>
<p style="margin-top:8px">If the math won't clear the fee, you get an honest no, in writing.</p></div>
</div></div>
<p class="cap center" style="margin-top:18px;text-align:center">While you wait: <a href="field-notes.html">read the field notes</a>.</p>
</div></section>'''

ways=f'''<section class="sec" id="ways">{ph(['bg-02','d-lisbon','bg-07'])}<div class="wrap">
<div class="head" data-rv><span class="lab">One desk</span><h2 class="h2">Four ways in. <em>One desk.</em></h2></div>
<div class="split"><div class="card hero" data-rv><span class="lab">Every door leads to the same desk</span>
<div class="rows" style="margin-top:8px">{row('WhatsApp','',c='var(--green)')}{row('Email','',c='var(--gold2)')}{row('Call me back','',c='var(--gold2)')}{row('Text me','',c='var(--ink3)',extra='<span style="display:block;margin-top:6px"><span class="pill" style="--c:var(--gold2)">Coming soon</span></span>')}</div>
<div class="note" style="margin-top:12px;align-items:center"><span class="mk" style="width:26px;height:34px;display:grid;place-items:center;flex:none"><img src="img/fo-chevron-transparent-v2.png" alt="" style="width:22px"></span><span><b>First Officer</b> · one desk behind every door.</span></div></div>
<div class="stack">
<div class="card" data-rv><span class="num s tn">01</span><h4 class="h3" style="margin-top:6px">The call</h4><p>20 minutes on where your card spend goes and what it earns today.</p></div>
<div class="card" data-rv><span class="num s tn">02</span><h4 class="h3" style="margin-top:6px">The written answer</h4><p>A yes with the math behind it, or an honest no if it won't clear the fee.</p></div>
<div class="card" data-rv><span class="num s tn">03</span><h4 class="h3" style="margin-top:6px">Your decision</h4><p>Month to month, cancel anytime. Not ready? <a href="free-from-the-desk.html" style="color:var(--pink2)">Get the weekday note</a> instead.</p></div>
</div></div>
<a class="note" href="calculator.html" style="margin-top:14px;text-decoration:none" data-rv><span class="ic">🪙</span><span><b>Not sure it's worth 20 minutes?</b> Run your number on the <u>calculator</u> first and bring it with you.</span></a>
<p class="method" style="margin-top:20px">First Officer is an educational tool, not a licensed financial advisor. Your strategy is reviewed and fine-tuned by a person before it reaches you. Every redemption is booked by a person. Day-to-day answers are software-led, and a person steps in when needed. Calculator figures you bring here are estimates, not a projection of your results. See our <a href="terms-of-service.html">Terms &amp; Conditions</a>.</p>
</div></section>'''

tail='''<script>(function(){var f=document.getElementById('bkf');if(!f)return;f.addEventListener('submit',function(e){e.preventDefault();var d=new FormData(f),cb=document.querySelector('#p-cb.on'),m=document.querySelector('.mode .door.on');
var b='Name: '+d.get('n')+'\\nEmail: '+d.get('e')+'\\nIndustry: '+d.get('i')+'\\nCall by: '+(m?m.getAttribute('data-m'):'')+'\\nNumber: '+(d.get('p')||'')+'\\nBest time: '+d.get('t')+'\\n\\n'+(d.get('m')||'');
location.href='mailto:desk@upnonstop.com?subject='+encodeURIComponent((cb?'Callback request':'Found Money Call request')+' · '+d.get('n'))+'&body='+encodeURIComponent(b)})})();</script>'''
page('book.html','Book Your "Found Money" Call · First Officer', hero+nxt+ways, desc='The Found Money Call. Free, 20 minutes, your way.', src='book', tail=tail)
