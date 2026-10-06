# V09 Table to Graph: build sheet

Concept RAT-10, plotting equivalent-ratio pairs. Each table row becomes a point; the missing value is read off the graph. Status: **Approved (visual), 6 Oct 2026.** Freeze after the Open LMS sandbox check.

## 1 · Two states

| State | On screen |
|---|---|
| Question | Question; a ratio table (A as x, B as y, object icons in the headers) with the last y as an outlined "?"; an empty graph with labelled axes, origin at 0, uniform ticks; **Check the answer**. |
| Feedback | Row k (known rows) at 0.3 + 1.3k s: the row is highlighted, dashed guides run from both axes, the point drops in with its "(x, y)" label. Then a dotted line from (0, 0) through the points. Then for the asked row: a guide up from x to the line, the open point, a guide across to the y-axis, a ring on that y tick, and the table "?" becomes the answer. Stops. |

Same `<details>` + `:has` mechanism and fallback as V03. The graph is one inline SVG (viewBox, scales to width ≤ 460 px). Reduced motion: opened state appears at once.

## 2 · Data fields

| Field | Rule |
|---|---|
| `A`, `B` | Base ratio; rows are (A·k, B·k), k = 1…rows. The last row's y is asked. |
| `rows` | 3–5. |
| `xmax`, `xstep`, `ymax`, `ystep` | Axis ranges and uniform steps; every point must fit; max must be a multiple of step. No rescaling, origin always shown. |
| `labelA`, `labelB`, `noun`, `question`, `skin` | As V02. x = A, y = B always. |

Tested: 2:3 (x 0–10 by 2, y 0–15 by 3), 3:2 (x 0–15 by 3, y 0–10 by 2), blocks skin. The dotted line through (0, 0) is a reading aid; formal proportionality and slope are not taught here.

## 3 · Checklist

| Check | Result |
|---|---|
| Answer hidden until Check | Pass |
| Row highlight matched to its point; x = A, y = B | Pass |
| Origin and uniform scales | Pass |
| Rendered in Chromium: mid-plot, final, question (B) | Pass |
| 360 / 768 / 1280 px visual check | Review |
| Visual approval | Approved |
| Open LMS sandbox: inline SVG kept | Not yet run |
