# V04 Ratio Table: build sheet

Concept RAT-05, ratio tables. The same factor works on both columns. Status: **Approved (visual), 6 Oct 2026.** Freeze after the Open LMS sandbox check.

## 1 · Two states

| State | On screen |
|---|---|
| Question | Question; table headed by object icon + label for each column; complete rows except the asked cell, shown as an outlined "?"; **Check the answer**. |
| Feedback | 0 s: base row and asked row highlighted. 0.2 s: bracket arrow `× n` grows on the left of column A, base row → asked row. 1.0–2.0 s: a copy slides to the right of column B. 2.2 s: "?" becomes the answer. Stops. |

Same `<details>` + `:has` mechanism and fallback as V03. Reduced motion: opened state appears at once.

## 2 · Data fields

| Field | Rule |
|---|---|
| `A`, `B` | Base row (row 1). |
| `multipliers` | Row k = (A·m_k, B·m_k), increasing, 3–6 rows. |
| `target` | Index of the asked row; n = m_target / m_1, validated as a whole number. |
| `unknownColumn` | B by default. |
| Grid | Columns: arrow 120 px, A 130 px, B 130 px, arrow 120 px (76 / 88 px under 480 px). Slide distance = arrow + 2 × column. |
| `labelA`, `labelB`, `noun`, `question`, `skin` | As V02. |

Tested: 2:3 rows ×1, ×2, ×3, ×5 (asked last row); 3:2 rows ×1–×4 (asked middle row); beads and blocks.

## 3 · Checklist

| Check | Result |
|---|---|
| Answer hidden until Check | Pass |
| Same factor shown on both columns | Pass |
| Rendered in Chromium: question, mid-slide, final | Pass (Example A) |
| 360 / 768 / 1280 px visual check | Review |
| Visual approval | Approved |
| Open LMS sandbox | Not yet run |
