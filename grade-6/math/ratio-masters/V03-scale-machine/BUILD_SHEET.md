# V03 Scale Machine: build sheet

Concept RAT-04, missing values. Both quantities go through the same × n or ÷ n. Status: **Approved (visual), 6 Oct 2026.** Freeze after the Open LMS sandbox check.

## 1 · Two states

| State | On screen |
|---|---|
| Question (default) | Question; both inputs in boxed groups with counts; a chip `op ?` on each side; the known output; the unknown output as an outlined "?"; a **Check the answer** button. |
| Feedback (button open) | 0 s: left chip shows `op n`, group boxes darken. 0.4 s: `A op n = A′` under the left output. 1.0–1.9 s: a copy of the chip slides to the right side. 2.0 s: right output groups drop in. 2.6 s: "?" becomes the answer, with `B op n = B′`. Stops. |

The button is a native `<details>`/`<summary>`: keyboard operable, no script. The in-picture reveal uses `:has(.rm-check[open])`. Where `:has` is unsupported, the feedback sentence still shows the answer. Reduced motion: no animation; the opened state appears at once.

## 2 · Data fields

| Field | Rule |
|---|---|
| `A`, `B` | Input counts. For ÷, both must divide exactly by n. |
| `op`, `n` | × or ÷; n 2–6. Outputs A′, B′ validated as whole numbers. |
| `known` | Which output the question gives (A′ by default). |
| Groups | ×: outputs drawn as n boxes of A (or B). ÷: inputs drawn as n boxes of A′ (or B′). Every group is boxed. |
| `labelA`, `labelB`, `noun`, `question`, `skin` | As V02. |

Tested: 2:3 × 4 and 12:8 ÷ 4, in beads and blocks. Claimed: at most 24 objects on any side.

## 3 · Checklist

| Check | Result |
|---|---|
| Answer hidden until Check; feedback near the model | Pass |
| Same operation shown moving from one side to the other | Pass |
| Rendered in Chromium: question state, mid-slide, final | Pass (Examples A and B) |
| 360 / 768 / 1280 px visual check | Review |
| Visual approval | Approved |
| Open LMS sandbox: `<details>`, `:has`, inline SVG, style attributes kept | Not yet run |
