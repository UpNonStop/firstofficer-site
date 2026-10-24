/* First Officer v3: hero phone thread restyled to the New Bot app's chat (src/app/index.tsx + ui/theme.ts).
   Appended to the shadow-DOM CSS before fo-hero.js renders. CSS only; hero JS untouched. */
(function(){if(!window.CFG)return;var F="Inter,system-ui,-apple-system,'Segoe UI',sans-serif";
window.CFG.css+=[
".scr{background:#FAF6EE;font-family:"+F+"}",
".ts{font:500 12px "+F+";color:#8E8796;letter-spacing:.01em;margin:6px 0 10px}",
".rcpt{font:500 12px "+F+";color:#8E8796}",
".nm5{font:500 12.5px "+F+";color:#8E8796}",
".nm5 b{font:600 12px "+F+";color:#2A2230;background:rgba(232,197,71,.16);border-radius:6px;padding:1px 6px}",
".mm{margin:6px 0}.mm.o+.mm.o,.mm.f+.mm.f,.mm.s+.mm.s{margin-top:4px}.mm.o+.mm:not(.o),.mm:not(.o)+.mm.o{margin-top:14px}",
".b6{font:400 15.5px/1.48 "+F+";letter-spacing:-.006em;border-radius:18px;padding:10px 14px}",
/* client: white, goldLine hairline, 18 with 6 tail corner, 82% */
".mm.o .b6{background:#fff;color:#2A2230;box-shadow:inset 0 0 0 1px #EFE1BC;border-radius:18px 18px 6px 18px;max-width:82%}",
/* First Officer: unboxed ink text on cream, exactly like the app's replies */
".mm.f .b6{background:transparent;color:#2A2230;box-shadow:none;border-radius:0;padding:3px 4px 3px 0}",
/* specialists: white card, neutral hairline */
".mm.s .b6{background:#fff;color:#2A2230;box-shadow:inset 0 0 0 1px #E9E7EE;font-size:15px;border-radius:18px 18px 18px 6px}",
/* inline figures: goldWash chip, ink text. Numbers never pink. */
".b6 .e,.mm.f .b6 .e,.mm.o .b6 .e,.mm.s .b6 .e{background:rgba(232,197,71,.16);color:#2A2230;font:600 12px/1 "+F+";border-radius:6px;padding:3px 6px 2px}",
".q{font-family:"+F+";color:#5A5262;border-left-color:#EFE1BC}",
/* typing: ink3 dots, never white on pink */
".typ i,.mm.f .typ i{background:#8E8796;width:6px;height:6px}",
".mm.f .typ{background:#fff;box-shadow:inset 0 0 0 1px #E9E7EE;border-radius:18px 18px 18px 6px;padding:11px 13px!important}",
".dsk{font-family:"+F+";color:#8E8796}.dsk .typ{background:rgba(232,197,71,.16)}",
".tp{font-family:"+F+"}",
".deskh{font-family:"+F+"}",
/* hero First Officer node: outline rings only, no fill, no pink glow */
".fo{background:none!important;box-shadow:0 0 0 5px #fff,0 0 0 6.5px #f6c6df}#hero.M .fo{box-shadow:0 0 0 4px #fff,0 0 0 5.5px #f6c6df}"
].join("\n");})();
