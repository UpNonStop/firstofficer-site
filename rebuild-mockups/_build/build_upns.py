import sys; sys.path.insert(0,'/workspace/fo-rebuild-mockups/_build')
from common import *
from convert import convert
for n in ['062','063','064']:
    raw=open(f'{SRC}/content-assets/UPNS-{n}-WEB.html').read()
    raw=re.sub(r'<!--.*?-->','',raw,flags=re.S)
    raw=re.sub(r'html,body,\.gh-content,\.gh-canvas,\.post-content\{[^}]*\}','',raw)
    raw=re.sub(r'src="data:image/png;base64,[^"]+"','src="img/fo-chevron-alpha.png"',raw)
    body='<div class="upnsw">'+fix(raw,f'upns-{n}.html')+'</div>'
    body+='<section class="sec white"><div class="wrap"><p class="ctas"><a class="pill ghost" href="upns.html">← All dispatches</a></p></div></section>'
    write(f'upns-{n}.html',page(f'UPNS-{n} · The Intelligence Report · First Officer',body,active='free-from-the-desk.html',src=f'upns-{n}'))
    print('wrote',n)
save_log()
