# V08T Mixture Container, fill to a total: build sheet

Variant of V08. The recipe is pictures only, the question asks for a total amount, and each side starts with a full supply of cups. Status: **Approved (visual), 6 Oct 2026.** Freeze after the Open LMS sandbox check.

## 1 · Two states

| State | On screen |
|---|---|
| Question | Question ("You want T cups … in all…"); the recipe as pictures only (A full cups + B full cups, no numbers); a full supply of cups on each side in a grid; the jug with a "T cups" tag; an outlined "?" under the asked side; **Check the answer**. |
| Feedback | Cups pour one at a time from the top row down (tip, empty, layer drops in) until the jug reaches T. Unused cups stay full. At the end each side shows "… cups used" and the "?" becomes the answer. Stops. |

Same mechanism as V08. Reduced motion: opened state appears at once.

## 2 · Data fields

| Field | Rule |
|---|---|
| `A`, `B`, `n` | As V08; T = (A + B) × n. |
| `supply` | Full cups each side starts with. Default T. Must be ≥ the cups used on either side. |
| `cols`, `rows` | Supply grid, e.g. `cols=4, rows=3` or `cols=3, rows=5`. `rows` defaults to supply ÷ cols, rounded up. rows × cols must hold the supply. |
| `unknown`, `skin`, captions | As V08. |

Example calls in `build/generators/v08t.py`: lemonade `supply=15, cols=5, rows=3`; green paint `supply=12, cols=4, rows=3`; pink paint `supply=15, cols=3, rows=5`.

## 3 · Checklist

| Check | Result |
|---|---|
| Recipe in pictures only; question asks for a total | Pass |
| Full supply on each side; only used cups empty | Pass |
| Supply and grid adjustable in code, validated | Pass |
| Rendered in Chromium: question, final (all three grids) | Pass |
| 360 / 768 / 1280 px visual check | Review |
| Visual approval | Approved |
| Open LMS sandbox | Not yet run |
