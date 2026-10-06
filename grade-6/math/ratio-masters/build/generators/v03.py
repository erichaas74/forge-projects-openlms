import sys, json
P=sys.argv[1]
BEAD='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><circle class="rm-body" cx="16" cy="16" r="14"></circle><circle class="rm-detail" cx="16" cy="16" r="4.5"></circle></svg>'
BLOCK='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><rect class="rm-body" x="2" y="2" width="28" height="28" rx="4"></rect><rect class="rm-detail" x="9" y="9" width="14" height="14" rx="2"></rect></svg>'
ARROW='<svg class="rm-arrow" viewBox="0 0 24 32" focusable="false"><path d="M12 2 V26 M4 18 L12 28 L20 18"></path></svg>'
VARS={
 'by':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#FFFFFF;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FFFFFF;--rm-b-text:#6E5000;",
 'byk':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#4C7FE6;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FAD55C;--rm-b-text:#6E5000;",
 'rw':"--rm-a:#C8322B;--rm-a-edge:#8C1E19;--rm-a-detail:#FFFFFF;--rm-a-text:#B02A23;--rm-b:#FFFFFF;--rm-b-edge:#2F3440;--rm-b-detail:#DFE3E9;--rm-b-text:#2F3440;",
}
def objs(obj,s,count,clusters=None,extra=''):
    if not clusters: clusters=1
    per=count//clusters
    inner=''.join(f'<span class="rm-cluster">{obj.format(s=s)*per}</span>' for _ in range(clusters))
    return f'<div class="rm-objs rm-grouped{extra}">{inner}</div>'
def board(out,title,vk,obj,la,lb,A,B,op,f,question):
    oa = A*f if op=='×' else A//f
    ob = B*f if op=='×' else B//f
    assert (A*f if op=='×' else A/f)==oa and (B*f if op=='×' else B/f)==ob
    noun='blocks' if obj==BLOCK else 'beads'
    word='times' if op=='×' else 'divided by'
    mul = op=='×'
    in_a = objs(obj,'a',A, None if mul else f)
    in_b = objs(obj,'b',B, None if mul else f)
    out_a = objs(obj,'a',oa, f if mul else None)
    out_b = objs(obj,'b',ob, f if mul else None)
    fb = f'{A} {op} {f} = {oa}, so the same {op} {f} works on the {lb} side too. Answer: {ob} {lb} {noun}.'
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
.ratio-master{{--rm-ink:#1B1F2A;--rm-muted:#4A5263;--rm-panel:#F3F4F7;--rm-arrow:#9AA1AE;--rm-focus:#1E5BD8;
{VARS[vk]}
box-sizing:border-box;max-width:1040px;margin:0 auto;padding:40px 16px 48px;background:#FFFFFF;color:var(--rm-ink);font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.4}}
.ratio-master *,.ratio-master *::before,.ratio-master *::after{{box-sizing:border-box}}
.ratio-master .rm-question{{max-width:34ch;margin:0 auto 28px;text-align:center;font-size:clamp(20px,3vw,26px);font-weight:700;line-height:1.3}}
.ratio-master .rm-machine-model{{display:grid;--rm-gap:24px;grid-template-columns:repeat(2, minmax(0, 1fr));column-gap:var(--rm-gap);row-gap:6px;max-width:600px;margin:0 auto}}
.ratio-master .rm-lab{{text-align:center;font-size:20px;font-weight:700}}
.ratio-master .rm-lane{{display:flex;flex-direction:column;align-items:center;gap:8px}}
.ratio-master .rm-in{{justify-content:flex-end}}
.ratio-master .rm-objs{{display:flex;flex-wrap:wrap;justify-content:center;align-content:center;gap:6px;max-width:300px;min-height:42px}}
.ratio-master .rm-grouped{{max-width:300px;gap:8px}}
.ratio-master .rm-cluster{{display:flex;flex-wrap:wrap;justify-content:center;gap:6px;padding:6px;border:2px solid #B9BFCA;border-radius:12px;background:var(--rm-panel);transition:border-color .4s}}
.ratio-master .rm-num{{position:relative;min-width:56px;padding:0 8px;text-align:center;font-size:clamp(30px,5vw,40px);font-weight:800;line-height:1.2;font-variant-numeric:tabular-nums}}
.ratio-master .rm-arrow{{display:block;width:20px;height:28px;fill:none;stroke:var(--rm-arrow);stroke-width:3;stroke-linecap:round;stroke-linejoin:round}}
.ratio-master .rm-machine{{grid-column:1 / -1;display:flex;align-items:center;justify-content:center;gap:10px;margin:2px 0;padding:14px 16px;border:3px solid var(--rm-ink);border-radius:18px;background:var(--rm-panel);font-size:clamp(34px,6vw,48px);font-weight:800;line-height:1}}
.ratio-master .rm-op-cell{{position:relative;display:flex;justify-content:center;align-items:center;min-height:72px}}
.ratio-master .rm-chip{{position:relative;display:inline-flex;align-items:center;gap:8px;padding:10px 22px;border:3px solid var(--rm-ink);border-radius:16px;background:var(--rm-panel);font-size:clamp(30px,5vw,40px);font-weight:800;line-height:1;white-space:nowrap}}
.ratio-master .rm-eq{{font-size:20px;font-weight:700;color:var(--rm-ink);font-variant-numeric:tabular-nums}}
.ratio-master .rm-unknown{{color:var(--rm-muted)}}
.ratio-master .rm-answer{{outline:3px solid var(--rm-ink);border-radius:12px}}
.ratio-master .rm-reveal{{display:none}}
.ratio-master .rm-check{{max-width:520px;margin:28px auto 0;text-align:center}}
.ratio-master .rm-check summary{{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:10px 24px;border:2px solid var(--rm-ink);border-radius:999px;background:#FFFFFF;font-size:18px;font-weight:700;cursor:pointer;list-style:none}}
.ratio-master .rm-check summary::-webkit-details-marker{{display:none}}
.ratio-master .rm-check summary:focus-visible{{outline:3px solid var(--rm-focus);outline-offset:3px}}
.ratio-master .rm-check[open] summary{{background:var(--rm-panel)}}
.ratio-master .rm-feedback{{margin:14px 0 0;font-size:18px}}
.ratio-master:has(.rm-check[open]) .rm-hide{{display:none}}
.ratio-master:has(.rm-check[open]) .rm-late{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;border-radius:10px;background:#FFFFFF;animation:rm-gone .3s ease-out 2.6s both}}
@keyframes rm-gone{{from{{opacity:1}}to{{opacity:0}}}}
.ratio-master:has(.rm-check[open]) .rm-reveal{{display:flex;animation:rm-emerge .7s ease-out both}}
.ratio-master:has(.rm-check[open]) span.rm-reveal{{display:inline}}
.ratio-master:has(.rm-check[open]) .rm-chip.rm-reveal{{display:inline-flex}}
.ratio-master:has(.rm-check[open]) .rm-slide{{animation:rm-slide .9s ease-in-out 1s both}}
@keyframes rm-slide{{from{{left:calc(-100% - var(--rm-gap))}}to{{left:0}}}}
.ratio-master:has(.rm-check[open]) .rm-cluster{{border-color:var(--rm-ink)}}
.ratio-master .rm-d0{{animation-delay:.4s !important}}
.ratio-master .rm-d1{{animation-delay:2s !important}}
.ratio-master .rm-d2{{animation-delay:2.6s !important}}
.ratio-master .rm-obj{{display:block;width:36px;height:36px;flex:none}}
.ratio-master .rm-obj .rm-body{{stroke-width:2}}
.ratio-master .rm-obj .rm-detail{{stroke-width:1.5}}
.ratio-master .rm-obj-a .rm-body{{fill:var(--rm-a);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-a .rm-detail{{fill:var(--rm-a-detail);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-b .rm-body{{fill:var(--rm-b);stroke:var(--rm-b-edge)}}
.ratio-master .rm-obj-b .rm-detail{{fill:var(--rm-b-detail);stroke:var(--rm-b-edge)}}
.ratio-master .rm-a-text{{color:var(--rm-a-text)}}
.ratio-master .rm-b-text{{color:var(--rm-b-text)}}
.ratio-master .rm-sr{{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}}
@keyframes rm-emerge{{from{{opacity:0;transform:translateY(-20px)}}to{{opacity:1;transform:none}}}}
@media (prefers-reduced-motion: reduce){{.ratio-master .rm-reveal,.ratio-master .rm-slide{{animation:none !important}}.ratio-master:has(.rm-check[open]) .rm-late{{display:none}}.ratio-master .rm-cluster{{transition:none}}}}
@media (max-width: 480px){{.ratio-master .rm-obj{{width:28px;height:28px}}.ratio-master .rm-objs{{max-width:130px}}.ratio-master .rm-machine-model{{--rm-gap:12px}}.ratio-master .rm-chip{{padding:8px 14px}}}}
</style>
</helmet>
<div class="ratio-master" data-master="V03" data-skin="{'blocks' if obj==BLOCK else 'beads'}">
<h2 class="rm-question">{question}</h2>
<p class="rm-sr">{A} {la} and {B} {lb} {noun} go into the same machine. Out come {oa} {la} {noun} and an unknown number of {lb} {noun}.</p>
<div class="rm-machine-model" aria-hidden="true">
<span class="rm-lab rm-a-text">{la}</span>
<span class="rm-lab rm-b-text">{lb}</span>
<div class="rm-lane rm-in">{in_a}<span class="rm-num rm-a-text">{A}</span>{ARROW}</div>
<div class="rm-lane rm-in">{in_b}<span class="rm-num rm-b-text">{B}</span>{ARROW}</div>
<div class="rm-op-cell"><span class="rm-chip">{op} <span class="rm-hide rm-unknown">?</span><span class="rm-reveal">{f}</span></span></div>
<div class="rm-op-cell"><span class="rm-chip rm-hide rm-unknown">{op} ?</span><span class="rm-chip rm-reveal rm-slide">{op} {f}</span></div>
<div class="rm-lane">{ARROW}{out_a}<span class="rm-num rm-a-text">{oa}</span><span class="rm-eq rm-reveal rm-d0">{A} {op} {f} = {oa}</span></div>
<div class="rm-lane">{ARROW}<div class="rm-reveal rm-d1">{out_b}</div><span class="rm-num rm-answer rm-b-text"><span class="rm-late rm-unknown">?</span><span class="rm-reveal rm-d2">{ob}</span></span><span class="rm-eq rm-reveal rm-d2">{B} {op} {f} = {ob}</span></div>
</div>
<details class="rm-check">
<summary>Check the answer</summary>
<p class="rm-feedback">{fb}</p>
</details>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1040,"height":820}}}}'>
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
board('V03_ExampleA.dc.html','V03 Example A: times 4','by',BEAD,'blue','yellow',2,3,'×',4,'2 blue beads go with 3 yellow beads. How many yellow beads go with 8 blue beads?')
board('V03_ExampleB.dc.html','V03 Example B: divided by 4','rw',BEAD,'red','white',12,8,'÷',4,'12 red beads go with 8 white beads. How many white beads go with 3 red beads?')
board('V03_SkinBlocks.dc.html','V03 Skin test: blocks','byk',BLOCK,'blue','yellow',2,3,'×',4,'2 blue blocks go with 3 yellow blocks. How many yellow blocks go with 8 blue blocks?')
import os
if os.path.exists(P+'/canvas.json'):
    c=json.load(open(P+'/canvas.json'))
    for f in ['V03_ExampleA.dc.html','V03_ExampleB.dc.html','V03_SkinBlocks.dc.html']:
        c['boards'][f]['h']=820; c['boards'][f]['is_interactive']=True
    json.dump(c,open(P+'/canvas.json','w'),indent=2,ensure_ascii=False)
print('ok')
