"""Builder-only native hyperlink feature fallback; never run as an audit."""
from pathlib import Path
import json,zipfile,xml.etree.ElementTree as E
base=Path(__file__).resolve().parent;root=base.parents[1]
p=root/'6th Grade/Grade_6_History_Curriculum_Standards.xlsx'
links=json.loads((base/'workbook-links.json').read_text())
ns='http://schemas.openxmlformats.org/spreadsheetml/2006/main';rel='http://schemas.openxmlformats.org/officeDocument/2006/relationships';pkg='http://schemas.openxmlformats.org/package/2006/relationships'
E.register_namespace('',ns);E.register_namespace('r',rel)
with zipfile.ZipFile(p) as z:data={n:z.read(n) for n in z.namelist()}
for sn in range(1,6):
 name=f'xl/worksheets/sheet{sn}.xml';rn=f'xl/worksheets/_rels/sheet{sn}.xml.rels';doc=E.fromstring(data[name]);rs=E.fromstring(data[rn]) if rn in data else E.Element('{'+pkg+'}Relationships')
 old=doc.find('{'+ns+'}hyperlinks')
 if old is not None:doc.remove(old)
 h=E.Element('{'+ns+'}hyperlinks');before={'sheetPr','dimension','sheetViews','sheetFormatPr','cols','sheetData','sheetCalcPr','sheetProtection','protectedRanges','scenarios','autoFilter','sortState','dataConsolidate','customSheetViews','mergeCells','phoneticPr','conditionalFormatting','dataValidations'}
 at=max((j+1 for j,x in enumerate(doc) if x.tag.split('}')[-1] in before),default=0);doc.insert(at,h)
 for x in list(rs):
  if x.get('Type')==rel+'/hyperlink':rs.remove(x)
 for i,x in enumerate(v for v in links if v['sheet']==sn):
  a={'ref':x['cell']}
  if 'url' in x:
   rid=f'historyLink{i}';a['{'+rel+'}id']=rid;url=x['url']
   if not url.startswith('http'):
    file,_,anchor=url.partition('#');target=(p.parent/file).resolve();assert target.is_file()
    if anchor:assert f'id="{anchor}"' in target.read_text(encoding='utf-8')
   E.SubElement(rs,'{'+pkg+'}Relationship',{'Id':rid,'Type':rel+'/hyperlink','Target':url,'TargetMode':'External'})
  else:a['location']=x['location']
  E.SubElement(h,'{'+ns+'}hyperlink',a)
 data[name]=E.tostring(doc,encoding='utf-8',xml_declaration=True);data[rn]=E.tostring(rs,encoding='utf-8',xml_declaration=True)
temp=p.with_suffix('.links.tmp')
with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED) as z:
 for name,value in data.items():z.writestr(name,value)
temp.replace(p)
print(f'Added {len(links)} native hyperlinks.')
