# V05 Double Number Line: build sheet

Concept RAT-06, double number lines. Matching jumps on two aligned lines. Status: **Approved (visual), 6 Oct 2026.** Freeze after the Open LMS sandbox check.

## 1 · Two states

| State | On screen |
|---|---|
| Question | Question; line A on top, line B below, ticks vertically aligned and evenly spaced. The known line is fully labelled; the unknown line shows 0 and its first step only; the asked tick is an outlined "?". **Check the answer**. |
| Feedback | Known line first: each jump draws left to right (0.5 s, one every 0.6 s) with its `+step` label; the value it lands on bumps. Then a "n jumps" tag appears by that line's label. After a 0.9 s pause the unknown line does the same jumps; hidden values appear as each jump lands; the "?" becomes the answer on the last landing, and its "n jumps" tag appears. Stops. |

Same `<details>` + `:has` mechanism and fallback as V03. Reduced motion: opened state appears at once.

## 2 · Data fields

| Field | Rule |
|---|---|
| `A`, `B` | Step sizes for line A and line B. |
| `n` | Number of jumps, 2–6. The asked tick is the last one (A·n, B·n). Tick k at left = k / n × 100 %. |
| `unknownLine` | A or B. |
| `labelA`, `labelB`, `noun`, `question`, `skin` | As V02. The object icon sits beside each line label. |

Tested: 2:3 with 4 jumps (unknown bottom); 3:2 with 5 jumps (unknown top); beads and blocks. Spacing is proportional; numbers never rescale.

## 3 · Checklist

| Check | Result |
|---|---|
| Answer hidden until Check | Pass |
| Synchronised jumps; aligned pairs; even spacing | Pass |
| Rendered in Chromium: question (A), final (B) | Pass |
| 360 / 768 / 1280 px visual check | Review |
| Visual approval | Approved |
| Open LMS sandbox | Not yet run |
