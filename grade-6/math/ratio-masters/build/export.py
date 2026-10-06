"""Export Design-canvas boards (.dc.html) to production files.

For each example writes, under <out>/<master>/examples/<slug>/:
  fragment.html  the div.ratio-master markup only (paste into Moodle/Open LMS)
  styles.css     the scoped stylesheet for that fragment (no global rules)
  preview.html   a self-contained page (fragment + styles) for local review

Usage: python3 export.py <dir-with-.dc.html> <out-dir>
"""
import os, re, sys

MAP = {
    'V01-object-groups': {
        'V01_PartPart': 'example-a-part-to-part', 'V01_PartWhole': 'example-a-part-to-whole',
        'V01_ExampleB': 'example-b', 'V01_SkinBlocks': 'skin-blocks'},
    'V02-group-multiplier': {
        'Main': 'example-a', 'ExampleB': 'example-b', 'SkinBlocks': 'skin-blocks',
        'V02_A_Fraction': 'example-a-with-fraction', 'V02_B_Fraction': 'example-b-with-fraction',
        'V02_A_RatioOnly': 'example-a-with-ratio', 'V02_B_RatioOnly': 'example-b-with-ratio'},
    'V02F-group-multiplier-fractions': {
        'V02F_ExampleA': 'example-a', 'V02F_ExampleB': 'example-b', 'V02F_SkinBlocks': 'skin-blocks'},
    'V03-scale-machine': {
        'V03_ExampleA': 'example-a', 'V03_ExampleB': 'example-b', 'V03_SkinBlocks': 'skin-blocks'},
    'V04-ratio-table': {
        'V04_ExampleA': 'example-a', 'V04_ExampleB': 'example-b', 'V04_SkinBlocks': 'skin-blocks'},
    'V05-double-number-line': {
        'V05_ExampleA': 'example-a', 'V05_ExampleB': 'example-b', 'V05_SkinBlocks': 'skin-blocks'},
    'V06-equal-distributor': {
        'V06_ExampleA': 'example-a', 'V06_ExampleB': 'example-b', 'V06_SkinBlocks': 'skin-blocks'},
    'V07-comparator': {
        'V07_ExampleA': 'example-a', 'V07_ExampleB': 'example-b', 'V07_SkinBlocks': 'skin-apples'},
    'V08-mixture-container': {
        'V08_ExampleA': 'example-a', 'V08_ExampleB': 'example-b', 'V08_SkinBlocks': 'skin-pink-paint'},
    'V08T-mixture-to-a-total': {
        'V08T_ExampleA': 'example-a', 'V08T_ExampleB': 'example-b', 'V08T_SkinBlocks': 'skin-pink-paint'},
    'V09-table-to-graph': {
        'V09_ExampleA': 'example-a', 'V09_ExampleB': 'example-b', 'V09_SkinBlocks': 'skin-blocks'},
    'V01F-part-over-whole-fraction': {
        'V01F_ExampleA': 'example-a', 'V01F_ExampleB': 'example-b', 'V01F_SkinBlocks': 'skin-blocks'},
    'V10-necklace-shortage': {
        'V10_ExampleA': 'example-a', 'V10_ExampleB': 'example-b', 'V10_SkinBlocks': 'skin-blocks-bracelets'},
}

def split(src):
    title = re.search(r'<title>(.*?)</title>', src, re.S).group(1).strip()
    style = re.search(r'<helmet>\s*<style>(.*?)</style>\s*</helmet>', src, re.S).group(1).strip('\n')
    css = '\n'.join(l for l in style.split('\n') if not l.startswith('body{')) + '\n'
    start = src.index('<div class="ratio-master"')
    end = src.index('</x-dc>')
    fragment = src[start:end].rstrip() + '\n'
    assert '<script' not in fragment and '{{' not in fragment
    return title, css, fragment

PREVIEW = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
body{{margin:0;background:#FFFFFF}}
{css}</style>
</head>
<body>
{fragment}</body>
</html>
'''

def main(src_dir, out_dir):
    n = 0
    for master, boards in MAP.items():
        for board, slug in boards.items():
            p = os.path.join(src_dir, board + '.dc.html')
            if not os.path.exists(p):
                continue
            title, css, fragment = split(open(p, encoding='utf-8').read())
            d = os.path.join(out_dir, master, 'examples', slug)
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, 'fragment.html'), 'w', encoding='utf-8').write(fragment)
            open(os.path.join(d, 'styles.css'), 'w', encoding='utf-8').write(css)
            open(os.path.join(d, 'preview.html'), 'w', encoding='utf-8').write(
                PREVIEW.format(title=title, css=css, fragment=fragment))
            n += 1
    print(f'exported {n} examples')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
