import sys
P=sys.argv[1]
BEAD='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" aria-hidden="true" focusable="false"><circle class="rm-body" cx="16" cy="16" r="14"></circle><circle class="rm-detail" cx="16" cy="16" r="4.5"></circle></svg>'
BLOCK='<svg class="rm-obj rm-obj-{s}" viewBox="0 0 32 32" aria-hidden="true" focusable="false"><rect class="rm-body" x="2" y="2" width="28" height="28" rx="4"></rect><rect class="rm-detail" x="9" y="9" width="14" height="14" rx="2"></rect></svg>'
VARS={
 'blueyellow_beads':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#FFFFFF;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FFFFFF;--rm-b-text:#6E5000;",
 'blueyellow_blocks':"--rm-a:#1E5BD8;--rm-a-edge:#123E99;--rm-a-detail:#4C7FE6;--rm-a-text:#1A4FBF;--rm-b:#F5BE0B;--rm-b-edge:#8A6400;--rm-b-detail:#FAD55C;--rm-b-text:#6E5000;",
 'redwhite_beads':"--rm-a:#C8322B;--rm-a-edge:#8C1E19;--rm-a-detail:#FFFFFF;--rm-a-text:#B02A23;--rm-b:#FFFFFF;--rm-b-edge:#2F3440;--rm-b-detail:#DFE3E9;--rm-b-text:#2F3440;",
}
HEAD='''<!doctype html>
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
.ratio-master{{--rm-ink:#1B1F2A;--rm-muted:#4A5263;--rm-panel:#F3F4F7;--rm-rule:#C9CED7;
{vars}
box-sizing:border-box;max-width:1040px;margin:0 auto;padding:40px 16px 48px;background:#FFFFFF;color:var(--rm-ink);font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.4}}
.ratio-master *,.ratio-master *::before,.ratio-master *::after{{box-sizing:border-box}}
.ratio-master .rm-question{{max-width:34ch;margin:0 auto 28px;text-align:center;font-size:clamp(20px,3vw,26px);font-weight:700;line-height:1.3}}
.ratio-master .rm-model{{display:flex;flex-direction:column;gap:10px;max-width:520px;margin:0 auto}}
.ratio-master .rm-pair{{display:grid;grid-template-columns:minmax(0,1fr) 2px minmax(0,1fr);align-items:center;column-gap:18px}}
.ratio-master .rm-pair > :first-child{{display:flex;flex-wrap:wrap;justify-content:flex-end;gap:6px}}
.ratio-master .rm-pair > :last-child{{display:flex;flex-wrap:wrap;justify-content:flex-start;gap:6px}}
.ratio-master .rm-split{{align-self:stretch;background:var(--rm-rule)}}
.ratio-master .rm-group{{padding:12px 0;background:var(--rm-panel);border-radius:14px}}
.ratio-master .rm-head{{font-size:20px;font-weight:700}}
.ratio-master .rm-totals{{margin-top:6px;padding-top:12px;border-top:3px solid var(--rm-ink)}}
.ratio-master .rm-totals .rm-split{{background:transparent}}
.ratio-master .rm-total{{position:relative;display:inline-block;min-width:64px;padding:2px 12px;border-radius:12px;text-align:center;font-size:40px;font-weight:800;line-height:1.2;font-variant-numeric:tabular-nums}}
.ratio-master .rm-answer{{outline:3px solid var(--rm-ink)}}
.ratio-master .rm-q{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;border-radius:12px;background:#FFFFFF;color:var(--rm-muted)}}
.ratio-master .rm-obj{{display:block;width:36px;height:36px;flex:none}}
.ratio-master .rm-obj .rm-body{{stroke-width:2}}
.ratio-master .rm-obj .rm-detail{{stroke-width:1.5}}
.ratio-master .rm-obj-a .rm-body{{fill:var(--rm-a);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-a .rm-detail{{fill:var(--rm-a-detail);stroke:var(--rm-a-edge)}}
.ratio-master .rm-obj-b .rm-body{{fill:var(--rm-b);stroke:var(--rm-b-edge)}}
.ratio-master .rm-obj-b .rm-detail{{fill:var(--rm-b-detail);stroke:var(--rm-b-edge)}}
.ratio-master .rm-a-text{{color:var(--rm-a-text)}}
.ratio-master .rm-b-text{{color:var(--rm-b-text)}}
.ratio-master .rm-notation{{display:flex;align-items:center;justify-content:center;gap:16px;margin:28px 0 0;font-size:40px;font-weight:800;font-variant-numeric:tabular-nums}}
.ratio-master .rm-frac{{display:inline-flex;flex-direction:column;align-items:center;line-height:1.15}}
.ratio-master .rm-frac > span{{padding:0 8px}}
.ratio-master .rm-frac > span + span{{border-top:4px solid var(--rm-ink)}}
.ratio-master .rm-sr{{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}}
@keyframes rm-add{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:none}}}}
@keyframes rm-fade{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes rm-out{{from{{opacity:1}}to{{opacity:0}}}}
.ratio-master .rm-step{{animation:rm-add .6s ease-out both}}
.ratio-master .rm-fade{{animation:rm-fade .5s ease-out both}}
.ratio-master .rm-out{{animation:rm-out .4s ease-out both}}
@media (prefers-reduced-motion: reduce){{.ratio-master .rm-step,.ratio-master .rm-fade{{animation:none}}.ratio-master .rm-q{{display:none}}}}
@media (max-width: 480px){{.ratio-master .rm-obj{{width:30px;height:30px}}.ratio-master .rm-pair{{column-gap:10px}}.ratio-master .rm-total{{font-size:32px}}}}
</style>
</helmet>
'''
FOOT='''</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1040,"height":780}}'>
class Component extends DCLogic {
renderVals() {
return {};
}
}
</script>
</body>
</html>
'''
def board(out,title,varkey,obj,la,lb,noun,A,B,n,question,notation=None):
    gap=1.0 if n<=3 else 0.8
    o=[HEAD.format(title=title,vars=VARS[varkey])]
    o.append(f'<div class="ratio-master" data-master="V02" data-skin="{"blocks" if obj==BLOCK else "beads"}">\n')
    o.append(f'<h2 class="rm-question">{question}</h2>\n')
    o.append(f'<p class="rm-sr">Each group has {A} {la} {noun} on the left and {B} {lb} {noun} on the right. There are {n} groups. That makes {A*n} {la} and {B*n} {lb} {noun}.</p>\n')
    o.append('<div class="rm-model" aria-hidden="true">\n')
    o.append(f'<div class="rm-pair rm-head"><span class="rm-a-text">{la}</span><span class="rm-split"></span><span class="rm-b-text">{lb}</span></div>\n')
    for k in range(n):
        st='' if k==0 else f' rm-step" style="animation-delay: {k*gap:g}s'
        o.append(f'<div class="rm-pair rm-group{st}"><div>{obj.format(s="a")*A}</div><span class="rm-split"></span><div>{obj.format(s="b")*B}</div></div>\n')
    t=(n-1)*gap+0.8
    o.append(f'<div class="rm-pair rm-totals"><div><span class="rm-total rm-a-text rm-fade" style="animation-delay: {t:g}s">{A*n}</span></div><span class="rm-split"></span><div><span class="rm-total rm-answer rm-b-text">{B*n}<span class="rm-q rm-out" style="animation-delay: {t+0.8:g}s">?</span></span></div></div>\n')
    o.append('</div>\n')
    if notation=='ratio':
        o.append(f'<p class="rm-notation rm-fade" style="animation-delay: {t+1.6:g}s" aria-label="{A} to {B} equals {A*n} to {B*n}"><span><span class="rm-a-text">{A}</span> : <span class="rm-b-text">{B}</span></span><span>=</span><span><span class="rm-a-text">{A*n}</span> : <span class="rm-b-text">{B*n}</span></span></p>\n')
    elif notation=='frac':
        o.append(f'<p class="rm-notation rm-fade" style="animation-delay: {t+1.6:g}s" aria-label="{A} over {B} equals {A*n} over {B*n}"><span class="rm-frac"><span class="rm-a-text">{A}</span><span class="rm-b-text">{B}</span></span><span>=</span><span class="rm-frac"><span class="rm-a-text">{A*n}</span><span class="rm-b-text">{B*n}</span></span></p>\n')
    o.append('</div>\n'); o.append(FOOT)
    open(P+'/'+out,'w').write(''.join(o))
qa='2 blue beads go with 3 yellow beads. How many yellow beads go with 6 blue beads?'
qb='3 red beads go with 2 white beads. How many white beads go with 12 red beads?'
qk='2 blue blocks go with 3 yellow blocks. How many yellow blocks go with 6 blue blocks?'
board('Main.dc.html','V02 Example A','blueyellow_beads',BEAD,'blue','yellow','beads',2,3,3,qa)
board('ExampleB.dc.html','V02 Example B','redwhite_beads',BEAD,'red','white','beads',3,2,4,qb)
board('SkinBlocks.dc.html','V02 Skin test: blocks','blueyellow_blocks',BLOCK,'blue','yellow','blocks',2,3,3,qk)
board('V02_A_Fraction.dc.html','V02 Example A: fraction','blueyellow_beads',BEAD,'blue','yellow','beads',2,3,3,qa,'frac')
board('V02_B_Fraction.dc.html','V02 Example B: fraction','redwhite_beads',BEAD,'red','white','beads',3,2,4,qb,'frac')
board('V02_A_RatioOnly.dc.html','V02 Example A: ratio','blueyellow_beads',BEAD,'blue','yellow','beads',2,3,3,qa,'ratio')
board('V02_B_RatioOnly.dc.html','V02 Example B: ratio','redwhite_beads',BEAD,'red','white','beads',3,2,4,qb,'ratio')
print('ok')
