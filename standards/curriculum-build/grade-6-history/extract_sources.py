from pathlib import Path
from pypdf import PdfReader
import urllib.request
base=Path(__file__).resolve().parent
root=base.parents[1]
r=PdfReader(root/'reference-standards/TN_Social_Studies_2027-28_K-12.pdf')
hits=list(range(80,98))
print('TN Grade 6 pages:',[i+1 for i in hits])
(base/'tn-extract.txt').write_text('\n'.join(f'PDF PAGE {i+1}\n'+r.pages[i].extract_text() for i in hits),encoding='utf-8')
url='https://www.socialstudies.org/sites/default/files/c3/C3-Framework-for-Social-Studies.pdf'
path=root/'reference-standards/NCSS_C3_Framework_2013.pdf'
if False and not path.exists():
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        path.write_bytes(urllib.request.urlopen(req,timeout=30).read())
    except Exception as e:print('C3 download:',e)
if path.exists():
    c=PdfReader(path)
    (base/'c3-extract.txt').write_text('\n'.join(f'PDF PAGE {i+1}\n'+p.extract_text() for i,p in enumerate(c.pages)),encoding='utf-8')
    print('C3 extracted:',len(c.pages),'pages')
