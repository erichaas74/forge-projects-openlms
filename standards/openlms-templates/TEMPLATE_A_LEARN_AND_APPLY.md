# Template A — Learn & Apply

**Use for:** individual lessons that teach new content. In math: **W1-I, W2-I, W3-I** of every project.

**What students experience:** a short warm-up, a worked example they step through with built-in checks, their own project work, then a short check with fresh numbers. If the check shows a gap, a reteach page and second check open for them only.

Shared settings (H5P, quizzes, assignments, restrictions, naming) are in the [README](README.md#part-3--settings-used-by-every-template).

## Build steps

Create a subsection named `Template A — Learn & Apply`, then add these items in order.

| # | Slot | Activity name | Activity type | Fill from build guide | Settings | Completion |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | — | `[ID] Teacher notes` | Page, **hidden from students** | Skills, Teach and model, Prepare and hand off, Mathematical practice, 90-minute timeline, Standards | — | None |
| 1 | ① Launch | `[ID] ① Warm-up` | H5P → **Arithmetic Quiz** (whole-number facts) or **Question Set** (3–4 items) | Retrieval items named in *Prepare and hand off* of the **previous** lesson, plus the prerequisite in *Skills… Builds on* | Practice category; save state on | Receive a grade |
| 2 | ① Launch | `[ID] ① Today's brief` | Text and media area | *Focus and project connection*, rewritten as 2–3 student sentences | — | None |
| 3 | ② Teach | `[ID] ② Worked example` | H5P → **Interactive Book**: one page per modeling step, with a Fill in the Blanks or Drag the Words check on each page. *Alternative:* Interactive Video if you record the model. | *Teach and model*. Use the guide's model numbers, never the project's real answers. | Practice category; save state on | Receive a grade |
| 4 | ② Teach | `[ID] ② Resources` | Page or File | *Resources and reading* (cards, diagrams, reading). Link the Project Hub's Project data instead of copying it. | — | View |
| 5 | ③ Work | `[ID] ③ Project work` | **Assignment**, individual | *Activity steps* as a numbered list; tell students which project file or table to update | Individual evidence category; Online text + File; grading = **Checklist** from the work-related parts of *How the work is judged* | Make a submission |
| 6 | ④ Check | `[ID] ④ Check` | **Quiz**: auto-graded items only (calculated, numerical, Cloze) | *Individual work to collect* (the number items) and *How the work is judged* (answers) | Individual evidence; 1 attempt; deferred feedback; link **Primary** competencies | Receive a grade |
| 6b | ④ Check | `[ID] ④ Explain` | **Quiz** with Essay question(s), attachments allowed | The explanation and any "show your algorithm" work from *Individual work to collect*; marking guide from *How the work is judged* | Individual evidence; link **Primary** competencies | Make a submission |
| 7 | Stuck | `[ID] If you're stuck: [skill]` | Page, restricted (see below) | *If students struggle*: the signal, the model to redo, the hint | Display: hidden entirely unless the condition is met | View |
| 8 | Stuck | `[ID] Recheck` | Quiz (1–3 calculated items), same restriction | The recheck example named in *If students struggle* | Individual evidence; 1 attempt | Receive a grade |
| 9 | ⑤ Wrap | `[ID] ⑤ Carry forward` | Text and media area | *Prepare and hand off*: what to save and what comes next | — | None |

### Stuck route
Restrict items 7 and 8 with **Grade → `[ID] ④ Check` → must be < 70%** AND **Activity completion → `[ID] ④ Check` → complete**. Or use the PLD group rule from the README. If the recheck is still low, the guide's *Prepare and hand off* names the next lesson's support window; the teacher picks it up there.

### Calculated-question pattern for the Check
- One question per number task in *Individual work to collect*.
- Wildcards replace every number; the formula reproduces the guide's answer for the guide's values.
- Check that the guide's own example values appear as one dataset item, so the teacher's key matches.
- Tolerance: nominal 0.005 for money; 0 for whole-number answers.

## Worked example: M1-W1-I — Read the kit and price the quantities

| # | Item | What goes in it (from `grade-6/math/project-1/BUILD_GUIDE.md`) |
| --- | --- | --- |
| 1 | ① Warm-up | Arithmetic Quiz on multiplication facts (prerequisite: multiplication, fractions, money). |
| 2 | ① Today's brief | "Today you'll build one supply kit with counters, work out what 12 kits need, and find which supplier's blue clips cost less each." |
| 3 | ② Worked example | Interactive Book: page 1, six-kit table (12 blue, 18 gold, 1.5 m ribbon); page 2, blue:gold = 2:3 versus blue/all = 2/5 (Drag the Words: "ratio" / "fraction"); page 3, $2.40 ÷ 12 = $0.20 versus $1.80 ÷ 10 = $0.18 (Fill in the Blanks); page 4, 936 ÷ 24 = 39 by partial groups, then the standard algorithm. |
| 4 | ② Resources | Link to the Project Hub kit brief and initial supplier cards; note "read the kit recipe and 6 price rows". |
| 5 | ③ Project work | 1. Build one kit with counters and explain both comparisons. 2. Make the 12-kit table (24 blue, 36 gold, 3 m ribbon). 3. Find and label both blue unit prices; explain why the cheaper clip may not mean the cheapest order. 4. Add one purchasing question. Checklist: table complete with units; both unit prices labeled; explanation present. |
| 6 | ④ Check | Q1 (Cloze, see note below): 3 red and 2 green counters → red:green and red/all. Q2 (calculated): *"{n} clips cost ${p}"* → `{p}/{n}`; guide values 8 and 2.00 give $0.25. Q3 (calculated): *"Show {={d}*{q}} ÷ {d}"* → `{q}`; guide values 24 and 36 give 864 ÷ 24 = 36. Link 6.RP.A.1, 6.RP.A.2. |
| 6b | ④ Explain | Essay: "Explain the difference between your ratio and your fraction." Essay with attachment: photo of 864 ÷ 24 by the standard algorithm (the guide judges the place-value steps, not just 36). |
| 7 | If you're stuck: ratios | "Circle all 5 counters and label the two groups. 2:3 compares the groups; 2/5 compares blue to all." Plus "rebuild tens and ones" for division. |
| 8 | Recheck | 4 blue / 1 gold → 4:1 and 4/5; 672 ÷ 21 = 32. |
| 9 | ⑤ Carry forward | "Save your 12-kit table — your team uses it next lesson." |

Q1 needs ratio notation, which calculated questions can't mark. Use **Embedded answers (Cloze)** with short-answer blanks (`3:2` and `3/5`) for the guide's values, and add two or three more Cloze versions with other counts as random variants.

## Before students see it
- [ ] Every `[placeholder]` replaced; activity names start with the lesson ID.
- [ ] H5P items in the Practice category; Work and Check in Individual evidence.
- [ ] Check quiz: guide's example values give the guide's answers; 5 random datasets checked by hand.
- [ ] Stuck route tested with a test student scoring below and above the threshold.
- [ ] Competencies linked on the Check (Primary) and Work (Supporting).
- [ ] Math displays correctly in H5P and the quiz.
- [ ] Brickfield accessibility check run; Drag the Words has a keyboard route.
