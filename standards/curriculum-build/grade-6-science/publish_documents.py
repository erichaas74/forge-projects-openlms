"""Publish course/project Markdown from science.json; never read creation archives."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
d=json.loads((HERE/'science.json').read_text(encoding='utf-8'))
out=ROOT/'scope-and-sequence';plans=out/'science-projects';plans.mkdir(exist_ok=True)
resources={r['id']:r for r in d['resources']}
national={r['id']:r for r in d['national']}
def cell(x):return str(x).replace('|','/').replace('\n','<br>')
def table(headers,rows):return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(cell(v) for v in r)+' |' for r in rows])
def reslinks(ids):return '; '.join(f"[{resources[i]['title']}]({resources[i]['url']})" for i in ids)
def lessonlink(l):return f"[{l['id']}](science-projects/{next(p['slug'] for p in d['projects'] if l in p['lessons'])}.md#{l['id'].lower()})"
course=[ '# Grade 6 science scope and sequence',f"\nUpdated {d['date']}. {d['status']}",
 '\n## Course overview',
 'Students move from energy-transfer investigations to ecosystem explanations, connected Earth-system models, and a researched environmental recommendation. National standards drive learning and assessment; Tennessee is a separate content check.',
 table(['Item','Plan'],[['Schedule',d['scope']],['Starting input','User-identified recovered Grade 6 project handoff, including the revised S4 report/presentation. Project-creation files are not curriculum inputs.'],['National design basis','NGSS (2013), 17 selected middle-school performance expectations. The rest of the band is explicitly outside this term and requires schoolwide allocation.'],['Tennessee check','October 2022 science standards, implemented 2025–26; selected 2027–28. All 20 Grade 6 content expectations have planned routes; this is not implementation compliance or mastery.'],['Homework','No required homework; materials and essential evidence are planned inside 48 hours.'],['Assessment','Task-specific descriptive criteria; individual evidence distinct from team product quality. No invented grade weights or passing thresholds.'],['Current workbook','[Grade 6 science workbook](<../6th Grade/Grade_6_Science_Curriculum_Standards.xlsx>)'],['Project handoff','[Grade 6 recovered handoff](<../6th Grade/Grade_6_Project_Handoff.md>)']]),
 '\n## Projects at a glance',
 table(['Project','What students do','Final product / experience','Reading / resources','Assessment'],[[f"[{p['id']} {p['title']}](science-projects/{p['slug']}.md)",p['glance'],p['product'],'Short bounded source selections, diagrams and data; named register in each project. Reading remains in class.','Draft/practice feedback, specific individual checks, revised product and fresh application.'] for p in d['projects']]),
 '\n## Progression and weekly sequence',
 'S1 establishes systems, energy transfers and fair comparisons. S2 develops data interpretation, interactions, matter/energy models and evidence-based conservation. S3 applies energy and modeling to circulation, water and forecasts. S4 increases independence in source evaluation, alternative comparison, monitoring and communication. Retain short targeted retrieval where needed; another subject’s teaching is not assumed.',
 table(['Strand','Progression'],[['Practices','Observe/model and plan tests → interpret/argue from ecological evidence → collect and integrate Earth-system observations → research, evaluate and communicate a revised recommendation.'],['Concepts','Energy transfer → ecosystem energy and matter → solar-driven circulation/water and climate → resource use, technology and biodiversity.'],['Crosscutting reasoning','System boundaries and energy → cause/effect and stability → interacting systems across time/space → monitored environmental impacts and tradeoffs.'],['Independence','Guided controls and models → alternate explanations → multi-source model use → individually defended recommendations.']])]
for p in d['projects']:
 course+=['\n### '+p['id']+' — '+p['title'],table(['Course week','Priority learning','Individual / group lesson','Evidence / feedback'],[[4*(p['n']-1)+w,p['lessons'][2*(w-1)]['focus']+' '+p['lessons'][2*(w-1)+1]['focus'],lessonlink(p['lessons'][2*(w-1)])+': '+p['lessons'][2*(w-1)]['title']+'; '+lessonlink(p['lessons'][2*(w-1)+1])+': '+p['lessons'][2*(w-1)+1]['title'],'Save and revise the same project record; private evidence in both lessons. '+p['lessons'][2*(w-1)+1]['check']] for w in range(1,5)])]
course+=['\n## Assessment and practical review',
 table(['Project','Major individual evidence','Team product','Review dimensions'],[
 ['S1','Energy explanation, controlled investigation plan, direct construction/test participation and fresh thermal case.','Tested and revised carrier with design record.','Mechanism, fair comparison, measurements, justified combination/revision, limitations.'],
 ['S2','Resource/interaction interpretation, matter-energy model, empirical case argument and new ecosystem comparison.','Case file and evidence conference.','Data interpretation, causal reasoning, fair evaluation and biodiversity/service connections.'],
 ['S3','Circulation/water/greenhouse models, collected weather log, climate questions and revised fresh forecast.','Connected route briefing.','Causal mechanisms, data/source use, system connections, uncertainty and revision.'],
 ['S4','Resource/per-capita argument, technology comparison, biodiversity reasoning, monitoring and individual defense.','One illustrated report used for a presentation.','Scientific accuracy, fair alternatives, evidence, monitoring, substantive revision and clear communication.']]),
 'Practice receives feedback; final products and fresh applications receive separate descriptive judgments: supported reasoning, independently demonstrated reasoning, or missing/incomplete evidence. These are evidence descriptions, not school grading cutoffs. Recheck with a different case after support. Each lesson specifies what to collect and what quality looks like.',
 table(['Review finding','Concrete planning correction','Still to verify'],[
 ['S3 has seven broad home targets in eight lessons.','Split regional climate, water impacts, greenhouse mechanism and climate attribution across separate lessons. W2-G uses two short data cases; W3-I begins with its recheck.','Trial the W2 pair and confirm reading, model work and individual checks fit.'],
 ['S1 requires physical construction/testing, not only diagrams.','Two initial and two revised trial windows; compare three class designs before combining features.','Kit access, instrument precision, actual reset time and safe supervision.'],
 ['S2 claims must use empirical evidence.','Specify dated terrestrial/aquatic data and a named Tennessee invasive-species case; label hypothetical practice separately.','Select/verify actual source datasets and prepare accessible packets in Step 6.'],
 ['S4 could become an oversized writing task.','One 6–8-slide report doubles as presentation; no simulation, separate long paper or construction product. All learners still receive resource, energy and biodiversity checks.','Time a representative draft/revision and six-team presentation schedule.'],
 ['Existing/developing energy comparison needed a concrete case.','S4-W2-I uses established PV/wind and DOE’s dated perovskite-silicon research case.','Prepare age-appropriate cards and avoid presenting 2024 research claims as current market status.']]),
 '\n## Assumptions and unresolved needs', '\n'.join('- '+x for x in d['assumptions']),
 table(['Affected area','Action','Owner role to confirm','Readiness consequence'],d['open_needs']),
 '\n## National standards and component routes',
 'Primary means central teaching/review with individual evidence; Supporting means purposeful use/reinforcement. A lesson contributes specified components; it does not independently certify the entire performance expectation. Route verification describes the plan. Materials and actual student learning are separate. Official wording and boundaries remain in the source PDF.',
 table(['NGSS','Learning and boundary','Teaching/practice/individual evidence route','Three-dimensional focus'],[[x['id'],x['learning']+' '+x['boundary'],', '.join(x['primary_routes']),x['dci']+'; '+x['sep']+'; '+x['ccc']] for x in d['national']]),
 '\n### Middle-school allocation boundary',
 'This is the proposed Grade 6 term allocation for the four supplied projects. It does not cover all middle-school NGSS. The following expectations require another course/term or Grades 7–8 ownership. Do not certify a complete Grades 6–8 program until the school confirms that allocation and prerequisites. Grade 6 introductions to a concept do not claim the remaining full expectation.',
 table(['Domain','Outside this term; schoolwide owner to confirm'],[[prefix,', '.join(x for x in d['remaining_ngss'] if x.startswith('MS-'+prefix))] for prefix in ['PS','LS','ESS','ETS'] if any(x.startswith('MS-'+prefix) for x in d['remaining_ngss'])]),
 '\n## Tennessee content-compliance check',
 'All 20 expectations are reviewed at the component level below. Covered in plan means explicit teaching and evidence are specified; it is not completed material production, observed mastery or a legal/accreditation determination. Report substantive gaps rather than routine national/state wording differences.',
 table(['TN / recovered ID','Required learning','Home; evidence destinations','Status / next action'],[[x['id']+' / '+x['forge'],x['learning'],x['home']+'; '+', '.join(x['routes']),x['status']+'. '+x['action']] for x in d['tn']]),
 '\n## Source and resource register',
 table(['ID / title','Assigned use','Access / production status'],[[f"{r['id']} — [{r['title']}]({r['url']})",r['selection'],r['status']] for r in d['resources']]),
 '\n## Material-production handoff',
 'Step 6 produces the specified student packets, accessible graphics, empirical data selections, worked/developing examples, fresh assessment cases and scoring guidance. Walk through the busiest pair with actual materials before expanding production. Confirm calendar, class size and physical access. After teaching, use observed timing and student work to revise the same lesson records and regenerate the published views.']
(out/'GRADE_6_SCIENCE_SCOPE_AND_SEQUENCE.md').write_text('\n\n'.join(course)+'\n',encoding='utf-8')
for p in d['projects']:
 rows=[f"# {p['id']} — {p['title']}",f"Updated {d['date']}. {d['status']}",
 '[Course map](../GRADE_6_SCIENCE_SCOPE_AND_SEQUENCE.md) · [Science workbook](<../../6th Grade/Grade_6_Science_Curriculum_Standards.xlsx>)',
 '## Project overview',f"**Question:** {p['question']}",f"**What students do:** {p['glance']}",f"**Final product:** {p['product']}",
 '**Lasting understandings:**\n'+'\n'.join('- '+v for v in p['understandings']),
 '**Schedule:** Four weeks; eight 90-minute blocks, individual then group each week. No required homework. Minimum 30 minutes of actual project work per block. Class-size assumption: 24 students/six groups of four; confirm before teaching.',
 '**Evidence and access:** Keep individual reasoning and support records separate from team product quality. Use the lesson-specific criteria below; no invented weights or cutoffs. Provide readable diagrams, vocabulary previews, chunked text, captions and equivalent oral/text responses while preserving the scientific task. Physical construction/test expectations still require direct accessible participation. Extend with an alternate explanation or constraint, not an extra polished product.',
 '## Texts, resources and materials',
 table(['Resource','Assigned selection','Status'],[[f"[{resources[r]['title']}]({resources[r]['url']})",resources[r]['selection'],resources[r]['status']] for r in p['resources']]),
 '### Materials to build in Step 6','\n'.join('- '+v for v in p['materials']),
 '**Reading plan:** New prose generally stays around 120–250 words per block plus diagrams/data. These are planning estimates, not verified reading levels. Teacher modeling and supported first reading precede independent reasoning. Exact excerpts, counts, accessibility and final keys must be checked in Step 6.',
 '## Eight lesson plans']
 for l in p['lessons']:
  rows += [f"<a id=\"{l['id'].lower()}\"></a>\n### {l['id']} — {l['title']}",f"**Week {l['week']} / {l['mode']} / 90 minutes.**",
   f"**Focus and project connection:** {l['focus']}",f"**Resources:** {reslinks(l['resources'])}. {l['reading']} Teacher-created tasks named below are specifications pending Step 6, not finished handouts.",
   f"**Instruction and modeling:** {l['model']}",
   '**Activity sequence:**\n'+'\n'.join(f'{i+1}. {v}' for i,v in enumerate(l['steps'])),
   f"**Individual work and assessment:** {l['check']}",f"**Quality criteria:** {l['criteria']}",f"**Feedback, support and fresh recheck:** {l['response']}",
   f"**Preparation and next handoff:** {l['prep']}",
   '**Skills taught and checked:**\n'+l['skills'].replace('\n','  \n'),
   f"**Three-dimensional focus:** DCI contributions: {'; '.join(sorted(set(national[c]['dci'] for c in l['primary'])))}. Practice: {l['sep']}. Crosscutting reasoning: {l['ccc']}.",
   f"**National standards:** Primary: {', '.join(l['primary'])}. Supporting: {', '.join(l['support']) or 'None separately claimed'}. {l['verification']}"]
  elapsed=0;times=[]
  for minutes,task in l['clock_segments']:
   times.append([f'{elapsed}–{elapsed+minutes}',task]);elapsed+=minutes
  rows += [table(['Minutes','Sequential activity'],times)]
 rows += ['## National learning-evidence review',table(['Lesson','Primary national targets and evidence','Supporting','Verification'],[[l['id'],', '.join(l['primary'])+'; '+l['check'],', '.join(l['support']) or 'None separately claimed',l['verification']] for l in p['lessons']]),
  '## Recovered assignments and Tennessee check',
  'Preserve the recovered home and recurrence components without treating the historical Forge crosswalk as the national design basis. Detailed Tennessee compliance is maintained once in the course appendix.',
  table(['Assignment','Recovered ID / TN reference','Learning to teach/revisit','Destinations in this project'],[[('Home' if int(x['forge'].split('.')[-1]) in p['home'] else 'Recurrence'),x['forge']+' / '+x['id'],x['learning'],', '.join(l['id'] for l in p['lessons'] if int(x['forge'].split('.')[-1]) in l['tn'])] for x in d['tn'] if int(x['forge'].split('.')[-1]) in p['home']+p['recur']]),
  '## Build and review handoff',
  'The lesson specifications have been reviewed for source-to-task alignment, prerequisite order, explicit individual evidence, separate group quality, safe/buildable procedures and 90-minute planning clocks. These are planning walkthroughs, not classroom trials. The course map records exact unresolved needs and the busiest-pair pacing condition.',
  '**Before teaching:** Produce one worked example on different content, a developing response with actionable feedback, a complete expected-product example and calibrated scoring guidance. Verify source selections, data provenance, accessibility and fresh-assessment independence. Trial the busiest pair with actual materials, then correct the maintained content records before regenerating documents and workbook.']
 (plans/f"{p['slug']}.md").write_text('\n\n'.join(rows)+'\n',encoding='utf-8')
print('Published course map and four complete eight-lesson project documents.')
