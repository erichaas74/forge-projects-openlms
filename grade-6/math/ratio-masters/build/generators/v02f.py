import sys, json
P=sys.argv[1]
BEAD='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><circle class="rm-body" cx="16" cy="16" r="14"></circle><circle class="rm-detail" cx="16" cy="16" r="4.5"></circle></svg>'
BLOCK='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><rect class="rm-body" x="2" y="2" width="28" height="28" rx="4"></rect><rect class="rm-detail" x="9" y="9" width="14" height="14" rx="2"></rect></svg>'
VARS={
 'by':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#FFFFFF;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FFFFFF;--rm-b-text:#6E5000;",
 'byk':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#4C7FE6;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FAD55C;--rm-b-text:#6E5000;",
 'rw':"--rm-a:#C8322B;--rm-a-edge:#8C1E19;--rm-a-detail:#FFFFFF;--rm-a-text:#B02A23;--rm-b:#FFFFFF;--rm-b-edge:#2F3440;--rm-b-detail:#DFE3E9;--rm-b-text:#2F3440;",
}
def board(out,title,vk,obj,la,lb,A,B,n,question):
    noun='blocks' if obj==BLOCK else 'beads'
    gap=1.0 if n<=3 else 0.8
    t=(n-1)*gap+0.8
    groups=[]
    for k in range(n):
        st='' if k==0 else f' rm-step" style="animation-delay: {k*gap:g}s'
        groups.append(f'<li class="rm-group{st}"><div class="rm-top">{obj.format(s="a")*A}</div><span class="rm-bar"></span><div class="rm-bottom">{obj.format(s="b")*B}</div></li>')
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
.ratio-master{{--rm-ink:#1B1F2A;--rm-muted:#4A5263;--rm-panel:#F3F4F7;
{VARS[vk]}
box-sizing:border-box;max-width:1040px;margin:0 auto;padding:40px 16px 48px;background:#FFFFFF;color:var(--rm-ink);font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.4}}
.ratio-master *,.ratio-master *::before,.ratio-master *::after{{box-sizing:border-box}}
.ratio-master .rm-question{{max-width:34ch;margin:0 auto 28px;text-align:center;font-size:clamp(20px,3vw,26px);font-weight:700;line-height:1.3}}
.ratio-master .rm-model{{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:24px}}
.ratio-master .rm-keys{{display:flex;flex-direction:column;justify-content:space-between;align-self:stretch;padding:14px 0;font-size:18px;font-weight:700;text-align:right}}
.ratio-master .rm-groups{{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;margin:0;padding:0;list-style:none}}
.ratio-master .rm-group{{display:flex;flex-direction:column;align-items:center;gap:10px;padding:14px 14px;background:var(--rm-panel);border-radius:14px}}
.ratio-master .rm-top,.ratio-master .rm-bottom{{display:flex;justify-content:center;gap:6px}}
.ratio-master .rm-bar{{align-self:stretch;height:3px;background:var(--rm-ink);border-radius:2px}}
.ratio-master .rm-frac{{display:inline-flex;flex-direction:column;align-items:center;font-weight:800;line-height:1.15;font-variant-numeric:tabular-nums}}
.ratio-master .rm-frac > span{{position:relative;padding:0 10px}}
.ratio-master .rm-frac > span + span{{border-top:4px solid var(--rm-ink)}}
.ratio-master .rm-total{{margin:32px auto 0;display:flex;justify-content:center;font-size:clamp(40px,7vw,56px)}}
.ratio-master .rm-q{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:#FFFFFF;color:var(--rm-muted)}}
.ratio-master .rm-notation{{display:flex;align-items:center;justify-content:center;gap:16px;margin:32px 0 0;font-size:clamp(40px,7vw,56px);font-weight:800}}
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
@keyframes rm-add{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:none}}}}
@keyframes rm-fade{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes rm-out{{from{{opacity:1}}to{{opacity:0}}}}
.ratio-master .rm-step{{animation:rm-add .6s ease-out both}}
.ratio-master .rm-fade{{animation:rm-fade .5s ease-out both}}
.ratio-master .rm-out{{animation:rm-out .4s ease-out both}}
@media (prefers-reduced-motion: reduce){{.ratio-master .rm-step,.ratio-master .rm-fade{{animation:none}}.ratio-master .rm-q{{display:none}}}}
@media (max-width: 480px){{.ratio-master .rm-obj{{width:30px;height:30px}}.ratio-master .rm-keys{{display:none}}}}
</style>
</helmet>
<div class="ratio-master" data-master="V02F" data-skin="{'blocks' if obj==BLOCK else 'beads'}">
<h2 class="rm-question">{question}</h2>
<p class="rm-sr">Each group is a fraction: {A} {la} {noun} on top and {B} {lb} {noun} on the bottom. There are {n} groups. Together that is {A*n} {la} over {B*n} {lb}. {A}/{B} = {A*n}/{B*n}.</p>
<div class="rm-model" aria-hidden="true">
<div class="rm-keys"><span class="rm-a-text">{la}</span><span class="rm-b-text">{lb}</span></div>
<ol class="rm-groups">
{chr(10).join(groups)}
</ol>
</div>
<p class="rm-notation rm-fade" style="animation-delay: {t:g}s" aria-hidden="true"><span class="rm-frac"><span class="rm-a-text">{A}</span><span class="rm-b-text">{B}</span></span><span>=</span><span class="rm-frac"><span class="rm-a-text">{A*n}</span><span class="rm-b-text">{B*n}<span class="rm-q rm-out" style="animation-delay: {t+1:g}s">?</span></span></span></p>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1040,"height":640}}}}'>
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
board('V02F_ExampleA.dc.html','V02F Example A','by',BEAD,'blue','yellow',2,3,3,'2 blue beads go with 3 yellow beads. How many yellow beads go with 6 blue beads?')
board('V02F_ExampleB.dc.html','V02F Example B','rw',BEAD,'red','white',3,2,4,'3 red beads go with 2 white beads. How many white beads go with 12 red beads?')
board('V02F_SkinBlocks.dc.html','V02F Skin test: blocks','byk',BLOCK,'blue','yellow',2,3,3,'2 blue blocks go with 3 yellow blocks. How many yellow blocks go with 6 blue blocks?')
import os
if os.path.exists(P+'/canvas.json'):
    c=json.load(open(P+'/canvas.json'))
    for i,(f,t) in enumerate([("V02F_ExampleA.dc.html","V02F Example A · beads 2/3 ×3"),("V02F_ExampleB.dc.html","V02F Example B · beads 3/2 ×4"),("V02F_SkinBlocks.dc.html","V02F Skin test · blocks 2/3 ×3")]):
        c['boards'][f]={"x":i*1120,"y":4100,"w":1040,"h":640,"title":t,"expand":"fill"}
        if f not in c['order']: c['order'].append(f)
    c['notes']['v02fheading']={"x":0,"y":3840,"text":"V02F Group Multiplier — fraction version","kind":"title1","maxW":3280}
    json.dump(c,open(P+'/canvas.json','w'),indent=2,ensure_ascii=False)
print('ok')
