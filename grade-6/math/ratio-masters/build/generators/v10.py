import sys, json, os
P=sys.argv[1]
def f3(x): return f"{x:.3f}".rstrip('0').rstrip('.')
BEAD='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><circle class="rm-body" cx="16" cy="16" r="14"></circle><circle class="rm-detail" cx="16" cy="16" r="4.5"></circle></svg>'
BLOCK='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><rect class="rm-body" x="2" y="2" width="28" height="28" rx="4"></rect><rect class="rm-detail" x="9" y="9" width="14" height="14" rx="2"></rect></svg>'
VARS={
 'by':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#FFFFFF;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FFFFFF;--rm-b-text:#6E5000;--rm-thread:#9AA1AE;",
 'byk':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#4C7FE6;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FAD55C;--rm-b-text:#6E5000;--rm-thread:#9AA1AE;",
 'rw':"--rm-a:#C8322B;--rm-a-edge:#8C1E19;--rm-a-detail:#FFFFFF;--rm-a-text:#B02A23;--rm-b:#FFFFFF;--rm-b-edge:#2F3440;--rm-b-detail:#DFE3E9;--rm-b-text:#2F3440;--rm-thread:#9AA1AE;",
}
def board(out,title,vk,obj,la,lb,A,B,haveA,haveB,claim,who,item,cols):
    noun='blocks' if obj==BLOCK else 'beads'
    can=min(haveA//A, haveB//B); assert can<claim
    short = 'a' if haveA//A < haveB//B else 'b'
    lshort = la if short=='a' else lb
    t=0.3; ua=ub=0; trayA=['']*haveA; trayB=['']*haveB; neck=[]
    for k in range(claim):
        slots=[]; ok=True
        for j in range(A+B):
            side='a' if j<A else 'b'
            if side=='a' and ua<haveA:
                trayA[ua]=f3(t); ua+=1; slots.append(f'<span class="rm-slot"><span class="rm-place" style="animation-delay: {f3(t)}s">{obj.format(s="a")}</span></span>')
            elif side=='b' and ub<haveB:
                trayB[ub]=f3(t); ub+=1; slots.append(f'<span class="rm-slot"><span class="rm-place" style="animation-delay: {f3(t)}s">{obj.format(s="b")}</span></span>')
            else:
                ok=False; slots.append(f'<span class="rm-slot rm-slot-{side}"><span class="rm-miss" style="animation-delay: {f3(t)}s"></span></span>')
            t+=0.22
        tag = (f'<span class="rm-tag rm-tag-ok" style="animation-delay: {f3(t)}s">complete</span>' if ok
               else f'<span class="rm-tag rm-tag-short" style="animation-delay: {f3(t)}s">not enough {lshort}</span>')
        neck.append(f'<div class="rm-neck"><p class="rm-nlab">{item.capitalize()} {k+1}{tag}</p><div class="rm-thread">{"".join(slots)}</div></div>')
        t+=0.35
    done=t+0.2
    def tray(items,s,have):
        return ''.join(f'<span class="rm-tb"{(" style=" + chr(34) + "animation-delay: " + d + "s" + chr(34)) if d else ""}>{obj.format(s=s)}</span>'.replace('class="rm-tb" style','class="rm-tb rm-used" style') for d in items)
    leftA,leftB=haveA-ua,haveB-ub
    def ans(v,d): return f'<span class="rm-ans"><span class="rm-hide rm-unknown">?</span><span class="rm-late rm-unknown" style="animation-delay: {f3(d)}s">?</span><span class="rm-reveal" style="animation-delay: {f3(d)}s">{v}</span></span>'
    question=f'Each {item} needs {A} {la} and {B} {lb} {noun}. {who} has {haveA} {la} and {haveB} {lb} {noun}. {who} says that makes {claim} {item}s. Is that right?'
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
.ratio-master{{--rm-ink:#1B1F2A;--rm-muted:#4A5263;--rm-panel:#F3F4F7;--rm-focus:#1E5BD8;--rm-warn:#B42318;
{VARS[vk]}
box-sizing:border-box;max-width:1040px;margin:0 auto;padding:36px 16px 48px;background:#FFFFFF;color:var(--rm-ink);font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.4}}
.ratio-master *,.ratio-master *::before,.ratio-master *::after{{box-sizing:border-box}}
.ratio-master .rm-question{{max-width:44ch;margin:0 auto 12px;text-align:center;font-size:clamp(19px,2.8vw,24px);font-weight:700;line-height:1.3}}
.ratio-master .rm-recipe{{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:6px 10px;width:max-content;max-width:100%;margin:0 auto 22px;padding:6px 16px;border:2px solid #D7DBE2;border-radius:999px;font-size:17px;font-weight:700}}
.ratio-master .rm-recipe .rm-obj{{width:24px;height:24px}}
.ratio-master .rm-recipe span{{display:inline-flex;gap:3px}}
.ratio-master .rm-top{{display:flex;flex-wrap:wrap;justify-content:center;gap:16px 28px;margin-bottom:22px}}
.ratio-master .rm-tray{{padding:10px 14px 12px;border-radius:16px;background:var(--rm-panel);text-align:center}}
.ratio-master .rm-tray h3{{margin:0 0 8px;font-size:17px}}
.ratio-master .rm-tgrid{{display:grid;grid-template-columns:repeat({cols}, 34px);gap:6px;justify-content:center}}
.ratio-master .rm-tb{{display:block;width:34px;height:34px}}
.ratio-master .rm-left{{margin:8px 0 0;font-size:16px;font-weight:800;min-height:24px}}
.ratio-master .rm-left-0{{color:var(--rm-warn)}}
.ratio-master .rm-necks{{display:grid;grid-template-columns:repeat(auto-fit, minmax(230px, 1fr));gap:14px 22px;max-width:900px;margin:0 auto}}
.ratio-master .rm-neck{{padding:8px 12px 12px;border:2px solid #D7DBE2;border-radius:16px}}
.ratio-master .rm-nlab{{display:flex;align-items:center;justify-content:space-between;gap:8px;margin:0 0 6px;font-size:16px;font-weight:800}}
.ratio-master .rm-tag{{padding:2px 10px;border-radius:999px;font-size:13px;font-weight:800;opacity:0}}
.ratio-master .rm-tag-ok{{background:var(--rm-ink);color:#FFFFFF}}
.ratio-master .rm-tag-short{{background:var(--rm-warn);color:#FFFFFF}}
.ratio-master .rm-thread{{position:relative;display:flex;justify-content:center;gap:6px;padding:2px 6px}}
.ratio-master .rm-thread::before{{content:"";position:absolute;left:0;right:0;top:50%;height:2px;margin-top:-1px;background:var(--rm-thread)}}
.ratio-master .rm-slot{{position:relative;display:block;width:36px;height:36px;border:2px dashed #AEB4BF;border-radius:{"8px" if obj==BLOCK else "50%"};background:#FFFFFF}}
.ratio-master .rm-place{{position:absolute;inset:-2px;opacity:0}}
.ratio-master .rm-miss{{position:absolute;inset:-5px;border:3px dashed var(--rm-warn);border-radius:{"10px" if obj==BLOCK else "50%"};opacity:0}}
.ratio-master .rm-obj{{display:block;width:100%;height:100%}}
.ratio-master .rm-obj .rm-body{{stroke-width:2}}
.ratio-master .rm-obj .rm-detail{{stroke-width:1.5}}
.ratio-master .rm-obj-a .rm-body{{fill:var(--rm-a);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-a .rm-detail{{fill:var(--rm-a-detail);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-b .rm-body{{fill:var(--rm-b);stroke:var(--rm-b-edge)}}
.ratio-master .rm-obj-b .rm-detail{{fill:var(--rm-b-detail);stroke:var(--rm-b-edge)}}
.ratio-master .rm-a-text{{color:var(--rm-a-text)}}
.ratio-master .rm-b-text{{color:var(--rm-b-text)}}
.ratio-master .rm-answer{{margin:22px 0 0;text-align:center;font-size:clamp(22px,3.4vw,28px);font-weight:800}}
.ratio-master .rm-ans{{position:relative;display:inline-flex;align-items:center;justify-content:center;min-width:52px;margin:0 4px;padding:0 10px;outline:3px solid var(--rm-ink);border-radius:12px;font-variant-numeric:tabular-nums}}
.ratio-master .rm-unknown{{color:var(--rm-muted)}}
.ratio-master .rm-reveal,.ratio-master .rm-late,.ratio-master .rm-left span{{display:none}}
.ratio-master .rm-check{{max-width:600px;margin:20px auto 0;text-align:center}}
.ratio-master .rm-check summary{{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:10px 24px;border:2px solid var(--rm-ink);border-radius:999px;background:#FFFFFF;font-size:18px;font-weight:700;cursor:pointer;list-style:none}}
.ratio-master .rm-check summary::-webkit-details-marker{{display:none}}
.ratio-master .rm-check summary:focus-visible{{outline:3px solid var(--rm-focus);outline-offset:3px}}
.ratio-master .rm-check[open] summary{{background:var(--rm-panel)}}
.ratio-master .rm-feedback{{margin:14px 0 0;font-size:18px}}
.ratio-master:has(.rm-check[open]) .rm-used{{animation:rm-use .3s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-place{{animation:rm-pop .3s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-miss{{animation:rm-miss .6s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-tag{{animation:rm-fade .4s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-left span{{display:inline;animation:rm-fade .4s ease-out {f3(done)}s both}}
.ratio-master:has(.rm-check[open]) .rm-hide{{display:none}}
.ratio-master:has(.rm-check[open]) .rm-reveal{{display:inline;animation:rm-fade .4s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-late{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;border-radius:12px;background:#FFFFFF;animation:rm-gone .3s ease-out both}}
.ratio-master .rm-sr{{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}}
@keyframes rm-use{{from{{opacity:1}}to{{opacity:.15}}}}
@keyframes rm-pop{{from{{opacity:0;transform:scale(.4)}}to{{opacity:1;transform:none}}}}
@keyframes rm-miss{{0%{{opacity:0;transform:scale(1.4)}}60%{{opacity:1;transform:none}}100%{{opacity:1}}}}
@keyframes rm-fade{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes rm-gone{{from{{opacity:1}}to{{opacity:0}}}}
@media (prefers-reduced-motion: reduce){{.ratio-master:has(.rm-check[open]) .rm-used{{animation:none;opacity:.15}}.ratio-master:has(.rm-check[open]) .rm-place,.ratio-master:has(.rm-check[open]) .rm-miss,.ratio-master:has(.rm-check[open]) .rm-tag{{animation:none;opacity:1}}.ratio-master .rm-reveal,.ratio-master:has(.rm-check[open]) .rm-left span{{animation:none !important}}.ratio-master:has(.rm-check[open]) .rm-late{{display:none}}}}
</style>
</helmet>
<div class="ratio-master" data-master="V10" data-skin="{'blocks' if obj==BLOCK else 'beads'}">
<h2 class="rm-question">{question}</h2>
<p class="rm-recipe">1 {item}: <span>{obj.format(s="a")*A}</span> + <span>{obj.format(s="b")*B}</span></p>
<p class="rm-sr">{haveA} {la} and {haveB} {lb} {noun} are shared into {claim} {item}s, {A} {la} and {B} {lb} each.</p>
<div class="rm-top" aria-hidden="true">
<div class="rm-tray"><h3 class="rm-a-text">{haveA} {la}</h3><div class="rm-tgrid">{tray(trayA,"a",haveA)}</div><p class="rm-left{" rm-left-0" if leftA==0 else ""}"><span>{leftA} left</span></p></div>
<div class="rm-tray"><h3 class="rm-b-text">{haveB} {lb}</h3><div class="rm-tgrid">{tray(trayB,"b",haveB)}</div><p class="rm-left{" rm-left-0" if leftB==0 else ""}"><span>{leftB} left</span></p></div>
</div>
<div class="rm-necks" aria-hidden="true">{''.join(neck)}</div>
<p class="rm-answer">{who} can make {ans(can,done)} {item}s.</p>
<details class="rm-check">
<summary>Check the answer</summary>
<p class="rm-feedback">No. Each {item} uses {A if short=='a' else B} {lshort} {noun}, and {haveA if short=='a' else haveB} {lshort} {noun} only make {can} {item}s ({can} × {A if short=='a' else B} = {can*(A if short=='a' else B)}). {item.capitalize()} {claim} runs out of {lshort}. Answer: {can} {item}s, not {claim}.</p>
</details>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1040,"height":900}}}}'>
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
board('V10_ExampleA.dc.html','V10 Example A: necklace shortage','by',BEAD,'blue','yellow',2,3,8,9,4,'Maya','necklace',5)
board('V10_ExampleB.dc.html','V10 Example B: necklace shortage','rw',BEAD,'red','white',3,2,10,8,4,'Leo','necklace',5)
board('V10_SkinBlocks.dc.html','V10 Skin test: bracelet shortage','byk',BLOCK,'blue','yellow',2,3,8,9,4,'Maya','bracelet',5)
if os.path.exists(P+'/canvas.json'):
    c=json.load(open(P+'/canvas.json'))
    for i,(f,t) in enumerate([("V10_ExampleA.dc.html","V10 Example A · 8 blue, 9 yellow → only 3, not 4"),("V10_ExampleB.dc.html","V10 Example B · 10 red, 8 white → only 3, not 4"),("V10_SkinBlocks.dc.html","V10 Skin test · blocks, bracelets")]):
        c['boards'][f]={**c['boards'].get(f,{}),"x":i*1120,"y":16440,"w":1040,"h":900,"title":t,"expand":"fill","is_interactive":True}
        if f not in c['order']: c['order'].append(f)
    c['notes']['v10heading']={"x":0,"y":16200,"text":"V10 Necklace shortage — why the claim fails","kind":"title1","maxW":3280}
    json.dump(c,open(P+'/canvas.json','w'),indent=2,ensure_ascii=False)
print('ok')
