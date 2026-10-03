"""Maintained science planning content. Generates science.json; no workbook writes."""
from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
STATUS='Steps 1–5 planning drafted and reviewed; materials, access arrangements and classroom timing remain to verify in Step 6. This is a 16-week sequence, not a verified full-year course or student mastery claim.'
resources=[
 ['NGSS','NGSS — All Grades, arranged by disciplinary core idea','https://www.nextgenscience.org/sites/default/files/AllDCI.pdf','Middle-school energy, ecosystems, Earth systems, human impacts and engineering sections; teacher reference.','Saved official PDF: reference-standards/NGSS_All_Grades_DCI.pdf. 2013 framework; source checked 2026-10-03.'],
 ['TN','Tennessee Academic Standards for Science','https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/science/New%2010-28-22%20Science%20Standards.pdf','PDF pages 49–52: Grade 6 overview and all 20 expectations; teacher compliance reference.','October 2022 adoption; implementation 2025–26; selected school year 2027–28. Local PDF verified; official status checked 2026-10-03.'],
 ['HEAT','U.S. Department of Energy — Heat Flow','https://bsesc.energy.gov/energy-basics/heat-flow','The conduction, convection and radiation explanations; select a diagram and a 150–200-word adapted reading.','Public source located; student adaptation, attribution, access and reading fit pending Step 6.'],
 ['CARP','Tennessee Wildlife Resources Agency — Invasive Carp','https://www.tn.gov/content/tn/twra/wildlife/fish/invasive-carp.html','Bighead Carp and controlling spread sections; select ecological effects and management evidence, not fishing instructions.','Teacher review source; prepare bounded 200-word student selection and verified evidence table. No animal collection.'],
 ['WATER','USGS — The Water Cycle','https://labs.waterdata.usgs.gov/visualizations/water-cycle/index.html','Diagram: atmosphere, land, groundwater, ocean and human water-use pathways; accessible static equivalent.','Public diagram available; captioned/local accessible excerpt pending Step 6.'],
 ['WEATHER','NOAA — Weather systems and patterns','https://www.noaa.gov/education/resource-collections/weather-atmosphere/weather-systems-patterns','Global winds, air masses, fronts and Coriolis effect sections; split into short lesson selections.','Prepare vocabulary support and bounded readings; do not assign whole webpage each lesson.'],
 ['OCEAN','NOAA — Thermohaline Circulation','https://oceanservice.noaa.gov/education/tutorial_currents/05conveyor1.html','Opening explanation and circulation diagram: temperature, salinity and density.','Accessible annotated diagram and brief adaptation pending.'],
 ['CLIMATE','NASA — Causes of climate change','https://science.nasa.gov/climate-change/causes/','Greenhouse mechanism and human/natural factors; choose evidence graphics with dates, axes and source attribution.','Teacher source inspected; bounded age-appropriate packet, chart provenance and captions pending.'],
 ['GREEN','EPA — Environmental Benefits of Green Infrastructure','https://www.epa.gov/green-infrastructure/environmental-benefits-green-infrastructure','Water quality, water supply and habitat benefits relevant to the selected park case.','Prepare 150–250-word attributed selection; distinguish possible benefits from measured local outcomes.'],
 ['OPTIONS','EPA — Types of Green Infrastructure','https://www.epa.gov/green-infrastructure/types-green-infrastructure','Select rain gardens/bioretention and permeable surfaces as the two default park options.','Select exact diagrams and practical constraints before producing the packet.'],
 ['ENERGY','U.S. Energy Information Administration — Renewable energy explained','https://www.eia.gov/energyexplained/renewable-sources/','Source types and linked technology descriptions; compare solar PV, wind and a developing application.','Prepare evidence cards with dated source information; no unverified current cost or efficiency claims.'],
 ['DEV','U.S. Department of Energy — Perovskite Research Directions','https://www.energy.gov/cmei/systems/perovskite-research-directions','Use the dated April 2024 research case: perovskite-silicon tandem potential, durability and scaling challenges. Compare with established silicon PV.','Source checked 2026-10-03. Treat 2024 results as a dated case, not current market status. Prepare a 100-word plain-language adaptation; no solar-cell construction.'],
]

ngss_specs=[
 ('MS-PS3-3','Design, construct and test a device that controls thermal transfer.','PS3.A/B; ETS1.A/B','Design solutions','Energy and matter','No calculation of total thermal energy required.'),
 ('MS-PS3-4','Plan a controlled investigation relating transfer, material, mass and temperature change.','PS3.A/B','Plan investigations','Scale, proportion and quantity','Temperature measures average particle kinetic energy; compare effects without total-energy calculations.'),
 ('MS-LS2-1','Interpret data on resources, individual growth and population size.','LS2.A','Analyze data','Cause and effect','Use abundant/scarce resource cases; correlation alone does not prove cause.'),
 ('MS-LS2-2','Explain and predict interaction patterns across ecosystems.','LS2.A','Construct explanations','Patterns','Compare competitive, predatory and mutually beneficial relationships in more than one ecosystem.'),
 ('MS-LS2-3','Model matter cycling and energy flow through living and nonliving ecosystem parts.','LS2.B','Develop/use models','Energy and matter','Define a system boundary; no chemical equations required.'),
 ('MS-LS2-4','Argue from empirical evidence that ecosystem changes affect populations.','LS2.C','Argue from evidence','Stability and change','Distinguish measured evidence from hypothetical practice data.'),
 ('MS-LS2-5','Evaluate competing biodiversity and ecosystem-service solutions.','LS2.C; LS4.D; ETS1.B','Argue from evidence','Stability and change','Compare ecological, social and economic constraints; more than naming a preferred solution.'),
 ('MS-ESS2-4','Model multiple water pathways driven by solar energy and gravity.','ESS2.C','Develop/use models','Energy and matter','Include changes of state; no latent-heat calculations.'),
 ('MS-ESS2-5','Collect data linking interacting air masses to weather changes and probable forecasts.','ESS2.C/D','Plan investigations','Cause and effect','Track temperature, pressure, humidity, precipitation and wind; no symbol memorization requirement.'),
 ('MS-ESS2-6','Model unequal heating, rotation, circulation and regional climate.','ESS2.C/D','Develop/use models','Systems and system models','Include latitude, altitude, land distribution and ocean circulation; no Coriolis dynamics calculations.'),
 ('MS-ESS3-3','Design a scientifically justified method to monitor and reduce human environmental impact.','ESS3.C; ETS1.B','Design solutions','Cause and effect','Specify both mitigation and a measurable monitoring method.'),
 ('MS-ESS3-4','Argue how population growth and per-person resource use affect Earth systems.','ESS3.C','Argue from evidence','Cause and effect','Separate population size from per-capita consumption; evidence informs but does not dictate values.'),
 ('MS-ESS3-5','Ask evidence-clarifying questions about causes of recent global temperature rise.','ESS3.D','Ask questions','Stability and change','Examine human and natural factors; distinguish global trends from individual weather events.'),
 ('MS-ETS1-1','Define measurable criteria and constraints with scientific and environmental considerations.','ETS1.A','Define problems','Design context: systems','Do not replace measurable criteria with appearance preferences.'),
 ('MS-ETS1-2','Systematically evaluate competing solutions against common criteria and constraints.','ETS1.B','Argue from evidence','Design context: cause/effect','Use the same criteria for all alternatives; no invented weighted score required.'),
 ('MS-ETS1-3','Analyze tests of several designs and combine their useful characteristics.','ETS1.B/C','Analyze data','Design context: patterns','Compare at least three class designs; identify why features may work together.'),
 ('MS-ETS1-4','Use a model to generate data for iterative tests and design modifications.','ETS1.B/C','Develop/use models','Design context: systems','Compare successive physical prototype tests; improvement is constrained, not a universal optimum.')
]
ngss={x[0]:dict(zip(['id','learning','dci','sep','ccc','boundary'],x)) for x in ngss_specs}
tn_codes=['6.PS3.1','6.PS3.2','6.LS2.1','6.LS2.2','6.LS2.3','6.LS2.4','6.LS2.5','6.LS4.1',*[f'6.ESS2.{i}' for i in range(1,8)],*[f'6.ESS3.{i}' for i in range(1,4)],'6.ETS1.1','6.ETS1.2']
tn_learning=[
 'Analyze energy sources and conservation across kinetic, elastic/gravitational/chemical potential and thermal transfers.',
 'Use models as evidence that thermal transfers change a system; distinguish conduction, convection and radiation. Thermal route selected.',
 'Use living/nonliving resource data to explain population size.',
 'Predict competitive, symbiotic and predatory interactions across ecosystems.',
 'Model energy transfer through a food web AND energy pyramid.',
 'Explain biotic/abiotic health patterns in terrestrial AND aquatic ecosystems.',
 'Use existing evidence of a named Tennessee invasive species; design a response to reduce impacts.',
 'Explain biodiversity effects on food, medicine, clean water and ecosystem services.',
 'Diagram atmospheric and ocean convection caused by uneven heating.',
 'Use evidence of solar heating and salinity effects to justify ocean circulation.',
 'Explain regional climate through atmospheric flow, geographic features and ocean heat transfer.',
 'Model solar-energy/gravity-driven water cycling through multiple Earth systems.',
 'Interpret human AND other-organism impacts on water cycling, landforms and atmospheric systems.',
 'Model greenhouse gases regulating average surface temperature and habitability.',
 'Collect and interpret air-mass/weather data to predict probable local patterns.',
 'Use consumption data to explain renewable/nonrenewable resource sustainability and Earth-system impacts.',
 'Investigate and compare existing AND developing renewable/alternative energy technologies.',
 'Evaluate and communicate human effects on the biosphere, including conservation, habitat, endangerment and extinction.',
 'Design, evaluate and improve a biodiversity-maintenance solution.',
 'Design, physically construct and test a thermal-transfer device combining useful solution parts; explain results.'
]
tn=[{'id':c,'forge':f'FF.G6.SCI.{i+1:02}','learning':v} for i,(c,v) in enumerate(zip(tn_codes,tn_learning))]
projects=[]
def project(n,title,slug,question,glance,product,understandings,home,recur,resource_ids,materials):
 p=dict(n=n,id=f'S{n}',title=title,slug=slug,question=question,glance=glance,product=product,understandings=understandings,home=home,recur=recur,resources=resource_ids,materials=materials,lessons=[])
 projects.append(p);return p
def lesson(p,title,focus,primary,support,tn_ids,resources,reading,model,steps,check,criteria,response,prep,prereq,practice,sep,ccc,clock='standard'):
 i=len(p['lessons']);lid=f"{p['id']}-W{i//2+1}-{'I' if i%2==0 else 'G'}"
 p['lessons'].append(dict(id=lid,week=i//2+1,mode='Individual' if i%2==0 else 'Group',title=title,focus=focus,primary=primary.split(),support=support.split(),tn=tn_ids,resources=resources.split(),reading=reading,model=model,steps=steps,check=check,criteria=criteria,response=response,prep=prep,prereq=prereq,practice=practice,sep=sep,ccc=ccc,clock=clock,verification='Confirmed in plan for the named contribution; whole performance expectation is evidenced across its mapped route. Materials and observed learning remain separate.'))

p=project(1,'Thermal Cargo Challenge','S1_THERMAL_CARGO_CHALLENGE','How can we keep a small cargo sample cool using a tested design?',
 'Investigate energy transfer, build a small insulated carrier, compare results and improve it.',
 'One reusable design record with labeled energy model, investigation plan, prototype sketches, test table/graph and justified revision; a physical carrier and a short individual explanation.',
 ['Energy moves between a system and surroundings; insulation slows transfer rather than making cold.','Fair comparisons and repeated measurements help distinguish promising designs.','Testing and combining useful features can improve a design within constraints.'],[1,2,20],[],['HEAT'],
 ['T1: Cargo brief, materials/cost cards, reusable design record and rubric; Pending Step 6.','T2: Measured-energy/material/mass dataset and controlled-investigation planning card; verify provenance and axes before use.','T3: Identical lidded cups, water, ice packs, thermometers, trays, timers, balance, paper/cardboard/reused fabric and tape; supervised physical construction/testing required.','T4: Different-case transfer assessment, model/developing explanations and answer guidance; Pending Step 6.'])
lesson(p,'Trace energy into and out of the cargo','Define the system and explain why a cold sample warms.','MS-PS3-3','MS-PS3-4',[1,2],'HEAT','One cargo diagram and about 150 words; read the diagram aloud together.',
 'Model a warm drink cooling: draw sample, container and room; arrows show transfer from warmer to cooler objects. Contrast temperature with total thermal energy. Use a rolling ball, stretched band and battery-driven fan as separate energy-accounting examples; energy is transferred, not used up.',
 ['Record a prediction for identical cold samples in bare and wrapped cups.','Observe teacher-prepared temperature readings at start and finish; label system boundaries.','Build a before/after energy model and annotate conduction, moving-fluid convection and radiation paths.','Use short energy-source cards to trace gravitational, elastic and chemical stores into motion/thermal effects.','Revise the cargo explanation after a partner challenges the direction of an arrow.'],
 'Collect each student’s labeled cargo model and one energy-source transfer chain; a fresh warm-lunchbox prompt checks transfer direction.',
 'Energy arrows run from warmer surroundings toward the cold cargo; name the system, source and destination. Preserve energy accounting; temperature is not energy amount.',
 'If cold is drawn flowing outward, compare two objects at different temperatures, redraw energy arrows, then recheck an ice pack beside a warm bottle. Extend by changing the system boundary.',
 'Prepare safe sealed samples and actual readings; carry unresolved arrow/temperature errors into W1-G opening. Save the same model for revision.',
 'Read a thermometer and compare numbers.','Annotate a system and an energy chain.','Develop a model','Energy and matter')
lesson(p,'Set criteria and compare carrier ideas','Turn the cargo need into measurable requirements before building.','MS-ETS1-1 MS-ETS1-2','MS-PS3-3',[2,20],'HEAT','Cargo brief and three small material cards; at most 200 new words.',
 'Model criteria versus constraints using a rainproof book bag, then return to cargo. Propose a local design target: least warming over 10 minutes among feasible carriers; equal 100 mL samples, comparable start temperatures and room conditions. Set a fixed material allowance, not a grading cutoff.',
 ['Agree on success measures, allowed materials and size limits.','Sketch two different carriers and label their expected thermal effects.','Compare them in one criteria table, including cost/reuse and accessibility.','Choose one design with a reason and record a concern to test.','Each learner independently identifies a controlled variable and a possible unfair comparison.'],
 'Two sketches, shared criteria table and private control-variable note.',
 'Requirements are measurable; both designs face the same constraints; choice refers to a transfer mechanism and a tradeoff.',
 'If a criterion is “looks good,” replace it with an observable measure and recheck a new example. Offer a labeled sketch frame; extension compares reusable-material waste.',
 'Prepare material cards and inspect kit access for every learner; bring selected sketch into investigation planning.',
 'System/transfer model from W1-I.','Compare two designs using common criteria.','Define problems and evaluate solutions','Cause and effect')
lesson(p,'Plan a fair thermal investigation','Separate material and mass effects from uncontrolled changes.','MS-PS3-4','MS-PS3-3',[1,2],'HEAT','A two-part investigation card and small labeled data table; about 150 words.',
 'Demonstrate how equal temperature does not imply equal stored energy for different masses. Plan matched comparisons: same material/different masses and same mass/different materials under measured equal energy input. Explain sensors, measurement intervals, replicates and controls; equal heating time alone does not guarantee equal energy transfer.',
 ['Write a question and prediction for each comparison.','Specify input energy, material, mass and temperature measurements without calculating joules.','Identify controls and at least two repeats; sketch the apparatus.','Critique a deliberately confounded example and repair it.','Use a supplied source-verified table to explain what result would support or challenge the prediction.'],
 'Individual investigation plan addressing material, mass, transfer and temperature change; a corrected unfair-test example.',
 'Vary one factor at a time; match energy input where claimed; connect temperature change to average particle motion. Name measurement limits.',
 'If a student equates equal minutes with equal transfer, show different heaters and ask what must be measured; recheck the plan. Provide a variable grid without choosing the variables for them.',
 'Produce keyed empirical or clearly labeled illustrative tables and the measurement diagram. Carry control checks into prototype tests.',
 'Thermometer reading, controlled variables.','Repair and explain a controlled plan.','Plan investigations','Scale, proportion and quantity')
lesson(p,'Build and measure the first carrier','Construct the proposed device and collect comparable evidence.','MS-PS3-3 MS-ETS1-4','MS-PS3-4',[2,20],'HEAT','Illustrated setup and safety checklist; no new article.',
 'Show equal water volumes, matched starting temperatures, thermometer placement and reading at 0, 2, 4, 6, 8 and 10 minutes. Model recording an unexpected result without changing it. Keep the comparison cup exposed to the same surroundings.',
 ['Assemble the carrier with pre-cut permitted materials.','Use trays and sealed/secured sample cups; assign operator, recorder, timer and observer roles that rotate.','Run a 10-minute trial beside a bare control and repeat after resetting samples.','During intervals, label the prototype energy pathways and calculate temperature changes.','Clean up and each student explains one measurement and a limitation.'],
 'Actual prototype, two-trial table with units, individual feature-to-mechanism explanation.',
 'The device exists and was tested; data include controls and honest anomalies. Explain a feature’s effect rather than claiming proof from one favorable reading.',
 'If start conditions differ, mark the comparison limited and reset the next run; recheck with a matched pair. Offer an accessible recording role plus direct individual design/test participation.',
 'Verify thermometers and kits; no flames, mains wiring, sharp construction or unsupervised hot liquids. Preserve data for class comparison.',
 'Fair-test plan and selected sketch.','Construct, measure and explain a device.','Design/test solutions','Energy and matter','lab')
lesson(p,'Compare results across three designs','Identify useful features from several tested carriers.','MS-ETS1-3 MS-ETS1-2','MS-PS3-3',[1,2,20],'HEAT','Three class-design records and graph labels; no extra reading.',
 'Model a comparison using different example data: examine start temperature, control, repeats and material use before judging warming rate. A small difference within measurement variation may be inconclusive.',
 ['Plot or annotate the two trials from your carrier.','Compare at least three class designs using the agreed criteria.','Identify a useful feature in two different designs and explain its mechanism.','Sketch one combined revision and predict an observable change.','Independently justify the combination and identify one uncertainty.'],
 'Comparison of three designs, combined-feature sketch and individual evidence-based justification.',
 'Use test data and common criteria; select features for scientific reasons; distinguish a prediction from an observed improvement.',
 'If “best” means lowest final temperature despite unequal starts, compare changes and controls then recheck another pair. Extension identifies whether combining features could add unwanted mass.',
 'Compile actual class data with provenance; if unavailable, clearly label a practice dataset and retain the real-test requirement for W3-G.',
 'Tables, temperature differences, controls.','Compare multiple designs and plan a combined revision.','Analyze data','Patterns')
lesson(p,'Improve and retest the carrier','Use the first evidence to revise a feature and measure again.','MS-ETS1-4 MS-PS3-3','MS-ETS1-3',[2,20],'HEAT','Previous plans and concise reset checklist.',
 'Model a revision record: what changed, why, expected effect, what remained controlled. Explain why no improvement is still useful evidence.',
 ['Modify the selected feature combination within the same constraints.','Run two reset trials with the unchanged control procedure.','Compare original/revised temperature changes and repeat variation.','Refine the energy model to explain supported or unsupported predictions.','Each student chooses retain, modify or reject with a data-based reason.'],
 'Revised physical carrier, new trial records and private revision decision.',
 'Modification responds to evidence; testing is comparable; conclusions match results without invented success.',
 'If teams alter several features without a rationale, identify the inference limit and plan a next isolating comparison. Recheck with a single-feature cause/effect prompt.',
 'Provide spare materials/reset samples; carry any unobserved physical participation into W4-I supervised support.',
 'Three-design comparison and revision hypothesis.','Modify and retest a physical model.','Develop/use models','Systems and system models','lab')
lesson(p,'Explain the final design independently','Turn the tested work into a clear scientific explanation.','MS-PS3-3 MS-PS3-4','MS-ETS1-2',[1,2,20],'HEAT','Own design record and one new investigation prompt.',
 'Compare an evidence-based explanation with “the fabric keeps cold in.” Model claim, measurements, mechanism and limitation using a different device. Revisit material/mass controls briefly.',
 ['Use opening support to repair the named unresolved component.','Complete the design record using existing sketches/data rather than recopying.','Individually explain energy sources and transfer mechanisms for the carrier.','Plan a new controlled comparison involving a different mass or material.','Revise the explanation after precise feedback and mark supported versus solo evidence.'],
 'Individual explanation and fresh investigation plan attached to the shared design record.',
 'Explain conservation and mechanisms; use actual data; retain controlled comparison logic across changed values/materials.',
 'If evidence is listed but not explained, connect one temperature change to one mechanism orally then recheck a fresh case. Offer a scribe/audio response while retaining individual reasoning.',
 'Prepare fresh prompt and key; identify who still needs direct test evidence before W4-G.',
 'Tested prototype and data interpretation.','Explain and transfer investigation reasoning.','Construct explanations','Energy and matter','workshop')
lesson(p,'Demonstrate the carrier and transfer the learning','Share the tested solution and respond to an unfamiliar cargo case.','MS-PS3-3 MS-ETS1-3 MS-ETS1-4','MS-ETS1-1',[1,2,20],'HEAT','Final record and short new-case card.',
 'Model a concise demonstration using already collected data and a safe setup; distinguish retelling procedures from explaining a result. State that the new case asks for reasoning, not an unplanned rebuild.',
 ['Finish a targeted supervised check if physical construction/testing evidence is missing.','Teams demonstrate the carrier and explain one improvement using the graph.','Each member explains a mechanism or test decision; peers record a useful question.','Individually recommend changes for keeping a warm sample warm and justify energy direction.','Archive the unresolved learning record for S2 energy models and S3 convection.'],
 'Team demonstration quality, individual oral contribution and fresh thermal-transfer response kept separately.',
 'Claims refer to measured evidence; explain a useful feature combination and limits; correctly transfer direction to a warm-cargo case.',
 'If a student repeats the team answer without a mechanism, use a brief different-material prompt and record a targeted next check. Do not infer competence from attendance.',
 'Assume six teams of four: 30 minutes for six 5-minute demonstrations; verify class size. Teacher records contributions across earlier lessons and today.',
 'Final design record and individual explanation.','Demonstrate and apply to a new case.','Communicate explanations','Energy and matter','presentation')

p=project(2,'Tennessee Ecosystem Detectives','S2_TENNESSEE_ECOSYSTEM_DETECTIVES','What evidence explains an ecosystem change, and which response could help?',
 'Investigate changing populations, trace food-web effects and recommend a response to an invasive species using evidence.',
 'One case file with an ecosystem model, annotated data, competing explanations and a revised invasive-species response; each student writes a short independent case conclusion.',
 ['Resource changes and organism interactions can alter populations.','Matter cycles while energy flows through ecosystems.','Several indicators and credible evidence are needed to evaluate ecosystem health and conservation choices.'],list(range(3,9)),[1],['CARP'],
 ['E1: Paired terrestrial/aquatic evidence packet with measured resource/population data, dates and locations; Pending Step 6.','E2: Organism cards, food-web/matter tokens, energy-pyramid diagram and biome reference cards; Pending Step 6.','E3: TWRA invasive-carp source selection and empirical native-population evidence with confound notes; Pending Step 6.','E4: Competing response cards, fresh ecosystem case and model/developing conclusions; Pending Step 6.'])
lesson(p,'Read the ecosystem evidence','Use living and nonliving resource data to frame the case.','MS-LS2-1','MS-LS2-4',[3,6],'CARP','One paired forest/pond data sheet; about 150 words plus graphs.',
 'Model axis reading with an unrelated garden example. Compare organism growth and population count; show that co-occurring trends suggest a hypothesis rather than proving a cause.',
 ['Observe contrasting forest and freshwater photos and define each system.','Annotate a resource series and population series with units/time.','Separate living/nonliving variables; record two patterns.','Propose two possible explanations and a missing measurement.','Start a case file and revise one unsupported statement.'],
 'Individual annotated resource/population graph and two explanations with evidence limits.',
 'Distinguish growth from number, name a resource, use a data pattern and avoid unsupported causation.',
 'If a student reads higher bars as healthier, label what the bars measure and recheck a different graph. Offer axis-reading scaffold; extend by identifying a confound.',
 'Select empirical data with provenance; synthetic practice must be labeled. Carry graph difficulties into W1-G.',
 'Read tables/axes and identify organism needs.','Interpret resource/population patterns.','Analyze data','Cause and effect')
lesson(p,'Predict interactions across habitats','Compare competition, predation and symbiosis in forest and pond systems.','MS-LS2-2','MS-LS2-1',[3,4],'CARP','Six short organism-pair cards, maximum 200 words total.',
 'Model a predator/prey explanation in grassland, then mutual benefit and competition. Include parasitism/commensalism as symbiotic patterns without assuming all symbiosis helps both organisms.',
 ['Sort organism relationships using effects on each organism.','Build small forest and pond interaction diagrams.','Predict changes if food becomes scarce; explain the mechanism.','Challenge one prediction using a competing interpretation.','Each student predicts an unfamiliar pair and revises a diagram.'],
 'Two-habitat comparison and individual new-interaction prediction.',
 'Explain effects on both organisms and carry a pattern across ecosystems; distinguish competition from predation.',
 'If every interaction is labeled predation, ask what is consumed and recheck two organisms sharing food. Provide relation arrows; extension examines indirect effects.',
 'Prepare checked organism facts; keep interaction diagrams for food webs.',
 'Resource limitations and population patterns.','Compare and predict relationships.','Construct explanations','Patterns')
lesson(p,'Trace matter and energy through the web','Model living/nonliving connections and energy availability.','MS-LS2-3','MS-LS2-2',[1,5],'CARP','One food-web diagram and energy-pyramid caption; about 120 words.',
 'Use a meadow to model Sun-to-producer energy and matter moving through organisms, air, water, soil and decomposers. Energy is transferred/dispersed rather than cycling like matter. Avoid a universal 10-percent rule.',
 ['Draw a bounded freshwater food web using verified organism cards.','Use distinct arrow styles for feeding/energy and matter transfers.','Add decomposers and nonliving reservoirs.','Build an energy pyramid explaining less energy available at higher levels without claiming disappearance.','Individually trace one matter path and one energy path, then revise an arrow.'],
 'Student ecosystem model with boundary, nonliving reservoirs, food web and energy pyramid.',
 'Arrows have meaning; matter cycles; energy enters/leaves; decomposers and heat transfer are accounted for.',
 'If energy loops to the Sun, trace one energy unit through the model and redraw; fresh check follows a different organism. Provide icons; extend by changing system boundaries.',
 'Prepare keyed card relationships and an accessible tactile/text model option; carry models into case analysis.',
 'Interactions and S1 conservation.','Develop a two-pathway ecosystem model.','Develop/use models','Energy and matter')
lesson(p,'Compare signs of ecosystem health','Evaluate multiple indicators in land and water ecosystems.','MS-LS2-1 MS-LS2-4','MS-LS2-3',[3,5,6],'CARP','Paired monitoring tables and brief biome cards; about 200 words.',
 'Model why desert precipitation should not be judged by rainforest expectations. Compare appropriate reference conditions, biotic diversity/population evidence and abiotic temperature/water/soil measures.',
 ['Compare forest and freshwater indicator data to appropriate baselines.','Use biome reference cards for tundra, taiga, desert, grassland, rainforest and marine settings to avoid one universal health threshold.','Explain one physical and one biological change affecting a population.','Evaluate an alternative cause and identify additional evidence needed.','Each learner writes a bounded health conclusion for both terrestrial and aquatic cases.'],
 'Paired individual health explanations supported by indicators and a competing-cause note.',
 'Use both biotic and abiotic patterns; comparisons suit the ecosystem; distinguish biodiversity from sheer abundance.',
 'If one high count is treated as proof of health, compare dominance versus varied species and recheck another case. Provide a baseline/changed table; extension considers sampling effort.',
 'Prepare small source-verified tables and biome cards; retain case conclusions for the invasive-species investigation.',
 'Graphs, system boundaries and interaction explanations.','Compare ecosystem indicators and argue from data.','Analyze data and argue from evidence','Stability and change')
lesson(p,'Investigate invasive carp evidence','Connect a specific Tennessee species to native-population effects.','MS-LS2-4','MS-LS2-1 MS-LS2-2',[3,4,7],'CARP','TWRA Bighead Carp selection and a dated empirical evidence table; about 200 words.',
 'Model tracing an ecological claim back to its evidence. Distinguish invasive from merely nonnative and separate competition evidence from an unsupported assertion that every decline has one cause.',
 ['Locate the Tennessee waterway and identify bighead carp and native competitors.','Read source statements and annotate a verified population/resource record.','Trace a plausible effect through the food web.','Compare a competing explanation such as changed water conditions.','Individually write claim, measured evidence, mechanism and limitation.'],
 'Source-linked individual invasive-species argument and revised food web.',
 'Name the species/place; use existing empirical evidence; explain competition and distinguish evidence strength from certainty.',
 'If evidence is only a quoted conclusion, locate the supporting observation and recheck another claim. Offer a source/evidence organizer; extend by evaluating sampling bias.',
 'Verify an empirical dataset/report supporting the case before material readiness; no fish collection or handling. Carry uncertainties to response design.',
 'Population evidence, food webs and alternate explanations.','Evaluate a named invasive-species case.','Argue from evidence','Cause and effect')
lesson(p,'Compare responses and ecosystem services','Evaluate two possible responses to invasive-species impacts.','MS-LS2-5 MS-ETS1-2','MS-LS2-4',[7,8],'CARP','Two management summaries and ecosystem-service cards; about 200 words.',
 'Model common comparison criteria: impact on native organisms, feasibility, unintended effects and monitoring. Use a non-carp example. Explain food, clean water, medicine potential, pollination, decomposition and climate-related services without claiming each is supplied by one species.',
 ['Compare two evidence-based carp-management approaches, such as targeted removal and movement barriers, using the same criteria.','Explain tradeoffs and uncertainty; distinguish mitigation from eradication.','Connect biodiversity changes to two human resources/services.','Draft a bounded response proposal with a monitoring indicator.','Each student explains why the rejected alternative may still have a useful feature.'],
 'Comparison table, response proposal and private biodiversity/service explanation.',
 'Evaluate both solutions fairly, cite evidence and identify an unintended effect; explain a causal service connection.',
 'If “remove every fish” is proposed, trace native food-web effects and revise; recheck another intervention. Extend by changing a constraint.',
 'Prepare source-checked management cards and limitations; bring response proposal to case revision.',
 'Carp evidence and ecosystem-health indicators.','Compare conservation solutions.','Evaluate solutions','Stability and change')
lesson(p,'Close the case with an individual argument','Revise the explanation using all the case evidence.','MS-LS2-4 MS-LS2-3','MS-LS2-5',[1,3,4,5,6,7,8],'CARP','Existing case file and short fresh evidence note.',
 'Show how a new observation can narrow a claim without erasing useful evidence. Model integrating one graph and one model rather than copying the entire packet.',
 ['Use a targeted opening clinic for unresolved data/model errors.','Assemble one concise case conclusion using existing annotations.','Revise the proposed response after feedback about a risk or missing indicator.','Individually explain an ecosystem model and apply it to a new resource change.','Mark evidence versus predictions and retain a question for the case conference.'],
 'Individual 150–250-word or equivalent explanation, model annotation and revised response.',
 'Reasoning links population change to evidence/mechanisms; revised response addresses a specific limitation; matter/energy remain distinct.',
 'If a conclusion overstates cause, add the alternative and a discriminating measurement, then recheck a new claim. Oral response may replace writing length while preserving reasoning.',
 'Prepare fresh evidence and feedback examples; identify individual gaps before the conference.',
 'Complete evidence file and response comparison.','Synthesize and revise a causal argument.','Argue from evidence','Cause and effect','workshop')
lesson(p,'Explain the case and transfer to a new ecosystem','Defend a response and interpret a different ecosystem case.','MS-LS2-1 MS-LS2-2 MS-LS2-5','MS-LS2-3 MS-LS2-4',[1,3,4,5,6,7,8],'CARP','One new land/aquatic case with short source note and graph.',
 'Model a concise case conference: claim, evidence, limitation, response. Explain that a new context requires checking its facts rather than copying the Tennessee conclusion.',
 ['Teams share case conclusions and answer an evidence question.','Each member explains one indicator, interaction or response tradeoff.','Individually interpret a new resource graph and predict an interaction.','Compare two responses for the new case and justify a choice.','Archive the case file; carry conservation criteria to S4.'],
 'Observed individual contribution, new data interpretation and response comparison.',
 'Transfer a scientific pattern with appropriate evidence; avoid assuming the same intervention suits every ecosystem.',
 'If the old solution is copied, identify a changed condition and re-evaluate; record an S4 opening recheck if needed. Extension asks what cannot be inferred.',
 'Assume six 5-minute team conferences; prepare teacher observation roster and accessible individual response options.',
 'Case argument and ecological comparison criteria.','Defend and transfer reasoning.','Communicate explanations','Patterns','presentation')

p=project(3,'Weather Route Control','S3_WEATHER_ROUTE_CONTROL','How can Earth-system models and weather evidence help us revise a route forecast?',
 'Build connected models of air, ocean and water movement; collect weather records and revise a route briefing when new observations arrive.',
 'One route briefing file with a route map, linked system diagrams, weather log, evidence-based forecast and revised recommendation. Short individual models/checks remain attachments, not extra polished reports.',
 ['Unequal heating, Earth’s rotation and geography shape circulation and regional climates.','Water follows multiple pathways driven by solar energy and gravity.','Weather forecasts use changing observations and uncertainty; climate explanations use longer evidence records.'],list(range(9,16)),[1,2],['WEATHER','OCEAN','WATER','CLIMATE'],
 ['W1: Latitude/globe diagram, warm/cool and fresh/salt density observations with provenance, regional-climate profiles; Pending Step 6.','W2: Accessible water-cycle map and sourced human/organism land-water-atmosphere comparison data; Pending Step 6.','W3: Radiation model, dated global-temperature/greenhouse/solar/volcanic graphs; Pending Step 6.','W4: Archived three-time-point weather maps for a bounded route, station log and new observation overlay; Pending Step 6. No travel decisions or real emergency forecasting.'])
lesson(p,'Model uneven heating and moving air','Build the first circulation model for the route file.','MS-ESS2-6','MS-PS3-3',[1,2,9],'WEATHER','Global winds selection and latitude diagram; about 180 words.',
 'Use a globe and light-spread diagram to compare energy per area by latitude. Trace warm less-dense air rising and cooler air replacing it. Explain convection as moving matter; a rising arrow alone is not a circulation loop.',
 ['Annotate an uneven-heating diagram with evidence from a light-spread model.','Draw a closed atmospheric circulation loop with warming/cooling locations.','Compare model predictions to a simple wind/temperature pattern.','Attach the model to a fictional route map and identify a question about likely climate.','Individually explain why “heat always rises” is an incomplete description.'],
 'Individual convection diagram with solar source, density changes and return flow.',
 'Connect uneven heating to moving air and energy transfer; identify what the model simplifies.',
 'If arrows show only upward movement, track replacement air and recheck a new convection situation. Provide labeled locations but leave arrows blank; extension distinguishes radiation from convection.',
 'Prepare accessible globe/diagram demonstration and route map. Leave rotation and full ocean reasoning for W1-G to avoid overload.',
 'S1 energy pathways; locate equator and poles.','Develop an atmospheric circulation component.','Develop/use models','Systems and system models')
lesson(p,'Connect ocean currents and Earth’s rotation','Use temperature and salinity evidence to extend the system model.','MS-ESS2-6','MS-PS3-4',[1,2,9,10],'OCEAN WEATHER','NOAA circulation diagram and short rotation caption; about 180 words.',
 'Model density comparisons with teacher-recorded fresh/salt and warm/cool water observations, varying one factor at a time. Add the effect of Earth’s rotation on broad circulation paths and continental boundaries; no Coriolis calculations.',
 ['Interpret temperature/salinity density observations and identify controls.','Draw surface/deep ocean movement and explain energy transport.','Use a globe/rotating-map representation to annotate deflection and continent constraints.','Compare the ocean and atmospheric models and connect them without claiming identical mechanisms.','Each student predicts a circulation change and supports it with evidence.'],
 'Linked ocean/atmosphere model and private salinity/rotation explanation.',
 'Explain density from temperature/salinity, solar energy input and rotation/land boundaries; observations support the claim.',
 'If salt is described as pulling water downward, compare equal-volume masses and density, then recheck a different pair. Provide a pre-labeled map; extension identifies a model limitation.',
 'Validate demonstration footage/data; do not mix several unobserved variable changes. Bring circulation model to regional-climate work.',
 'Convection loop and relative density.','Extend and use a circulation model.','Develop/use models','Systems and system models')
lesson(p,'Explain why regions have different climates','Use circulation and geographic features to explain regional patterns.','MS-ESS2-6','MS-ESS2-4',[9,10,11],'WEATHER OCEAN','Three concise regional profiles and a mountain cross-section; about 200 words.',
 'Model two locations at similar latitude but different ocean-current exposure. Add altitude, coast/interior and mountain lifting/rain-shadow reasoning. Distinguish a long-term climate pattern from today’s weather.',
 ['Compare regional temperature/precipitation profiles using axes and reference periods.','Trace atmospheric/ocean heat transfer on the route map.','Annotate a mountain rain-shadow diagram with rising/cooling/condensing and descending/drier air.','Explain how at least two geographic/circulation factors affect one route region.','Individually predict a contrasting region and name uncertainty.'],
 'Individual regional-climate explanation and revised system map.',
 'Use model mechanisms and data; include ocean and atmosphere connections and geographic variation without treating latitude as the only cause.',
 'If one rainy day is called climate, contrast daily and long-term records and recheck another statement. Offer paired profile frames; extension examines two plausible influences.',
 'Provide dated, comparable climate summaries; preserve annotations for the final briefing rather than a separate geography report.',
 'Atmosphere/ocean model, axes and location.','Use a model to explain regional patterns.','Develop/use models','Systems and system models')
lesson(p,'Follow water and explain landscape changes','Model water pathways and examine human and organism impacts.','MS-ESS2-4','MS-ESS3-3',[12,13],'WATER','USGS diagram and two small comparison datasets; about 150 new words.',
 'Model two paths from ocean to atmosphere to land and back, labeling state changes, Sun-driven processes and gravity. Use vegetation removal/regrowth evidence and organism effects such as transpiration/root stabilization; distinguish landform influence on water from changes organisms cause to land.',
 ['Trace multiple water pathways including groundwater and transpiration.','Compare infiltration/runoff/erosion evidence for vegetated and cleared sites.','Interpret an organism-impact case linking root or burrowing changes to land and a vegetation/transpiration record to atmospheric moisture.','Revise the route water model with a supported human and nonhuman effect.','Individually explain a fresh pathway and one evidence limit.'],
 'Individual water-cycle model plus two short data-backed impact explanations covering human and other-organism effects.',
 'Separate energy driver from gravity; conserve water through pathways; connect evidence to water, landform and atmosphere effects without overclaiming.',
 'If the cycle is a single fixed loop, give a groundwater starting point and recheck two return paths. If organism effects are omitted, trace plant-water-air transfers before a fresh check.',
 'Prepare validated short datasets; avoid reading a long article here. Carry unfinished data explanation into W3-I opening; retain a 35-minute model-work window.',
 'States of water, Sun/energy, regional climate.','Trace and revise a coupled water-system model.','Develop models and analyze data','Energy and matter','systems')
lesson(p,'Explain greenhouse warming','Model energy entering, leaving and interacting with greenhouse gases.','MS-ESS3-5','MS-ESS2-6',[1,2,14],'CLIMATE','Simplified NASA radiation graphic and about 180 words.',
 'Draw incoming sunlight, surface absorption and outgoing infrared radiation. Explain greenhouse gases absorbing/emitting infrared energy and habitability; avoid ozone-hole explanations or a sealed-jar analogy as proof of atmospheric radiation.',
 ['Repair a water-model issue in the opening clinic.','Build an Earth energy model with an explicit atmosphere boundary.','Compare natural greenhouse warming with an increase in greenhouse gases.','Use a supplied dated graph to frame a question about long-term warming evidence.','Individually explain the mechanism and why one cold day does not disprove a global trend.'],
 'Individual greenhouse model and an evidence-clarifying question for the climate investigation.',
 'Distinguish incoming/outgoing radiation, natural/enhanced effects and weather/climate timescales; question names evidence needed.',
 'If gases are said to create energy or block all sunlight, trace sources and infrared pathways; recheck a corrected model. Provide radiation labels; extend by asking about energy balance over time.',
 'Prepare accessible graphics and verified time-series labels; save broader attribution comparison for W4-I.',
 'Energy conservation and regional climate versus weather.','Construct a radiation model and ask a question.','Ask questions and develop models','Stability and change')
lesson(p,'Collect weather evidence for a forecast','Use changing observations to explain air-mass interactions.','MS-ESS2-5','MS-ESS2-6',[9,11,15],'WEATHER','Air masses/fronts selections plus three station/map snapshots; about 180 words.',
 'Model extracting temperature, pressure, humidity, wind and precipitation at a fixed station across times. Trace front movement and explain why a forecast states likelihood and uncertainty rather than certainty.',
 ['Collect observations from a source-labeled archived weather sequence in a shared log.','Compare the route’s stations and locate contrasting air masses/fronts.','Connect changes in the measurements to the passage of a front.','Draft a probable weather forecast and route recommendation.','Each student explains two observations and one uncertainty before the team combines ideas.'],
 'Individual data-log entries and an observation-based probabilistic forecast.',
 'Use multiple weather variables across time; link evidence to interacting air masses; distinguish measurement from forecast.',
 'If a symbol alone is treated as proof of rain, compare humidity/pressure/wind evidence and recheck a new snapshot. Provide a symbol key; extension considers forecast confidence.',
 'Select archived maps with timestamps/timezone, units and source; prepare final fresh overlay separately. No real-world travel or emergency advice.',
 'Air circulation, water processes and graph reading.','Collect and interpret a time sequence.','Plan investigations and collect data','Cause and effect')
lesson(p,'Question the evidence for climate change','Compare long-term evidence and finish the connected briefing.','MS-ESS3-5','MS-ESS2-6 MS-ESS2-4',[11,12,13,14],'CLIMATE','Dated temperature, greenhouse-gas, solar and volcanic evidence panels; about 150 words.',
 'Model a question that clarifies a timescale, measurement or proposed cause, rather than a yes/no opinion. Compare human greenhouse-gas forcing and natural factors; explain that several independent records support the dominant recent human contribution.',
 ['Use an opening clinic on the weakest system-model component.','Annotate a global-temperature trend and relevant human/natural factor records.','Write two answerable questions that would clarify evidence or distinguish explanations.','Use the packet to address one question and acknowledge a remaining limit.','Complete the route briefing’s system panels without turning climate attribution into a day-to-day forecast.'],
 'Individual evidence annotations, two precise questions and a source-based response; completed model attachments.',
 'Questions identify variables/timescales and clarify causal evidence; distinguish global climate change from local weather predictions.',
 'If questions only ask opinions, identify a measurable variable and rewrite; recheck a new evidence panel. Offer question stems without supplying the answer; extension compares timescales.',
 'Verify graph dates, baselines and source attribution; prepare short individual model prompts for unresolved water/greenhouse components.',
 'Greenhouse model and reading time-series graphs.','Ask and refine evidence questions.','Ask questions','Stability and change','workshop')
lesson(p,'Brief and revise the route forecast','Use a new observation to revise the forecast and explain mechanisms.','MS-ESS2-5 MS-ESS2-6','MS-ESS2-4 MS-ESS3-5',[9,10,11,12,13,14,15],'WEATHER','Final route file and held-back weather observation; no new article.',
 'Model a short briefing structure: conditions, evidence, probable development, recommendation, uncertainty. Demonstrate marking what changed rather than starting a second report.',
 ['Teams present the forecast with circulation and geographic evidence.','Each member explains an observation or system connection.','Release a new front/pressure snapshot; teams revise the same route file.','Individually justify a forecast revision and complete a targeted fresh model question.','Archive the weather log, models and unresolved needs for S4 environmental monitoring.'],
 'Individual revised forecast, targeted model response and teacher-recorded explanation; team briefing judged separately.',
 'New evidence changes or supports the recommendation for an explained reason; account for uncertainty and preserve causal model logic.',
 'If the team ignores contrary evidence, compare original/new measurements and request one warranted revision. Recheck individually rather than counting a spokesperson’s answer for all.',
 'Six teams of four is a pacing assumption; use 30 minutes for 5-minute briefings and short private checks afterward. Increase the observation plan if enrollment differs.',
 'Route file, weather data and connected Earth-system models.','Explain and revise a forecast.','Communicate explanations','Cause and effect','presentation')

p=project(4,'A Better Park: Report and Presentation','S4_A_BETTER_PARK','What change would make a neighborhood park better for people and the environment?',
 'Research one park problem, compare two improvements, and revise a scientific recommendation into a concise report used for a presentation.',
 'One six- to eight-slide illustrated report (or equivalent accessible document) and a four- to six-minute team presentation. Include the problem, evidence, options, recommendation, tradeoffs, monitoring and sources; each student explains individual reasoning. No simulation or separate long paper.',
 ['Resource use and human actions affect Earth systems and biodiversity.','A justified recommendation compares benefits, constraints and unintended effects.','Monitoring and evidence-based revision help evaluate whether an improvement works.'],list(range(16,20)),[1,2,3,4,5,6,7,8,11,12,13,14,20],['GREEN','OPTIONS','ENERGY','WATER','CLIMATE'],
 ['P1: Shared fictional park map/photos, measured case evidence with provenance and constraints; default problem is runoff and lost habitat along a path.','P2: Two improvement-source cards, local-feasibility notes, resource consumption/per-capita data and existing/developing energy technology cards; Pending Step 6.','P3: Report scaffold, source tracker, review criteria and descriptive examples; Pending Step 6.','P4: Fresh impact/monitoring prompt and individual oral/written assessment roster; Pending Step 6.'])
lesson(p,'Define a park problem worth changing','Identify the environmental problem and measurable success criteria.','MS-ESS3-3 MS-ETS1-1','MS-LS2-4',[3,6,12,13,16,18],'GREEN WATER','Park case and annotated map; about 200 words.',
 'Model a problem statement for a different site: observed issue, affected people/organisms, mechanism and measurable improvement. Distinguish an observation from an assumed cause and a preference from a constraint.',
 ['Inspect the shared park map, observations and a small resource-use table.','Choose one bounded issue; default is runoff and reduced habitat beside a path.','Trace possible water/soil/organism effects and define what needs investigation.','Write success criteria, constraints and a research question.','Each learner contributes an independent problem/evidence note before the team agrees.'],
 'Individual problem statement and evidence note; shared report outline with criteria.',
 'Problem is bounded and scientifically investigable; criteria measure impact, not decoration; include people and other organisms.',
 'If the goal is “make it nicer,” identify a measurable environmental change and recheck a different proposal. Offer a map glossary; extension identifies a conflicting stakeholder need.',
 'Prepare accessible map/data and choose verified source cases. Different topic choices must retain the same required learning through short in-class checks.',
 'S2 ecosystem health and S3 runoff mechanisms.','Define a problem and monitoring question.','Define problems','Cause and effect')
lesson(p,'Explain resource use with data','Separate population growth, individual consumption and environmental impact.','MS-ESS3-4','MS-ESS3-3',[16,18],'ENERGY WATER','Two dated population/per-person consumption tables and source notes; about 150 words.',
 'Use simple hypothetical practice values: 100 users at 2 L each versus 200 at 2 L; then 100 at 4 L. Label the examples invented, then model an argument from the source-verified dataset. Renewable does not mean unlimited or impact-free.',
 ['Interpret population and per-capita consumption separately.','Calculate small totals with units and annotate a supplied measured trend.','Connect the resource demand to a documented Earth-system effect.','Compare a resource-saving change and its possible tradeoff.','Each student writes an evidence-based argument; save one relevant chart for the report.'],
 'Individual argument addressing both population and per-person use, with source-linked evidence and a mechanism.',
 'Do not confuse totals and rates; distinguish renewable/nonrenewable resources and support the impact claim with evidence.',
 'If per-person use is mistaken for total, use equal groups to separate the variables then recheck new values. Provide calculator/table support; extension considers rebound in use.',
 'Prepare dated empirical dataset and separate clearly labeled arithmetic examples. Carry resource findings into options research.',
 'Read tables; multiply simple quantities; distinguish claim/evidence.','Interpret two resource-demand drivers.','Argue from evidence','Cause and effect')
lesson(p,'Compare energy technologies','Evaluate existing and developing energy options without a sales pitch.','MS-ESS3-3','MS-ETS1-2',[1,2,14,16,17,20],'ENERGY CLIMATE','Three bounded technology cards, about 250 words total.',
 'Trace source-to-electricity-to-use energy transformations. Compare an existing solar-PV lighting application, another renewable technology such as wind, and a documented developing technology/application. Compare reliability, storage/material needs and impacts using dated evidence; do not imply the electric grid is a single energy source.',
 ['Extract comparable facts from the technology cards.','Explain one thermal/energy principle from S1 and connect it to energy use or efficiency.','Compare benefits, limitations and a practical park need using common criteria.','Identify which claim is measured, predicted or still under development.','Individually justify an energy recommendation or explain why the park problem does not require new lighting.'],
 'Individual existing/developing technology comparison and source-quality note; use relevant evidence in the same report.',
 'Investigate more than one technology; distinguish current evidence from proposed performance; explain an energy mechanism and tradeoff.',
 'If renewable is treated as zero impact, trace materials/land/storage needs and recheck another option. Offer energy-flow icons; extension separates energy source from delivery system.',
 'Verify current developing-technology source before handout production; this component remains Unverified until a specific dated technology source is selected. No extra presentation is assigned.',
 'S1 transfer/conservation and resource demand.','Compare technology evidence.','Obtain/evaluate information','Energy and matter')
lesson(p,'Compare two improvements for wildlife and people','Evaluate biodiversity solutions using the same evidence criteria.','MS-LS2-5 MS-ETS1-2','MS-ESS3-3',[3,4,5,6,7,8,18,19],'GREEN OPTIONS','EPA option selections, habitat indicators and brief conservation cases; about 250 words.',
 'Compare a planted rain garden with a permeable-path/habitat-edge option on the default site. Use scientific, feasibility and social criteria; explain why local soils, maintenance and habitat context matter. Include short endangerment/extinction and invasive-species cases without claiming all apply to the fictional park.',
 ['Review the same criteria for both options.','Trace effects on resources, food-web relationships and at least two ecosystem services.','Evaluate relevant empirical evidence and local implementation limits.','Use a comparison table to choose a provisional improvement and identify a weakness.','Individually justify a biodiversity tradeoff and one way to improve the proposal.'],
 'Two-option evaluation and each learner’s biodiversity/service explanation and proposed improvement.',
 'Both options receive fair consideration; explanation connects habitat change to organisms/services; conservation/endangerment/extinction concepts are distinguished.',
 'If flower count is treated as biodiversity proof, consider native species/habitat interactions and a monitoring indicator; recheck another claim. Extension evaluates an unintended effect.',
 'Prepare local-condition evidence and short source-checked conservation cards. Keep evaluation tied to the same report, with individual component notes attached.',
 'S2 interactions, invasive-species reasoning and ecosystem services.','Evaluate and improve a biodiversity proposal.','Evaluate solutions','Stability and change')
lesson(p,'Draft the report and monitoring plan','Turn the recommendation into a testable, evidence-based proposal.','MS-ESS3-3 MS-ETS1-1','MS-LS2-5',[11,12,13,16,18,19],'GREEN WATER','Existing source notes plus one monitoring example; no new long reading.',
 'Model a six-panel report on a different problem: problem, mechanism/evidence, options, recommendation, monitoring/limits, sources. Specify baseline, indicator, method, frequency, comparison and a criterion for revising the recommendation.',
 ['Draft the report using existing maps, notes and comparison table.','Add an annotated visual explaining the science and a relevant data display.','Describe how implementation success could be monitored without inventing future results.','Include costs/maintenance as constraints and identify a possible harm.','Each student writes or records a private justification of the monitoring design.'],
 'Six- to eight-slide draft (or equivalent), individual monitoring method and a source trail.',
 'The recommendation follows evidence; monitoring can detect the intended impact and confounds; predictions are labeled and sources are traceable.',
 'If “check whether it worked” lacks a measure, choose an indicator/time/comparison and recheck with a changed condition. Offer a report frame; extension addresses seasonal variation.',
 'Prepare an accessible report template and different-topic example; bring draft and exact feedback question to W3-G.',
 'Evidence comparison and measurable criteria.','Design monitoring and draft a report.','Design solutions','Cause and effect')
lesson(p,'Review and strengthen the proposed change','Use critique to improve the science and biodiversity proposal.','MS-LS2-5 MS-ETS1-2','MS-ESS3-3',[8,16,18,19],'GREEN OPTIONS','Drafts, original sources and a concise review checklist.',
 'Model useful critique: name a claim, locate supporting evidence and ask about a constraint or unintended effect. Demonstrate a substantive revision, such as relocating a habitat feature, rather than changing colors.',
 ['Partners review the same criteria for alternatives and recommended change.','Check one source-to-claim connection and one monitoring limitation.','Revise the biodiversity strategy and report in response to evidence-based critique.','Rehearse each learner’s explanation without scripts replacing understanding.','Individually record before/after reasoning and what evidence prompted the change.'],
 'Revised report, individual revision note and teacher observation of evidence discussion.',
 'Revision changes the proposal or reasoning for a scientific reason; evaluate alternatives and preserve honest uncertainty.',
 'If feedback is only praise, give a claim/evidence/constraint prompt and recheck a new slide. Extension explains when the rejected option would become preferable.',
 'Allocate teacher conferences across six teams during report revision; bring only the unresolved component list to W4-I.',
 'Draft report and monitoring proposal.','Critique and revise a solution.','Argue from evidence','Stability and change')
lesson(p,'Finish the report and explain your own reasoning','Complete the shared product and check individual science learning.','MS-ESS3-3 MS-ESS3-4','MS-LS2-5 MS-ETS1-2',[16,17,18,19],'GREEN ENERGY','Own report plus short fresh resource/monitoring case.',
 'Show a clear evidence caption and a statement of a limit; use a different park problem. Revisit the weakest resource, technology or biodiversity component in a targeted clinic.',
 ['Finish the report without adding a separate long paper.','Audit visual labels, claims, source credits and predicted versus observed benefits.','Individually explain one resource/energy choice and one biodiversity effect.','Respond to a new population/consumption or monitoring case to demonstrate transfer.','Prepare one scientific question for reviewers and rehearse concise answers.'],
 'Final report, individual explanation and fresh resource/monitoring response.',
 'Scientific claims are accurate and sourced; individual reasoning addresses the required components beyond the team’s chosen topic.',
 'If polished slides conceal weak reasoning, use a brief oral different-case check and mark support accurately. Provide an accessible audio/text equivalent; extension challenges the monitoring comparison.',
 'Prepare the final response key and presentation roster; unresolved developing-technology evidence stays open until the specific resource is verified.',
 'Revised proposal and source trail.','Finalize and independently transfer reasoning.','Communicate explanations','Cause and effect','workshop')
lesson(p,'Present a change worth making','Present the report and answer evidence-based questions.','MS-ESS3-3 MS-LS2-5','MS-ESS3-4 MS-ETS1-2',[16,17,18,19],'GREEN OPTIONS','Final report and individual question slips; no added research.',
 'Model a clear recommendation with an evidence reference and honest limit. Explain that the audience is reviewing a proposal, not hearing invented implementation results.',
 ['Use a short final clinic for named gaps.','Each team gives a four- to six-minute presentation using the report itself.','Every student explains part of the science and answers an individual question.','Reviewers identify an evidence strength and a question about impact or feasibility.','Each learner submits a final note about one justified improvement and one unresolved uncertainty.'],
 'Presented report, individual oral/question evidence and a final revision/limit note.',
 'Explain the problem, compare alternatives fairly, justify the change and monitoring; assess scientific understanding separately from presentation polish.',
 'If an answer only repeats a slide, ask for the causal connection using a new example; record a targeted recheck. Allow equivalent live audio/text responses with the same individual criteria.',
 'Assume 24 students in six teams: 36 minutes for six 6-minute slots; collect individual evidence throughout the project. Larger enrollment needs a revised observation schedule before teaching.',
 'Completed report and independently explained recommendation.','Present and defend scientific reasoning.','Communicate information','Cause and effect','report')

# The developing-technology source was checked before publication; retain its date.
projects[3]['resources'].append('DEV')
energy_lesson=projects[3]['lessons'][2]
energy_lesson['resources'].append('DEV')
energy_lesson['model']=energy_lesson['model'].replace('a documented developing technology/application','perovskite-silicon tandem solar cells in DOE’s dated April 2024 research case')
energy_lesson['prep']='Prepare the DOE 2024 perovskite-silicon case alongside established silicon-PV and wind cards. Compare durability and scale limitations, not unverified current market claims; keep the student adaptation brief.'
projects[3]['lessons'][6]['prep']='Prepare the final response key and presentation roster; include a fresh existing-versus-developing technology comparison using the dated DOE case.'

clocks={
 'standard':[(10,'Retrieve prerequisites and read the assigned resource'),(20,'Explicit model and guided turn'),(35,'Project investigation/model/report work with individual annotations'),(15,'Independent evidence and targeted feedback'),(5,'Different-example recheck'),(5,'Save work and handoff')],
 'lab':[(10,'Retrieve controls; safety/setup check'),(10,'Model procedure and guided measurement'),(50,'Project construction/testing: build or modify 15; two 10-minute trials with reset/cleanup 15; annotate while waiting'),(15,'Independent interpretation and fresh recheck'),(5,'Archive measurements and next action')],
 'workshop':[(15,'Targeted clinic and guided recheck'),(35,'Individual project completion and revision'),(25,'Fresh independent application and selected component checks'),(10,'Feedback and different-example recheck'),(5,'Archive evidence/handoff')],
 'systems':[(10,'Retrieve pathways and inspect diagrams'),(20,'Model drivers and guide one impact-data example'),(35,'Project water-model construction and paired-data analysis'),(15,'Independent human/organism explanation'),(5,'Targeted correction/recheck'),(5,'Save unfinished component for named clinic')],
 'presentation':[(10,'Targeted clinic and preparation'),(35,'Project briefing/demonstrations and evidence questions'),(25,'Fresh individual application and revision'),(15,'Feedback and specific rechecks'),(5,'Archive individual and group evidence separately')],
 'report':[(10,'Targeted clinic and final preparation'),(36,'Project presentations: six teams, maximum six minutes each'),(24,'Individual question responses and reviewer-based revision notes'),(15,'Targeted feedback and fresh rechecks'),(5,'Archive final report and evidence')]
}
for p in projects:
 assert len(p['lessons'])==8
 for l in p['lessons']:
  l['clock_segments']=clocks[l['clock']]
  l['skills']=f"Teach / revisit: {l['focus']}\nPractice: {l['practice']}\nCheck: {l['check']}\nBuilds on: {l['prereq']}"
  l['link']=f"../scope-and-sequence/science-projects/{p['slug']}.md#{l['id'].lower()}"
  assert all(c in ngss for c in l['primary']+l['support'])
  assert sum(x[0] for x in l['clock_segments'])==90
  assert not set(l['primary'])&set(l['support'])
  assert set(l['tn'])<=set(p['home']+p['recur'])

for x in tn:
 num=int(x['forge'].split('.')[-1]);x['home']=next(p['id'] for p in projects if num in p['home'])
 x['routes']=[l['id'] for p in projects for l in p['lessons'] if num in l['tn']]
 x['status']='Covered in plan'
 x['action']='Produce the dated DOE perovskite-silicon comparison card and individual prompt in S4-W2-I/W4-I; source selected, materials pending.' if num==17 else 'Produce/check materials and collect individual evidence; current status describes planning only.'
for x in ngss.values():
 x['primary_routes']=[l['id'] for p in projects for l in p['lessons'] if x['id'] in l['primary']]
 x['support_routes']=[l['id'] for p in projects for l in p['lessons'] if x['id'] in l['support']]
 assert x['primary_routes']
full_ngss=set(re.findall(r'MS-(?:PS\d|LS\d|ESS\d|ETS\d)-\d+', (HERE/'ngss-source-extract.txt').read_text(encoding='utf-8')))
remaining=sorted(full_ngss-set(ngss))
data=dict(status=STATUS,date='2026-10-03',resources=[dict(zip(['id','title','url','selection','status'],x)) for x in resources],national=list(ngss.values()),tn=tn,projects=projects,remaining_ngss=remaining,scope='16 weeks; 32 × 90-minute blocks; 48 hours; one individual and one group block weekly; four supplied projects.',
 assumptions=['Planning class size: 24 students, six groups of four; confirm actual enrollment and observation capacity.','No required homework; essential reading, work, feedback and individual evidence occur in class.','Grade 5 reading/graph/measurement readiness is checked in project openings; support is budgeted, not assumed completed elsewhere.','Physical S1 construction and testing require accessible kits, supervision and functioning thermometers. A video-only route cannot certify construction/test evidence.','School-year baseline for Tennessee checks: 2027–28. Dates, holidays, grading policy, accreditor and schoolwide Grades 6–8 NGSS allocation remain to confirm.'],
 open_needs=[['S1 physical access','Confirm kits, supervision and accessible participation for each learner.','School/teacher','Construction/testing route cannot be called ready without actual access.'],['S2 empirical evidence','Produce and verify dated terrestrial/aquatic/invasive-species datasets; label practice data.','Material author','Empirical-argument claims depend on actual evidence selected.'],['S3 pacing and data','Trial W2-I/G plus W3–W4 teacher observation; verify weather/climate archives and graphic accessibility.','Teacher/material author','Planning clocks do not establish learner completion.'],['S4 technology adaptation','Adapt the selected DOE 2024 perovskite-silicon case and established-technology cards without overstating current readiness.','Material author','Teacher sources exist; student evidence cards are not yet produced.'],['All projects material production','Create student packets, examples, fresh assessments and scoring guidance from these specifications.','Material author','Plans are not classroom-ready materials.'],['Course calendar and school scope','Confirm enrollment, actual dates, remaining year and Grades 7–8 NGSS ownership; supplied set is a term sequence.','School','No full-year, full middle-school or accreditation claim.']])
(HERE/'science.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(f"Wrote {sum(len(p['lessons']) for p in projects)} lessons, {len(ngss)} NGSS routes, {len(tn)} Tennessee checks; {len(remaining)} other middle-school expectations remain outside this sequence.")
