import sys, json, math, os
P=sys.argv[1]
ITEMS={
 'coin':'<svg class="rm-item" viewBox="0 0 32 32" focusable="false"><circle cx="16" cy="16" r="14" fill="#F2C12E" stroke="#8A6400" stroke-width="2"></circle><text x="16" y="21.5" text-anchor="middle" font-size="16" font-weight="800" fill="#6E5000" font-family="system-ui, sans-serif">$</text></svg>',
 'toy':'<svg class="rm-item" viewBox="0 0 32 32" focusable="false"><rect x="2" y="2" width="28" height="28" rx="4" fill="#C8322B" stroke="#8C1E19" stroke-width="2"></rect><circle cx="11" cy="11" r="3" fill="#FFFFFF"></circle><circle cx="21" cy="11" r="3" fill="#FFFFFF"></circle><circle cx="11" cy="21" r="3" fill="#FFFFFF"></circle><circle cx="21" cy="21" r="3" fill="#FFFFFF"></circle></svg>',
 'block':'<svg class="rm-item" viewBox="0 0 32 32" focusable="false"><rect x="2" y="2" width="28" height="28" rx="4" fill="#1E5BD8" stroke="#123E99" stroke-width="2"></rect><rect x="9" y="9" width="14" height="14" rx="2" fill="#4C7FE6" stroke="#123E99" stroke-width="1.5"></rect></svg>',
}
ICONS={
 'pencil':'<svg class="rm-ricon" viewBox="0 0 32 32" focusable="false"><path d="M6 24 L22 8 L26 12 L10 28 Z" fill="#F2C12E" stroke="#1B1F2A" stroke-width="2" stroke-linejoin="round"></path><path d="M6 24 L4 30 L10 28 Z" fill="#E9D8B4" stroke="#1B1F2A" stroke-width="2" stroke-linejoin="round"></path><path d="M22 8 L24 6 L28 10 L26 12" fill="#E79A9A" stroke="#1B1F2A" stroke-width="2" stroke-linejoin="round"></path></svg>',
 'hour':'<svg class="rm-ricon" viewBox="0 0 32 32" focusable="false"><circle cx="16" cy="16" r="13" fill="#FFFFFF" stroke="#1B1F2A" stroke-width="2.5"></circle><path d="M16 8 V16 L22 19" fill="none" stroke="#1B1F2A" stroke-width="2.5" stroke-linecap="round"></path></svg>',
 'apple':'<svg class="rm-ricon" viewBox="0 0 32 32" focusable="false"><path d="M16 9 C10 5 3 9 4 17 C5 25 11 30 16 27 C21 30 27 25 28 17 C29 9 22 5 16 9 Z" fill="#D23A2E" stroke="#8C1E19" stroke-width="2"></path><path d="M18 6 C21 3 25 4 26 6 C23 8 20 8 18 6 Z" fill="#3E8E3E"></path></svg>',
}
U=44
def f3(x): return f"{x:.3f}".rstrip('0').rstrip('.')
def panel(pid,name,cap,item,recv,T,G,unit_pre,unit_post,ans_delay):
    per=T//G; assert T%G==0
    PC=math.ceil(T/2); gw=1.7; Wu=max(PC,G*gw); gw=Wu/G; off=(Wu-PC)/2
    ry=2.9; cw=min(1.5,gw-0.15); ch=1.05+per*1.05+0.35; Hu=ry+ch+0.15
    stack_bottom=ry+ch-0.25
    o=[]
    for c in range(G):
        x=c*gw+(gw-cw)/2
        o.append(f'<span class="rm-recv" style="left: {f3(x/Wu*100)}%; top: {f3(ry/Hu*100)}%; width: {f3(cw/Wu*100)}%; height: {f3(ch/Hu*100)}%"><svg class="rm-cup" viewBox="0 0 {cw*100:.0f} {ch*100:.0f}" preserveAspectRatio="none" focusable="false"><rect x="4" y="4" width="{cw*100-8:.0f}" height="{ch*100-8:.0f}" rx="14" fill="rgba(150,180,220,0.18)" stroke="rgba(27,31,42,0.65)" stroke-width="6"></rect></svg><span class="rm-ricon-wrap">{ICONS[recv]}</span></span>')
    for k in range(T):
        pr,pc=divmod(k,PC); sx=off+pc; sy=pr*1.1
        r,c=divmod(k,G)
        tx=c*gw+(gw-1)/2; ty=stack_bottom-(r+1)*1.05
        d=0.3+r*0.9+c*0.08
        o.append(f'<span class="rm-coin" style="left: {f3(tx/Wu*100)}%; top: {f3(ty/Hu*100)}%; width: {f3(100/Wu)}%; height: {f3(100/Hu)}%; translate: {f3((sx-tx)*100)}% {f3((sy-ty)*100)}%; transition-delay: {f3(d)}s">{ITEMS[item]}</span>')
    fx=(gw-cw)/2-0.12
    o.append(f'<span class="rm-focus rm-reveal" style="left: {f3(fx/Wu*100)}%; top: {f3((ry-0.12)/Hu*100)}%; width: {f3((cw+0.24)/Wu*100)}%; height: {f3((ch+0.24)/Hu*100)}%; animation-delay: {f3(ans_delay-0.3)}s"></span>')
    stage=(f'<div class="rm-stage" style="padding-top: {f3(Hu/Wu*100)}%"><span class="rm-pile" style="left: {f3((off-0.15)/Wu*100)}%; top: {f3(-0.15/Hu*100)}%; width: {f3((PC+0.3)/Wu*100)}%; height: {f3(2.5/Hu*100)}%"></span>'+''.join(o)+'</div>')
    return (f'<section class="rm-panel" id="{pid}" style="width: min(100%, {round(Wu*U)+32}px)">'
            f'<h3 class="rm-pname">{name}<span class="rm-win rm-reveal" style="animation-delay: {f3(ans_delay+0.8)}s">{{WIN_{pid}}}</span></h3><p class="rm-pcap">{cap}</p>{stage}'
            f'<p class="rm-unit">{unit_pre}<span class="rm-ans"><span class="rm-hide rm-unknown">?</span><span class="rm-late rm-unknown" style="animation-delay: {f3(ans_delay)}s">?</span><span class="rm-reveal" style="animation-delay: {f3(ans_delay)}s">{per}</span></span>{unit_post}</p></section>'), per, 0.3+(per-1)*0.9+(G-1)*0.08+0.6
def board(out,title,question,pa,pb,better,basis,fb):
    # first pass to get timing
    _,pa_per,da=panel('pa',*pa,0); _,pb_per,db=panel('pb',*pb,0)
    t=max(da,db)+0.3
    ha,_,_=panel('pa',*pa,t); hb,_,_=panel('pb',*pb,t)
    win='pa' if (pa_per<pb_per)==(better=='less') else 'pb'
    ha=ha.replace('{WIN_pa}','Better buy' if win=='pa' else '').replace('<span class="rm-win rm-reveal" style="animation-delay: {:}s"></span>'.format(f3(t+0.8)),'')
    hb=hb.replace('{WIN_pb}','Better buy' if win=='pb' else '').replace('<span class="rm-win rm-reveal" style="animation-delay: {:}s"></span>'.format(f3(t+0.8)),'')
    if 'Better buy' in ha+hb and basis.startswith('More'):
        ha=ha.replace('Better buy','Faster'); hb=hb.replace('Better buy','Faster')
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
box-sizing:border-box;max-width:1040px;margin:0 auto;padding:40px 16px 48px;background:#FFFFFF;color:var(--rm-ink);font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.4}}
.ratio-master *,.ratio-master *::before,.ratio-master *::after{{box-sizing:border-box}}
.ratio-master .rm-question{{max-width:36ch;margin:0 auto 8px;text-align:center;font-size:clamp(20px,3vw,26px);font-weight:700;line-height:1.3}}
.ratio-master .rm-basis{{margin:0 0 20px;text-align:center;font-size:18px;font-weight:700;color:var(--rm-muted)}}
.ratio-master .rm-panels{{display:flex;flex-wrap:wrap;justify-content:center;align-items:flex-start;gap:24px}}
.ratio-master .rm-panel{{min-width:min(100%, 290px);padding:14px 16px 16px;border:2px solid #D7DBE2;border-radius:18px}}
.ratio-master .rm-pname{{display:flex;align-items:center;justify-content:center;gap:10px;margin:0;font-size:22px}}
.ratio-master .rm-pcap{{margin:2px 0 12px;text-align:center;font-size:18px;color:var(--rm-muted)}}
.ratio-master .rm-win{{padding:2px 12px;border-radius:999px;background:var(--rm-ink);color:#FFFFFF;font-size:15px}}
.ratio-master .rm-stage{{position:relative;height:0}}
.ratio-master .rm-pile{{position:absolute;border-radius:14px;background:var(--rm-panel)}}
.ratio-master .rm-coin{{position:absolute;z-index:2;display:flex;align-items:center;justify-content:center;transition:translate .6s ease-in-out}}
.ratio-master .rm-item{{display:block;width:86%;height:86%}}
.ratio-master .rm-recv{{position:absolute;z-index:3;pointer-events:none}}
.ratio-master .rm-cup{{position:absolute;inset:0;width:100%;height:100%}}
.ratio-master .rm-ricon-wrap{{position:absolute;left:0;right:0;top:6%;display:flex;justify-content:center}}
.ratio-master .rm-ricon{{display:block;width:62%;height:auto}}
.ratio-master .rm-focus{{position:absolute;z-index:4;border:3px dashed var(--rm-ink);border-radius:14px}}
.ratio-master .rm-unit{{margin:14px 0 0;text-align:center;font-size:clamp(20px,3vw,24px);font-weight:800}}
.ratio-master .rm-ans{{position:relative;display:inline-flex;align-items:center;justify-content:center;min-width:48px;margin:0 4px;padding:0 8px;outline:3px solid var(--rm-ink);border-radius:10px;font-variant-numeric:tabular-nums}}
.ratio-master .rm-unknown{{color:var(--rm-muted)}}
.ratio-master .rm-reveal,.ratio-master .rm-late{{display:none}}
.ratio-master .rm-verdict{{margin:20px auto 0;max-width:40ch;text-align:center;font-size:clamp(20px,3vw,24px);font-weight:800}}
.ratio-master .rm-check{{max-width:560px;margin:22px auto 0;text-align:center}}
.ratio-master .rm-check summary{{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:10px 24px;border:2px solid var(--rm-ink);border-radius:999px;background:#FFFFFF;font-size:18px;font-weight:700;cursor:pointer;list-style:none}}
.ratio-master .rm-check summary::-webkit-details-marker{{display:none}}
.ratio-master .rm-check summary:focus-visible{{outline:3px solid var(--rm-focus);outline-offset:3px}}
.ratio-master .rm-check[open] summary{{background:var(--rm-panel)}}
.ratio-master .rm-feedback{{margin:14px 0 0;font-size:18px}}
.ratio-master:has(.rm-check[open]) .rm-coin{{translate:0 0 !important}}
.ratio-master:has(.rm-check[open]) .rm-hide{{display:none}}
.ratio-master:has(.rm-check[open]) .rm-reveal{{display:block;animation:rm-pop .45s ease-out both}}
.ratio-master:has(.rm-check[open]) .rm-ans .rm-reveal,.ratio-master:has(.rm-check[open]) .rm-win.rm-reveal{{display:inline-block}}
.ratio-master:has(.rm-check[open]) .rm-late{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;border-radius:10px;background:#FFFFFF;animation:rm-gone .3s ease-out both}}
.ratio-master .rm-sr{{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}}
@keyframes rm-pop{{from{{opacity:0;transform:scale(.7)}}to{{opacity:1;transform:none}}}}
@keyframes rm-gone{{from{{opacity:1}}to{{opacity:0}}}}
@media (prefers-reduced-motion: reduce){{.ratio-master .rm-coin{{transition:none}}.ratio-master .rm-reveal{{animation:none !important}}.ratio-master:has(.rm-check[open]) .rm-late{{display:none}}}}
</style>
</helmet>
<div class="ratio-master" data-master="V07">
<h2 class="rm-question">{question}</h2>
<p class="rm-basis">{basis}</p>
<p class="rm-sr">{pa[0]}: {pa[1]}. {pb[0]}: {pb[1]}. {basis}</p>
<div class="rm-panels" aria-hidden="true">
{ha}
{hb}
</div>
<p class="rm-verdict rm-reveal" style="animation-delay: {f3(t+0.8)}s" aria-hidden="true">{fb[0]}</p>
<details class="rm-check">
<summary>Check the answer</summary>
<p class="rm-feedback">{fb[1]}</p>
</details>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1040,"height":860}}}}'>
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
board('V07_ExampleA.dc.html','V07 Example A: better buy',
      'Store A sells 4 pencils for $8. Store B sells 3 pencils for $9. Which store is the better buy?',
      ('Store A','4 pencils for $8','coin','pencil',8,4,'$',' per pencil'),
      ('Store B','3 pencils for $9','coin','pencil',9,3,'$',' per pencil'),
      'less','Less money per pencil is better.',
      ('$2 is less than $3, so Store A is the better buy.','Store A: $8 ÷ 4 = $2 per pencil. Store B: $9 ÷ 3 = $3 per pencil. $2 < $3, so Store A is the better buy.'))
board('V07_ExampleB.dc.html','V07 Example B: faster machine',
      'Machine A makes 12 toys in 3 hours. Machine B makes 10 toys in 2 hours. Which machine is faster?',
      ('Machine A','12 toys in 3 hours','toy','hour',12,3,'',' toys per hour'),
      ('Machine B','10 toys in 2 hours','toy','hour',10,2,'',' toys per hour'),
      'more','More toys per hour is faster.',
      ('5 is more than 4, so Machine B is faster.','Machine A: 12 ÷ 3 = 4 toys per hour. Machine B: 10 ÷ 2 = 5 toys per hour. 5 > 4, so Machine B is faster.'))
board('V07_SkinBlocks.dc.html','V07 Skin test: apples',
      'Stand A sells 4 apples for $8. Stand B sells 3 apples for $9. Which stand is the better buy?',
      ('Stand A','4 apples for $8','coin','apple',8,4,'$',' per apple'),
      ('Stand B','3 apples for $9','coin','apple',9,3,'$',' per apple'),
      'less','Less money per apple is better.',
      ('$2 is less than $3, so Stand A is the better buy.','Stand A: $8 ÷ 4 = $2 per apple. Stand B: $9 ÷ 3 = $3 per apple. $2 < $3, so Stand A is the better buy.'))
if os.path.exists(P+'/canvas.json'):
    c=json.load(open(P+'/canvas.json'))
    for i,(f,t) in enumerate([("V07_ExampleA.dc.html","V07 Example A · price per pencil (less is better)"),("V07_ExampleB.dc.html","V07 Example B · toys per hour (more is better)"),("V07_SkinBlocks.dc.html","V07 Skin test · apples")]):
        c['boards'][f]={"x":i*1120,"y":10220,"w":1040,"h":860,"title":t,"expand":"fill","is_interactive":True}
        if f not in c['order']: c['order'].append(f)
    c['notes']['v07heading']={"x":0,"y":9980,"text":"V07 Comparator — compare per one","kind":"title1","maxW":3280}
    c['boards']['V06_BuildSpec.dc.html']={"x":3360,"y":8920,"w":1040,"h":1000,"title":"V06 build sheet","expand":"fill"}
    if 'V06_BuildSpec.dc.html' not in c['order']: c['order'].append('V06_BuildSpec.dc.html')
    json.dump(c,open(P+'/canvas.json','w'),indent=2,ensure_ascii=False)
print('ok')
