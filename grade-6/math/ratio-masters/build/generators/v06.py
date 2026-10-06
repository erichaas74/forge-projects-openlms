import sys, json, math, os
P=sys.argv[1]
ITEMS={
 'coin':'<svg class="rm-item" viewBox="0 0 32 32" focusable="false"><circle cx="16" cy="16" r="14" fill="#F2C12E" stroke="#8A6400" stroke-width="2"></circle><text x="16" y="21.5" text-anchor="middle" font-size="16" font-weight="800" fill="#6E5000" font-family="system-ui, sans-serif">$</text></svg>',
 'apple':'<svg class="rm-item" viewBox="0 0 32 32" focusable="false"><path d="M16 9 C10 5 3 9 4 17 C5 25 11 30 16 27 C21 30 27 25 28 17 C29 9 22 5 16 9 Z" fill="#D23A2E" stroke="#8C1E19" stroke-width="2"></path><path d="M16 9 C16 6 17 4 19 2" fill="none" stroke="#5B3A1E" stroke-width="2" stroke-linecap="round"></path><path d="M18 6 C21 3 25 4 26 6 C23 8 20 8 18 6 Z" fill="#3E8E3E"></path></svg>',
 'block':'<svg class="rm-item" viewBox="0 0 32 32" focusable="false"><rect x="2" y="2" width="28" height="28" rx="4" fill="#1E5BD8" stroke="#123E99" stroke-width="2"></rect><rect x="9" y="9" width="14" height="14" rx="2" fill="#4C7FE6" stroke="#123E99" stroke-width="1.5"></rect></svg>',
}
GROUPS={
 'notebook':'<svg class="rm-gicon" viewBox="0 0 40 48" focusable="false"><rect x="7" y="3" width="29" height="42" rx="4" fill="#FFFFFF" stroke="#1B1F2A" stroke-width="2.5"></rect><path d="M15 15 H30 M15 22 H30 M15 29 H26" stroke="#9AA1AE" stroke-width="2.5" stroke-linecap="round"></path><circle cx="7" cy="11" r="2.5" fill="#FFFFFF" stroke="#1B1F2A" stroke-width="2"></circle><circle cx="7" cy="20" r="2.5" fill="#FFFFFF" stroke="#1B1F2A" stroke-width="2"></circle><circle cx="7" cy="29" r="2.5" fill="#FFFFFF" stroke="#1B1F2A" stroke-width="2"></circle><circle cx="7" cy="38" r="2.5" fill="#FFFFFF" stroke="#1B1F2A" stroke-width="2"></circle></svg>',
 'bag':'<svg class="rm-gicon" viewBox="0 0 40 48" focusable="false"><path d="M14 14 C14 6 26 6 26 14" fill="none" stroke="#1B1F2A" stroke-width="2.5" stroke-linecap="round"></path><path d="M6 14 H34 L31 43 C31 45 29 46 27 46 H13 C11 46 9 45 9 43 Z" fill="#E9D8B4" stroke="#1B1F2A" stroke-width="2.5" stroke-linejoin="round"></path></svg>',
 'box':'<svg class="rm-gicon" viewBox="0 0 40 48" focusable="false"><rect x="4" y="16" width="32" height="28" rx="3" fill="#E9D8B4" stroke="#1B1F2A" stroke-width="2.5"></rect><path d="M4 22 H36" stroke="#1B1F2A" stroke-width="2.5"></path><path d="M10 16 L14 8 H26 L30 16" fill="none" stroke="#1B1F2A" stroke-width="2.5" stroke-linejoin="round"></path></svg>',
}
def f3(x): return f"{x:.3f}".rstrip('0').rstrip('.')
def board(out,title,item,group,T,G,question,pile_cap,group_cap,ans_pre,ans_post,unit_word,fb):
    assert T%G==0
    per=T//G
    PC=math.ceil(T/2)               # pile columns (2 rows)
    gw=1.7                          # width of one group, in item units
    Wu=max(PC, G*gw)
    gw=Wu/G
    pile_off=(Wu-PC)/2
    icon_y=2.2+0.7; icon_h=1.1
    jar_y=icon_y+icon_h+0.15; jar_w=min(1.5, gw-0.15); jar_h=per*1.05+0.45
    stack_y=jar_y+jar_h-0.25-per*1.05   # items settle from the bottom of the jar
    Hu=jar_y+jar_h+0.15
    coins=[]
    for k in range(T):
        pr, pcol = divmod(k, PC)
        sx=pile_off+pcol; sy=pr*1.1
        r, c = divmod(k, G)
        tx=c*gw+(gw-1)/2; ty=stack_y+(per-1-r)*1.05
        dx=(sx-tx)*100; dy=(sy-ty)*100
        delay=0.3+r*0.9+c*0.08
        coins.append(f'<span class="rm-coin" style="left: {f3(tx/Wu*100)}%; top: {f3(ty/Hu*100)}%; translate: {f3(dx)}% {f3(dy)}%; transition-delay: {f3(delay)}s">{ITEMS[item]}</span>')
    top_y=icon_y+0.25                          # container shape starts here (handle / lid / spiral)
    cw=jar_w; ch=jar_y+jar_h-top_y
    def shape(kind):
        W=cw*100; H=ch*100; t=(jar_y-top_y)*100   # t = where the body starts
        st='fill="rgba(150,180,220,0.18)" stroke="rgba(27,31,42,0.65)" stroke-width="7" stroke-linejoin="round"'
        if kind=='bag':
            return (f'<path d="M{W*0.3:.0f} {t:.0f} C{W*0.3:.0f} {t*0.15:.0f} {W*0.7:.0f} {t*0.15:.0f} {W*0.7:.0f} {t:.0f}" fill="none" stroke="rgba(27,31,42,0.65)" stroke-width="7" stroke-linecap="round"></path>'
                    f'<path d="M4 {t:.0f} H{W-4:.0f} L{W-12:.0f} {H-20:.0f} Q{W-14:.0f} {H-4:.0f} {W-30:.0f} {H-4:.0f} H30 Q14 {H-4:.0f} 12 {H-20:.0f} Z" {st}></path>')
        if kind=='box':
            return (f'<path d="M4 {t:.0f} L{W*0.18:.0f} {t*0.2:.0f} M{W-4:.0f} {t:.0f} L{W*0.82:.0f} {t*0.2:.0f}" fill="none" stroke="rgba(27,31,42,0.65)" stroke-width="7" stroke-linecap="round"></path>'
                    f'<rect x="4" y="{t:.0f}" width="{W-8:.0f}" height="{H-t-4:.0f}" rx="10" {st}></rect>')
        # notebook: a see-through notebook; spiral rings along the top edge
        rings=''.join(f'<circle cx="{W*(i+0.5)/4:.0f}" cy="{t:.0f}" r="9" fill="#FFFFFF" stroke="rgba(27,31,42,0.65)" stroke-width="6"></circle>' for i in range(4))
        return f'<rect x="4" y="{t:.0f}" width="{W-8:.0f}" height="{H-t-4:.0f}" rx="12" {st}></rect>{rings}'
    kind={'notebook':'notebook','bag':'bag','box':'box'}[group]
    icons=''.join(f'<span class="rm-jar" style="left: {f3((c*gw+(gw-cw)/2)/Wu*100)}%; top: {f3(top_y/Hu*100)}%; width: {f3(cw/Wu*100)}%; height: {f3(ch/Hu*100)}%"><svg viewBox="0 0 {cw*100:.0f} {ch*100:.0f}" focusable="false">{shape(kind)}</svg></span>' for c in range(G))
    done=0.3+(per-1)*0.9+(G-1)*0.08+0.6
    fx=(gw-jar_w)/2-0.12
    hl=f'<span class="rm-focus rm-reveal" style="left: {f3(fx/Wu*100)}%; top: {f3((icon_y+0.05)/Hu*100)}%; width: {f3((jar_w+0.24)/Wu*100)}%; height: {f3((Hu-icon_y-0.13)/Hu*100)}%; animation-delay: {f3(done+0.2)}s"></span>'
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
.ratio-master .rm-question{{max-width:34ch;margin:0 auto 24px;text-align:center;font-size:clamp(20px,3vw,26px);font-weight:700;line-height:1.3}}
.ratio-master .rm-wrap{{width:min(100%, {round(Wu*56)}px);margin:0 auto}}
.ratio-master .rm-cap{{margin:0 0 8px;text-align:center;font-size:20px;font-weight:700}}
.ratio-master .rm-cap-bottom{{margin:6px 0 0}}
.ratio-master .rm-stage{{position:relative;height:0;padding-top:{f3(Hu/Wu*100)}%}}
.ratio-master .rm-pile{{position:absolute;left:{f3((pile_off-0.15)/Wu*100)}%;top:{f3(-0.15/Hu*100)}%;width:{f3((PC+0.3)/Wu*100)}%;height:{f3(2.5/Hu*100)}%;border-radius:16px;background:var(--rm-panel)}}
.ratio-master .rm-coin{{position:absolute;z-index:2;width:{f3(100/Wu)}%;height:{f3(100/Hu)}%;display:flex;align-items:center;justify-content:center;transition:translate .6s ease-in-out}}
.ratio-master .rm-item{{display:block;width:86%;height:86%}}
.ratio-master .rm-group{{position:absolute;display:flex;align-items:center;justify-content:center}}
.ratio-master .rm-gicon{{display:block;height:100%;width:auto}}
.ratio-master .rm-jar{{position:absolute;z-index:3;pointer-events:none}}
.ratio-master .rm-jar svg{{display:block;width:100%;height:100%;overflow:visible}}
.ratio-master .rm-focus{{position:absolute;z-index:4;border:3px dashed var(--rm-ink);border-radius:14px}}
.ratio-master .rm-answer{{margin:24px 0 0;text-align:center;font-size:clamp(24px,4vw,32px);font-weight:800}}
.ratio-master .rm-ans{{position:relative;display:inline-flex;align-items:center;justify-content:center;min-width:56px;margin:0 4px;padding:0 10px;outline:3px solid var(--rm-ink);border-radius:12px;font-variant-numeric:tabular-nums}}
.ratio-master .rm-unknown{{color:var(--rm-muted)}}
.ratio-master .rm-reveal,.ratio-master .rm-late{{display:none}}
.ratio-master .rm-check{{max-width:520px;margin:24px auto 0;text-align:center}}
.ratio-master .rm-check summary{{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:10px 24px;border:2px solid var(--rm-ink);border-radius:999px;background:#FFFFFF;font-size:18px;font-weight:700;cursor:pointer;list-style:none}}
.ratio-master .rm-check summary::-webkit-details-marker{{display:none}}
.ratio-master .rm-check summary:focus-visible{{outline:3px solid var(--rm-focus);outline-offset:3px}}
.ratio-master .rm-check[open] summary{{background:var(--rm-panel)}}
.ratio-master .rm-feedback{{margin:14px 0 0;font-size:18px}}
.ratio-master:has(.rm-check[open]) .rm-coin{{translate:0 0 !important}}
.ratio-master:has(.rm-check[open]) .rm-hide{{display:none}}
.ratio-master:has(.rm-check[open]) .rm-reveal{{display:block;animation:rm-pop .45s ease-out both}}
.ratio-master:has(.rm-check[open]) span.rm-ans .rm-reveal{{display:inline}}
.ratio-master:has(.rm-check[open]) .rm-late{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;border-radius:12px;background:#FFFFFF;animation:rm-gone .3s ease-out {f3(done+0.6)}s both}}
.ratio-master .rm-sr{{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}}
@keyframes rm-pop{{from{{opacity:0;transform:scale(.7)}}to{{opacity:1;transform:none}}}}
@keyframes rm-gone{{from{{opacity:1}}to{{opacity:0}}}}
@media (prefers-reduced-motion: reduce){{.ratio-master .rm-coin{{transition:none}}.ratio-master .rm-reveal{{animation:none !important}}.ratio-master:has(.rm-check[open]) .rm-late{{display:none}}}}
</style>
</helmet>
<div class="ratio-master" data-master="V06" data-skin="{item}-{group}">
<h2 class="rm-question">{question}</h2>
<p class="rm-sr">{pile_cap} in a pile, to be shared equally among {group_cap}.</p>
<div class="rm-wrap" aria-hidden="true">
<p class="rm-cap">{pile_cap}</p>
<div class="rm-stage">
<span class="rm-pile"></span>
{icons}
{chr(10).join(coins)}
{hl}
</div>
<p class="rm-cap rm-cap-bottom">{group_cap}</p>
</div>
<p class="rm-answer">{ans_pre}<span class="rm-ans"><span class="rm-hide rm-unknown">?</span><span class="rm-late rm-unknown">?</span><span class="rm-reveal" style="animation-delay: {f3(done+0.6)}s">{per}</span></span>{ans_post}</p>
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
board('V06_ExampleA.dc.html','V06 Example A: cost of 1 notebook','coin','notebook',18,6,
      '6 notebooks cost $18. How much does 1 notebook cost?','$18','6 notebooks','1 notebook costs $','',
      'dollars','$18 shared equally by 6 notebooks is $3 each: 18 ÷ 6 = 3. Answer: $3 per notebook.')
board('V06_ExampleB.dc.html','V06 Example B: apples in 1 bag','apple','bag',20,5,
      '20 apples fill 5 bags equally. How many apples go in 1 bag?','20 apples','5 bags','1 bag holds ',' apples',
      'apples','20 apples shared equally by 5 bags is 4 each: 20 ÷ 5 = 4. Answer: 4 apples per bag.')
board('V06_SkinBlocks.dc.html','V06 Skin test: blocks in boxes','block','box',18,6,
      '18 blocks are packed equally into 6 boxes. How many blocks go in 1 box?','18 blocks','6 boxes','1 box holds ',' blocks',
      'blocks','18 blocks shared equally by 6 boxes is 3 each: 18 ÷ 6 = 3. Answer: 3 blocks per box.')
if os.path.exists(P+'/canvas.json'):
    c=json.load(open(P+'/canvas.json'))
    for i,(f,t) in enumerate([("V06_ExampleA.dc.html","V06 Example A · $18 ÷ 6 notebooks"),("V06_ExampleB.dc.html","V06 Example B · 20 apples ÷ 5 bags"),("V06_SkinBlocks.dc.html","V06 Skin test · 18 blocks ÷ 6 boxes")]):
        c['boards'][f]={"x":i*1120,"y":8920,"w":1040,"h":820,"title":t,"expand":"fill","is_interactive":True}
        if f not in c['order']: c['order'].append(f)
    c['notes']['v06heading']={"x":0,"y":8680,"text":"V06 Equal Distributor — unit rates","kind":"title1","maxW":3280}
    json.dump(c,open(P+'/canvas.json','w'),indent=2,ensure_ascii=False)
print('ok')
