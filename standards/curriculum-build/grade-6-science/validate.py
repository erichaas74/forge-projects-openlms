"""Read-only reconciliation of maintained content, published plans and saved workbook."""
from pathlib import Path
import json, re, zipfile, xml.etree.ElementTree as E
from urllib.parse import unquote

base = Path(__file__).resolve().parent
root = base.parents[1]
d = json.loads((base / 'science.json').read_text(encoding='utf-8'))
ns = {'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
      'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
workbook = root / '6th Grade/Grade_6_Science_Curriculum_Standards.xlsx'
lessons = [l for p in d['projects'] for l in p['lessons']]
by_id = {l['id']:l for l in lessons}
assert len(lessons) == len(by_id) == 32
assert all(len(p['lessons']) == 8 for p in d['projects'])
assert sum(sum(m for m,_ in l['clock_segments']) for l in lessons) == 2880
assert all(sum(m for m,_ in l['clock_segments']) == 90 for l in lessons)
assert sorted(n for p in d['projects'] for n in p['home']) == list(range(1,21))
assert len(d['national']) == 17 and len(d['tn']) == 20
tn_source = (base/'tn-source-extract.txt').read_text(encoding='utf-8')
tn_grade=tn_source.split('SIXTH GRADE: ACADEMIC STANDARDS',1)[1].split('PDF PAGE 53',1)[0]
source_tn=set()
prefix=None
for line in tn_grade.splitlines():
    heading=re.match(r'(6\.(?:PS|LS|ESS|ETS)\d):',line)
    if heading:prefix=heading.group(1)
    item=re.match(r'(\d+)\)',line)
    if item:source_tn.add(prefix+'.'+item.group(1))
assert source_tn == {t['id'] for t in d['tn']}
ngss_source = (base/'ngss-source-extract.txt').read_text(encoding='utf-8')
assert set(re.findall(r'\bMS-(?:PS|LS|ESS|ETS)\d-\d+\b',ngss_source)) == {n['id'] for n in d['national']} | set(d['remaining_ngss'])
for n in d['national']:
    assert set(n['primary_routes']) == {l['id'] for l in lessons if n['id'] in l['primary']}
    assert n['primary_routes']
for i,t in enumerate(d['tn'],1):
    assert set(t['routes']) == {l['id'] for l in lessons if i in l['tn']}
    assert any(v.startswith(t['home']) for v in t['routes'])
for p in d['projects']:
    for n in p['home']+p['recur']:
        assert any(n in l['tn'] for l in p['lessons']), (p['id'],n)

course = root/'scope-and-sequence/GRADE_6_SCIENCE_SCOPE_AND_SEQUENCE.md'
docs = [course]+[root/f"scope-and-sequence/science-projects/{p['slug']}.md" for p in d['projects']]
for path in docs:
    body=path.read_text(encoding='utf-8')
    for match in re.finditer(r'\]\((?:<([^>]+)>|([^\s)]+))\)',body):
        url=match.group(1) or match.group(2)
        if url.startswith(('http:','https:')):continue
        target,_,anchor=unquote(url).partition('#')
        resolved=(path.parent/target).resolve()
        assert resolved.exists(),(path,url)
        if anchor:assert f'id="{anchor}"' in resolved.read_text(encoding='utf-8'),url
for p,path in zip(d['projects'],docs[1:]):
    body=path.read_text(encoding='utf-8')
    for l in p['lessons']:
        assert f'id="{l["id"].lower()}"' in body
        for field in ['focus','model','check','criteria','response','prep']:
            assert l[field] in body,(l['id'],field)
        assert all(step in body for step in l['steps'])

links=json.loads((base/'workbook-links.json').read_text())
with zipfile.ZipFile(workbook) as z:
    shared=E.fromstring(z.read('xl/sharedStrings.xml'))
    strings=[''.join(t.text or '' for t in si.iter('{'+ns['s']+'}t')) for si in shared]
    book=E.fromstring(z.read('xl/workbook.xml'))
    assert [s.get('name') for s in book.find('s:sheets',ns)] == ['Course overview','Project 1','Project 2','Project 3','Project 4']
    total_links=0
    for sn in range(1,6):
        sheet=E.fromstring(z.read(f'xl/worksheets/sheet{sn}.xml'))
        vals={}
        for c in sheet.findall('.//s:sheetData/s:row/s:c',ns):
            v=c.find('s:v',ns)
            if c.get('t')=='s':value=strings[int(v.text)]
            elif c.get('t')=='inlineStr':value=''.join(c.itertext())
            else:value=v.text if v is not None else ''
            assert c.get('t')!='e',(sn,c.get('r'),value)
            vals[c.get('r')]=value
        if sn>1:
            p=d['projects'][sn-2]
            pane=sheet.find('s:sheetViews/s:sheetView/s:pane',ns)
            assert float(pane.get('xSplit'))==1 and float(pane.get('ySplit'))==6
            for row,l in enumerate(p['lessons'],7):
                assert vals[f'A{row}'].startswith(l['id']+'\n')
                assert vals[f'D{row}']==l['model']
                assert vals[f'E{row}']=='\n'.join(f'{i}. {s}' for i,s in enumerate(l['steps'],1))
                assert vals[f'F{row}']==f"Collect: {l['check']}\nJudge: {l['criteria']}\nFeedback/support: {l['response']}"
                assert vals[f'G{row}']==l['prep'] and vals[f'H{row}']==l['skills']
                assert all(vals.get(f'{c}{row}') for c in 'ABCDEFGHI')
        rels=E.fromstring(z.read(f'xl/worksheets/_rels/sheet{sn}.xml.rels'))
        targets={x.get('Id'):x.get('Target') for x in rels}
        actual=sheet.findall('s:hyperlinks/s:hyperlink',ns)
        expected=[v for v in links if v['sheet']==sn]
        assert len(actual)==len(expected)
        expected={v['cell']:v for v in expected}
        for h in actual:
            spec=expected[h.get('ref')]
            if 'location' in spec:assert h.get('location')==spec['location']
            else:
                url=targets[h.get('{'+ns['r']+'}id')]
                assert url==spec['url']
                if not url.startswith('http'):
                    path,_,anchor=unquote(url).partition('#')
                    target=(workbook.parent/path).resolve()
                    assert target.exists()
                    if anchor:assert f'id="{anchor}"' in target.read_text(encoding='utf-8')
        total_links+=len(actual)
assert total_links==55
print('PASS: 32 unique lessons / 2,880 minutes / 4 projects; 17 NGSS and 20 Tennessee routes reconciled with official source extracts; all lesson documents and local anchors match; five saved workbook tabs, lesson values, freeze panes and 55 hyperlinks verified. Read-only audit; no deliverables changed.')
