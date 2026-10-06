import sys
P=sys.argv[1]
BEAD='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><circle class="rm-body" cx="16" cy="16" r="14"></circle><circle class="rm-detail" cx="16" cy="16" r="4.5"></circle></svg>'
BLOCK='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" focusable="false"><rect class="rm-body" x="2" y="2" width="28" height="28" rx="4"></rect><rect class="rm-detail" x="9" y="9" width="14" height="14" rx="2"></rect></svg>'
VARS={
 'by':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#FFFFFF;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FFFFFF;--rm-b-text:#6E5000;--rm-thread:#9AA1AE;",
 'byk':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#4C7FE6;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FAD55C;--rm-b-text:#6E5000;--rm-thread:transparent;",
 'rw':"--rm-a:#C8322B;--rm-a-edge:#8C1E19;--rm-a-detail:#FFFFFF;--rm-a-text:#B02A23;--rm-b:#FFFFFF;--rm-b-edge:#2F3440;--rm-b-detail:#DFE3E9;--rm-b-text:#2F3440;--rm-thread:#9AA1AE;",
}
def pct(x,n): return f"{x*100/n:.3f}".rstrip('0').rstrip('.')+'%'
def name(d): return f"rm-mv-{'p' if d>=0 else 'n'}{abs(d)}"
def board(out,title,vk,obj,seq,la,lb,question,kind='pp'):
    A=seq.count('a'); B=seq.count('b')
    right = A+B if kind=='pw' else B
    n = A+1+right
    off=(n-len(seq))/2
    dxs=set(); moved=[]; unsorted=[]
    ia=ib=0
    for i,s in enumerate(seq):
        unsorted.append(f'<span class="rm-slot" style="left: {pct(i+off,n)}; width: {pct(1,n)}">{obj.format(s=s)}</span>')
        if kind=='pw':
            if s=='a': final=A+1+ia; ia+=1
            else: final=A+1+A+ib; ib+=1
        else:
            if s=='a': final=ia; ia+=1
            else: final=A+1+ib; ib+=1
        dx=round((i+off-final)*100); dxs.add(dx)
        moved.append(f'<span class="rm-slot rm-move {name(dx)}" style="left: {pct(final,n)}; width: {pct(1,n)}; animation-delay: {0.8+0.2*i:g}s">{obj.format(s=s)}</span>')
    if kind=='pw':
        dxs.add(None)
        for j in range(A):
            moved.append(f'<span class="rm-slot rm-fade" style="left: {pct(j,n)}; width: {pct(1,n)}; animation-delay: {0.8+0.2*len(seq)+0.9:g}s">{obj.format(s="a")}</span>')
    end=0.8+0.2*(len(seq)-1)+1.0 + (0.9 if kind=='pw' else 0)
    kf=''.join(f"@keyframes {name(d)}{{from{{transform:translate({d}%, calc(-100% - 72px))}}to{{transform:none}}}}\n.ratio-master .{name(d)}{{animation-name:{name(d)}}}\n" for d in sorted(x for x in dxs if x is not None))
    rnum = A+B if kind=='pw' else B
    rlab = 'all' if kind=='pw' else lb
    rcls = '' if kind=='pw' else ' rm-b-text'
    def row(cls,a,colon,b,delay,anim):
        return (f'<div class="{cls}">'
          f'<span class="rm-cell rm-a-text {anim}" style="left: 0%; width: {pct(A,n)}; animation-delay: {delay:g}s">{a}</span>'
          f'<span class="rm-cell {anim}" style="left: {pct(A,n)}; width: {pct(1,n)}; animation-delay: {delay:g}s">{colon}</span>'
          f'<span class="rm-cell{rcls} {anim}" style="left: {pct(A+1,n)}; width: {pct(right,n)}; animation-delay: {delay:g}s">{b}</span></div>\n')
    order=', '.join({'a':la,'b':lb}[s] for s in seq)
    noun='blocks' if obj==BLOCK else 'beads'
    sr=(f'Unsorted: {len(seq)} {noun}: {order}. ' + (f'Sorted: {A} {la} {noun} on the left, {B} {lb} {noun} on the right. {la} : {lb} = {A} : {B}.' if kind=='pp'
         else f'Sorted: {A} {la} {noun} on the left, all {A+B} {noun} on the right. {la} : all = {A} : {A+B}.'))
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
.ratio-master .rm-stage{{width:min(100%, {n*60}px);margin:0 auto}}
.ratio-master .rm-unsorted,.ratio-master .rm-labels,.ratio-master .rm-beads,.ratio-master .rm-nums{{position:relative}}
.ratio-master .rm-unsorted,.ratio-master .rm-beads{{height:0;padding-top:calc(100% / {n})}}
.ratio-master .rm-unsorted{{margin-bottom:32px}}
.ratio-master .rm-labels{{height:32px;font-size:18px;font-weight:700}}
.ratio-master .rm-answer{{padding:8px 0 14px;background:var(--rm-panel);border-radius:16px}}
.ratio-master .rm-nums{{height:clamp(52px,9vw,76px);margin-top:10px;font-size:clamp(36px,7vw,60px);font-weight:800;font-variant-numeric:tabular-nums}}
.ratio-master .rm-cell{{position:absolute;top:0;bottom:0;display:flex;align-items:center;justify-content:center;white-space:nowrap}}
.ratio-master .rm-beads .rm-colon{{font-size:clamp(28px,5vw,44px);font-weight:800}}
.ratio-master .rm-slot{{position:absolute;top:0;height:100%;display:flex;align-items:center;justify-content:center}}
.ratio-master .rm-slot .rm-obj{{display:block;width:84%;height:84%}}
.ratio-master .rm-thread{{position:absolute;top:50%;height:2px;margin-top:-1px;background:var(--rm-thread)}}
.ratio-master .rm-obj .rm-body{{stroke-width:2}}
.ratio-master .rm-obj .rm-detail{{stroke-width:1.5}}
.ratio-master .rm-obj-a .rm-body{{fill:var(--rm-a);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-a .rm-detail{{fill:var(--rm-a-detail);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-b .rm-body{{fill:var(--rm-b);stroke:var(--rm-b-edge)}}
.ratio-master .rm-obj-b .rm-detail{{fill:var(--rm-b-detail);stroke:var(--rm-b-edge)}}
.ratio-master .rm-a-text{{color:var(--rm-a-text)}}
.ratio-master .rm-b-text{{color:var(--rm-b-text)}}
.ratio-master .rm-sr{{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}}
@keyframes rm-add{{from{{opacity:0;transform:translateY(-14px)}}to{{opacity:1;transform:none}}}}
@keyframes rm-fade{{from{{opacity:0}}to{{opacity:1}}}}
.ratio-master .rm-move{{position:absolute;z-index:1;animation-duration:1s;animation-timing-function:ease-in-out;animation-fill-mode:both}}
{kf}.ratio-master .rm-fade{{animation:rm-fade .5s ease-out both}}
.ratio-master .rm-add{{animation:rm-add .6s ease-out both}}
@media (prefers-reduced-motion: reduce){{.ratio-master .rm-move,.ratio-master .rm-fade,.ratio-master .rm-add{{animation:none}}}}
</style>
</helmet>
<div class="ratio-master" data-master="V01" data-kind="{'part_to_whole' if kind=='pw' else 'part_to_part'}" data-skin="{'blocks' if obj==BLOCK else 'beads'}">
<h2 class="rm-question">{question}</h2>
<p class="rm-sr">{sr}</p>
<div class="rm-stage" aria-hidden="true">
<div class="rm-unsorted">
<span class="rm-thread" style="left: {pct(off+0.5,n)}; width: {pct(len(seq)-1,n)}"></span>
{chr(10).join(unsorted)}
</div>
<div class="rm-answer">
{row('rm-labels',la,'',rlab,end,'rm-fade')}<div class="rm-beads">
{chr(10).join(moved)}
<span class="rm-cell rm-colon rm-fade" style="left: {pct(A,n)}; width: {pct(1,n)}; animation-delay: {end:g}s">:</span>
</div>
{row('rm-nums',A,':',rnum,end+0.7,'rm-add')}</div>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1040,"height":620}}}}'>
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
board('V01_PartPart.dc.html','V01 Example A: blue to yellow','by',BEAD,'ababa','blue','yellow','What is the ratio of blue beads to yellow beads?')
board('V01_PartWhole.dc.html','V01 Example A variant: blue to all beads','by',BEAD,'ababa','blue','yellow','What is the ratio of blue beads to all the beads?','pw')
board('V01_ExampleB.dc.html','V01 Example B: red to white','rw',BEAD,'ababbabab','red','white','What is the ratio of red beads to white beads?')
board('V01_SkinBlocks.dc.html','V01 Skin test: blue to yellow blocks','byk',BLOCK,'ababa','blue','yellow','What is the ratio of blue blocks to yellow blocks?')
print('ok')
