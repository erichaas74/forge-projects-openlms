import sys, json, os
P=sys.argv[1]
def f3(x): return f"{x:.3f}".rstrip('0').rstrip('.')
SKINS={
 'lemonade':{'a':('lemon juice','#F5CF3B','#8A6400'),'b':('water','#9CC9F5','#1A4FBF')},
 'paint':{'a':('blue paint','#3B6FD8','#123E99'),'b':('yellow paint','#F5CF3B','#8A6400')},
 'redwhite':{'a':('red paint','#D0453B','#8C1E19'),'b':('white paint','#FFFFFF','#2F3440')},
}
BH=26; CUP=44
def cup(side,delay=0):
    return (f'<svg class="rm-cup rm-cup-{side}" viewBox="0 0 30 30" focusable="false">'
            f'<path class="rm-liquid" style="animation-delay: {f3(delay)}s" d="M6 9 H22 L20.5 26 Q20.3 27.5 18.8 27.5 H9.2 Q7.7 27.5 7.5 26 Z"></path>'
            f'<path d="M5 6 H23 L21 26.5 Q20.8 28.5 18.8 28.5 H9.2 Q7.2 28.5 7 26.5 Z" fill="none" stroke-width="2.2" stroke-linejoin="round"></path>'
            f'<path d="M22.5 10 H25.5 Q28 10 28 13 V16 Q28 19 25 19 H21.6" fill="none" stroke-width="2.2" stroke-linecap="round"></path></svg>')
def board(out,title,skin,A,B,n,unknown,question,ans_line,fb):
    S=SKINS[skin]; la,ca,da=S['a']; lb,cb,db=S['b']
    per=A+B; N=per*n; H=N*BH
    bands=[]; left=[]; right=[]; labels=[]; t=0.3
    for b in range(n):
        rowb=b*per*BH+(per*BH-CUP)/2
        labels.append(f'<span class="rm-blab" style="bottom: {f3(rowb+7)}px">batch {b+1}</span>')
        for j in range(per):
            side='a' if j<A else 'b'; k=j if side=='a' else j-A
            idx=b*per+j; top=' rm-batch-top' if j==per-1 else ''
            bands.append(f'<span class="rm-band rm-band-{side}{top}" style="bottom: {idx*BH}px; animation-delay: {f3(t+0.6)}s"></span>')
            slot=f'<span class="rm-slot" style="bottom: {f3(rowb)}px; left: {k*(CUP+4)}px; animation-delay: {f3(t)}s"><span class="rm-pour" style="animation-delay: {f3(t+0.45)}s">{cup(side,t+0.45)}</span></span>'
            (left if side=='a' else right).append(slot)
            t+=0.55
        t+=0.25
    done=t
    ta,tb=A*n,B*n; uv=tb if unknown=='b' else ta
    colw=lambda k: k*(CUP+4)-4
    def total(side,v,cls):
        is_unknown=(side==unknown)
        if is_unknown:
            return f'<p class="rm-ctotal {cls}"><span class="rm-ans"><span class="rm-hide rm-unknown">?</span><span class="rm-late rm-unknown">?</span><span class="rm-reveal" style="animation-delay: {f3(done)}s">{v}</span></span> cups</p>'
        return f'<p class="rm-ctotal {cls}"><span class="rm-reveal rm-inline" style="animation-delay: {f3(done)}s">{v} cups</span></p>'
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
.ratio-master{{--rm-ink:#1B1F2A;--rm-muted:#4A5263;--rm-panel:#F3F4F7;--rm-focus:#1E5BD8;--rm-ca:{ca};--rm-cb:{cb};--rm-da:{da};--rm-db:{db};
box-sizing:border-box;max-width:1040px;margin:0 auto;padding:40px 16px 48px;background:#FFFFFF;color:var(--rm-ink);font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.4}}
.ratio-master *,.ratio-master *::before,.ratio-master *::after{{box-sizing:border-box}}
.ratio-master .rm-question{{max-width:38ch;margin:0 auto 12px;text-align:center;font-size:clamp(20px,3vw,26px);font-weight:700;line-height:1.3}}
.ratio-master .rm-recipe{{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:6px 10px;width:max-content;max-width:100%;margin:0 auto 26px;padding:8px 18px;border:2px solid #D7DBE2;border-radius:999px;font-size:18px;font-weight:700}}
.ratio-master .rm-recipe span{{display:inline-flex;align-items:center;gap:6px}}
.ratio-master .rm-sw{{display:inline-block;width:22px;height:16px;border:1.5px solid rgba(27,31,42,.5);border-radius:3px}}
.ratio-master .rm-band-a{{background:var(--rm-ca)}}
.ratio-master .rm-band-b{{background:var(--rm-cb) repeating-linear-gradient(135deg, rgba(255,255,255,0) 0 6px, rgba(27,31,42,.22) 6px 8px)}}
.ratio-master .rm-row{{display:flex;justify-content:center;align-items:flex-end;gap:18px}}
.ratio-master .rm-col{{display:flex;flex-direction:column;align-items:center}}
.ratio-master .rm-chead{{display:flex;align-items:center;gap:6px;margin:0 0 8px;font-size:17px;font-weight:700;white-space:nowrap}}
.ratio-master .rm-cups{{position:relative;height:{H}px}}
.ratio-master .rm-ctotal{{min-height:44px;margin:10px 0 0;font-size:22px;font-weight:800}}
.ratio-master .rm-slot{{position:absolute;width:{CUP}px;height:{CUP}px;opacity:0}}
.ratio-master .rm-pour{{display:block;transform-origin:50% 90%}}
.ratio-master .rm-cup{{display:block;width:{CUP}px;height:{CUP}px}}
.ratio-master .rm-cup-a{{stroke:var(--rm-da)}}
.ratio-master .rm-cup-b{{stroke:var(--rm-db)}}
.ratio-master .rm-cup-a .rm-liquid{{fill:var(--rm-ca)}}
.ratio-master .rm-cup-b .rm-liquid{{fill:var(--rm-cb)}}
.ratio-master .rm-liquid{{stroke:none;transform-box:fill-box;transform-origin:50% 100%}}
.ratio-master .rm-blabs{{position:relative;width:62px;height:{H}px}}
.ratio-master .rm-blab{{position:absolute;right:0;font-size:14px;font-weight:700;color:var(--rm-muted);white-space:nowrap;opacity:0}}
.ratio-master .rm-jugwrap{{position:relative;margin:0 6px}}
.ratio-master .rm-jug{{position:relative;width:140px;height:{H}px;border:4px solid rgba(27,31,42,.7);border-top:none;border-radius:0 0 22px 22px;background:rgba(150,180,220,.12);overflow:hidden}}
.ratio-master .rm-jug::before{{content:"";position:absolute;inset:0;z-index:2;background:linear-gradient(90deg, rgba(255,255,255,.35), rgba(255,255,255,0) 30%);pointer-events:none}}
.ratio-master .rm-jugrim{{position:absolute;left:-10px;top:-4px;width:160px;height:4px;border-radius:2px;background:rgba(27,31,42,.7)}}
.ratio-master .rm-band{{position:absolute;left:0;right:0;height:{BH}px;border-top:1px solid rgba(27,31,42,.25);opacity:0}}
.ratio-master .rm-band.rm-batch-top::after{{content:"";position:absolute;left:0;right:0;top:-2px;height:4px;background:var(--rm-ink)}}
.ratio-master .rm-answer{{margin:20px 0 0;text-align:center;font-size:clamp(22px,3.6vw,30px);font-weight:800}}
.ratio-master .rm-ans{{position:relative;display:inline-flex;align-items:center;justify-content:center;min-width:52px;margin:0 4px;padding:0 10px;outline:3px solid var(--rm-ink);border-radius:12px;font-variant-numeric:tabular-nums}}
.ratio-master .rm-unknown{{color:var(--rm-muted)}}
.ratio-master .rm-reveal,.ratio-master .rm-late{{display:none}}
.ratio-master .rm-check{{max-width:560px;margin:22px auto 0;text-align:center}}
.ratio-master .rm-check summary{{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:10px 24px;border:2px solid var(--rm-ink);border-radius:999px;background:#FFFFFF;font-size:18px;font-weight:700;cursor:pointer;list-style:none}}
.ratio-master .rm-check summary::-webkit-details-marker{{display:none}}
.ratio-master .rm-check summary:focus-visible{{outline:3px solid var(--rm-focus);outline-offset:3px}}
.ratio-master .rm-check[open] summary{{background:var(--rm-panel)}}
.ratio-master .rm-feedback{{margin:14px 0 0;font-size:18px}}
.ratio-master:has(.rm-check[open]) .rm-band{{animation:rm-pour-in .4s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-slot{{animation:rm-cup-in .3s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-pour{{animation:rm-tip .55s ease-in-out both}}
.ratio-master:has(.rm-check[open]) .rm-liquid{{animation:rm-drain .45s ease-in both}}
.ratio-master:has(.rm-check[open]) .rm-blab{{opacity:1}}
.ratio-master:has(.rm-check[open]) .rm-hide{{display:none}}
.ratio-master:has(.rm-check[open]) .rm-reveal{{display:inline;animation:rm-pop .45s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-late{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;border-radius:12px;background:#FFFFFF;animation:rm-gone .3s ease-out {f3(done)}s both}}
.ratio-master .rm-sr{{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}}
@keyframes rm-pour-in{{from{{opacity:0;transform:translateY(-{H}px)}}to{{opacity:1;transform:none}}}}
@keyframes rm-cup-in{{from{{opacity:0;transform:scale(.6)}}to{{opacity:1;transform:none}}}}
@keyframes rm-tip{{0%{{transform:none}}40%{{transform:rotate(var(--rm-tilt))}}100%{{transform:none}}}}
@keyframes rm-drain{{from{{transform:scaleY(1)}}to{{transform:scaleY(0)}}}}
@keyframes rm-pop{{from{{opacity:0;transform:scale(.7)}}to{{opacity:1;transform:none}}}}
@keyframes rm-gone{{from{{opacity:1}}to{{opacity:0}}}}
.ratio-master .rm-left .rm-pour{{--rm-tilt:35deg}}
.ratio-master .rm-right .rm-pour{{--rm-tilt:-35deg}}
.ratio-master .rm-right .rm-cup{{transform:scaleX(-1)}}
@media (prefers-reduced-motion: reduce){{.ratio-master:has(.rm-check[open]) .rm-band,.ratio-master:has(.rm-check[open]) .rm-slot{{animation:none;opacity:1}}.ratio-master:has(.rm-check[open]) .rm-pour,.ratio-master:has(.rm-check[open]) .rm-pour .rm-liquid,.ratio-master .rm-reveal{{animation:none !important}}.ratio-master:has(.rm-check[open]) .rm-liquid{{transform:scaleY(0)}}.ratio-master:has(.rm-check[open]) .rm-late{{display:none}}}}
@media (max-width: 520px){{.ratio-master .rm-blabs{{display:none}}.ratio-master .rm-col:first-child{{display:none}}.ratio-master .rm-row{{gap:8px}}.ratio-master .rm-jug{{width:96px}}.ratio-master .rm-jugrim{{width:116px}}.ratio-master .rm-chead{{font-size:15px}}}}
</style>
</helmet>
<div class="ratio-master" data-master="V08" data-skin="{skin}">
<h2 class="rm-question">{question}</h2>
<p class="rm-recipe">1 batch: <span><span class="rm-sw rm-band-a"></span>{A} cup{"s" if A!=1 else ""} {la}</span> + <span><span class="rm-sw rm-band-b"></span>{B} cup{"s" if B!=1 else ""} {lb}</span></p>
<p class="rm-sr">The jug is filled with {n} batches. Each batch pours {A} cups of {la} from the left and {B} cups of {lb} from the right.</p>
<div class="rm-row" aria-hidden="true">
<div class="rm-col"><p class="rm-chead">&nbsp;</p><div class="rm-blabs">{''.join(labels)}</div><p class="rm-ctotal">&nbsp;</p></div>
<div class="rm-col rm-left"><p class="rm-chead"><span class="rm-sw rm-band-a"></span>{la}</p><div class="rm-cups" style="width: {colw(A)}px">{''.join(left)}</div>{total('a',ta,'')}</div>
<div class="rm-col"><p class="rm-chead">&nbsp;</p><div class="rm-jugwrap"><div class="rm-jug">{''.join(bands)}</div><span class="rm-jugrim"></span></div><p class="rm-ctotal">&nbsp;</p></div>
<div class="rm-col rm-right"><p class="rm-chead"><span class="rm-sw rm-band-b"></span>{lb}</p><div class="rm-cups" style="width: {colw(B)}px">{''.join(right)}</div>{total('b',tb,'')}</div>
</div>
<details class="rm-check">
<summary>Check the answer</summary>
<p class="rm-feedback">{fb}</p>
</details>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1040,"height":{max(760, H+420)}}}}}'>
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
board('V08_ExampleA.dc.html','V08 Example A: lemonade','lemonade',2,3,3,'b',
 'You make 3 batches of lemonade. How many cups of water do you need?',
 '3 batches → ? cups of water',
 '1 batch has 3 cups of water, so 3 batches have 3 × 3 = 9 cups of water (and 6 cups of lemon juice). Answer: 9 cups of water.')
board('V08_ExampleB.dc.html','V08 Example B: green paint','paint',1,2,4,'a',
 'You make 4 batches of green paint. How many cups of blue paint do you need?',
 '4 batches → ? cups of blue paint',
 '1 batch has 1 cup of blue paint, so 4 batches have 4 × 1 = 4 cups of blue paint (and 8 cups of yellow). Answer: 4 cups of blue paint.')
board('V08_SkinBlocks.dc.html','V08 Skin test: pink paint','redwhite',2,3,3,'b',
 'You make 3 batches of pink paint. How many cups of white paint do you need?',
 '3 batches → ? cups of white paint',
 '1 batch has 3 cups of white paint, so 3 batches have 3 × 3 = 9 cups of white paint (and 6 cups of red). Answer: 9 cups of white paint.')
if os.path.exists(P+'/canvas.json'):
    c=json.load(open(P+'/canvas.json'))
    for i,(f,t) in enumerate([("V08_ExampleA.dc.html","V08 Example A · lemonade 2:3 × 3"),("V08_ExampleB.dc.html","V08 Example B · green paint 1:2 × 4"),("V08_SkinBlocks.dc.html","V08 Skin test · pink paint 2:3 × 3")]):
        c['boards'][f]={**c['boards'].get(f,{}),"x":i*1120,"y":11540,"w":1040,"h":860,"title":t,"expand":"fill","is_interactive":True}
        if f not in c['order']: c['order'].append(f)
    c['notes']['v08heading']={"x":0,"y":11300,"text":"V08 Mixture Container — fill complete batches","kind":"title1","maxW":3280}
    if 'V07_BuildSpec.dc.html' not in c['boards']:
        c['boards']['V07_BuildSpec.dc.html']={"x":3360,"y":10220,"w":1040,"h":1000,"title":"V07 build sheet","expand":"fill"}
    if 'V07_BuildSpec.dc.html' not in c['order']: c['order'].append('V07_BuildSpec.dc.html')
    json.dump(c,open(P+'/canvas.json','w'),indent=2,ensure_ascii=False)
print('ok')
