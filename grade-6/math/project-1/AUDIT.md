# Grade 6 Math – M1 Supply Exchange: Audit

Audited October 4, 2026, against the [M1 teacher plan](../../../standards/scope-and-sequence/math-projects/M1_SUPPLY_EXCHANGE.md), the generated [build guide](BUILD_GUIDE.md), the [Open LMS templates](../../../standards/openlms-templates/README.md) and the official Tennessee Grade 6 text ([local PDF](../../../standards/reference-standards/TN_Math_2021_K-12.pdf) pp. 64–69).

**Result:** The plan's numbers are correct and all eight standards have a teach, practice and individual-check route. Before building, settle one project-rule question (finding P2) and fix the four Moodle mechanics marked **Must fix**. No student materials exist yet; the project is not classroom-ready.

The Open LMS build for all eight lessons is in [OPENLMS_COURSE_BUILD.md](OPENLMS_COURSE_BUILD.md). It already applies the Moodle fixes below and marks where it waits on a plan decision.

## What was checked

- Every worked example, check item, recheck and answer key in the eight lessons (about 70 calculations), solved independently.
- Every purchasing scenario, by brute force over all whole-pack combinations: the 12-kit order, the 18-kit order, the Week 3 stock limit, the final offers, and the final offers with the stock limit.
- Each primary standard against the official TN wording, part by part.
- The build guide against its generator (`build_math_guides.py` reproduces it exactly; no drift).
- The five Open LMS template build sheets against how Moodle 5.x quiz, forum, workshop and restriction settings actually behave.

## Verified purchasing keys

All cases stay under the $24 budget, and stock (10 of each) only binds after the change.

| Case | Need | Cheapest, mixing suppliers within an item | Cheapest, one supplier per item |
| --- | --- | --- | --- |
| 12 kits, initial offers | 24 blue, 36 gold, 3 m | $13.50 (2 A blue, 2 A gold, 1 A spool) | $13.50 (same) |
| 18 kits, initial offers | 36 blue, 54 gold, 4.5 m | $20.60 (blue 3 A *or* 4 B = $7.20; 3 A gold $10.80; 1 A + 1 B spool $2.60) | $21.00 (ribbon 2 A spools $3.00) |
| 18 kits, A gold limited to 2 packs | same | $21.20 (gold 4 B $11.40) | $21.60 (matches the W3-G audit sum) |
| 18 kits, final offers | same | $20.51 (4 B blue $7.60; 3 A gold $10.26; 1 A + 1 B spool $2.65) | $20.86 (ribbon 3 B spools $3.00) |
| 18 kits, final offers, A gold limited | same | $22.25 (gold 4 B $12.00) | $22.60 |

The guide's all-A final order of $21.48 is correct and feasible.

Two useful teaching moments the plan doesn't mention: for 18 kits, blue costs exactly $7.20 from either supplier, even though B is cheaper per clip ($0.18 vs $0.20). Gold is cheaper per clip from B ($0.19 vs $0.20) but cheaper as a whole order from A ($10.80 vs $11.40).

## Findings: plan content

Severity: **Decide** = a choice only the curriculum owner can make; **Should fix** = a real gap or error; **Note** = low impact.

| # | Severity | Where | Finding | Recommended fix |
| --- | --- | --- | --- | --- |
| P1 | Should fix | M1-W3-G individual audit | `11.40 ÷ 15 = 0.76` has no meaning in the project ($11.40 buys 4 packs = 60 clips, and 15 is the pack size). It is also the only decimal-division item in that audit, and its divisor is a whole number. | Use `11.40 ÷ 2.85 = 4` (packs bought; decimal divisor) or `11.40 ÷ 60 = 0.19` (price per clip). |
| P2 | Decide | Project data | The brief says "split suppliers if useful" only at Week 3, so it's unclear whether teams may mix suppliers *within one item* in Weeks 1–2. The answer changes the 18-kit key ($20.60 vs $21.00). The W3-G audit sum ($21.60) assumes one supplier per item, but the W3-G model mixes gold (2 A + 2 B). | State the rule in the brief. Recommended: mixing is allowed from the start, because it is a valid purchasing strategy and the old scope plan said "suppliers may be combined". |
| P3 | Should fix | 6.EE.A.1 | The standard says *write* and evaluate, but every check item only evaluates. All powers use exponent 2 or 3. | Add one write item to M1-W3-I (for example, `5 × 5 × 5 × 5` as a power). Include exponent 1. Decide on exponent 0: "whole-number exponents" technically includes it, and the earlier plan wanted it. |
| P4 | Should fix | 6.RP.A.2 | The requirements table lists a "nonzero divisor" component, but no lesson teaches or checks it. | Add one item to M1-W1-I: why "price per 0 packs" has no meaning. |
| P5 | Should fix | 6.RP.A.3d | TN adds "manipulate and transform units appropriately when multiplying or dividing quantities". The plan names only within-system conversion. | In W2-I and W2-G judging, require unit labels through each step (for example, $/clip × clips = $). No new lesson time needed. |
| P6 | Should fix | 6.NS.B.4 | All three factored sums reduce to `k(2 + 3)`: 24 + 36, 30 + 45, 36 + 54. Students can copy the pattern without understanding it. | Vary the inner sum in checks, for example `36 + 8 = 4(9 + 2)` (the TN example) or `20 + 35 = 5(4 + 7)`. |
| P7 | Note | 6.RP.A.3b | Speed items only ask for distance in a given time. The TN example also asks for time for a given distance. | Optional second speed item in W2-I. |
| P8 | Note | Plan header | The M1 planning-status line says "especially M2-W2-G", which was copied from the course-level note. | Point to M1's busiest pair or say "course-wide". |
| P9 | Note | Superseded `M1_SUPPLY_EXCHANGE_SCOPE_AND_SEQUENCE.md` | Links to `C:/Users/erich/Desktop/...`, a local path that doesn't resolve in the repo. | Remove the link or mark it as offline. |
| P10 | Note | M1-W3-G check | Eight computation items plus a written justification don't fit in a 15-minute check. The plan already says to spread them across conferences. | Moodle build opens the audit quiz at the start of team work (see the build file). |
| P11 | Note | 6.NS.B.2 | All three division items are 3-digit ÷ 2-digit. | Optional: include one 4-digit dividend in the W3-I revisit. |

## Findings: Open LMS templates

| # | Severity | Template | Finding | Fix (applied in the build file and template sheets) |
| --- | --- | --- | --- | --- |
| T1 | Must fix | A, B, D, E | The Check quiz mixes auto-graded items with an Essay. A quiz attempt with an unmarked essay has no grade, so the "grade < 70%" stuck route and "receive a grade" completion don't fire until the teacher marks it. Students who need help won't see it during the lesson. | Split each check: **④ Check** = auto-graded items only (drives routing); **④ Explain** = separate essay quiz or assignment, marked by the teacher. |
| T2 | Must fix | B | The ⑤ Team challenge forum uses *Visible groups*. In that mode students can see other teams' posts but can't reply to them, so "question one other team's claim" is impossible. | Use a Standard forum with **No groups**. Team members post under their own name and say which team they're on. |
| T3 | Must fix | E | The Workshop activity has no team submissions and assigns reviewers per student, not per team. | Use a Standard forum (no groups) for the ledger swap: one member posts the team ledger; the teacher names the reviewing team. |
| T4 | Must fix | README review options | "Show marks and feedback after the quiz closes" only takes effect if the quiz has a close date. | Set a close date at the end of the lesson day, or tick *Later, while the quiz is still open*. |
| T5 | Should fix | A | The W1-I division item is a calculated question, so it marks only the quotient. The guide judges "36 with place-value steps". | Collect a photo of the written algorithm in ④ Explain. |
| T6 | Should fix | Hub / E | Project Hub item 5 *Final product* and Template E item 4 *Final team product* are the same graded assignment, built twice. | Keep the Hub item; Template E points to it. |
| T7 | Note | A–E | Moodle calculated-question formulas have no gcd/lcm functions. Decimal wildcards such as 0.1 can display as 0.30000000000000004 after `{=…}` arithmetic. | For GCF/LCM, build several Numerical variants and pull one with a Random question. For divisors, use exact binary decimals (0.25, 0.5, 0.75). |
| T8 | Note | A | The Cloze answer `3:2` is matched exactly, so `3 : 2` and `3 to 2` would be marked wrong. | Add those spellings as extra correct answers. |
| T9 | Note | README | Worked examples exist for only five of the eight lessons. | W2-I, W2-G and W3-I are now built in OPENLMS_COURSE_BUILD.md. |

## Still to do before teaching

These are unchanged from the plan's Step 6 handoff. Nothing in this audit creates them.

- Make the student materials: kit brief, supplier cards, ledger, ratio grid and axes, fraction strips, decimal grids, and the worked, developing and complete example files.
- Record the Interactive Videos (W1-G, W2-G) or swap in an Interactive Book. Make the Find Multiple Hotspots image (W3-G).
- Build the course in a sandbox, run each template's *Before students see it* checklist, and trial the busiest pair (W2-I/W2-G).
- Confirm class size, accommodations and the calendar.
