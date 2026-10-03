# Open LMS lesson templates

Build sheets for turning each project lesson's build guide into an Open LMS lesson. Build each template **once** in a template course, then copy it into real courses and fill it from the lesson's build guide.

Written for the Farm and Forge Open LMS site (Moodle 5.x, Snap theme, core H5P with framework v1.28, Personalized Learning Designer enabled, Database activity disabled). Menu names can differ slightly in Snap; when a step doesn't match what you see, use the activity's settings page and look for the named setting.

## The five templates

| Template | Use for | Math lessons | Build sheet |
| --- | --- | --- | --- |
| **A. Learn & Apply** | Individual lessons that teach new content | W1-I, W2-I, W3-I | [Template A](TEMPLATE_A_LEARN_AND_APPLY.md) |
| **B. Team Build** | Group lessons that build the team product | W1-G, W2-G | [Template B](TEMPLATE_B_TEAM_BUILD.md) |
| **C. Curveball** | Conditions change and teams revise | W3-G | [Template C](TEMPLATE_C_CURVEBALL.md) |
| **D. Workshop & Defend** | Individual catch-up and final write-up | W4-I | [Template D](TEMPLATE_D_WORKSHOP_AND_DEFEND.md) |
| **E. Showcase** | Final exchange, hearing or test | W4-G | [Template E](TEMPLATE_E_SHOWCASE.md) |

Every template has the same five slots, matching the 90-minute timeline in the build guides:

| Slot | Minutes | Purpose |
| --- | --- | --- |
| ① Launch | 0–10 | Retrieval warm-up and the day's brief |
| ② Teach | 10–30 | Model and guided practice |
| ③ Work | 30–70 | Project work |
| ④ Check | 70–85 | Individual evidence and a recheck on a different example |
| ⑤ Wrap | 85–90 | Save work and set up the next lesson |

Plus two support items in every template: a hidden **Teacher notes** page and an **If you're stuck** route that opens only for students who need it.

## Rules every template follows

1. **Graded individual evidence lives in Moodle Quiz or Assignment.** H5P is for practice and engagement; its grades go in the zero-weight Practice category.
2. **Individual and team work are graded separately.** Team products never stand in for a student's own evidence.
3. **Fresh numbers for checks.** Use calculated questions so each student gets a different example, as the guides' "recheck on a different example" rule requires.
4. **No invented grading policy.** Rubrics use descriptive levels (Secure / Developing / Not yet evidenced), not point cutoffs, unless the school supplies a policy.
5. **One H5P item per slot at most.** Keeps lessons focused.

## Part 1 — Set up the template course (once)

Use the sandbox course (`course/view.php?id=11`) or a new course named **Lesson Templates**.

1. **Course settings → Course format:** Custom sections. Set **Course layout** to show all sections on one page.
2. **Completion tracking:** Course settings → Completion tracking → **Enable completion tracking: Yes**.
3. **Sections:** create one section named **Templates**. Inside it you will build five subsections, one per template (`Template A — Learn & Apply`, and so on).
4. **Groups (for testing B, C and E):** Participants → Groups → create *Team 1*, *Team 2*; create a grouping **Teams** containing them. Create one more group **Needs support** (used by the stuck routes). Enrol two test students and put them in different teams.
5. **Gradebook categories:** Grades → Gradebook setup → add three categories:
   - **Individual evidence** — weight as the school decides.
   - **Team product** — weight as the school decides.
   - **Practice** — weight **0** (or *Exclude from total*). All H5P activities go here.
6. **Competencies (optional in the template course, required in real courses):** see Part 4.

## Part 2 — Project Hub (one per project, top of each project section)

Not part of the five lesson templates; build it once per project in the real course.

| Order | Item | Activity type | Fill from build guide | Key settings |
| --- | --- | --- | --- | --- |
| 1 | **Project launch** | H5P activity → **Course Presentation** (create it in the Content bank first) | *Essential question*, *What students do*, *Final product* | Practice category; completion = viewed |
| 2 | **Project data** | H5P → **Information Wall** (searchable cards) or **Accordion** | *Project data* — one card per supplier, site, dataset or rule | Practice category; no grade |
| 3 | **Practice map** (optional) | H5P → **Game Map** with short practice exercises per stage | Practice items from the eight lessons | Practice category; never required |
| 4 | **Team product file** | **Wiki** (Group mode: Separate groups, Grouping: Teams, Wiki mode: Collaborative) *or* **Assignment** with group submission | *Final product* | No grade on the wiki itself; grading happens on item 5 |
| 5 | **Final product** | **Assignment**, Group submission = Yes, Grouping = Teams, Grading method = **Rubric** | *Final product* and *What good work shows* → rubric rows | Team product category |

The Database activity would make a better team ledger but is disabled on this site; the wiki works until an admin enables it.

## Part 3 — Settings used by every template

### H5P activities
- Create the H5P content in **Content bank** (course → More → Content bank → Add), then add an **H5P** activity that points at it. Content bank items can be reused across lessons.
- **Grade:** grade category = Practice. **Attempts options:** *Enable attempt tracking* = Yes, *Grading method* = Highest. Turn on **save state** (*Enable saved state*) so students can leave and resume.
- **Completion:** *Receive a grade* for scored types; *View* for presentations.
- Test math once: put a fraction and an exponent (for example `\(\frac{3}{4}\)` and `\(2^3\)`) in an H5P text field and confirm MathJax displays it.

### Quizzes (Check slot)
- **Grade category:** Individual evidence. **Attempts:** 1 for the check; the recheck quiz in the stuck route gets its own attempt.
- **Question behaviour:** *Deferred feedback* for checks; *Interactive with multiple tries* for practice.
- **Review options:** show marks and feedback after the quiz closes, so students see their result before the next lesson.
- **Calculated questions:** use wildcards for every number that should change, for example *"{n} clips cost ${p}. What is the price per clip?"* with answer formula `{p}/{n}`. Show computed values in the question text with `{={d}*{q}}`. Generate at least 20 dataset items and check several by hand before use.
- **Explanation items:** add one **Essay** question for the "explain why" part. It is manually graded, so set a marking guide in the feedback.

### Assignments
- **Submission types:** Online text (default) and File submissions (for photos of paper work).
- **Grading method:** Rubric or **Checklist** (installed) built from *How the work is judged*. Use **Marking guide** where criteria are one or two sentences.
- **Group lessons:** individual evidence is always a *separate* assignment with Group submission = No.
- **Completion:** *Make a submission*.

### Restrict access for the "If you're stuck" route
Two options; pick one per course and use it everywhere.
- **Simple (built into Moodle):** the reteach page and recheck quiz are restricted by **Grade → [Check quiz] → must be < 70%** *and* **Activity completion → [Check quiz] → must be complete**. Set *Display: hidden entirely* so other students don't see it. 70% is a routing threshold for support, not a grading cutoff.
- **Personalized Learning Designer (PLD):** a rule *When [Check quiz] is graded and grade < 70%* → action *Add user to group "Needs support: [lesson ID]"* and *Send notification*. Restrict the reteach items by that group. PLD keeps a record of who was routed, which helps the next lesson's opening.

### Teacher notes (in every template)
A **Page** named `Teacher notes — [lesson ID]`, set to **Hide from students**. Paste in: *Skills taught and checked*, *Teach and model*, *Prepare and hand off*, *Mathematical practice*, the *90-minute timeline* table, and *Standards*. Teachers see the whole plan inside the lesson; students never do.

### Naming
Name every activity `[lesson ID] [slot] [what it is]`, for example `M1-W1-I ④ Check: ratios and unit price`. Gradebook columns then sort by lesson and slot.

## Part 4 — Standards as competencies (real courses)

1. Site admin → Competencies → **Import competency framework** from CSV. One framework per subject and grade (for example *Grade 6 Mathematics*). Use each build guide's **What each standard requires** table: code as the ID number, plain-language requirement as the description.
2. Course → More → **Competencies** → add the competencies for that course.
3. On each **Check** activity, link the lesson's **Primary** standards (from *Standards*). On the **Work** activity, link the **Supporting** standards. Set *Upon activity completion* = **Attach evidence**, so ratings come from teacher judgment, not completion alone.
4. Teachers rate competencies while grading in the assignment grader or Open Grader.

## Part 5 — Copy a template into a real course

1. In the real course, open the project section. More → **Import** → choose the template course.
2. Select only the subsection for the template you need (and its activities). Finish the import.
3. Move the imported subsection into the right project section and rename it `[lesson ID] · Week N · Individual/Group — [lesson title]`.
4. Open the lesson's `BUILD_GUIDE.md` and fill each slot using that template's **Fill from build guide** column. Replace every `[placeholder]`.
5. Re-point restrictions: imported restrictions may still reference the template's quiz. Open each restricted item and select the new lesson's Check quiz.
6. Run the template's **Before students see it** checklist.

The first import is a good moment to confirm how your site handles subsections on import; if a subsection doesn't come across with its activities, import the activities and create the subsection by hand, then drag them in.

## Field map: build guide → lesson slots

| Build guide field | Where it goes |
| --- | --- |
| Focus and project connection | Subsection description, rewritten for students as "Today you will…" |
| Skills taught and checked | Teacher notes; also the competency links |
| Resources and reading | ② Teach (Page, File or URL); project data comes from the Project Hub |
| Teach and model | ② Teach H5P content; full text in Teacher notes |
| Activity steps | ③ Work instructions, as a numbered list |
| Individual work to collect | ④ Check quiz or assignment |
| How the work is judged | Quiz answer key, or the rubric / checklist / marking guide |
| If students struggle | Stuck route: reteach page and recheck quiz |
| Prepare and hand off | Teacher notes; the handoff line also goes in ⑤ Wrap |
| Mathematical practice | Teacher notes; optionally a rubric row |
| 90-minute timeline | Teacher notes |
| Standards | Competency links (Primary on Check, Supporting on Work) |
