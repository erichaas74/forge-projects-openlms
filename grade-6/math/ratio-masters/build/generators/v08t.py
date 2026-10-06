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
def board(out,title,skin,A,B,n,unknown,question,ans_line,fb,supply=None,cols=5,rows=None):
    # supply: full cups each side starts with (default = total cups wanted)
    # cols / rows: how the supply cups are laid out (e.g. cols=4, rows=3 or cols=3, rows=5)
    PERROW=cols
    S=SKINS[skin]; la,ca,da=S['a']; lb,cb,db=S['b']
    per=A+B; N=per*n; H=N*BH
    SUP=supply or N
    ROWS=rows or -(-SUP//PERROW)
    assert SUP>=max(A*n,B*n), 'supply must cover the cups used'
    assert ROWS*PERROW>=SUP, 'rows x cols must hold the supply'
    bands=[]; left=[]; right=[]; labels=[]; t=0.3
    for b in range(n):
        rowb=b*per*BH+(per*BH-CUP)/2
        labels.append(f'<span class="rm-blab" style="bottom: {f3(rowb+7)}px">batch {b+1}</span>')
        for j in range(per):
            side='a' if j<A else 'b'; k=j if side=='a' else j-A
            idx=b*per+j; top=' rm-batch-top' if j==per-1 else ''
            bands.append(f'<span class="rm-band rm-band-{side}{top}" style="bottom: {idx*BH}px; animation-delay: {f3(t+0.6)}s"></span>')
            kk=(b*A+k) if side=='a' else (b*B+k)
            slot=f'<span class="rm-slot" style="bottom: {(ROWS-1-kk//PERROW)*(CUP+8)}px; left: {(kk%PERROW)*(CUP+4)}px; animation-delay: {f3(t)}s"><span class="rm-pour" style="animation-delay: {f3(t+0.45)}s">{cup(side,t+0.45)}</span></span>'
            (left if side=='a' else right).append(slot)
            t+=0.55
        t+=0.25
    done=t
    for side,used in (('a',A*n),('b',B*n)):
        for kk in range(used,SUP):
            cell=f'<span class="rm-slot rm-full" style="bottom: {(ROWS-1-kk//PERROW)*(CUP+8)}px; left: {(kk%PERROW)*(CUP+4)}px"><span class="rm-pour-none">{cup(side,0)}</span></span>'
            (left if side=='a' else right).append(cell)
    ta,tb=A*n,B*n; uv=tb if unknown=='b' else ta
    colw=lambda k: k*(CUP+4)-4
    def total(side,v,cls):
        is_unknown=(side==unknown)
        if is_unknown:
            return f'<p class="rm-ctotal {cls}"><span class="rm-ans"><span class="rm-hide rm-unknown">?</span><span class="rm-late rm-unknown">?</span><span class="rm-reveal" style="animation-delay: {f3(done)}s">{v}</span></span> cups used</p>'
        return f'<p class="rm-ctotal {cls}"><span class="rm-reveal rm-inline" style="animation-delay: {f3(done)}s">{v} cups used</span></p>'
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
.ratio-master .rm-recipe span{{display:inline-flex;align-items:center;gap:4px}}
.ratio-master .rm-rcups .rm-cup{{width:38px;height:38px}}
.ratio-master .rm-rlab{{font-weight:600;color:var(--rm-muted)}}
.ratio-master .rm-rcups .rm-liquid{{animation:none !important;transform:none !important}}
.ratio-master .rm-sw{{display:inline-block;width:22px;height:16px;border:1.5px solid rgba(27,31,42,.5);border-radius:3px}}
.ratio-master .rm-band-a{{background:var(--rm-ca)}}
.ratio-master .rm-band-b{{background:var(--rm-cb) repeating-linear-gradient(135deg, rgba(255,255,255,0) 0 6px, rgba(27,31,42,.22) 6px 8px)}}
.ratio-master .rm-row{{display:flex;justify-content:center;align-items:flex-end;gap:18px}}
.ratio-master .rm-col{{display:flex;flex-direction:column;align-items:center}}
.ratio-master .rm-chead{{display:flex;align-items:center;gap:6px;margin:0 0 8px;font-size:17px;font-weight:700;white-space:nowrap}}
.ratio-master .rm-cups{{position:relative;height:{H}px}}
.ratio-master .rm-right .rm-pour-none .rm-cup{{transform:scaleX(-1)}}
.ratio-master .rm-ctotal{{min-height:44px;margin:10px 0 0;font-size:22px;font-weight:800}}
.ratio-master .rm-slot{{position:absolute;width:{CUP}px;height:{CUP}px}}
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
.ratio-master .rm-target{{position:absolute;left:50%;top:-30px;transform:translateX(-50%);padding:1px 10px;border-radius:999px;background:var(--rm-ink);color:#FFFFFF;font-size:14px;font-weight:700;white-space:nowrap}}
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
.ratio-master:has(.rm-check[open]) .rm-pour{{animation:rm-tip .55s ease-in-out both}}
.ratio-master:has(.rm-check[open]) .rm-pour .rm-liquid{{animation:rm-drain .45s ease-in both}}
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
@media (prefers-reduced-motion: reduce){{.ratio-master:has(.rm-check[open]) .rm-band,.ratio-master:has(.rm-check[open]) .rm-slot{{animation:none;opacity:1}}.ratio-master:has(.rm-check[open]) .rm-pour,.ratio-master:has(.rm-check[open]) .rm-pour .rm-liquid,.ratio-master .rm-reveal{{animation:none !important}}.ratio-master:has(.rm-check[open]) .rm-pour .rm-liquid{{transform:scaleY(0)}}.ratio-master:has(.rm-check[open]) .rm-late{{display:none}}}}
@media (max-width: 520px){{.ratio-master .rm-blabs{{display:none}}.ratio-master .rm-col:first-child{{display:none}}.ratio-master .rm-row{{gap:8px}}.ratio-master .rm-jug{{width:96px}}.ratio-master .rm-target{{position:absolute;left:50%;top:-30px;transform:translateX(-50%);padding:1px 10px;border-radius:999px;background:var(--rm-ink);color:#FFFFFF;font-size:14px;font-weight:700;white-space:nowrap}}
.ratio-master .rm-jugrim{{width:116px}}.ratio-master .rm-chead{{font-size:15px}}.ratio-master .rm-left .rm-cups,.ratio-master .rm-right .rm-cups{{zoom:.45}}}}
</style>
</helmet>
<div class="ratio-master" data-master="V08" data-skin="{skin}">
<h2 class="rm-question">{question}</h2>
<p class="rm-recipe" aria-label="Recipe: {A} cups of {la} and {B} cups of {lb}">Recipe: <span class="rm-rcups">{cup("a",-1)*A}</span><span class="rm-rlab">{la}</span> + <span class="rm-rcups rm-right">{cup("b",-1)*B}</span><span class="rm-rlab">{lb}</span></p>
<p class="rm-sr">The jug is filled with {n} batches. Each batch pours {A} cups of {la} from the left and {B} cups of {lb} from the right.</p>
<div class="rm-row" aria-hidden="true">
<div class="rm-col rm-left"><p class="rm-chead"><span class="rm-sw rm-band-a"></span>{la}</p><div class="rm-cups" style="width: {colw(PERROW)}px; height: {max(H, ROWS*(CUP+8))}px">{''.join(left)}</div>{total('a',ta,'')}</div>
<div class="rm-col"><p class="rm-chead">&nbsp;</p><div class="rm-jugwrap"><span class="rm-target">{N} cups</span><div class="rm-jug">{''.join(bands)}</div><span class="rm-jugrim"></span></div><p class="rm-ctotal">&nbsp;</p></div>
<div class="rm-col rm-right"><p class="rm-chead"><span class="rm-sw rm-band-b"></span>{lb}</p><div class="rm-cups" style="width: {colw(PERROW)}px; height: {max(H, ROWS*(CUP+8))}px">{''.join(right)}</div>{total('b',tb,'')}</div>
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
board('V08T_ExampleA.dc.html','V08T Example A: 15 cups of lemonade','lemonade',2,3,3,'b',
 'You want 15 cups of lemonade in all. How many cups of water do you need?','',
 'Each batch is 2 + 3 = 5 cups. 15 cups is 3 batches (15 ÷ 5 = 3). Each batch has 3 cups of water, so 3 × 3 = 9. Answer: 9 cups of water.',
 supply=15, cols=5, rows=3)
board('V08T_ExampleB.dc.html','V08T Example B: 12 cups of green paint','paint',1,2,4,'a',
 'You want 12 cups of green paint in all. How many cups of blue paint do you need?','',
 'Each batch is 1 + 2 = 3 cups. 12 cups is 4 batches (12 ÷ 3 = 4). Each batch has 1 cup of blue, so 4 × 1 = 4. Answer: 4 cups of blue paint.',
 supply=12, cols=4, rows=3)
board('V08T_SkinBlocks.dc.html','V08T Skin test: 15 cups of pink paint','redwhite',2,3,3,'b',
 'You want 15 cups of pink paint in all. How many cups of white paint do you need?','',
 'Each batch is 2 + 3 = 5 cups. 15 cups is 3 batches (15 ÷ 5 = 3). Each batch has 3 cups of white, so 3 × 3 = 9. Answer: 9 cups of white paint.',
 supply=15, cols=3, rows=5)
if os.path.exists(P+'/canvas.json'):
    c=json.load(open(P+'/canvas.json'))
    for i,(f,t) in enumerate([("V08T_ExampleA.dc.html","V08T Example A · lemonade, 15 cups in all"),("V08T_ExampleB.dc.html","V08T Example B · green paint, 12 cups in all"),("V08T_SkinBlocks.dc.html","V08T Skin test · pink paint, 15 cups in all")]):
        c['boards'][f]={**c['boards'].get(f,{}),"x":i*1120,"y":12760,"w":1040,"h":860,"title":t,"expand":"fill","is_interactive":True}
        if f not in c['order']: c['order'].append(f)
    c['notes']['v08theading']={"x":0,"y":12520,"text":"V08T Mixture Container — fill to a total","kind":"title1","maxW":3280}
    json.dump(c,open(P+'/canvas.json','w'),indent=2,ensure_ascii=False)
print('ok')
