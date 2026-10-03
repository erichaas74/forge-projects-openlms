"""Read-only inspection of source coverage, published views and saved workbook."""
from pathlib import Path
import json,re,zipfile,xml.etree.ElementTree as E
base=Path(__file__).resolve().parent;root=base.parents[1]
d=json.loads((base/'history.json').read_text(encoding='utf-8'))
lessons=[l for p in d['projects'] for l in p['lessons']];ids={l['id'] for l in lessons}
assert len(ids)==len(lessons)==32 and all(len(p['lessons'])==8 for p in d['projects'])
assert sum(l['minutes'] for l in lessons)==2880
assert sorted(v for p in d['projects'] for v in p['home'])==list(range(1,23))
content=[t for t in d['tn'] if t['id'].startswith('6.')]
raw=(base/'tn-extract.txt').read_text(encoding='utf-8')
assert {t['id'] for t in content}==set(re.findall(r'(?m)^(6\.\d{2})\s',raw))
assert len(content)==62 and len(d['tn'])==68
for t in d['tn']:
 assert set(t['routes'])<=ids and t['routes'] and t['source_text']
 if t['id'].startswith('6.'):
  number=int(t['id'].split('.')[1]);assert set(t['routes'])=={l['id'] for l in lessons if number in l['tn']}
assert next(t for t in d['tn'] if t['id']=='6.39')['status']=='Unverified'
for n in d['national']:
 assert set(n['primary_routes'])=={l['id'] for l in lessons if n['id'] in l['primary']}
 assert set(n['support_routes'])=={l['id'] for l in lessons if n['id'] in l['supporting']}
 assert n['primary_routes'] or n['support_routes']
docs=[root/'scope-and-sequence/GRADE_6_HISTORY_SCOPE_AND_SEQUENCE.md']+[root/f"scope-and-sequence/history-projects/{p['slug']}.md" for p in d['projects']]
for path in docs:
 body=path.read_text(encoding='utf-8');assert '\ufffd' not in body
 for m in re.finditer(r'\]\((?:<([^>]+)>|([^\s)]+))\)',body):
  url=m.group(1) or m.group(2)
  if url.startswith('http'):continue
  file,_,anchor=url.partition('#');target=(path.parent/file).resolve();assert target.exists(),url
  if anchor:assert f'id="{anchor}"' in target.read_text(encoding='utf-8')
for p,path in zip(d['projects'],docs[1:]):
 body=path.read_text(encoding='utf-8')
 for l in p['lessons']:
  assert f'id="{l["id"].lower()}"' in body
  assert all(l[k] in body for k in ['content','model','activity','evidence','criteria','support','handoff'])
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
file=root/'6th Grade/Grade_6_History_Curriculum_Standards.xlsx'
links=json.loads((base/'workbook-links.json').read_text());count=0
with zipfile.ZipFile(file) as z:
 strings=[''.join(t.text or '' for t in si.iter('{'+ns['s']+'}t')) for si in E.fromstring(z.read('xl/sharedStrings.xml'))]
 book=E.fromstring(z.read('xl/workbook.xml'));assert [s.get('name') for s in book.find('s:sheets',ns)]==['Course overview','Project 1','Project 2','Project 3','Project 4']
 for sn in range(1,6):
  doc=E.fromstring(z.read(f'xl/worksheets/sheet{sn}.xml'));values={}
  for c in doc.findall('.//s:sheetData/s:row/s:c',ns):
   v=c.find('s:v',ns);text=strings[int(v.text)] if c.get('t')=='s' else v.text if v is not None else ''
   assert c.get('t')!='e';values[c.get('r')]=text
  if sn>1:
   p=d['projects'][sn-2];pane=doc.find('s:sheetViews/s:sheetView/s:pane',ns)
   assert float(pane.get('xSplit'))==1 and float(pane.get('ySplit'))==6
   for row,l in enumerate(p['lessons'],7):
    assert values[f'A{row}'].startswith(l['id']+'\n')
    assert all(values.get(f'{col}{row}') for col in 'ABCDEFGHI')
    assert values[f'D{row}']==l['model'] and values[f'E{row}']==l['activity']
    assert values[f'G{row}']==l['handoff'] and values[f'H{row}']==l['skills']
    assert l['evidence'] in values[f'F{row}'] and l['criteria'] in values[f'F{row}']
    assert 'C3 Primary' in values[f'I{row}'] and 'TN ' not in values[f'I{row}']
  rs=E.fromstring(z.read(f'xl/worksheets/_rels/sheet{sn}.xml.rels'));targets={x.get('Id'):x.get('Target') for x in rs}
  expected={x['cell']:x for x in links if x['sheet']==sn};actual=doc.findall('s:hyperlinks/s:hyperlink',ns);assert len(actual)==len(expected)
  for h in actual:
   e=expected[h.get('ref')]
   if 'location' in e:assert h.get('location')==e['location']
   else:
    url=targets[h.get('{'+ns['r']+'}id')];assert url==e['url']
    if not url.startswith('http'):
     target,_,anchor=url.partition('#');path=(file.parent/target).resolve();assert path.is_file()
     if anchor:assert f'id="{anchor}"' in path.read_text(encoding='utf-8')
  count+=len(actual)
assert count==55
print('PASS: 32 unique 90-minute outlines, 4 projects, 22 C3 contributions, all 10 theme routes, 62 TN content and 6 SSP checks; one flagged chronology item preserved. Five saved workbook tabs, all lesson values, pane settings, 55 hyperlinks and document anchors inspected. No files modified.')
