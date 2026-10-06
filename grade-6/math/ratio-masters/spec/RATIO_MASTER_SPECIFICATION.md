# Ratio Master Specification — Grade 6

Version 1.0 • 6 October 2026

## Architecture

One structured math record selects a teaching master, a practice pattern and a visual skin. The teaching master is rendered to HTML/CSS/SVG at BUILD TIME; the browser does not read JSON or compute new values. H5P practice uses a real, installed content type. The instructional sequence is SEE → TRY → SEE → TRY → APPLY.

Shared design applies to artwork, labels, quantity colors, writing and spacing where controllable. H5P native controls and host styling remain governed by the installed platform.

## Concept catalog

| Concept ID | Concept | Teaching master | Practice pattern | Concrete H5P starting point |
|---|---|---|---|---|
| RAT-01 | Identify/write A:B | V01 Object Groups | H02 Enter | Fill in the Blanks |
| RAT-02 | Part-to-part / part-to-whole | V01 Highlight Groups variant | H01 Select | Multiple Choice |
| RAT-03 | Equivalent ratios | V02 Group Multiplier | H02 Enter | Fill in the Blanks |
| RAT-04 | Missing values | V03 Scale Machine | H02 Enter | Fill in the Blanks |
| RAT-05 | Ratio tables | V04 Ratio Table | H02 Enter | Fill in the Blanks; retain table as adjacent visual |
| RAT-06 | Double number lines | V05 Number-Line Jumps | H04 Drag | Drag and Drop; enter-value fallback |
| RAT-07 | Unit rates | V06 Equal Distributor | H02 Enter | Fill in the Blanks |
| RAT-08 | Compare ratios/rates | V07 Comparator | H01 Select | Multiple Choice |
| RAT-09 | Mixtures/recipes | V08 Mixture Container | H04 Drag | Drag and Drop with fixed tokens; entry fallback |
| RAT-10 | Plot equivalent-ratio pairs | V09 Table to Graph | H01 Select | Multiple Choice using a graph stimulus |

RAT-10 is Grade 6 coordinate representation of equivalent ratios. Formal proportional-relationship analysis may be reserved for a later-grade extension. No standard graph editor is assumed.

## Teaching masters

| ID | Required math-specific fields | Optional fields | Sequence | Limits / fallback |
|---|---|---|---|---|
| V01 | values A/B, ordered labels, ratioKind | highlightTarget, showNumbers, showNotation | Identify/count groups; highlight either second part or whole; reveal ordered ratio | Discrete counts only; group large quantities |
| V02 | baseRatio, multiplier, labels | showScaleEquations, revealTiming | One complete group; repeat same group; show totals and equal scale | Positive integer repetitions; division uses V03 |
| V03 | baseRatio, operation, factor | objectInset, equationLabels | Both quantities enter same operation; both outputs appear | Validate exact outputs; avoid fractional discrete objects |
| V04 | baseRatio, complete ordered rows | highlightedRow, scaleArrows | Highlight a row; show same factor for both columns; reveal next row | Teaching table is complete; unanswered practice is separate |
| V05 | paired ordered ticks, labels, units | jumpCount, highlightedPair | Synchronized jumps; vertically aligned corresponding values | Proportional numeric spacing; wrap to a legible static model if necessary |
| V06 | total, groupCount, labels, units | distributionOrder, continuousModel | Distribute equally; focus on one group; show amount per one | Integer distribution for discrete objects; use bars for continuous amounts |
| V07 | two ordered ratio/rate pairs, comparisonBasis, units | commonReference, percentBars | Show both relationships; normalize to same denominator or unit; compare | Specify part/whole vs part/part; keep comparison direction explicit |
| V08 | baseRatio, multiplier, ingredient labels, units | containerShape, segmentedLayers | Fill complete recipe sets; show composition and totals | Tokens or bands must encode quantity, not arbitrary decoration |
| V09 | ordered points, axis labels/units, axis min/max/ticks | complete table, highlightOrder | Highlight row; highlight matching coordinate; repeat | Origin and uniform axis scales; no arbitrary rescaling |

Every master also needs an ID, prompt/statement, skin, scaffold level and accessible summary. Document max counts and number of groups actually tested; do not claim unbounded support.

## H5P practice patterns

| ID | Authoring behavior | Native starting point | Required answer data | Important constraint |
|---|---|---|---|---|
| H01 | Select a ratio/model/rate | Multiple Choice | options, correct IDs, distractor rationales | Image choices depend on enabled types; use supported stimulus/option format |
| H02 | Enter missing number/text | Fill in the Blanks | marked text, accepted answer strings | Text matching; no assumed numeric tolerance |
| H03 | Match representations | Drag and Drop or Drag the Words | targets, tokens, correct mapping | Content-type-specific matching, not a universal native Match type |
| H04 | Drag/build fixed model | Drag and Drop | background, fixed tokens, zones, mapping | Not a dynamic unlimited add/remove builder |
| H05 | Guided multiple steps | Question Set / Column / Course Presentation | ordered child questions and answers | Container and child support verified locally; no assumed gating |

For every practice blueprint include editor fields, asset dimensions, answer key, misconception feedback, supported retry options, accessible alternative and LMS reporting test. Use a selection or entry alternative if dragging is inaccessible in the deployed version.

An H5P blueprint is not a `.h5p` file. For production, author and export a working seed package from the installed version; preserve its library identifiers, metadata, dependencies, content structure and asset references. Automated variants must use that verified structure, not invented package fields.

## Data contract

Canonical examples are in `RATIO_EXAMPLE_PROBLEMS.json`. CSV contains the same values with lists serialized as JSON in cells.

Required common fields:
- `id`, `conceptId`, `grade`, `skill`, `visualTemplate`, `practiceTemplate`, `h5pType`.
- `ratioA`, `ratioB`: positive numbers describing the ordered base relationship; not necessarily reduced.
- `labelA`, `labelB`, `unitA`, `unitB`: explicit identities and units.
- `quantityA`, `quantityB`: displayed/known amounts; `null` for an unknown.
- `ratioKind`: `part_to_part`, `part_to_whole` or `rate`.
- `prompt`: student practice question; teaching uses a separate complete example.
- `answer`: number, string or option ID with documented meaning.
- `acceptedAnswers`: explicit strings for entry, or correct option IDs for selection.
- `skin`, `difficulty`, `scaffold`, `hints`, `correctFeedback`, `incorrectFeedback`.
- `templateData`: template-specific rows, ticks, competing rate or graph points.
- `teachingExample`: a complete worked example with its own values, allowing practice to use different values.

`difficulty` 1–4 indicates cognitive/numeric challenge; `scaffold` 0–3 indicates support. They are independent. Higher difficulty does not automatically remove support.

Keep teacher answers in authoring data, never in visible teaching markup accidentally. H5P client-side answers are not secure enough for high-stakes testing. Teaching examples can reveal their own outcomes; use a different value set for practice when revealing the exact practice answer would defeat the task.

## Mathematical checks

For equivalent ratios, require `quantityA / ratioA = quantityB / ratioB`. If A is known and B is unknown, `B = A × ratioB / ratioA`. Validate before rendering. Do not compare raw counts when the reference quantities differ.

For part-to-whole, explicitly define the second quantity as the total. Three blue and two yellow gives blue:yellow = 3:2, but blue:all = 3:5. Do not automatically reuse a part-to-part base ratio for a whole question.

For rates, the unit for B/A must be shown. Six notebooks cost $18: 18/6 = $3 per notebook. A comparator must define whether larger or smaller is desirable.

For graph points, consistently use x = A and y = B unless the data explicitly defines another order. All plotted pairs must satisfy the declared relationship.

## Visual skins

Initial choices: beads, blocks, sports, animals, food, recipe, paint, space, robots, nature, money, school.

Skins provide object markup/SVG, colors, outline and label conventions. Reuse math logic and layout. Test beads with center holes and white outlines; test one block variant before freezing V02. Do not rely on color alone.

## Accessibility and animation

- Semantic headings, readable system fonts and visible focus where controls exist.
- Text description of each visual relationship; meaningful SVG title/description where supported.
- Quantity identity encoded by label and/or shape as well as color.
- Short animation ending on a complete stable final state.
- Reduced-motion mode immediately displays complete static explanation.
- CSS scoped beneath `.ratio-master`; no global resets.
- Mouse, touch and keyboard checks for deployed H5P controls.
- No essential data hidden behind hover.
- No horizontal page scrolling at 360, 768 and 1280 px widths; group/tick legibility takes precedence over squeezing a diagram.

## Moodle/Open LMS validation

Record host version, H5P versions/types and user permissions. Test whether the chosen editor/delivery path retains CSS, SVG and semantic controls. If filtering strips them, use an approved stylesheet/file delivery route or a static SVG/PNG teaching fallback. Do not recommend disabling filtering site-wide.

Use a properly configured H5P activity when grades/attempt reporting are required. Check a student attempt, gradebook result, completion settings, retry and re-entry in the real sandbox. A visual embedded in a Book is not evidence of grade reporting. Do not assume custom HTML/CSS can be inserted into arbitrary H5P text fields.

## Acceptance and freeze checklist

1. One short prompt; clear quantity order; mathematical model dominates.
2. All counts, ratios, values, units and graph scales verified.
3. Example A and Example B use the same structure.
4. Alternate skin changes artwork only.
5. Animation explains the concept and stops; full static/reduced-motion version exists.
6. Responsive preview checked at the specified widths; no tiny unreadable objects.
7. Required interactions work with supported mouse, touch and keyboard behavior.
8. H5P correct, wrong and retry states tested; unsupported enhancements identified.
9. Actual sandbox delivery checked before approving production.
10. Approved markup/styles/assets/version saved; tracker advanced to Frozen only after approval.

Suggested status progression: Not started → Prototype → Review → Approved → Sandbox verified → Frozen. Record blockers and platform test results separately from visual approval.

## Production handoff to Codex

Preserve the frozen master's appearance and structure. Substitute validated data at build time. Change only documented parameters. Generate two variants for inspection before batching. Do not redesign, invent H5P libraries, add custom script to teaching components or claim LMS results without a student-role reporting test. Ask for missing platform information when it blocks packaging; continue independent visual work meanwhile.

## Official references

Checked 6 October 2026. Host configuration remains a local verification step.

- Moodle H5P activity: https://docs.moodle.org/en/H5P_activity — activity setup, grades and attempts depend on activity/teacher settings.
- H5P Fill in the Blanks: https://h5p.org/tutorial-fill-in-the-blanks — answer markup, alternative text answers and retry setting.
- H5P Drag and Drop: https://h5p.org/drag-and-drop — text/image draggables and drop zones.
