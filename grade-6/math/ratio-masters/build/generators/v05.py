import sys, json
P=sys.argv[1]
BEAD='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><circle class="rm-body" cx="16" cy="16" r="14"></circle><circle class="rm-detail" cx="16" cy="16" r="4.5"></circle></svg>'
BLOCK='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><rect class="rm-body" x="2" y="2" width="28" height="28" rx="4"></rect><rect class="rm-detail" x="9" y="9" width="14" height="14" rx="2"></rect></svg>'
VARS={
 'by':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#FFFFFF;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FFFFFF;--rm-b-text:#6E5000;",
 'byk':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#4C7FE6;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FAD55C;--rm-b-text:#6E5000;",
 'rw':"--rm-a:#C8322B;--rm-a-edge:#8C1E19;--rm-a-detail:#FFFFFF;--rm-a-text:#B02A23;--rm-b:#FFFFFF;--rm-b-edge:#2F3440;--rm-b-detail:#DFE3E9;--rm-b-text:#2F3440;",
}
def pct(x,k): return f"{x*100/k:.3f}".rstrip('0').rstrip('.')+'%'
def board(out,title,vk,obj,la,lb,A,B,k,unknown,question):
    noun='blocks' if obj==BLOCK else 'beads'
    known = 'b' if unknown=='a' else 'a'
    D=0.6; S=0.3
    first, second = known, unknown
    def t0(side): return S if side==first else S + k*D + 0.9
    def land(side,i): return t0(side) + (i-1)*D + 0.5   # jump i lands (i>=1)
    def nums(side):
        step = A if side=='a' else B
        cls = 'rm-a-text' if side=='a' else 'rm-b-text'
        o=[]
        for i in range(k+1):
            v=step*i; pos=f'left: {pct(i,k)}'
            if side==known:
                bump = f' rm-land" style="{pos}; animation-delay: {land(side,i):g}s' if i>=1 else f'" style="{pos}'
                o.append(f'<span class="rm-n {cls}{bump}">{v}</span>')
            elif i==0:
                o.append(f'<span class="rm-n {cls}" style="{pos}">{v}</span>')
            elif i==k:
                o.append(f'<span class="rm-n rm-ans {cls}" style="{pos}"><span class="rm-hide rm-unknown">?</span><span class="rm-late rm-unknown" style="animation-delay: {land(side,i):g}s">?</span><span class="rm-reveal rm-pop" style="animation-delay: {land(side,i):g}s">{v}</span></span>')
            elif i==1:
                o.append(f'<span class="rm-n {cls} rm-land" style="{pos}; animation-delay: {land(side,i):g}s">{v}</span>')
            else:
                o.append(f'<span class="rm-n {cls}" style="{pos}"><span class="rm-reveal rm-pop" style="animation-delay: {land(side,i):g}s">{v}</span></span>')
        return ''.join(o)
    def ticks(): return ''.join(f'<span class="rm-tick" style="left: {pct(i,k)}"></span>' for i in range(k+1))
    def arcs(side):
        step = A if side=='a' else B
        cls = 'rm-arc-a' if side=='a' else 'rm-arc-b'
        o=[]
        for i in range(k):
            d=t0(side)+i*D
            o.append(f'<span class="rm-arc {cls} rm-reveal rm-draw" style="left: {pct(i,k)}; width: {pct(1,k)}; animation-delay: {d:g}s"></span>'
                     f'<span class="rm-jump {cls} rm-reveal rm-pop" style="left: {pct(i+0.5,k)}; animation-delay: {d+0.35:g}s">+{step}</span>')
        return ''.join(o)
    def count(side):
        return f'<span class="rm-count rm-reveal rm-pop" style="animation-delay: {t0(side)+k*D:g}s">{k} jumps</span>'
    ua = A*k; ub = B*k
    kv, uv = (ua, ub) if unknown=='b' else (ub, ua)
    kl, ul = (la, lb) if unknown=='b' else (lb, la)
    ks, us = (A, B) if unknown=='b' else (B, A)
    html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<style>
body{{margin:0;background:#FFFFFF}}
.ratio-master{{--rm-ink:#1B1F2A;--rm-muted:#4A5263;--rm-panel:#F3F4F7;--rm-focus:#1E5BD8;
{VARS[vk]}
box-sizing:border-box;max-width:1040px;margin:0 auto;padding:40px 16px 48px;background:#FFFFFF;color:var(--rm-ink);font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.4}}
.ratio-master *,.ratio-master *::before,.ratio-master *::after{{box-sizing:border-box}}
.ratio-master .rm-question{{max-width:34ch;margin:0 auto 28px;text-align:center;font-size:clamp(20px,3vw,26px);font-weight:700;line-height:1.3}}
.ratio-master .rm-dnl{{width:min(100%, 720px);margin:0 auto}}
.ratio-master .rm-line-lab{{display:flex;align-items:center;gap:8px;margin:0;font-size:18px;font-weight:700}}
.ratio-master .rm-track{{position:relative;margin:0 28px}}
.ratio-master .rm-arcs{{position:relative;height:72px}}
.ratio-master .rm-axis{{position:relative;height:3px;background:var(--rm-ink)}}
.ratio-master .rm-tick{{position:absolute;top:-10px;width:3px;height:23px;margin-left:-1.5px;background:var(--rm-ink)}}
.ratio-master .rm-nums{{position:relative;height:52px}}
.ratio-master .rm-n{{position:absolute;transform:translateX(-50%);font-size:clamp(20px,3.6vw,28px);font-weight:800;line-height:1.2;font-variant-numeric:tabular-nums;white-space:nowrap}}
.ratio-master .rm-top .rm-n{{top:12px}}
.ratio-master .rm-bottom .rm-n{{bottom:12px}}
.ratio-master .rm-ans{{display:inline-flex;align-items:center;justify-content:center;min-width:48px;padding:0 8px;outline:3px solid var(--rm-ink);border-radius:10px;background:#FFFFFF}}
.ratio-master .rm-unknown{{color:var(--rm-muted)}}
.ratio-master .rm-arc{{position:absolute;height:44px;border:3px solid currentColor}}
.ratio-master .rm-top .rm-arc{{bottom:3px;border-bottom:none;border-radius:50% 50% 0 0 / 100% 100% 0 0}}
.ratio-master .rm-bottom .rm-arc{{top:3px;border-top:none;border-radius:0 0 50% 50% / 0 0 100% 100%}}
.ratio-master .rm-jump{{position:absolute;transform:translateX(-50%);font-size:17px;font-weight:800;white-space:nowrap}}
.ratio-master .rm-top .rm-jump{{top:-4px}}
.ratio-master .rm-bottom .rm-jump{{bottom:-4px}}
.ratio-master .rm-count{{margin-left:6px;padding:2px 10px;border-radius:999px;background:var(--rm-panel);color:var(--rm-ink);font-size:15px;font-weight:700}}
.ratio-master .rm-arc-a{{color:var(--rm-a-text)}}
.ratio-master .rm-arc-b{{color:var(--rm-b-text)}}
.ratio-master .rm-gap{{height:20px}}
.ratio-master .rm-bottom + .rm-line-lab{{margin-top:26px}}
.ratio-master .rm-reveal{{display:none}}
.ratio-master .rm-late{{display:none}}
.ratio-master .rm-check{{max-width:520px;margin:28px auto 0;text-align:center}}
.ratio-master .rm-check summary{{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:10px 24px;border:2px solid var(--rm-ink);border-radius:999px;background:#FFFFFF;font-size:18px;font-weight:700;cursor:pointer;list-style:none}}
.ratio-master .rm-check summary::-webkit-details-marker{{display:none}}
.ratio-master .rm-check summary:focus-visible{{outline:3px solid var(--rm-focus);outline-offset:3px}}
.ratio-master .rm-check[open] summary{{background:var(--rm-panel)}}
.ratio-master .rm-feedback{{margin:14px 0 0;font-size:18px}}
.ratio-master:has(.rm-check[open]) .rm-hide{{display:none}}
.ratio-master:has(.rm-check[open]) .rm-reveal{{display:block}}
.ratio-master:has(.rm-check[open]) span.rm-n .rm-reveal{{display:inline}}
.ratio-master:has(.rm-check[open]) .rm-pop{{animation:rm-pop .4s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-draw{{animation:rm-draw .5s ease-in-out both}}
.ratio-master:has(.rm-check[open]) .rm-land{{animation:rm-land .45s ease-out both}}
.ratio-master:has(.rm-check[open]) span.rm-count{{display:inline-block}}
.ratio-master:has(.rm-check[open]) .rm-late{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;border-radius:10px;background:#FFFFFF;animation:rm-gone .3s ease-out both}}
.ratio-master .rm-obj{{display:block;width:24px;height:24px;flex:none}}
.ratio-master .rm-obj .rm-body{{stroke-width:2}}
.ratio-master .rm-obj .rm-detail{{stroke-width:1.5}}
.ratio-master .rm-obj-a .rm-body{{fill:var(--rm-a);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-a .rm-detail{{fill:var(--rm-a-detail);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-b .rm-body{{fill:var(--rm-b);stroke:var(--rm-b-edge)}}
.ratio-master .rm-obj-b .rm-detail{{fill:var(--rm-b-detail);stroke:var(--rm-b-edge)}}
.ratio-master .rm-a-text{{color:var(--rm-a-text)}}
.ratio-master .rm-b-text{{color:var(--rm-b-text)}}
.ratio-master .rm-sr{{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}}
@keyframes rm-pop{{from{{opacity:0;transform:scale(.6)}}to{{opacity:1;transform:none}}}}
@keyframes rm-gone{{from{{opacity:1}}to{{opacity:0}}}}
@keyframes rm-draw{{from{{clip-path:inset(0 100% 0 0)}}to{{clip-path:inset(0 0 0 0)}}}}
@keyframes rm-land{{0%{{transform:translateX(-50%) scale(1)}}40%{{transform:translateX(-50%) scale(1.35)}}100%{{transform:translateX(-50%) scale(1)}}}}
.ratio-master .rm-n.rm-pop,.ratio-master .rm-n .rm-pop{{transform-origin:center}}
@media (prefers-reduced-motion: reduce){{.ratio-master .rm-pop,.ratio-master .rm-draw,.ratio-master .rm-land{{animation:none !important}}.ratio-master:has(.rm-check[open]) .rm-late{{display:none}}}}
@media (max-width: 480px){{.ratio-master .rm-track{{margin:0 18px}}.ratio-master .rm-arc b{{font-size:14px}}}}
</style>
</helmet>
<div class="ratio-master" data-master="V05" data-skin="{'blocks' if obj==BLOCK else 'beads'}">
<h2 class="rm-question">{question}</h2>
<p class="rm-sr">Double number line. Top line: {la} {noun}, counting by {A}. Bottom line: {lb} {noun}, counting by {B}. The ticks line up: 0 with 0, {A} with {B}. The question asks for the {ul} value under {kv} {kl}.</p>
<div class="rm-dnl" aria-hidden="true">
<p class="rm-line-lab rm-a-text">{obj.format(s="a")}{la}{count("a")}</p>
<div class="rm-track rm-top">
<div class="rm-arcs">{arcs('a')}</div>
<div class="rm-axis">{ticks()}</div>
<div class="rm-nums">{nums('a')}</div>
</div>
<div class="rm-gap"></div>
<div class="rm-track rm-bottom">
<div class="rm-nums">{nums('b')}</div>
<div class="rm-axis">{ticks()}</div>
<div class="rm-arcs">{arcs('b')}</div>
</div>
<p class="rm-line-lab rm-b-text">{obj.format(s="b")}{lb}{count("b")}</p>
</div>
<details class="rm-check">
<summary>Check the answer</summary>
<p class="rm-feedback">{k} jumps of {ks} make {kv}, so {k} jumps of {us} make {uv}. Answer: {uv} {ul} {noun}.</p>
</details>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1040,"height":720}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''
    open(P+'/'+out,'w').write(html)
board('V05_ExampleA.dc.html','V05 Example A: double number line','by',BEAD,'blue','yellow',2,3,4,'b','2 blue beads go with 3 yellow beads. How many yellow beads go with 8 blue beads?')
board('V05_ExampleB.dc.html','V05 Example B: double number line','rw',BEAD,'red','white',3,2,5,'a','3 red beads go with 2 white beads. How many red beads go with 10 white beads?')
board('V05_SkinBlocks.dc.html','V05 Skin test: blocks','byk',BLOCK,'blue','yellow',2,3,4,'b','2 blue blocks go with 3 yellow blocks. How many yellow blocks go with 8 blue blocks?')
import os
if os.path.exists(P+'/canvas.json'):
    c=json.load(open(P+'/canvas.json'))
    for i,(f,t) in enumerate([("V05_ExampleA.dc.html","V05 Example A · 2:3, find 8 : ?"),("V05_ExampleB.dc.html","V05 Example B · 3:2, find ? : 10"),("V05_SkinBlocks.dc.html","V05 Skin test · blocks 2:3")]):
        c['boards'][f]={"x":i*1120,"y":7720,"w":1040,"h":720,"title":t,"expand":"fill","is_interactive":True}
        if f not in c['order']: c['order'].append(f)
    c['notes']['v05heading']={"x":0,"y":7480,"text":"V05 Double Number Line — jumps in step","kind":"title1","maxW":3280}
    c['boards']['V04_BuildSpec.dc.html']={"x":3360,"y":6520,"w":1040,"h":1000,"title":"V04 build sheet","expand":"fill"}
    if 'V04_BuildSpec.dc.html' not in c['order']: c['order'].append('V04_BuildSpec.dc.html')
    json.dump(c,open(P+'/canvas.json','w'),indent=2,ensure_ascii=False)
print('ok')
