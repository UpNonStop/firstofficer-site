L=[('product-recovered.html','product-modes.html'),('pricing.html','pricing-modes.html'),('freebies.html','freebies-modes.html'),('calculator.html','calculator-modes.html'),('about.html','about-modes.html'),('trust.html','trust-modes.html'),('industries.html','industries-modes.html'),('book.html','book-modes.html'),('home-recovered.html','home-modes.html')]
def relink(h):
    for a,b in L: h=h.replace('href="'+a,'href="'+b)
    return h
def nxt(n,href,h,p,b):
    return f'<section class="sec tight pnx"><div class="wrap"><a class="nxt reveal" href="{href}"><span class="nxk"><span class="thr" aria-hidden="true"><i class="te"></i><i class="tb"></i><i class="tr"></i><i class="tl"></i></span>Next chapter · {n}</span><b class="nxh">{h}</b><span class="nxp">{p}</span><span class="nxb">{b} <span class="ar">→</span></span></a></div></section>\n'
