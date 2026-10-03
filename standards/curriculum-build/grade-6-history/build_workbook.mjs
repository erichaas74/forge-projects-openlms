import fs from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
import {Workbook,SpreadsheetFile,FileBlob} from '@oai/artifact-tool';
const root='C:/Users/erich/Desktop/standards',base=`${root}/curriculum-build/grade-6-history`;
const d=JSON.parse(await fs.readFile(`${base}/history.json`,'utf8')),res=Object.fromEntries(d.resources.map(r=>[r.id,r]));
const wb=Workbook.create(),links=[],widths=[20,42,46,52,55,66,54,64,48];
const headers=['Lesson','Lesson focus and project connection','Texts, resources and reading plan','Instruction and modeling','Lesson activity design','Student work, assessment, feedback and support','Preparation and next-lesson handoff','Skills taught and checked','Standards - national'];
function sheet(name,ws,n=135){const s=wb.worksheets.add(name);s.showGridLines=false;s.getRangeByIndexes(0,0,n,ws.length).format={font:{name:'Arial',size:11,color:'#24354B'},wrapText:true,verticalAlignment:'top'};ws.forEach((w,i)=>s.getRangeByIndexes(0,i,n,1).format.columnWidth=w);return s;}
function section(s,row,title,last){s.getRange(`A${row}:${last}${row}`).merge();s.getRange(`A${row}`).values=[[title]];s.getRange(`A${row}:${last}${row}`).format={font:{name:'Arial',size:12,bold:true,color:'#24354B'},fill:'#E5EBF2',rowHeight:30,verticalAlignment:'center'};}
function table(s,row,heads,rows,ws){const last=String.fromCharCode(64+heads.length);s.getRange(`A${row}:${last}${row}`).values=[heads];s.getRange(`A${row}:${last}${row}`).format={fill:'#304967',font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},rowHeight:55,verticalAlignment:'center'};s.getRange(`A${row+1}:${last}${row+rows.length}`).values=rows;rows.forEach((r,i)=>{const lines=Math.max(...r.map((v,j)=>String(v??'').split('\n').reduce((n,t)=>n+Math.max(1,Math.ceil(t.length/(ws[j]*.8))),0)));const h=Math.max(55,lines*14+18);if(h>409)throw Error(`Too tall: ${s.name}/${row+i+1}`);s.getRange(`A${row+i+1}:${last}${row+i+1}`).format={rowHeight:h,fill:i%2?'#FFFFFF':'#F5F7FA',borders:{bottom:{color:'#CCD5DF',style:'thin'}}};});return row+rows.length+3;}
function link(sn,cell,url,location){links.push({sheet:sn,cell,...(url?{url}:{location})});wb.worksheets.getItemAt(sn-1).getRange(cell).format.font.color='#175E9C';}
const cw=[30,62,68,62,62],overview=sheet('Course overview',cw,130);
section(overview,2,'GRADE 6 HISTORY — Scope and sequence','E');
table(overview,4,['Course','Schedule','National framework','Content','Planning stage'],[['Grade 6 ancient history / social studies',d.scope,'NCSS (2010), public theme framework; C3 (2013), selected Grades 6–8 contributions.','Early humans, Mesopotamia, Egypt/Nubia, Israel, India, China, Greece and Rome.',d.status]],cw);
section(overview,7,'Projects at a glance','E');
table(overview,8,['Project','What students do','Final product / experience','Reading / resources','Assessments'],d.projects.map(p=>[`${p.id} ${p.title}`,p.glance,p.product,'Bounded source cards, maps and short adapted context readings; exact excerpts/access pending.','Individual map/source reasoning and revised explanation; team quality reviewed separately.']),cw);
d.projects.forEach((p,i)=>link(1,`A${9+i}`,null,`'Project ${p.n}'!A2`));
section(overview,15,'Use and completion boundary','E');
table(overview,16,['Area','Current plan','Next stage'],[['Course map','Open the linked full course map for weekly progression, national routes, source records and Tennessee check.','Detailed lesson plans follow in Step 5.'],['Interpretation','National themes organize learning; C3 guides inquiry. Framework contributions do not certify the entire middle-school program.','Schoolwide grade-band ownership and accreditor criteria remain to supply.'],['Planning assumptions','No required homework; 24 learners/six teams; eight 90-minute blocks per project.','Confirm actual class/calendar, source access and practical workload.'],['H3 science connection','One paired historical display; one modern water-timer investigation, supplied shadow observations; historical and measured claims distinct.','Verify sources, procedure and accessible kits.'],['Chronology concern','TN 6.39 groups woodblock printing with Han; dated evidence requires later chronology.','One item Unverified; resolve interpretation before certifying that component.']],cw.slice(0,3));
link(1,'B17','../scope-and-sequence/GRADE_6_HISTORY_SCOPE_AND_SEQUENCE.md');
section(overview,25,'Tennessee content check — separate from national design','E');
let next=table(overview,26,['TN requirement / components','Outline and individual evidence destinations','Status','Action'],d.tn.map(t=>[`${t.id}\n${t.source_text}`,t.routes.join(', '),t.status,t.action]),cw.slice(0,4));
section(overview,next,'Remaining planning and material needs','E');
next=table(overview,next+1,['Area','Action'],d.needs,cw.slice(0,2));
section(overview,next,'Official framework and compliance sources','E');
const sr=next+1;table(overview,sr,['Source','Full title','Assigned use','Access / limits'],d.resources.slice(0,3).map(r=>[r.id,r.title,r.selection,r.status]),cw.slice(0,4));d.resources.slice(0,3).forEach((r,i)=>link(1,`B${sr+1+i}`,r.url));
overview.freezePanes.freezeRows(8);
const expected=[];
for(const p of d.projects){
 const s=sheet(`Project ${p.n}`,widths,100);section(s,2,`${p.id} — ${p.title}`,'I');
 s.getRange('A4:B4').merge();s.getRange('A4').values=[['Step 4 block outlines']];s.getRange('C4:I4').merge();s.getRange('C4').values=[['Detailed procedures, exact source excerpts, examples and assessment prompts remain Step 5 work.']];s.getRange('A4:I4').format.rowHeight=35;
 const rows=p.lessons.map(l=>[`${l.id}\nWeek ${l.week} | ${l.mode}`,`${l.title}\n${l.content}`,`${l.resources.map(id=>res[id].title).join('; ')}\n${l.reading}\nOpen for the linked outline and source details.`,l.model,l.activity,`Collect: ${l.evidence}\nJudge: ${l.criteria}\nFeedback/support: ${l.support}`,l.handoff,l.skills,`C3 Primary: ${l.primary.join(', ')}\nSupporting: ${l.supporting.join(', ')||'None separately assigned'}\nNCSS themes: ${l.themes.map(t=>'T'+t).join(', ')} (local labels).\nConfirmed at outline level; exact source-dependent interpretations conditional. Whole-band coverage and detailed plans are not claimed.`]);
 table(s,6,headers,rows,widths);expected.push(rows);s.getRange('A7:A14').format.font.bold=true;
 p.lessons.forEach((l,i)=>link(p.n+1,`C${7+i}`,l.link));
 section(s,17,'Learning and individual evidence review','I');
 let r=table(s,18,['Lesson','Primary C3 and evidence','Supporting C3','Plan verification / limits'],p.lessons.map(l=>[l.id,`${l.primary.join(', ')}\n${l.evidence}`,l.supporting.join(', ')||'None separately assigned',l.verification]),widths.slice(0,4));
 section(s,r,'Resources and source-selection handoff','I');
 const rr=r+1;r=table(s,rr,['Resource','Full title','Assigned use','Readiness'],[['Project outline',`${p.id} ${p.title}`,p.product,'Step 4 outline exists; detailed Step 5 lessons pending.'],...p.resources.map(id=>{const x=res[id];return [id,x.title,x.selection,x.status];})],widths.slice(0,4));
 link(p.n+1,`B${rr+1}`,`../scope-and-sequence/history-projects/${p.slug}.md`);p.resources.forEach((id,i)=>link(p.n+1,`B${rr+2+i}`,res[id].url));
 section(s,r,'Recovered learning assignments','I');
 table(s,r+1,['Assignment','Local recovered IDs','Use'],[['Home',p.home.map(i=>`SS.${String(i).padStart(2,'0')}`).join(', '),'Historical bundled learning retained; not official national or Tennessee codes.'],['Recurrence',p.recur.map(i=>`SS.${String(i).padStart(2,'0')}`).join(', ')||'Prior-grade foundations','SSP.01–06 recur across the term. Course appendix contains the official TN content check.']],widths.slice(0,3));
 s.freezePanes.freezeRows(6);s.freezePanes.freezeColumns(1);
}
wb.recalculate();
console.log((await wb.inspect({kind:'table',range:'Project 3!A7:B8',tableMaxRows:2,tableMaxCols:2,maxChars:700})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:8},maxChars:500})).ndjson);
const dest=`${root}/6th Grade/Grade_6_History_Curriculum_Standards.xlsx`;
await(await SpreadsheetFile.exportXlsx(wb)).save(dest);
await fs.writeFile(`${base}/workbook-links.json`,JSON.stringify(links,null,2));
// The bundled API lacks native hyperlink authoring; reuse the established XML-only feature fallback.
execFileSync('C:/Users/erich/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',[`${base}/write_native_links.py`],{stdio:'inherit'});
await fs.mkdir(`${base}/previews`,{recursive:true});
for(const [sheetName,range,name] of [['Course overview','A8:C10','overview'],...d.projects.map(p=>[`Project ${p.n}`,'D6:F7',`project-${p.n}`]),['Project 2','D8:F8','oral-history'],['Course overview','A64:D65','chronology']]){const b=await wb.render({sheetName,range,scale:1,format:'png'});await fs.writeFile(`${base}/previews/${name}.png`,new Uint8Array(await b.arrayBuffer()));}
const saved=await SpreadsheetFile.importXlsx(await FileBlob.load(dest));
for(let i=0;i<4;i++){const s=saved.worksheets.getItem(`Project ${i+1}`);if(JSON.stringify(s.getRange('A7:I14').values)!==JSON.stringify(expected[i]))throw Error('Saved lesson mismatch');}
console.log('Saved and reopened five tabs; all 32 nine-column outline rows match.');
