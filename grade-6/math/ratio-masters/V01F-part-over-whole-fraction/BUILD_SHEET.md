# V01F Part over whole, fraction model: build sheet

Concept RAT-02 (part to whole), written as a fraction. The selected beads go above a fraction bar and the entire collection below. Status: **Approved (visual), 6 Oct 2026.** Freeze after the Open LMS sandbox check.

## 1 · Two states

| State | On screen |
|---|---|
| Question | Question ("What fraction of the beads are blue?"); the bead string; an empty fraction model: "blue beads" over a bar over "all beads", with "?" over "?" beside it; **Check the answer**. |
| Feedback | Each A bead in the string gets a ring as a copy pops in above the bar (0.45 s apart); the numerator "?" becomes A. Then every bead in the string is ringed in turn as the whole collection pops in below the bar (0.32 s apart); the denominator becomes N. Then "A/N of the beads are blue." Stops. |

Same `<details>` + `:has` mechanism and fallback as V03. Reduced motion: opened state appears at once.

## 2 · Data fields

| Field | Rule |
|---|---|
| `sequence` | Order of beads in the string, e.g. `a b a b a`. A = count of a, N = length. |
| `labelA`, `labelB`, `noun`, `question`, `skin` | As V01. |

Tested: 3/5 (blue), 4/9 (red), blocks. Claimed: N ≤ 12.

## 3 · Checklist

| Check | Result |
|---|---|
| Part above the bar, whole below; answer hidden until Check | Pass |
| Rendered in Chromium: question (A), final (B) | Pass |
| 360 / 768 / 1280 px visual check | Review |
| Visual approval | Approved |
| Open LMS sandbox | Not yet run |
