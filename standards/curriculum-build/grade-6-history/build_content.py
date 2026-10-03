"""Maintained Steps 1–5 history planning build. No project-creation archive inputs."""
from pathlib import Path
import re,json
base=Path(__file__).resolve().parent
STATUS='Steps 1–5 planning build: four projects and 32 detailed teacher lesson plans. Step 6 student packets, source-dependent checks and classroom pacing remain. Tennessee 6.39 chronology is Unverified; SSP.01 oral modality is Conditional.'
themes=['Culture','Time, Continuity, and Change','People, Places, and Environments','Individual Development and Identity','Individuals, Groups, and Institutions','Power, Authority, and Governance','Production, Distribution, and Consumption','Science, Technology, and Society','Global Connections','Civic Ideals and Practices']
# Interpretive summaries, not verbatim official wording. Theme IDs are local labels.
specs={
'D1.5.6-8':'Select sources suited to the inquiry.',
'D2.His.1.6-8':'Connect events to historical context.',
'D2.His.2.6-8':'Distinguish continuity and change.',
'D2.His.3.6-8':'Investigate historical significance.',
'D2.His.4.6-8':'Explain influences on past perspectives.',
'D2.His.6.6-8':'Explain perspective effects on source information.',
'D2.His.9.6-8':'Classify evidence behind a historical interpretation.',
'D2.His.10.6-8':'Detect limits in the historical record.',
'D2.His.11.6-8':'Use corroboration to infer source purpose and audience.',
'D2.His.14.6-8':'Explain multiple causes and effects.',
'D2.His.15.6-8':'Weigh the influence of different causes.',
'D2.His.16.6-8':'Organize evidence into historical argument.',
'D2.Geo.1.6-8':'Map cultural and environmental patterns.',
'D2.Geo.4.6-8':'Explain cultural and economic effects on environments and daily life.',
'D2.Civ.6.6-8':'Explain how organizations shape lives.',
'D3.1.6-8':'Gather and corroborate relevant sources.',
'D3.2.6-8':'Judge credibility for the intended use.',
'D3.3.6-8':'Support claims while identifying evidence limits.',
'D4.1.6-8':'Argue from multiple sources with limitations.',
'D4.2.6-8':'Explain using reasoning, sequence and relevant detail.',
'D4.4.6-8':'Critique argument credibility.',
'D4.5.6-8':'Critique explanation structure.'}
def c(s):
    # Short authoring notation; all output contains complete, verified framework IDs.
    return [('D2.'+v+'.6-8' if v.startswith(('His.','Geo.','Civ.')) else v+'.6-8') for v in s.split()]
resources=[
dict(id='NCSS',title='NCSS National Curriculum Standards for Social Studies (2010): public executive summary and themes',url='https://www.socialstudies.org/standards/national-curriculum-standards-social-studies-executive-summary',selection='Ten-theme organizing framework; public middle-grades discussion. Full proprietary middle-grades performance expectations are not reproduced or individually certified.',status='Official public framework reviewed 2026-10-03.'),
dict(id='C3',title='NCSS C3 Framework (2013), Grades 6–8 inquiry indicators',url='https://www.socialstudies.org/sites/default/files/c3/C3-Framework-for-Social-Studies.pdf',selection='Questions, maps, institutions, historical context/perspective/evidence/causation, source evaluation and communication. Selected indicators only.',status='Official PDF reviewed online 2026-10-03; selected grade-band contributions, not a complete C3 band claim.'),
dict(id='TN',title='Tennessee Social Studies Standards: implementation 2027–28',url='https://www.tn.gov/education/districts/academic-standards/social-studies-standards.html',selection='Local official PDF pages 81–98: SSP.01–06 and content 6.01–6.62.',status='2024 adoption, 2027–28 implementation. Separate content check; 6.39 chronology unresolved.'),
dict(id='HISTORY',title='OpenStax — World History Volume 1, to 1500',url='https://openstax.org/books/world-history-volume-1/pages/1-introduction',selection='Teacher background: early humans, river-valley societies, ancient Israel/India/China/Greece/Rome. Select topic sections and primary-source boxes; prepare short attributed student adaptations.',status='Teacher reference located; exact excerpts, dates, image rights, reading fit and source packets remain Step 5/6 work. Do not assign whole college chapters.'),
dict(id='NEAR',title='The Met — Art of the Ancient Near East: educator resource',url='https://www.metmuseum.org/-/media/files/learn/for-educators/publications-for-educators/art-of-the-ancient-near-east.pdf',selection='Select one Mesopotamian artifact with museum provenance and one writing/architecture example. Supplement with a verified Hammurabi translation.',status='Resource located; object selection, lawful accessible images and translation excerpt pending.'),
dict(id='EGYPT',title='The Met — Egyptian Art',url='https://www.metmuseum.org/departments/egyptian-art',selection='Select an Egyptian artifact/monument and a Nubian-perspective source, with dates and provenance.',status='Department collection entry point; exact paired objects and text selections pending.'),
dict(id='HAN',title='The Met — Han Dynasty (206 BCE–220 CE)',url='https://www.metmuseum.org/essays/han-dynasty-206-b-c-220-a-d',selection='Statecraft, Confucian institutions, exchange and paragraph on timekeeping/astronomical instruments. Source is a modern museum interpretation.',status='Department of Asian Art, October 2000. Teacher source inspected; adapted selection and an exact primary artifact record pending.'),
dict(id='CLOCK',title='American School of Classical Studies at Athens — An Athenian Clepsydra',url='https://www.ascsa.edu.gr/uploads/media/hesperia/146678.pdf',selection='Archaeological scholarly account of Athenian court timing; isolate one object image/description and its reconstruction limits.',status='Search-indexed research source; full PDF retrieval failed. Access and precise page selection conditional before Step 5.'),
dict(id='SKY',title='Science Museum — Ancient Greek Computing',url='https://blog.sciencemuseum.org.uk/ancient-greek-computing/',selection='Antikythera mechanism as a dated Hellenistic astronomical-prediction case. Distinguish modern reconstruction from surviving evidence; not a navigation-device claim.',status='Teacher source reviewed; short caption/diagram selection pending. No complex reconstruction required.'),
dict(id='PRINT',title='British Library / International Dunhuang Programme — Diamond Sutra display guide',url='https://idp.bl.uk/wp-content/uploads/2025/01/BL.SR_.Large_.Print_.Guide_.V3.pdf',selection='Dated printed Diamond Sutra as a later timeline comparison, outside Han. A later surviving print is not by itself proof of the first invention date.',status='Official source located; use for chronology scrutiny, not a claim that every Chinese innovation belongs to Han.'),
dict(id='ROME',title='British Museum — Greece and Rome',url='https://www.britishmuseum.org/our-work/departments/greece-and-rome',selection='Select Roman infrastructure/inscription/coin evidence with creator/date/place; pair with a translated legal or historical excerpt.',status='Teacher collection entry point; exact objects, translations and contrasting account selections pending.')]
projects=[]
def project(n,title,slug,q,glance,product,home,recur,rs,understandings):
    p=dict(n=n,id=f'H{n}',title=title,slug=slug,question=q,glance=glance,product=product,home=home,recur=recur,resources=rs.split(),understandings=understandings,lessons=[]);projects.append(p);return p
def lesson(p,title,content,tn,th,primary,rs,model,activity,evidence,criteria,support,handoff,prereq):
    i=len(p['lessons']);lid=f"{p['id']}-W{i//2+1}-{'I' if i%2==0 else 'G'}"
    p['lessons'].append(dict(id=lid,week=i//2+1,mode='Individual' if i%2==0 else 'Group',title=title,content=content,tn=tn,themes=th,primary=c(primary),supporting=c('D3.1') if 'D3.1' not in primary.split() else [],resources=rs.split(),model=model,activity=activity,evidence=evidence,criteria=criteria,support=support,handoff=handoff,prereq=prereq,minutes=90,
    reading='Planning limit: 150–250 words of new adapted prose plus up to two images/maps/source cards. Exact excerpts, provenance and access pending; essential reading stays in class.',
    verification='Confirmed in the Step 4 outline for the specified contribution; source-dependent interpretations conditional until exact selections are verified. Detailed procedures and fresh assessment prompts remain Step 5.'))

p=project(1,'First Cities Evidence Dig','H1_FIRST_CITIES_EVIDENCE_DIG','How can evidence explain the move from mobile communities to early cities?',
'Reconstruct early settlement and a Mesopotamian city using artifacts, maps and competing explanations.',
'One evidence reconstruction board with a map/timeline, labeled artifacts, causal links and a revised explanation; each student supplies a private source-based argument.',list(range(1,11)),[],'HISTORY NEAR',[
'Historical explanations depend on evidence and its limits.','Agriculture changed work, settlement and exchange unevenly.','Geography, institutions and technology interact in city development.'])
lesson(p,'Read time and question the evidence','BCE/CE, BC/AD, circa, decades/centuries; primary/secondary sources and archaeological inference.',[1],[2], 'His.1 His.9 D1.5','HISTORY NEAR',
'Contrast an artifact with a modern caption; place three dated examples on a timeline and distinguish observation from inference.',
'Annotate a timeline; classify sources; pose the settlement inquiry and choose two sources that could answer a supporting question.',
'Individual dated sequence, source classification and justified source choice.',
'Correct chronology and labels; source choice matches question; inference exceeds neither object nor caption.',
'If oldest BCE is reversed, model an ordered number line and recheck new dates; offer a labeled chronology strip.',
'Prepare timeline cards and provenance labels; save the inquiry/source log for all projects.','Grade 5 maps, sequence and evidence language.')
lesson(p,'Compare mobile and settled lives','Paleolithic tools, fire, hunting, shelter and mobility; Neolithic agriculture, domestication, surplus, barter, clothing/shelter and specialized work.',[2,3],[2,7,8], 'His.2 His.14','HISTORY',
'Model a multi-cause chain on a different settlement; explain that mobile lifeways did not simply disappear everywhere.',
'Compare two evidence sets; construct a settlement-change chain; teams propose and challenge two explanations.',
'Private continuity/change comparison and one evidence-supported cause/effect chain.',
'Distinguishes material evidence from assumptions; includes both continuity and change without ranking people.',
'If surplus is automatic, add a failed-harvest case and revise; use pictured process cards with a fresh explanation.',
'Create bounded site cases and preserve individual chains on the reconstruction board.','H1-W1-I source and chronology routines.')
lesson(p,'Locate the Fertile Crescent','Tigris, Euphrates, Zagros, Mediterranean and Persian Gulf; rainfall/floods, water access, irrigation and agricultural risk.',[5,6],[3], 'Geo.1 Geo.4','HISTORY NEAR',
'Model map selection by purpose/date; explain how irrigation modifies the environment rather than saying rivers guarantee prosperity.',
'Label a bounded regional map; compare two possible settlement locations; annotate benefits, risks and human adaptations.',
'Individual map and location explanation using two features and an adaptation.',
'Features are positioned meaningfully; cultural/economic decisions and environmental effects are connected.',
'If modern borders become ancient boundaries, compare dated maps then recheck; provide readable relief and text equivalents.',
'Prepare relief/water maps and carry location decisions into the city model.','Timeline and cause/effect reasoning.')
lesson(p,'Explain how an early city worked','Food supply, technology, culture, writing, religion, government and social structure; irrigation/metallurgy/animals/wheel/sail/plow; surplus, trade, transport and city-states.',[4,7,8],[5,7,8], 'His.14 Civ.6','HISTORY NEAR',
'Model surplus-to-specialization with alternatives; show institutions allocating water/work without a modern market assumption.',
'Build a city systems diagram; match each civilization characteristic to evidence; analyze agricultural tools and a trade route.',
'Each student explains an institution and two links among agriculture, labor and exchange.',
'All seven characteristics appear with evidence; mechanisms explain tool and trade effects; no single-cause story.',
'If diagram is only pictures, add labeled causal verbs and recheck a new link; offer a systems organizer.',
'Prepare verified agriculture/technology cards; keep the same city board for law and belief sources.','Map, adaptation and settlement chains.')
lesson(p,'Read authority, hierarchy and beliefs','City-state versus monarchy/empire; Mesopotamian social hierarchy; polytheism and nature; writing, tablets, ziggurats and Gilgamesh.',[9,10,11,12],[1,4,5,6], 'Civ.6 His.4 His.6','HISTORY NEAR',
'Compare a ruler inscription with an archaeological account; teach how elite sources preserve some voices and omit others.',
'Annotate a social-role/source chart; distinguish belief from historical claim; connect cuneiform and architecture to institutions.',
'Individual explanation of power/social position and one source-perspective limitation.',
'Defines government forms; explains daily-life effects and belief context; treats an epic as literature/evidence rather than a literal event log.',
'If a ruler speaks for everyone, identify absent groups and recheck a different source; use role/source labels.',
'Select translations and exact object records; distinguish first-known empire claims and Gilgamesh traditions from universal absolutes.','Institutions and artifact inference.')
lesson(p,'Compare law and lived experience','Hammurabi, written law, status-dependent justice; corroboration and source purpose.',[13,10],[6,10], 'His.11 D3.2 D3.3','HISTORY NEAR',
'Model inferring audience/purpose by comparing a law excerpt with a second account; written law does not prove equal enforcement.',
'Compare two adapted laws and contextual evidence; explain affected groups; revise an unsupported equality claim.',
'Private corroborated source-purpose inference and a claim with one limitation.',
'Cites both sources; explains relevance and status differences; avoids reading modern equality into the text.',
'If paraphrase becomes endorsement, separate description from evaluation and recheck; offer side-by-side source chunks.',
'Prepare verified translator/date/section labels and carry law evidence into reconstruction.','Hierarchy and source perspective.')
lesson(p,'Defend the city reconstruction','Synthesize chronology, geography, technology, institutions and competing settlement explanations.',list(range(1,14)),[2,3,5], 'His.16 D4.1 D4.4','HISTORY NEAR',
'Model a supported claim with an alternative explanation and an evidence limit on a different site.',
'Finish existing board annotations; independently argue which explanation fits; use peer credibility feedback to revise.',
'Individual argument from at least two source types plus one substantive revision.',
'Evidence supports mechanisms and chronology; alternative is fairly considered; uncertainty remains visible.',
'If claim repeats a caption, ask how evidence supports it; recheck an unfamiliar artifact; allow oral reasoning with citations.',
'Prepare short fresh artifact check and archive each student’s source choices.','All H1 source and city-system work.')
lesson(p,'Review competing reconstructions','Evidence conference, new artifact interpretation and unresolved inquiry.',list(range(1,14)),[2,10], 'D4.2 D4.5 His.10','HISTORY NEAR',
'Demonstrate critiquing sequence and causal links without judging decorative design.',
'Teams give concise reconstruction walkthroughs; each learner responds to a new artifact/caption; revise one causal link.',
'Private new-source inference, limitation and teacher-recorded explanation; team board reviewed separately.',
'New evidence is contextualized; explanation order is coherent; revision changes reasoning.',
'If new object is dated incorrectly, use timeline/source clinic and a second card; carry missing evidence forward.',
'Save map/source log and individual unresolved needs for H2; prepare source packets before detailed lessons.','Source credibility, causal argument and timeline.')

p=project(2,'River Kingdoms Atlas','H2_RIVER_KINGDOMS_ATLAS','How did geography, institutions and beliefs shape different societies?',
'Build a small linked exhibit for Egypt/Nubia, ancient Israel and India, using common comparison questions and distinct contexts.',
'One shared atlas exhibit with three concise society panels and a common timeline/map. Every student completes evidence for all three; no specialist-only coverage.',list(range(11,16)),list(range(1,11)),'HISTORY EGYPT',[
'Similar geographic challenges can lead to different institutions.','Beliefs and social position shape perspectives and daily life.','Comparison requires distinct dates, places and evidence for each society.'])
lesson(p,'Explain Egypt along the Nile','Egypt map: Nile/delta, Upper/Lower Egypt, Nubia, Sahara, Red/Mediterranean seas; irrigation/calendar; occupations, enslaved people, pharaoh; polytheism, afterlife/mummification.',[14,15,16,17],[1,3,5], 'Geo.1 Geo.4 Civ.6','HISTORY EGYPT',
'Model Nile direction versus Upper/Lower labels; connect calendar/irrigation decisions and social work to environmental conditions.',
'Annotate map and seasonal sequence; compare occupation roles; add a respectful beliefs/context caption.',
'Individual map plus one agriculture/institution explanation and belief-context annotation.',
'Correct relative locations; causal links use evidence; afterlife belief is attributed to historical practitioners.',
'If Upper means north, follow upstream and recheck a blank map; chunk text and read captions together.',
'Prepare two brief context cards and exact map/monument records; carry Egypt annotations to W1-G.','H1 rivers, institutions and source labels.')
lesson(p,'Connect Egypt and Nubia','Hatshepsut policies/trade, Ramses military growth, Tutankhamun tomb discovery and revised knowledge; hieroglyphics/papyrus/Giza; Nubian trade/conflict and agency.',[18,19,20],[2,8,9], 'His.3 His.6 His.10','HISTORY EGYPT',
'Model how a later discovery changes an interpretation; give Nubian actors their own context rather than defining them only through Egypt.',
'Build a compact evidence panel; place rulers/discovery on separate timeline lanes; compare trade/conflict accounts and artifact limits.',
'Each student explains one figure’s significance, an achievement and how a discovery or perspective changes knowledge.',
'Distinguishes ancient events from modern excavation; includes Nubian agency and sourced achievement effects.',
'If tomb wealth proves all lives were alike, compare nonelite evidence and recheck; use a discovery/event timeline key.',
'Keep panel to existing notes and two captions; select a Nubian-perspective source before Step 5.','Egypt map/social structure and H1 evidence limits.')
lesson(p,'Trace ancient Israel and its traditions','Dead/Red/Mediterranean seas, Jordan, Jerusalem, Sinai; Ur/Canaan/Egypt movements; Judaism, Abraham/Moses, Tanakh/Torah, monotheism, Ten Commandments, responsibility.',[21,22,23],[1,2,3], 'Geo.1 His.4 D3.2','HISTORY',
'Distinguish traditions recorded in sacred texts, archaeological evidence and modern historical interpretation; teach religions academically with a common template.',
'Map attributed movement accounts; annotate people/texts/beliefs/context; compare what different source types can establish.',
'Individual route/source explanation and a respectful Judaism profile.',
'Uses attribution where historical evidence is contested; accurate text/belief terms; no devotional activity required.',
'If every account is called verified eyewitness history, classify source type and recheck; provide pronunciation and neutral profiles.',
'Select an accessible religious-studies/history source and exact attributed excerpts.','Chronology, geography and source-purpose reasoning.')
lesson(p,'Explain kingdoms, exile and return','Saul, David/Jerusalem, Solomon/temple; kingdom division, Assyrian/Babylonian conquest/exiles, Persian return; cross-society comparison.',[24,25,14,20],[2,5,9], 'His.1 His.14 D4.2','HISTORY EGYPT',
'Model a dated movement explanation separating political cause from a tradition’s meaning; avoid modern-border substitution.',
'Construct kingdom/conquest sequence; compare one Egypt/Nubia and Israel movement; add two evidence-based exhibit captions.',
'Private cause/effect sequence and comparison with dated evidence from both contexts.',
'Actors/sequence are coherent; multiple political/geographic factors appear; similarity does not erase difference.',
'If all exile periods merge, separate timeline bands and recheck events; use a movement legend.',
'Limit captions to 60–80 words each; retain Israel panel and shared chronology.','Israel routes/traditions and Egypt/Nubia evidence.')
lesson(p,'Investigate Indus cities','India subcontinent, Himalayas, Indus/Ganges, Indian Ocean, monsoons; Harappa/Mohenjo-Daro, bricks, grid roads and sanitation.',[26,27],[3,7,8], 'Geo.1 Geo.4 His.9','HISTORY',
'Model a city-plan inference and its limits; compare economic/environmental decisions without claiming undeciphered writing supplies a known government.',
'Annotate map/city plan; identify water/sanitation evidence; compare a useful Mesopotamian pattern with a distinct Indus case.',
'Individual plan-based inference and explanation of two documented achievements.',
'Separates observation from unknown institutions; explains infrastructure rather than praising advanced design alone.',
'If a regular grid proves democracy, show inference limits and recheck a different plan; use magnified plans.',
'Prepare dated archaeological plan/source card and retain inference notes for India panel.','H1 city systems and H2 maps.')
lesson(p,'Explain traditions and social change in India','Indo-Aryan migrations/language/religious change; caste/social hierarchy; Hinduism: Vedas, dharma/karma/reincarnation/moksha; Buddhism: Siddhartha, Tripitaka, Four Noble Truths/Eightfold Path/Nirvana; medicine, yoga and numerals with correct dates.',[28,29,30,31,32],[1,4,5,8], 'His.4 Civ.6 D3.3','HISTORY',
'Use matched neutral religion profiles; distinguish beliefs, social practices and later developments. Explain changing scholarship on migration rather than a single unqualified invasion story.',
'Compare the two profiles and dated evidence cards; explain hierarchy’s daily-life effects; attach a short achievement timeline.',
'Private comparison including people/texts/beliefs, a social-position explanation and correctly dated achievement.',
'Keeps traditions distinct and attributed; does not portray caste or either religion as uniform across all people/time.',
'If unfamiliar terms replace explanation, model one in context and recheck another; provide a glossary and reduced-copy organizer.',
'Busiest H2 block: two profiles totaling about 250 words plus a diagram. Verify comprehension/time; move caption polish to W4-I, never required reading to homework.','Institution/perspective reasoning and Indus chronology.')
lesson(p,'Compare all three society panels','Common geographic, institutional and belief questions; Egypt/Nubia, Israel and India each required.',list(range(14,33)),[1,3,5,9], 'His.16 D4.1 D4.4','HISTORY EGYPT',
'Model comparison from two explicit pieces of evidence, with a counterexample and source limitation.',
'Use a targeted retrieval clinic; finish three short panels from saved notes; individually compare two societies and respond to a third-society question.',
'Independent comparison plus all-three-society retrieval record and one revised claim.',
'No society omitted; claims use common dimensions and context-specific evidence; revision improves reasoning.',
'If team specialization hides missing learning, administer short private checks and targeted source review; extend by challenging a comparison.',
'Keep one atlas, no separate long essays; prepare fresh map/source mini-checks for W4-G.','All H2 notes, profiles, maps and chronology.')
lesson(p,'Defend the linked atlas exhibit','Walkthrough, individual fresh map/source application and feedback.',list(range(14,33)),[2,10], 'D4.2 D4.5 D3.2','HISTORY EGYPT',
'Model audience questions about evidence and coherent explanation, not costume or visual polish.',
'Six short team walkthroughs; every learner explains a source; collect a fresh map/context response and revise one caption.',
'Teacher-observed explanation and private fresh source/map interpretation; shared atlas assessed separately.',
'Accurate context/source use; all required societies remain represented; feedback changes a claim or connection.',
'If a comparison overgeneralizes belief, require attribution and a new example; record unresolved society/component for H3 opening.',
'Archive individual checks separately; carry comparison and scholarly uncertainty routines into H3.','Evidence-based comparison and source limitations.')

p=project(3,'Ancient Science: Inventions, Sky and Navigation','H3_ANCIENT_SCIENCE','How did China and Greece use observations and inventions, and how can we compare their methods?',
'Study China and Greece in context, compare historical timekeeping evidence, and conduct one small investigation of a measurement principle.',
'One paired China–Greece display with map/timeline, historical source panels, comparison table and investigation data; a short demonstration and individual explanation. Shadow data are supplied; the one practical investigation tests a water timer.',list(range(16,20)),[1,2,3,4,5,6,8,10,12,13,14,15],'HISTORY HAN CLOCK SKY PRINT',[
'Scientific methods develop within institutions, needs and traditions.','A modern model tests a principle without reproducing every ancient instrument.','Chronology and corroboration distinguish exchange from coincidental similarity.'])
lesson(p,'Locate China and explain early authority','Gobi, Himalayas, Pacific, Tibet plateau, Yangtze/Yellow rivers; Xia tradition and Shang evidence; geographic governing constraints; Zhou/Mandate of Heaven and Legalism.',[33,34,35,36],[2,3,6], 'Geo.1 His.1 Civ.6','HISTORY',
'Model a geographic governance explanation; distinguish traditional accounts of Xia from excavated Shang evidence.',
'Annotate map and dynasty sequence; explain authority claims and Legalist responses to governing challenges; start China panel.',
'Individual map/context explanation and one claim distinguishing tradition/evidence.',
'Maps all required features; connects geography to institutions without assuming total isolation; dates/claim types are explicit.',
'If dynasty names become a list, connect a challenge and response then recheck; use a labeled timeline strip.',
'Prepare two context cards and retain authority questions for Qin/Han.','H1/H2 geography, evidence and hierarchy.')
lesson(p,'Connect Qin, Confucius and Han institutions','Qin Shi Huangdi/unification, walls/roads/canals/writing; Confucius, Analects, kinship/order/hierarchy; Han government and technological achievement chronology.',[37,38,39],[4,5,6,8], 'Civ.6 His.4 His.10','HISTORY HAN PRINT',
'Compare a philosophy excerpt and institutional account; show a dated invention strip rather than putting every Chinese invention in Han.',
'Trace policy/institution links; annotate Han timekeeping/astronomy, paper/silk/seismograph evidence; place compass, porcelain and printing records in evidenced periods.',
'Each student explains institutional influence and corrects one unsupported invention/date attribution.',
'Connects Confucian ideas to institutions; distinguishes invention, surviving evidence and later use. TN 6.39 chronology remains flagged.',
'If latest evidence becomes earliest invention, model the distinction and recheck; provide a date/evidence grid.',
'Verify all technology dates and exact source excerpts. Do not teach woodblock printing as securely Han; resolve the TN wording concern with the school.','China authority sequence and source limitation routines.')
lesson(p,'Compare Greek places and citizenship','Aegean, Asia Minor, Athens, Macedonia, Mediterranean, Peloponnese, Sparta; mountains/sea, city-states/trade/colonies; polis, law, civic participation; Athens/Sparta government, education, women and enslaved people.',[41,42,43,44],[3,4,5,6,10], 'Geo.1 Civ.6 His.4','HISTORY CLOCK',
'Model democratic participation with its historical exclusions; compare the same institutional dimensions for Athens and Sparta.',
'Annotate map; build a rights/roles matrix and explain a geographic/economic influence; connect court timing to participation.',
'Private map and citizenship comparison with two institutional differences and an exclusion.',
'No ancient/modern democracy equivalence; group status and place/date shape experiences; map explains spatial pattern.',
'If all residents become citizens, use eligibility/source clinic and recheck; provide matching comparison headings.',
'Prepare short context profiles and accessible court-clock source. CLOCK full-text access is conditional; replace with verified equivalent if unavailable.','China institutions and H2 common comparison questions.')
lesson(p,'Explain Greek conflict, ideas and achievements','Persian/Peloponnesian wars causes/effects; polytheism/Olympics; Socrates/Plato/Aristotle and education; Parthenon/Acropolis/columns; Greek/Hellenistic sky observation.',[45,46,47,48,49],[1,2,5,8], 'His.14 His.3 His.6','HISTORY SKY',
'Separate the two wars on a timeline; use a short philosophy/source example to show context and method, not a claim that all Greeks thought alike.',
'Complete conflict cause/effect strips; compare three philosopher question cards; add belief/architecture/context notes and inspect astronomical-prediction evidence.',
'Individual war comparison and an achievement/significance explanation citing a source limit.',
'Distinct war causes/consequences; philosophers and institutions contextualized; sky models described as historical interpretations.',
'If science lens displaces government/conflict, use private retrieval before adding instrument detail; glossary and comparison cards support reading.',
'Busiest H3 pair: cap new prose, reuse timeline, prioritize history evidence; complex gear reconstruction is not planned. Exact Antikythera dates/source boundaries pending.','Greek map/citizenship and China science context.')
lesson(p,'Plan a fair timekeeping comparison','Han water clocks/sundials, Athenian court timer, astronomical patterns; elapsed-time versus time-of-day; historical evidence versus modern measurement.',[39,48],[2,8], 'D1.5 D3.2 His.10','HAN CLOCK SKY',
'Model a source-purpose comparison and one controlled water-timer plan; supplied dated shadow observations illustrate a different method.',
'Select historical evidence from both societies; define elapsed-time question, fixed vessel/hole/start volume and repeated observations; predict limitations; read supplied shadow table.',
'Individual comparison plan naming sources, measurements/units, controls and evidence limits.',
'Same comparison questions for both cases; no direct China–Greece transmission claim; modern model is labeled.',
'If timer is mistaken for navigation proof, identify its documented use and recheck; offer a protocol diagram without filling in reasoning.',
'Prepare adult-prepunched plastic vessels, trays, water, graduated measures/timers; no sharp student construction. Verify full CLOCK access and a Han source record before claiming source comparison ready.','H3 context, source evaluation and measurement/graph entry check.')
lesson(p,'Test a modern timer and interpret its limits','Repeated elapsed-time observations; water-level/flow variability; comparison with supplied source-labeled shadow data.',[39,48],[8], 'D3.3 His.10 D4.2','HAN CLOCK',
'Demonstrate timing a fixed drained volume and honest anomaly recording; changing water level can affect rate. Results describe this model.',
'Assemble teacher-prepared timer; record three short trials under consistent start conditions; compare variation and shadow-table constraints; draft one bounded historical/scientific comparison.',
'Each student records/reads a trial, explains a data pattern and states one limit on historical inference.',
'Units and repeat conditions explicit; scientific observations separated from historical claims; no civilization accuracy ranking from a classroom model.',
'If invented perfect repeats replace measurements, keep anomalies and recheck inference; accessible direct timing/recording participation or labeled supplied data.',
'Budget setup/model 20, project trials/analysis 40, individual comparison 20, cleanup 10 minutes. Confirm kit access and trial durations before detailed production.','W3-I plan; no assumed completion of science course.')
lesson(p,'Trace exchange and finish the paired display','Silk Road goods/Buddhist diffusion; Macedonia/Alexander/Hellenistic diffusion; dated networks and distinct chronology.',[40,50,33,41],[2,3,8,9], 'His.1 D3.3 D4.4','HISTORY HAN SKY',
'Model evidence for a documented route versus unsupported transmission from similar objects; separate Han and Hellenistic timelines.',
'Annotate two exchange maps; add routes, society-context panels and timer data to the same display; critique one transmission claim.',
'Private route explanation and evidence-based comparison of exchange, with one similarity that does not prove borrowing.',
'Networks include intermediaries and dates; historical contexts remain distinct; display carries both society evidence and experiment limit.',
'If one direct route joins every inventor, examine route chronology and recheck; provide source/date keys.',
'Prepare a fresh invention/source card; keep final display compact—two panels, shared map/timeline and one data/comparison table.','Dynasties, Greek wars/ideas, timer evidence.')
lesson(p,'Demonstrate and defend ancient science comparisons','Paired display review; institutions, history, experiment limits and fresh source reasoning.',list(range(33,51)),[2,5,8,9], 'D4.1 D4.5 His.16','HISTORY HAN CLOCK SKY',
'Model explaining how a source and measured observation answer different questions; critique explanation order.',
'Teams give short demonstration/walkthroughs; each student explains China and Greece achievement/context; respond to a fresh dated source and revise comparison.',
'Private both-society explanation, data interpretation, institutional influence and evidence limit; team display separate.',
'Neither society omitted; scientific comparison and historical corroboration both visible; science standards not automatically credited.',
'If polished display masks history gaps, use separate map/institution/conflict mini-checks and source clinic; record unresolved component.',
'Archive individual history and measurement evidence; retain chronology concern for TN appendix.','All H3 context, source and investigation work.')

p=project(4,'Rome: Republic to Division','H4_ROME_REPUBLIC_TO_DIVISION','How did Rome’s institutions change, and what explains division and western collapse?',
'Build a Roman change-and-cause dossier, compare accounts and hold a historical evidence council using actual outcomes.',
'One team council dossier with map/timeline, institutional comparison and causal evidence chart. Each student submits a short independent multi-cause account and fresh-source revision.',list(range(20,23)),[1,2,3,4,5,6,8,10,13,16,17,18,19],'HISTORY ROME',[
'Institutions change through interacting political, social and economic forces.','Different groups experience expansion and policy differently.','Western collapse and eastern continuation require a multi-cause explanation.'])
lesson(p,'Locate Rome and explain the republic','Tiber, Rome, Italy/Alps, Mediterranean, Constantinople later timeline; geography/growth; patricians, plebeians and enslaved people; republican offices, Senate/assemblies, checks, participation and Twelve Tables.',[51,52,53,54],[3,4,5,6,10], 'Geo.1 Civ.6 His.4','HISTORY ROME',
'Model offices/participation without calling Rome a modern inclusive democracy; place later Constantinople on a dated map layer.',
'Annotate geographic growth map; diagram institutions and eligible participation; compare a rule to affected social groups.',
'Individual map plus institution/participation explanation including excluded groups.',
'Dates/layers explicit; government functions and social limits clear; geography connected to growth.',
'If checks imply equality for everyone, use participation matrix and recheck; accessible map/source chunks.',
'Prepare verified Twelve Tables translation and dated maps; reuse H3 citizenship comparison.','Greek polis and source-based comparison.')
lesson(p,'Explain republic-to-empire change','Julius Caesar military leadership, popular support, dictatorship/assassination; Augustus and Pax Romana expansion and institutions.',[55,56,54],[2,5,6], 'His.1 His.14 His.6','HISTORY ROME',
'Compare a ruler image/claim to another account; trace structural tensions alongside leaders and trigger events.',
'Build transition timeline; compare institutional change and source perspectives; add cause/effect evidence to council dossier.',
'Private multi-factor transition explanation and ruler-source purpose inference.',
'Distinguishes Caesar from Augustus and continuity from change; propaganda not treated as complete social evidence.',
'If one leader explains everything, add a structural evidence card and recheck; use dated actors/events.',
'Select contrasting accounts and dated coin/inscription; preserve institutional chart for W4 synthesis.','Republic roles and evidence limitation.')
lesson(p,'Explain engineering and everyday life','Arches, aqueducts, bridges, domes, roads, sanitation and Colosseum; work, distribution, trade and polytheistic practice.',[57,58],[1,3,7,8], 'Geo.4 Civ.6 D4.2','HISTORY ROME',
'Model infrastructure benefits and unequal access/costs; monument evidence cannot describe everyone’s daily life.',
'Trace two infrastructure systems on a city diagram; explain remaining examples through a short annotated gallery; connect civic/religious use to daily experience.',
'Individual system explanation and attributed polytheism/context note.',
'Explains function and human/environment effects; all named infrastructure appears; social differences recognized.',
'If drawings replace reasoning, add flow/use labels and recheck another structure; offer large diagrams.',
'No extra engineering build; select verified diagram/object sources and maintain the same dossier.','H1 technology and H3 model/historical evidence distinction.')
lesson(p,'Contextualize Christianity and Jewish diaspora','Christianity: Jesus/Paul, Bible, monotheism, sin/forgiveness, eternal life, Messiah; historical spread/persecution and imperial change; Roman/Jewish conflicts and dispersal.',[59,60,58],[1,4,5,9], 'His.4 His.6 D3.2','HISTORY',
'Use the common religion template from H2; distinguish faith claims from historical analysis and explain multiple diaspora phases.',
'Annotate religion/context cards; map dated displacement/spread; compare two attributed accounts without devotional performance.',
'Private Christianity profile and source-based diaspora cause/movement explanation.',
'Beliefs are accurately attributed; political conflict and movement dates are not collapsed into one expulsion or all-Jewish departure.',
'If sacred account becomes automatic modern historical proof, classify source purpose and corroborate; glossary and neutral response options.',
'Prepare sensitive, scholarly source selection and timeline; no present-day group blame.','H2 Judaism and respectful religious-source inquiry.')
lesson(p,'Map division and eastern continuation','Constantine/Constantinople; administrative division versus relocation; East/West and Byzantine continuation; territory/governing pressures.',[61,62,51],[2,3,5,6], 'Geo.1 His.2 His.14','HISTORY ROME',
'Model changing dated boundaries and multiple stages of division; 476 in the West does not end every Roman institution.',
'Layer empire maps; identify capital-location factors; sort continuity/change evidence for eastern/western regions.',
'Individual division map and explanation of one continuity and two capital/governance factors.',
'Distinguishes division from western collapse; East continues; time/place shapes cause.',
'If a single map becomes timeless, add dates and recheck layers; use paired maps with consistent scale.',
'Prepare map dates and source captions; save pressures for cause-ranking session.','Rome institutions, geography and regional comparison.')
lesson(p,'Weigh explanations for western collapse','Large territory, political instability/corruption, economic pressures, Germanic groups and military conflict; relative cause influence and evidence limits.',[62,52,56,61],[2,6,7,9], 'His.15 D3.3 D4.4','HISTORY ROME',
'Model comparing the explanatory reach of causes; avoid a single invasion-only or moral-decline explanation.',
'Compare three bounded interpretations with evidence; make a causal web; weigh two causes and challenge unsupported claims.',
'Private cause-ranking argument with evidence, a competing view and limitation.',
'Multiple interacting causes; relative influence justified; distinguishes evidence from a rhetorical moral claim.',
'If ranking is personal preference, require a sourced mechanism then recheck a new cause; provide an evidence/cause chart.',
'Select contrasting historian arguments and provenance; reserve revision for W4-I.','Division/continuation and source credibility.')
lesson(p,'Prepare the evidence council','Synthesize republic, empire, infrastructure, religion, diaspora, division and fall; evaluate arguments and coherent explanations.',list(range(51,63)),[2,5,6,10], 'His.16 D4.1 D4.5','HISTORY ROME',
'Model an evidence council discussing actual historical causes; conjectured policy outcomes, if mentioned, are labeled counterfactual.',
'Finish existing dossier; individually write a bounded multi-cause account; critique source credibility and sequence; revise one argument.',
'Independent 200–300-word or equivalent causal account with multiple sources, limitation and revision.',
'Historical outcomes accurate; East/West distinction preserved; evidence addresses causes and institutional change.',
'If team consensus replaces private learning, collect independent account first; scaffold organization without supplying the claim.',
'Prepare a fresh map/account check and a contribution roster; no game or alternative-history victory scoring.','All H4 institutional, geographic and causal work.')
lesson(p,'Hold the council and apply new evidence','Evidence council, fresh historical source interpretation and course-wide inquiry reflection.',list(range(51,63)),[2,9,10], 'D4.1 D4.4 His.10','HISTORY ROME',
'Model civil critique: identify claim, relevant source, limitation and evidence that would change the conclusion.',
'Teams present actual-history explanations; every student responds to a question; independently analyze a fresh source and revise the causal account.',
'Teacher-recorded response, fresh source inference and independent revision; team council quality assessed separately.',
'Civil discussion and supported reasoning; new evidence changes or sustains a conclusion for a stated reason.',
'If performance masks missing history, use targeted map/chronology/source recheck; record remaining learning for the next course.',
'Archive inquiry growth and unresolved content; use a class-approved exhibit correction as a bounded civic practice, without a full informed-action indicator claim.','All-course source selection, comparison and causation.')

# A modern oral-history source supplies the recurring SSP source modality without inventing an ancient eyewitness.
oral=projects[1]['lessons'][1]
oral['activity']+=' Compare a brief, sourced modern excavator oral recollection with a dated discovery record; distinguish recollection from ancient eyewitness evidence.'
oral['evidence']+=' Include one comparison of the oral recollection and discovery record.'
oral['handoff']+=' Select and caption a 60–90-second recorded excavator recollection, or attributed oral-history transcript, with creator/date/context; keep total new reading/listening within the block budget.'
# Separate official source text from maintained curriculum interpretation and evidence routes.
raw=(base/'tn-extract.txt').read_text(encoding='utf-8')
items=list(re.finditer(r'(?m)^6\.(\d{2})\s',raw));tn=[]
for i,m in enumerate(items):
    num=int(m.group(1));end=items[i+1].start() if i+1<len(items) else len(raw)
    text=raw[m.end():end]
    # Strip table/page metadata, retaining official requirement and bullet components.
    text=re.split(r'\n(?:PDF PAGE|Ancient |Standard\s*$)',text,1)[0]
    text=re.sub(r'\s+C(?:, [CEGHPT])+(?:\s|$)',' ',text)
    text=re.sub(r'\s+[GH](?:\s*)$','',text)
    text=' '.join(text.split())
    routes=[l['id'] for p in projects for l in p['lessons'] if num in l['tn']]
    tn.append(dict(id=f'6.{num:02}',source_text=text,routes=routes,status='Unverified' if num==39 else 'Covered in plan',action='Teach documented Han accomplishments and date later printing separately. Resolve apparent chronology conflict in official 6.39 before certifying that component; exact porcelain/compass attribution also needs source review.' if num==39 else 'Verify the exact source packet and individual component checks in Step 5; produce and trial materials in Step 6.'))
assert len(tn)==62 and all(t['routes'] for t in tn)
practice=['Varied primary/secondary source collection, including artifacts, maps, media and oral accounts.','Paraphrase, fact/opinion, purpose/perspective/bias, inference and argument limits.','Corroborate different accounts and ask further questions.','Defend claims, compare views, explain causes, distinguish prediction and counterfactual, engage in civic discourse.','Context, empathy, changing accounts, continuity/change and present connections.','Select/evaluate maps, spatial patterns and diffusion, changing regions and human–environment relationships.']
practice_routes=[['H1-W1-I','H1-W3-I','H2-W1-G','H3-W3-I','H4-W4-G'],['H1-W3-I','H1-W3-G','H2-W2-I','H3-W1-G','H4-W2-G'],['H1-W3-G','H2-W4-I','H3-W4-I','H4-W3-G'],['H1-W4-I','H2-W4-G','H3-W4-G','H4-W4-I','H4-W4-G'],['H1-W1-G','H2-W1-G','H2-W3-G','H3-W1-G','H4-W3-I','H4-W4-G'],['H1-W2-I','H2-W1-I','H2-W2-I','H2-W3-I','H3-W1-I','H3-W2-I','H3-W4-I','H4-W3-I']]
for i,(v,r) in enumerate(zip(practice,practice_routes),1):tn.append(dict(id=f'SSP.{i:02}',source_text=v,routes=r,status='Covered in plan',action='Recurring practice contributions; verify all source modalities and cumulative evidence in detailed planning. Oral-history study uses a sourced modern archaeology/discovery oral account, not a fabricated ancient eyewitness.'))
for p in projects:
    assert len(p['lessons'])==8
    for l in p['lessons']:
        assert set(l['primary']+l['supporting'])<=set(specs)
        l['link']=f"../scope-and-sequence/history-projects/{p['slug']}.md#{l['id'].lower()}"
        l['skills']=f"Teach / revisit: {l['content']}\nPractice: {l['activity']}\nCheck: {l['evidence']}\nBuilds on: {l['prereq']}"
national=[dict(id=k,learning=v,primary_routes=[l['id'] for p in projects for l in p['lessons'] if k in l['primary']],support_routes=[l['id'] for p in projects for l in p['lessons'] if k in l['supporting']]) for k,v in specs.items()]
assert all(n['primary_routes'] or n['support_routes'] for n in national)
needs=[
['Historical depth and calendar','16 weeks gives a survey across seven major society contexts. Confirm expected depth and actual dates; trial H2-W3 and H3-W2 before detailed expansion. Additional depth may need more time.'],
['Exact source packets','Step 5 selects creator/date/place/purpose/audience, excerpt boundaries and contrasting viewpoints; Step 6 builds accessible texts/images, fresh cases and answer/scoring guidance.'],
['H3 historical chronology','TN 6.39 groups printing with Han achievements. Teach evidence-based dates; keep the disputed attribution Unverified pending interpretation. Verify all invention chronology.'],
['H3 investigation access','Verify Greek clock source access; choose exact Han primary record. Prepare adult-made water-timer kits, equivalent participation and supplied shadow data with provenance.'],
['Religion and historical interpretation','Use matched academic religion profiles, accurate sacred-text attribution and scholarly context; keep tradition, belief and corroborated historical evidence distinct.'],
['Enrollment and observation','Assume 24 learners/six teams. Confirm class size and observation capacity before detailed clocks. No required homework.'],
['Program boundary','Selected NCSS themes/C3 contributions support this ancient-history term. Other geography/economics, contemporary civics and complete Grades 6–8 expectations require schoolwide ownership. Accreditor identity/criteria remain to supply separately.']]
from lesson_details import enrich
enrich(projects,resources,specs,tn)
needs=[
 ['Material production','Step 6: produce the 32 bounded source packets, accessible maps/cards, models, developing responses, held-back cases and response keys from the detailed specifications. Check primary-object provenance and exact excerpt fit.'],
 ['Historical chronology','TN 6.39 remains Unverified: date documented Han achievements and later printing separately; verify compass/porcelain attribution before certifying these components.'],
 ['Oral modality','SSP.01 is Conditional until a real 60–90-second modern archaeology oral account has verified speaker/date/context and transcript. A written discovery record does not satisfy oral evidence.'],
 ['Investigation','Pilot six adult-prepared water timers and labeled supplied shadow data; choose the Han primary artifact record. MacTutor provides the selected Greek scholarly context.'],
 ['Pacing and enrollment','All 32 budgets total 90 minutes with at least 30 minutes project work. Assume 24 students/six groups; trial H2-W3 and H3-W2 with actual readers. Keep no required homework.'],
 ['Program boundary','Selected NCSS themes/C3 contributions only; schoolwide grade-band ownership, accreditor identity and criteria remain separate.']]
data=dict(date='2026-10-03',status=STATUS,scope='16 weeks; four projects; eight 90-minute blocks per project; 32 blocks / 48 hours; individual then group each week; no required homework.',projects=projects,resources=resources,national=national,themes=[dict(id=f'NCSS-T{i}',title=v,routes=[l['id'] for p in projects for l in p['lessons'] if i in l['themes']]) for i,v in enumerate(themes,1)],tn=tn,needs=needs)
(base/'history.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('Maintained 4 projects / 32 detailed teacher plans / 22 C3 contributions / 10 NCSS themes / 62 TN content and 6 recurring practice checks.')
