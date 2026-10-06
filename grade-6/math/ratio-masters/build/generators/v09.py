import sys, json, os
P=sys.argv[1]
def f3(x): return f"{x:.3f}".rstrip('0').rstrip('.')
BEAD='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><circle class="rm-body" cx="16" cy="16" r="14"></circle><circle class="rm-detail" cx="16" cy="16" r="4.5"></circle></svg>'
BLOCK='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><rect class="rm-body" x="2" y="2" width="28" height="28" rx="4"></rect><rect class="rm-detail" x="9" y="9" width="14" height="14" rx="2"></rect></svg>'
VARS={
 'by':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#FFFFFF;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FFFFFF;--rm-b-text:#6E5000;",
 'byk':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#4C7FE6;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FAD55C;--rm-b-text:#6E5000;",
 'rw':"--rm-a:#C8322B;--rm-a-edge:#8C1E19;--rm-a-detail:#FFFFFF;--rm-a-text:#B02A23;--rm-b:#FFFFFF;--rm-b-edge:#2F3440;--rm-b-detail:#DFE3E9;--rm-b-text:#2F3440;",
}
def board(out,title,vk,obj,la,lb,A,B,k,xmax,xstep,ymax,ystep,question):
    rows=[(A*i,B*i) for i in range(1,k+1)]   # last row is asked
    for x,y in rows: assert x*B==y*A and x<=xmax and y<=ymax and xmax%xstep==0 and ymax%ystep==0
    W,H=300,240; L,T=56,16       # plot area and offsets in the SVG
    VW,VH=L+W+24,T+H+58
    X=lambda v: L+v*W/xmax; Y=lambda v: T+H-v*H/ymax
    g=[]
    for v in range(0,xmax+1,xstep):
        g.append(f'<line class="rm-grid" x1="{f3(X(v))}" y1="{T}" x2="{f3(X(v))}" y2="{T+H}"></line><text class="rm-tick" x="{f3(X(v))}" y="{T+H+22}" text-anchor="middle">{v}</text>')
    for v in range(0,ymax+1,ystep):
        g.append(f'<line class="rm-grid" x1="{L}" y1="{f3(Y(v))}" x2="{L+W}" y2="{f3(Y(v))}"></line><text class="rm-tick" x="{L-10}" y="{f3(Y(v)+6)}" text-anchor="end">{v}</text>')
    g.append(f'<line class="rm-axis" x1="{L}" y1="{T+H}" x2="{L+W}" y2="{T+H}"></line><line class="rm-axis" x1="{L}" y1="{T}" x2="{L}" y2="{T+H}"></line>')
    g.append(f'<text class="rm-axlab rm-a-fill" x="{L+W/2}" y="{T+H+48}" text-anchor="middle">{la} (x)</text>')
    g.append(f'<text class="rm-axlab rm-b-fill" x="16" y="{T+H/2}" text-anchor="middle" transform="rotate(-90 16 {T+H/2})">{lb} (y)</text>')
    step=1.3; t=0.3; trs=[]
    for i,(x,y) in enumerate(rows[:-1]):
        g.append(f'<path class="rm-guide rm-show" style="animation-delay: {f3(t+0.2)}s" d="M{f3(X(x))} {T+H} V{f3(Y(y))} H{L}"></path>')
        g.append(f'<circle class="rm-pt rm-pop" style="animation-delay: {f3(t+0.6)}s" cx="{f3(X(x))}" cy="{f3(Y(y))}" r="7"></circle>')
        g.append(f'<text class="rm-ptlab rm-show" style="animation-delay: {f3(t+0.7)}s" x="{f3(X(x)+10)}" y="{f3(Y(y)-10)}">({x}, {y})</text>')
        trs.append(t); t+=step
    ray=t
    xe=xmax; ye=xmax*B/A
    if ye>ymax: ye=ymax; xe=ymax*A/B
    g.append(f'<line class="rm-ray rm-show" style="animation-delay: {f3(ray)}s" x1="{L}" y1="{T+H}" x2="{f3(X(xe))}" y2="{f3(Y(ye))}"></line>')
    t+=0.9; tx,ty=rows[-1]; trs.append(t)
    g.append(f'<path class="rm-guide rm-guide-ans rm-show" style="animation-delay: {f3(t+0.2)}s" d="M{f3(X(tx))} {T+H} V{f3(Y(ty))}"></path>')
    g.append(f'<circle class="rm-pt rm-pt-ans rm-pop" style="animation-delay: {f3(t+0.7)}s" cx="{f3(X(tx))}" cy="{f3(Y(ty))}" r="8"></circle>')
    g.append(f'<path class="rm-guide rm-guide-ans rm-show" style="animation-delay: {f3(t+0.9)}s" d="M{f3(X(tx))} {f3(Y(ty))} H{L}"></path>')
    g.append(f'<circle class="rm-yring rm-pop" style="animation-delay: {f3(t+1.2)}s" cx="{L-22}" cy="{f3(Y(ty))}" r="16"></circle>')
    g.append(f'<text class="rm-ptlab rm-show" style="animation-delay: {f3(t+1.2)}s" x="{f3(X(tx)+11)}" y="{f3(Y(ty)-11)}">({tx}, {ty})</text>')
    done=t+1.4
    trows=[]
    for i,(x,y) in enumerate(rows):
        last=i==len(rows)-1
        ycell=(f'<span class="rm-ans"><span class="rm-hide rm-unknown">?</span><span class="rm-late rm-unknown" style="animation-delay: {f3(done)}s">?</span><span class="rm-reveal" style="animation-delay: {f3(done)}s">{y}</span></span>' if last else str(y))
        trows.append(f'<tr class="rm-tr" style="animation-delay: {f3(trs[i])}s"><td class="rm-a-text">{x}</td><td class="rm-b-text">{ycell}</td></tr>')
    noun='blocks' if obj==BLOCK else 'beads'
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
{VARS[vk]}
box-sizing:border-box;max-width:1040px;margin:0 auto;padding:40px 16px 48px;background:#FFFFFF;color:var(--rm-ink);font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.4}}
.ratio-master *,.ratio-master *::before,.ratio-master *::after{{box-sizing:border-box}}
.ratio-master .rm-question{{max-width:36ch;margin:0 auto 26px;text-align:center;font-size:clamp(20px,3vw,26px);font-weight:700;line-height:1.3}}
.ratio-master .rm-row{{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:28px 40px}}
.ratio-master .rm-table{{border-collapse:collapse;font-variant-numeric:tabular-nums}}
.ratio-master .rm-table th{{padding:6px 18px;border-bottom:3px solid var(--rm-ink);font-size:18px}}
.ratio-master .rm-table th span{{display:inline-flex;align-items:center;gap:6px}}
.ratio-master .rm-table td{{padding:6px 18px;border-bottom:1px solid var(--rm-rule);text-align:center;font-size:30px;font-weight:800}}
.ratio-master .rm-table td:first-child{{border-right:2px solid var(--rm-rule)}}
.ratio-master .rm-obj{{display:block;width:22px;height:22px}}
.ratio-master .rm-obj .rm-body{{stroke-width:2}}
.ratio-master .rm-obj .rm-detail{{stroke-width:1.5}}
.ratio-master .rm-obj-a .rm-body{{fill:var(--rm-a);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-a .rm-detail{{fill:var(--rm-a-detail);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-b .rm-body{{fill:var(--rm-b);stroke:var(--rm-b-edge)}}
.ratio-master .rm-obj-b .rm-detail{{fill:var(--rm-b-detail);stroke:var(--rm-b-edge)}}
.ratio-master .rm-a-text{{color:var(--rm-a-text)}}
.ratio-master .rm-b-text{{color:var(--rm-b-text)}}
.ratio-master .rm-graph{{display:block;width:min(100%, 460px);height:auto;overflow:visible}}
.ratio-master .rm-graph text{{font-family:system-ui,-apple-system,"Segoe UI",sans-serif}}
.ratio-master .rm-grid{{stroke:#E1E4EA;stroke-width:1.5}}
.ratio-master .rm-axis{{stroke:var(--rm-ink);stroke-width:3}}
.ratio-master .rm-tick{{font-size:15px;font-weight:700;fill:var(--rm-muted)}}
.ratio-master .rm-axlab{{font-size:17px;font-weight:800}}
.ratio-master .rm-a-fill{{fill:var(--rm-a-text)}}
.ratio-master .rm-b-fill{{fill:var(--rm-b-text)}}
.ratio-master .rm-guide{{fill:none;stroke:#7C8494;stroke-width:2;stroke-dasharray:6 5}}
.ratio-master .rm-guide-ans{{stroke:var(--rm-ink);stroke-width:2.5}}
.ratio-master .rm-ray{{stroke:#7C8494;stroke-width:2.5;stroke-dasharray:2 6;stroke-linecap:round}}
.ratio-master .rm-pt{{fill:var(--rm-ink);stroke:#FFFFFF;stroke-width:2.5;transform-box:fill-box;transform-origin:center}}
.ratio-master .rm-pt-ans{{fill:#FFFFFF;stroke:var(--rm-ink);stroke-width:4}}
.ratio-master .rm-yring{{fill:none;stroke:var(--rm-ink);stroke-width:3;transform-box:fill-box;transform-origin:center}}
.ratio-master .rm-ptlab{{font-size:15px;font-weight:700;fill:var(--rm-ink)}}
.ratio-master .rm-show,.ratio-master .rm-pop{{opacity:0}}
.ratio-master .rm-ans{{position:relative;display:inline-flex;align-items:center;justify-content:center;min-width:52px;padding:0 8px;outline:3px solid var(--rm-ink);border-radius:10px}}
.ratio-master .rm-unknown{{color:var(--rm-muted)}}
.ratio-master .rm-reveal,.ratio-master .rm-late{{display:none}}
.ratio-master .rm-check{{max-width:560px;margin:22px auto 0;text-align:center}}
.ratio-master .rm-check summary{{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:10px 24px;border:2px solid var(--rm-ink);border-radius:999px;background:#FFFFFF;font-size:18px;font-weight:700;cursor:pointer;list-style:none}}
.ratio-master .rm-check summary::-webkit-details-marker{{display:none}}
.ratio-master .rm-check summary:focus-visible{{outline:3px solid var(--rm-focus);outline-offset:3px}}
.ratio-master .rm-check[open] summary{{background:var(--rm-panel)}}
.ratio-master .rm-feedback{{margin:14px 0 0;font-size:18px}}
.ratio-master:has(.rm-check[open]) .rm-show{{animation:rm-fade .5s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-pop{{animation:rm-pop .4s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-tr{{animation:rm-rowhl 1.3s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-hide{{display:none}}
.ratio-master:has(.rm-check[open]) .rm-reveal{{display:inline;animation:rm-fade .4s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-late{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;border-radius:10px;background:#FFFFFF;animation:rm-gone .3s ease-out both}}
.ratio-master .rm-sr{{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}}
@keyframes rm-fade{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes rm-pop{{from{{opacity:0;transform:scale(0)}}to{{opacity:1;transform:none}}}}
@keyframes rm-rowhl{{0%{{background:transparent}}15%{{background:var(--rm-hl)}}75%{{background:var(--rm-hl)}}100%{{background:transparent}}}}
@keyframes rm-gone{{from{{opacity:1}}to{{opacity:0}}}}
@media (prefers-reduced-motion: reduce){{.ratio-master:has(.rm-check[open]) .rm-show,.ratio-master:has(.rm-check[open]) .rm-pop{{animation:none;opacity:1}}.ratio-master:has(.rm-check[open]) .rm-tr,.ratio-master .rm-reveal{{animation:none !important}}.ratio-master:has(.rm-check[open]) .rm-late{{display:none}}}}
</style>
</helmet>
<div class="ratio-master" data-master="V09" data-skin="{'blocks' if obj==BLOCK else 'beads'}">
<h2 class="rm-question">{question}</h2>
<p class="rm-sr">Table of {la} and {lb} {noun}: {"; ".join(f"{x} and {y}" for x,y in rows[:-1])}; {rows[-1][0]} and unknown. Graph: {la} on the x-axis from 0 to {xmax}, {lb} on the y-axis from 0 to {ymax}.</p>
<div class="rm-row">
<table class="rm-table"><thead><tr><th scope="col"><span>{obj.format(s="a")}{la} (x)</span></th><th scope="col"><span>{obj.format(s="b")}{lb} (y)</span></th></tr></thead><tbody>
{chr(10).join(trows)}
</tbody></table>
<svg class="rm-graph" viewBox="0 0 {VW} {VH}" aria-hidden="true" focusable="false">
{chr(10).join(g)}
</svg>
</div>
<details class="rm-check">
<summary>Check the answer</summary>
<p class="rm-feedback">Each row is a point (x, y). The points line up on a straight line that starts at (0, 0). Go up from {tx} to the line, then across: y = {ty}. Answer: {ty} {lb} {noun}.</p>
</details>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1040,"height":760}}}}'>
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
board('V09_ExampleA.dc.html','V09 Example A: table to graph','by',BEAD,'blue','yellow',2,3,4,10,2,15,3,
      '2 blue beads go with 3 yellow beads. Use the graph: how many yellow beads go with 8 blue beads?')
board('V09_ExampleB.dc.html','V09 Example B: table to graph','rw',BEAD,'red','white',3,2,4,15,3,10,2,
      '3 red beads go with 2 white beads. Use the graph: how many white beads go with 12 red beads?')
board('V09_SkinBlocks.dc.html','V09 Skin test: blocks','byk',BLOCK,'blue','yellow',2,3,4,10,2,15,3,
      '2 blue blocks go with 3 yellow blocks. Use the graph: how many yellow blocks go with 8 blue blocks?')
if os.path.exists(P+'/canvas.json'):
    c=json.load(open(P+'/canvas.json'))
    for i,(f,t) in enumerate([("V09_ExampleA.dc.html","V09 Example A · 2:3, find (8, ?)"),("V09_ExampleB.dc.html","V09 Example B · 3:2, find (12, ?)"),("V09_SkinBlocks.dc.html","V09 Skin test · blocks 2:3")]):
        c['boards'][f]={**c['boards'].get(f,{}),"x":i*1120,"y":13980,"w":1040,"h":760,"title":t,"expand":"fill","is_interactive":True}
        if f not in c['order']: c['order'].append(f)
    c['notes']['v09heading']={"x":0,"y":13740,"text":"V09 Table to Graph — plot equivalent pairs","kind":"title1","maxW":3280}
    json.dump(c,open(P+'/canvas.json','w'),indent=2,ensure_ascii=False)
print('ok')
