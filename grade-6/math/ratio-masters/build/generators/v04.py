import sys, json
P=sys.argv[1]
BEAD='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><circle class="rm-body" cx="16" cy="16" r="14"></circle><circle class="rm-detail" cx="16" cy="16" r="4.5"></circle></svg>'
BLOCK='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><rect class="rm-body" x="2" y="2" width="28" height="28" rx="4"></rect><rect class="rm-detail" x="9" y="9" width="14" height="14" rx="2"></rect></svg>'
VARS={
 'by':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#FFFFFF;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FFFFFF;--rm-b-text:#6E5000;",
 'byk':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#4C7FE6;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FAD55C;--rm-b-text:#6E5000;",
 'rw':"--rm-a:#C8322B;--rm-a-edge:#8C1E19;--rm-a-detail:#FFFFFF;--rm-a-text:#B02A23;--rm-b:#FFFFFF;--rm-b-edge:#2F3440;--rm-b-detail:#DFE3E9;--rm-b-text:#2F3440;",
}
HEADL='<svg class="rm-head-arrow" viewBox="0 0 16 16" focusable="false"><path d="M2 3 L13 8 L2 13"></path></svg>'
def board(out,title,vk,obj,la,lb,A,B,mults,target,question):
    rows=[(A*m,B*m) for m in mults]
    base=0; f=mults[target]//mults[base]
    assert rows[target][0]==rows[base][0]*f and rows[target][1]==rows[base][1]*f
    noun='blocks' if obj==BLOCK else 'beads'
    ta,tb=rows[target]
    g=[]
    g.append(f'<div class="rm-th" style="grid-column: 2; grid-row: 1">{obj.format(s="a")}<span class="rm-a-text">{la}</span></div>')
    g.append(f'<div class="rm-th" style="grid-column: 3; grid-row: 1">{obj.format(s="b")}<span class="rm-b-text">{lb}</span></div>')
    for i,(a,b) in enumerate(rows):
        r=i+2
        hl=' rm-hl' if i in (base,target) else ''
        g.append(f'<div class="rm-td rm-a-text{hl}" style="grid-column: 2; grid-row: {r}">{a}</div>')
        if i==target:
            g.append(f'<div class="rm-td{hl}" style="grid-column: 3; grid-row: {r}"><span class="rm-ans rm-b-text"><span class="rm-late rm-unknown">?</span><span class="rm-reveal rm-d2">{b}</span><span class="rm-hide rm-unknown">?</span></span></div>')
        else:
            g.append(f'<div class="rm-td rm-b-text{hl}" style="grid-column: 3; grid-row: {r}">{b}</div>')
    span=f'{base+2} / {target+3}'
    g.append(f'<div class="rm-arr rm-arr-l rm-reveal rm-grow" style="grid-column: 1; grid-row: {span}"><span class="rm-chip">× {f}</span><span class="rm-bracket">{HEADL}</span></div>')
    g.append(f'<div class="rm-arr rm-arr-r rm-reveal rm-slide" style="grid-column: 4; grid-row: {span}"><span class="rm-bracket">{HEADL}</span><span class="rm-chip">× {f}</span></div>')
    rowtxt='; '.join(f'{a} {la}, {b if i!=target else "unknown"} {lb}' for i,(a,b) in enumerate(rows))
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
.ratio-master{{--rm-ink:#1B1F2A;--rm-muted:#4A5263;--rm-panel:#F3F4F7;--rm-rule:#D7DBE2;--rm-hl:#FFF3C4;--rm-focus:#1E5BD8;
--rm-arrow-w:120px;--rm-col:130px;
{VARS[vk]}
box-sizing:border-box;max-width:1040px;margin:0 auto;padding:40px 16px 48px;background:#FFFFFF;color:var(--rm-ink);font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.4}}
.ratio-master *,.ratio-master *::before,.ratio-master *::after{{box-sizing:border-box}}
.ratio-master .rm-question{{max-width:34ch;margin:0 auto 28px;text-align:center;font-size:clamp(20px,3vw,26px);font-weight:700;line-height:1.3}}
.ratio-master .rm-grid{{display:grid;grid-template-columns:var(--rm-arrow-w) var(--rm-col) var(--rm-col) var(--rm-arrow-w);grid-auto-rows:64px;justify-content:center}}
.ratio-master .rm-th{{display:flex;align-items:center;justify-content:center;gap:8px;border-bottom:3px solid var(--rm-ink);font-size:20px;font-weight:700}}
.ratio-master .rm-td{{display:flex;align-items:center;justify-content:center;border-bottom:1px solid var(--rm-rule);font-size:clamp(28px,5vw,36px);font-weight:800;font-variant-numeric:tabular-nums;transition:background-color .4s}}
.ratio-master .rm-td[style*="grid-column: 2"]{{border-right:2px solid var(--rm-rule)}}
.ratio-master .rm-ans{{position:relative;display:inline-flex;align-items:center;justify-content:center;min-width:64px;padding:0 10px;outline:3px solid var(--rm-ink);border-radius:12px;line-height:1.25}}
.ratio-master .rm-unknown{{color:var(--rm-muted)}}
.ratio-master .rm-arr{{position:relative;display:flex;align-items:stretch;padding:32px 0}}
.ratio-master .rm-arr-l{{justify-content:flex-end;padding-right:6px}}
.ratio-master .rm-arr-r{{justify-content:flex-start;padding-left:6px}}
.ratio-master .rm-bracket{{position:relative;width:22px;border:3px solid var(--rm-ink)}}
.ratio-master .rm-arr-l .rm-bracket{{border-right:none;border-radius:16px 0 0 16px}}
.ratio-master .rm-arr-r .rm-bracket{{border-left:none;border-radius:0 16px 16px 0}}
.ratio-master .rm-head-arrow{{position:absolute;bottom:-9px;width:16px;height:16px;fill:none;stroke:var(--rm-ink);stroke-width:3;stroke-linecap:round;stroke-linejoin:round}}
.ratio-master .rm-arr-l .rm-head-arrow{{right:-8px}}
.ratio-master .rm-arr-r .rm-head-arrow{{left:-8px;transform:scaleX(-1)}}
.ratio-master .rm-chip{{align-self:center;margin:0 8px;padding:6px 12px;border:3px solid var(--rm-ink);border-radius:14px;background:var(--rm-panel);font-size:22px;font-weight:800;white-space:nowrap}}
.ratio-master .rm-reveal{{display:none}}
.ratio-master .rm-check{{max-width:520px;margin:28px auto 0;text-align:center}}
.ratio-master .rm-check summary{{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:10px 24px;border:2px solid var(--rm-ink);border-radius:999px;background:#FFFFFF;font-size:18px;font-weight:700;cursor:pointer;list-style:none}}
.ratio-master .rm-check summary::-webkit-details-marker{{display:none}}
.ratio-master .rm-check summary:focus-visible{{outline:3px solid var(--rm-focus);outline-offset:3px}}
.ratio-master .rm-check[open] summary{{background:var(--rm-panel)}}
.ratio-master .rm-feedback{{margin:14px 0 0;font-size:18px}}
.ratio-master:has(.rm-check[open]) .rm-hide{{display:none}}
.ratio-master:has(.rm-check[open]) .rm-reveal{{display:flex}}
.ratio-master:has(.rm-check[open]) span.rm-reveal{{display:inline;animation:rm-pop .5s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-hl{{background:var(--rm-hl)}}
.ratio-master:has(.rm-check[open]) .rm-grow{{animation:rm-grow .6s ease-out .2s both;transform-origin:top}}
.ratio-master:has(.rm-check[open]) .rm-slide{{animation:rm-slide 1s ease-in-out 1s both}}
.ratio-master:has(.rm-check[open]) .rm-late{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;border-radius:12px;background:inherit;animation:rm-gone .3s ease-out 2.2s both}}
.ratio-master .rm-late{{display:none}}
.ratio-master .rm-d2{{animation-delay:2.2s !important}}
.ratio-master .rm-obj{{display:block;width:26px;height:26px;flex:none}}
.ratio-master .rm-obj .rm-body{{stroke-width:2}}
.ratio-master .rm-obj .rm-detail{{stroke-width:1.5}}
.ratio-master .rm-obj-a .rm-body{{fill:var(--rm-a);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-a .rm-detail{{fill:var(--rm-a-detail);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-b .rm-body{{fill:var(--rm-b);stroke:var(--rm-b-edge)}}
.ratio-master .rm-obj-b .rm-detail{{fill:var(--rm-b-detail);stroke:var(--rm-b-edge)}}
.ratio-master .rm-a-text{{color:var(--rm-a-text)}}
.ratio-master .rm-b-text{{color:var(--rm-b-text)}}
.ratio-master .rm-sr{{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}}
@keyframes rm-grow{{from{{opacity:0;transform:scaleY(.2)}}to{{opacity:1;transform:none}}}}
@keyframes rm-slide{{from{{transform:translateX(calc(-1 * (var(--rm-arrow-w) + 2 * var(--rm-col))))}}to{{transform:none}}}}
@keyframes rm-pop{{from{{opacity:0;transform:scale(.6)}}to{{opacity:1;transform:none}}}}
@keyframes rm-gone{{from{{opacity:1}}to{{opacity:0}}}}
@media (prefers-reduced-motion: reduce){{.ratio-master .rm-reveal,.ratio-master .rm-grow,.ratio-master .rm-slide{{animation:none !important}}.ratio-master:has(.rm-check[open]) .rm-late{{display:none}}.ratio-master .rm-td{{transition:none}}}}
@media (max-width: 480px){{.ratio-master{{--rm-arrow-w:76px;--rm-col:88px}}.ratio-master .rm-chip{{margin:0 4px;padding:4px 6px;font-size:17px}}.ratio-master .rm-bracket{{width:14px}}.ratio-master .rm-th{{font-size:16px}}.ratio-master .rm-obj{{width:20px;height:20px}}}}
</style>
</helmet>
<div class="ratio-master" data-master="V04" data-skin="{'blocks' if obj==BLOCK else 'beads'}">
<h2 class="rm-question">{question}</h2>
<p class="rm-sr">Ratio table of {la} and {lb} {noun}. Rows: {rowtxt}.</p>
<div class="rm-grid" aria-hidden="true">
{chr(10).join(g)}
</div>
<details class="rm-check">
<summary>Check the answer</summary>
<p class="rm-feedback">{rows[base][0]} × {f} = {ta}, so the same × {f} works on the {lb} column too. Answer: {tb} {lb} {noun}.</p>
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
board('V04_ExampleA.dc.html','V04 Example A: ratio table','by',BEAD,'blue','yellow',2,3,[1,2,3,5],3,'2 blue beads go with 3 yellow beads. How many yellow beads go with 10 blue beads?')
board('V04_ExampleB.dc.html','V04 Example B: ratio table','rw',BEAD,'red','white',3,2,[1,2,3,4],2,'3 red beads go with 2 white beads. How many white beads go with 9 red beads?')
board('V04_SkinBlocks.dc.html','V04 Skin test: blocks','byk',BLOCK,'blue','yellow',2,3,[1,2,3,5],3,'2 blue blocks go with 3 yellow blocks. How many yellow blocks go with 10 blue blocks?')
import os
if os.path.exists(P+'/canvas.json'):
    c=json.load(open(P+'/canvas.json'))
    for i,(f,t) in enumerate([("V04_ExampleA.dc.html","V04 Example A · blue:yellow 2:3, find 10 : ?"),("V04_ExampleB.dc.html","V04 Example B · red:white 3:2, find 9 : ?"),("V04_SkinBlocks.dc.html","V04 Skin test · blocks 2:3")]):
        c['boards'][f]={"x":i*1120,"y":6520,"w":1040,"h":720,"title":t,"expand":"fill","is_interactive":True}
        if f not in c['order']: c['order'].append(f)
    c['notes']['v04heading']={"x":0,"y":6280,"text":"V04 Ratio Table — same factor on both columns","kind":"title1","maxW":3280}
    c['boards']['V03_BuildSpec.dc.html']={"x":3360,"y":5220,"w":1040,"h":1100,"title":"V03 build sheet","expand":"fill"}
    if 'V03_BuildSpec.dc.html' not in c['order']: c['order'].append('V03_BuildSpec.dc.html')
    json.dump(c,open(P+'/canvas.json','w'),indent=2,ensure_ascii=False)
print('ok')
