import sys, json, os
P=sys.argv[1]
def f3(x): return f"{x:.3f}".rstrip('0').rstrip('.')
BEAD='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><circle class="rm-body" cx="16" cy="16" r="14"></circle><circle class="rm-detail" cx="16" cy="16" r="4.5"></circle></svg>'
BLOCK='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><rect class="rm-body" x="2" y="2" width="28" height="28" rx="4"></rect><rect class="rm-detail" x="9" y="9" width="14" height="14" rx="2"></rect></svg>'
VARS={
 'by':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#FFFFFF;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FFFFFF;--rm-b-text:#6E5000;--rm-thread:#9AA1AE;",
 'byk':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#4C7FE6;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FAD55C;--rm-b-text:#6E5000;--rm-thread:transparent;",
 'rw':"--rm-a:#C8322B;--rm-a-edge:#8C1E19;--rm-a-detail:#FFFFFF;--rm-a-text:#B02A23;--rm-b:#FFFFFF;--rm-b-edge:#2F3440;--rm-b-detail:#DFE3E9;--rm-b-text:#2F3440;--rm-thread:#9AA1AE;",
}
def board(out,title,vk,obj,seq,la,lb,question):
    A=seq.count('a'); N=len(seq); noun='blocks' if obj==BLOCK else 'beads'
    t=0.3; hl={i:[] for i in range(N)}; num=[]; den=[]
    for i,s in enumerate(seq):
        if s=='a':
            hl[i].append(t); num.append(f'<span class="rm-fb rm-pop" style="animation-delay: {f3(t)}s">{obj.format(s="a")}</span>'); t+=0.45
    t_num=t; t+=0.5
    for i,s in enumerate(seq):
        hl[i].append(t); den.append(f'<span class="rm-fb rm-pop" style="animation-delay: {f3(t)}s">{obj.format(s=s)}</span>'); t+=0.32
    t_den=t; t_end=t+0.6
    string=''.join(f'<span class="rm-sb">{obj.format(s=s)}'+''.join(f'<span class="rm-ring" style="animation-delay: {f3(d)}s"></span>' for d in hl[i])+'</span>' for i,s in enumerate(seq))
    def ans(v,d): return f'<span class="rm-ans"><span class="rm-hide rm-unknown">?</span><span class="rm-late rm-unknown" style="animation-delay: {f3(d)}s">?</span><span class="rm-reveal" style="animation-delay: {f3(d)}s">{v}</span></span>'
    order=', '.join({'a':la,'b':lb}[s] for s in seq)
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
.ratio-master .rm-question{{max-width:34ch;margin:0 auto 26px;text-align:center;font-size:clamp(20px,3vw,26px);font-weight:700;line-height:1.3}}
.ratio-master .rm-string{{position:relative;display:flex;flex-wrap:wrap;justify-content:center;gap:8px;width:max-content;max-width:100%;margin:0 auto 34px;padding:4px 14px}}
.ratio-master .rm-string::before{{content:"";position:absolute;left:0;right:0;top:50%;height:2px;margin-top:-1px;background:var(--rm-thread)}}
.ratio-master .rm-sb{{position:relative;display:block;width:40px;height:40px}}
.ratio-master .rm-sb .rm-obj{{width:40px;height:40px}}
.ratio-master .rm-ring{{position:absolute;inset:-6px;border:4px solid var(--rm-ink);border-radius:50%;opacity:0}}
.ratio-master .rm-obj{{display:block;width:40px;height:40px;flex:none}}
.ratio-master .rm-obj .rm-body{{stroke-width:2}}
.ratio-master .rm-obj .rm-detail{{stroke-width:1.5}}
.ratio-master .rm-obj-a .rm-body{{fill:var(--rm-a);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-a .rm-detail{{fill:var(--rm-a-detail);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-b .rm-body{{fill:var(--rm-b);stroke:var(--rm-b-edge)}}
.ratio-master .rm-obj-b .rm-detail{{fill:var(--rm-b-detail);stroke:var(--rm-b-edge)}}
.ratio-master .rm-a-text{{color:var(--rm-a-text)}}
.ratio-master .rm-frac{{display:grid;grid-template-columns:auto auto auto;align-items:center;justify-content:center;column-gap:22px;row-gap:10px}}
.ratio-master .rm-flab{{font-size:19px;font-weight:700;text-align:right}}
.ratio-master .rm-frow{{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;min-height:44px;min-width:{N*48}px;max-width:min(100%, {N*48}px)}}
.ratio-master .rm-fbar{{grid-column:2;height:5px;border-radius:3px;background:var(--rm-ink)}}
.ratio-master .rm-fbar-n{{grid-column:3;height:5px;border-radius:3px;background:var(--rm-ink)}}
.ratio-master .rm-fnum{{grid-column:3;text-align:center;font-size:clamp(34px,6vw,48px);font-weight:800;line-height:1.15}}
.ratio-master .rm-fb{{display:block}}
.ratio-master .rm-ans{{position:relative;display:inline-flex;align-items:center;justify-content:center;min-width:60px;padding:0 10px;outline:3px solid var(--rm-ink);border-radius:12px;font-variant-numeric:tabular-nums}}
.ratio-master .rm-unknown{{color:var(--rm-muted)}}
.ratio-master .rm-say{{margin:26px 0 0;text-align:center;font-size:clamp(20px,3vw,26px);font-weight:800}}
.ratio-master .rm-pop,.ratio-master .rm-say{{opacity:0}}
.ratio-master .rm-reveal,.ratio-master .rm-late{{display:none}}
.ratio-master .rm-check{{max-width:560px;margin:22px auto 0;text-align:center}}
.ratio-master .rm-check summary{{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:10px 24px;border:2px solid var(--rm-ink);border-radius:999px;background:#FFFFFF;font-size:18px;font-weight:700;cursor:pointer;list-style:none}}
.ratio-master .rm-check summary::-webkit-details-marker{{display:none}}
.ratio-master .rm-check summary:focus-visible{{outline:3px solid var(--rm-focus);outline-offset:3px}}
.ratio-master .rm-check[open] summary{{background:var(--rm-panel)}}
.ratio-master .rm-feedback{{margin:14px 0 0;font-size:18px}}
.ratio-master:has(.rm-check[open]) .rm-pop{{animation:rm-pop .35s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-ring{{animation:rm-ring .45s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-say{{animation:rm-fade .5s ease-out {f3(t_end)}s both}}
.ratio-master:has(.rm-check[open]) .rm-hide{{display:none}}
.ratio-master:has(.rm-check[open]) .rm-reveal{{display:inline;animation:rm-fade .4s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-late{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;border-radius:12px;background:#FFFFFF;animation:rm-gone .3s ease-out both}}
.ratio-master .rm-sr{{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}}
@keyframes rm-pop{{from{{opacity:0;transform:scale(.4)}}to{{opacity:1;transform:none}}}}
@keyframes rm-ring{{0%{{opacity:0;transform:scale(1.3)}}40%{{opacity:1;transform:none}}100%{{opacity:0}}}}
@keyframes rm-fade{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes rm-gone{{from{{opacity:1}}to{{opacity:0}}}}
@media (prefers-reduced-motion: reduce){{.ratio-master:has(.rm-check[open]) .rm-pop,.ratio-master:has(.rm-check[open]) .rm-say{{animation:none;opacity:1}}.ratio-master:has(.rm-check[open]) .rm-ring,.ratio-master .rm-reveal{{animation:none !important}}.ratio-master:has(.rm-check[open]) .rm-late{{display:none}}}}
@media (max-width: 520px){{.ratio-master .rm-frac{{column-gap:10px}}.ratio-master .rm-flab{{font-size:15px}}.ratio-master .rm-frow{{min-width:0}}}}
</style>
</helmet>
<div class="ratio-master" data-master="V01F" data-skin="{'blocks' if obj==BLOCK else 'beads'}">
<h2 class="rm-question">{question}</h2>
<p class="rm-sr">A string of {N} {noun}: {order}. The {A} {la} {noun} go above the fraction bar; all {N} {noun} go below it.</p>
<div class="rm-string" aria-hidden="true">{string}</div>
<div class="rm-frac" aria-hidden="true">
<span class="rm-flab rm-a-text">{la} {noun}</span><div class="rm-frow">{''.join(num)}</div><span class="rm-fnum">{ans(A,t_num)}</span>
<span></span><span class="rm-fbar"></span><span class="rm-fbar-n"></span>
<span class="rm-flab">all {noun}</span><div class="rm-frow">{''.join(den)}</div><span class="rm-fnum">{ans(N,t_den)}</span>
</div>
<p class="rm-say" aria-hidden="true">{A}/{N} of the {noun} are {la}.</p>
<details class="rm-check">
<summary>Check the answer</summary>
<p class="rm-feedback">Put the {A} {la} {noun} on top (the part) and all {N} {noun} on the bottom (the whole). Answer: {A}/{N} of the {noun} are {la}.</p>
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
board('V01F_ExampleA.dc.html','V01F Example A: blue over all beads','by',BEAD,'ababa','blue','yellow','What fraction of the beads are blue?')
board('V01F_ExampleB.dc.html','V01F Example B: red over all beads','rw',BEAD,'ababbabab','red','white','What fraction of the beads are red?')
board('V01F_SkinBlocks.dc.html','V01F Skin test: blocks','byk',BLOCK,'ababa','blue','yellow','What fraction of the blocks are blue?')
if os.path.exists(P+'/canvas.json'):
    c=json.load(open(P+'/canvas.json'))
    for i,(f,t) in enumerate([("V01F_ExampleA.dc.html","V01F Example A · blue / all = 3/5"),("V01F_ExampleB.dc.html","V01F Example B · red / all = 4/9"),("V01F_SkinBlocks.dc.html","V01F Skin test · blocks 3/5")]):
        c['boards'][f]={**c['boards'].get(f,{}),"x":i*1120,"y":15220,"w":1040,"h":720,"title":t,"expand":"fill","is_interactive":True}
        if f not in c['order']: c['order'].append(f)
    c['notes']['v01fheading']={"x":0,"y":14980,"text":"V01F Part over whole — fraction model","kind":"title1","maxW":3280}
    json.dump(c,open(P+'/canvas.json','w'),indent=2,ensure_ascii=False)
print('ok')
