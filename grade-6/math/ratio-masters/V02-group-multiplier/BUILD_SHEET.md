# V02 Group Multiplier (and V02F): build sheet

Concept RAT-03, equivalent ratios. One question, one picture, as few numbers as possible. Status: **Approved (visual), 6 Oct 2026.** Freeze after the Open LMS sandbox check.

## 1 · Approved boards

| Board | Layout | Ending |
|---|---|---|
| V02 Example A / B / block skin | Rows of groups: A objects left, B objects right, divider between. Column labels at top. | Totals under each column; the unknown shows "?" then the answer. |
| V02 + fraction (A, B) | As V02. | Adds `A/B = A·n/B·n`. |
| V02 + ratio (A, B) | As V02. | Adds `A : B = A·n : B·n`. |
| V02F Example A / B / block skin | Each group is a fraction: A objects on top, bar, B objects below. Labels once at left (hidden under 480 px). | One equation `A/B = A·n/?`; "?" becomes the answer. |

## 2 · Sequence

| Time | On screen |
|---|---|
| 0 s | Question and group 1. |
| Every 1.0 s (n ≤ 3) or 0.8 s (n ≥ 4) | The next identical group rises in. |
| Last group + 0.8 s | Totals (V02) or equation (V02F) fade in with "?" in the unknown place. |
| +0.8–1.0 s | "?" fades, revealing the answer. V02 add-on line follows +0.8 s. Motion stops. |

Reduced motion: no animation, "?" hidden, final state shown at once. Text equivalent: one screen-reader sentence (`.rm-sr`) per board; there is no visible steps text, by request.

## 3 · Data fields and substitution

| Field / token | Rule |
|---|---|
| `A`, `B` (base ratio) | Positive integers 1–5, never reduced or reordered. |
| `n` (groups) | Integer 2–6. Totals = A·n and B·n, validated before render. |
| `unknown` | Which total shows "?" first (A or B side). |
| `labelA`, `labelB`, `noun` | Question, column labels, screen-reader sentence. |
| `question` | "{A} {labelA} {noun} go with {B} {labelB} {noun}. How many {labelB} {noun} go with {A·n} {labelA} {noun}?" |
| `skin` + `--rm-a*`, `--rm-b*` | Object SVG and colours only. Tested: beads, blocks. |
| `notation` | none \| fraction \| ratio (V02). V02F always fraction. |
| `animation-delay` | Group k = (k − 1) × gap; then as in section 2. |

Production fragment: `div.ratio-master` and its children. Stylesheet: the `.ratio-master` rules and `@keyframes`. No script or event attributes.

## 4 · Checklist

| Check | Result |
|---|---|
| One question, order explicit, model dominates | Pass |
| Counts: 2×3=6, 3×3=9; 3×4=12, 2×4=8 | Pass |
| A and B share structure; skin changes artwork only | Pass |
| Animation explains, then stops; reduced motion shows final state | Pass |
| 360 / 768 / 1280 px visual check | Review |
| Visual approval | Approved |
| Open LMS sandbox: keeps `<style>`, inline SVG, class and inline style attributes | Not yet run |
| Freeze | After sandbox |
