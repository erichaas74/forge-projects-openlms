import fs from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
import {Workbook,SpreadsheetFile,FileBlob} from '@oai/artifact-tool';
const root='C:/Users/erich/Desktop/standards',base=`${root}/curriculum-build/grade-6-science`;
const d=JSON.parse(await fs.readFile(`${base}/science.json`,'utf8'));
const refs=Object.fromEntries(d.resources.map(r=>[r.id,r]));
const wb=Workbook.create(),links=[];
const ink='#24354B',header='#304967',pale='#F5F7FA',line='#CCD5DF';
const widths=[20,38,46,56,62,76,50,60,47];
const headings=['Lesson','Lesson focus and project connection','Texts, resources and reading plan','Instruction and modeling','Lesson activity design','Student work, assessment, feedback and support','Preparation and next-lesson handoff','Skills taught and checked','Standards - national'];
function baseSheet(name,ws,count=130){const s=wb.worksheets.add(name);s.showGridLines=false;s.getRangeByIndexes(0,0,count,ws.length).format={font:{name:'Arial',size:11,color:ink},wrapText:true,verticalAlignment:'top'};ws.forEach((w,i)=>s.getRangeByIndexes(0,i,count,1).format.columnWidth=w);return s;}
function section(s,r,title,last='I'){s.getRange(`A${r}:${last}${r}`).merge();s.getRange(`A${r}`).values=[[title]];s.getRange(`A${r}:${last}${r}`).format={fill:'#E5EBF2',font:{name:'Arial',size:12,bold:true,color:ink},rowHeight:28,verticalAlignment:'center'};}
function fit(s,start,rows,ws,last,min=52){rows.forEach((row,i)=>{const lines=Math.max(...row.map((v,c)=>String(v??'').split('\n').reduce((n,t)=>n+Math.max(1,Math.ceil(t.length/(ws[c]*.82))),0)));const h=Math.max(min,lines*14+18);if(h>409)throw Error(`Row too high ${s.name} ${start+i} ${h}`);s.getRange(`A${start+i}:${last}${start+i}`).format={rowHeight:h,fill:i%2?'#FFFFFF':pale,borders:{bottom:{style:'thin',color:line}}};});}
function table(s,r,heads,rows,ws,last){s.getRange(`A${r}:${last}${r}`).values=[heads];s.getRange(`A${r}:${last}${r}`).format={fill:header,font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:58,verticalAlignment:'center'};if(rows.length){s.getRange(`A${r+1}:${last}${r+rows.length}`).values=rows;fit(s,r+1,rows,ws,last);}return r+rows.length+3;}
function link(sheet,cell,url,location){links.push({sheet,cell,...(url?{url}:{location})});wb.worksheets.getItemAt(sheet-1).getRange(cell).format.font.color='#175E9C';}
const cw=[26,58,68,58,63,56],cover=baseSheet('Course overview',cw,130);
section(cover,2,'GRADE 6 SCIENCE — Four projects, 32 teacher lesson plans','F');
table(cover,5,['Course','Grade / subject','Schedule','Purpose','Outcomes','Standards basis'],[[
 'Project-based science','Grade 6 | Science',d.scope,'Investigate energy, ecosystems and Earth systems; use evidence to explain and recommend improvements.','Investigate/test → analyze ecological evidence → model Earth systems → research and present a change.','NGSS (2013): 17 selected middle-school expectations. Tennessee 2022: separate Grade 6 content check for 2027–28.'
]],cw,'F');
section(cover,8,'Projects at a glance','F');
table(cover,9,['Project','What students will do','Final product / experience','Reading / resources','Assessment'],d.projects.map(p=>[`${p.id} ${p.title}`,p.glance,p.product,'Short source selections, diagrams, data and existing project records; essential reading in class.','Individual reasoning in every block, a revised team product and fresh application; see project criteria.']),cw.slice(0,5),'E');
d.projects.forEach((p,i)=>link(1,`A${10+i}`,null,`'Project ${p.n}'!A2`));
section(cover,16,'Use and planning status','F');
const notes=[['Status',d.status],['Full course map','Open the linked course map for weekly progression, source records, complete NGSS/Tennessee routes and unresolved needs.'],['How to use','Read the eight lesson rows on each project sheet. Linked resource cells open full teacher directions, prompts and clocks. Reference tables remain below the lessons.'],['Time and access','No required homework. Planning assumption: 24 learners/six teams. S1 needs physical kits/supervision; S3 pacing needs trial; actual dates and student starting needs remain to confirm.'],['S4 format','A Better Park is a research report and presentation. One report doubles as the presentation; no simulation, game rounds or additional long paper.'],['Grade-band boundary',`${d.remaining_ngss.length} other middle-school NGSS expectations are outside this term. Schoolwide Grades 6–8 ownership remains to confirm; this is not a full-year or full-band claim.`],['Assessment','Keep individual understanding separate from team quality. Use observable criteria, feedback and fresh rechecks. No invented point weights or passing scores.']];
for(let i=0;i<notes.length;i++){const r=17+i;cover.getRange(`A${r}`).values=[[notes[i][0]]];cover.getRange(`B${r}:F${r}`).merge();cover.getRange(`B${r}`).values=[[notes[i][1]]];cover.getRange(`A${r}:F${r}`).format={rowHeight:54,fill:i%2?'#FFFFFF':pale};cover.getRange(`A${r}`).format.font.bold=true;}
link(1,'B18','../scope-and-sequence/GRADE_6_SCIENCE_SCOPE_AND_SEQUENCE.md');
section(cover,26,'Tennessee content check — separate from the national design basis','F');
let next=table(cover,27,['TN / recovered ID','Required learning','Planned evidence destinations','Status','Next action'],d.tn.map(t=>[`${t.id}\n${t.forge}`,t.learning,`${t.home}: ${t.routes.filter(x=>x.startsWith(t.home)).join(', ')}\nLater recurrence: ${t.routes.filter(x=>!x.startsWith(t.home)).join(', ')||'None assigned'}`,t.status,t.action]),cw.slice(0,5),'E');
section(cover,next,'Source records and remaining readiness needs','F');
next=table(cover,next+1,['Area','Required action','Owner role','Readiness consequence'],d.open_needs,cw.slice(0,4),'D');
const sr=next+1;section(cover,next,'Official standards sources','F');
table(cover,sr,['Source','Full title','Assigned use','Status'],d.resources.filter(r=>['NGSS','TN'].includes(r.id)).map(r=>[r.id,r.title,r.selection,r.status]),cw.slice(0,4),'D');
link(1,`B${sr+1}`,refs.NGSS.url);link(1,`B${sr+2}`,refs.TN.url);
cover.freezePanes.freezeRows(9);
for(const p of d.projects){
 const s=baseSheet(`Project ${p.n}`,widths,160);section(s,2,`${p.id} — ${p.title}`);
 s.getRange('A4:B4').merge();s.getRange('A4').values=[['Project question']];s.getRange('C4:I4').merge();s.getRange('C4').values=[[p.question]];s.getRange('A4:I4').format.rowHeight=36;
 const rows=p.lessons.map(l=>[
  `${l.id}\nWeek ${l.week} | ${l.mode}`,
  `${l.title}\n${l.focus}`,
  l.resources.map(id=>refs[id].title).join('; ')+`\n${l.reading}\nOpen this cell for full lesson and source links.`,
  l.model,
  l.steps.map((v,i)=>`${i+1}. ${v}`).join('\n'),
  `Collect: ${l.check}\nJudge: ${l.criteria}\nFeedback/support: ${l.response}`,
  l.prep,
  l.skills,
  `NGSS primary: ${l.primary.join(', ')}\nSupporting: ${l.support.join(', ')||'None separately claimed'}\nConfirmed in plan for named components. Whole PE route spans lessons. Materials and student learning unverified.`
 ]);
 table(s,6,headings,rows,widths,'I');s.getRange('A7:A14').format.font.bold=true;
 p.lessons.forEach((l,i)=>link(p.n+1,`C${7+i}`,l.link));
 section(s,17,'National learning-evidence review');
 let r=table(s,18,['Lesson','Primary NGSS and individual evidence','Supporting NGSS','Plan verification / limits'],p.lessons.map(l=>[l.id,`${l.primary.join(', ')}\n${l.check}`,l.support.join(', ')||'None separately claimed',l.verification]),widths.slice(0,4),'D');
 section(s,r,'Resources and material production');
 const rr=r+1;
 const resourceRows=[['Full teacher plan',`${p.id} ${p.title}`,p.product,'Teacher plan exists; detailed clocks and preparation are here.','Click title.'],...p.resources.map(id=>[id,refs[id].title,refs[id].selection,refs[id].status,'Click title for full source.']),...p.materials.map((v,i)=>[`Build ${i+1}`,'Teacher-created material specification',v,'Pending Step 6; not a completed student handout.','See full plan.'])];
 r=table(s,rr,['Resource','Full title / location','Assigned use / specification','Readiness','Navigation'],resourceRows,widths.slice(0,5),'E');
 link(p.n+1,`B${rr+1}`,`../scope-and-sequence/science-projects/${p.slug}.md`);
 p.resources.forEach((id,i)=>link(p.n+1,`B${rr+2+i}`,refs[id].url));
 section(s,r,'NGSS components and three-dimensional learning');
 const used=[...new Set(p.lessons.flatMap(l=>l.primary.concat(l.support)))];
 r=table(s,r+1,['NGSS','Required learning / boundary','Project contribution','Practices and core ideas','Crosscutting reasoning'],used.map(id=>{const n=d.national.find(x=>x.id===id);return[id,`${n.learning}\n${n.boundary}`,p.lessons.filter(l=>l.primary.includes(id)||l.support.includes(id)).map(l=>l.id).join(', '),`${n.sep}\n${n.dci}`,n.ccc];}),widths.slice(0,5),'E');
 section(s,r,'Recovered learning assignments — preserve home and recurrence');
 r=table(s,r+1,['Assignment','Recovered / TN ID','Required learning','Project destinations'],d.tn.filter(t=>p.home.concat(p.recur).includes(Number(t.forge.split('.').at(-1)))).map(t=>[p.home.includes(Number(t.forge.split('.').at(-1)))?'Home':'Recurrence',`${t.forge}\n${t.id}`,t.learning,t.routes.filter(x=>x.startsWith(p.id)).join(', ')]),widths.slice(0,4),'D');
 s.freezePanes.freezeRows(6);s.freezePanes.freezeColumns(1);
 if(JSON.stringify(s.getRange('A7:I14').values)!==JSON.stringify(rows))throw Error(`Values differ for ${p.id}`);
}
wb.recalculate();
console.log((await wb.inspect({kind:'sheet',include:'id,name',maxChars:900})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#SPILL!',options:{useRegex:true,maxResults:5},maxChars:500})).ndjson);
const destination=`${root}/6th Grade/Grade_6_Science_Curriculum_Standards.xlsx`;
await(await SpreadsheetFile.exportXlsx(wb)).save(destination);
await fs.writeFile(`${base}/workbook-links.json`,JSON.stringify(links,null,2));
// Native hyperlink authoring is absent in this bundled API (bounded help lookup returned no entries).
// Keep this export-only capability repair in the builder, not in the read-only validator.
execFileSync('C:/Users/erich/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',[`${base}/write_native_links.py`],{stdio:'inherit'});
await fs.mkdir(`${base}/previews`,{recursive:true});
for(const [sheetName,range,name] of [['Course overview','A9:C11','overview'],...d.projects.map(p=>[`Project ${p.n}`,'D6:F7',`project-${p.n}`]),['Project 3','G6:I7','skills-standards'],['Course overview','A27:C30','tn-check']]){
 const preview=await wb.render({sheetName,range,scale:1,format:'png'});
 await fs.writeFile(`${base}/previews/${name}.png`,new Uint8Array(await preview.arrayBuffer()));
}
const saved=await SpreadsheetFile.importXlsx(await FileBlob.load(destination));
for(const p of d.projects){const s=saved.worksheets.getItem(`Project ${p.n}`);if(s.getRange('A7:A14').values.flat().filter(Boolean).length!==8)throw Error('Missing saved lessons');if(JSON.stringify(s.getRange('A6:I6').values[0])!==JSON.stringify(headings))throw Error('Saved headers differ');}
console.log('Saved and reopened 5-sheet science workbook; 32 lesson rows verified.');
