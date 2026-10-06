# V08 Mixture Container: build sheet

Concept RAT-09, mixtures and recipes. A jug is filled one cup at a time, in complete batches. Status: **Approved (visual), 6 Oct 2026.** Freeze after the Open LMS sandbox check.

## 1 · Two states

| State | On screen |
|---|---|
| Question | Question ("You make n batches…"); the recipe line under it, which stays put ("1 batch: A cups … + B cups …"); ingredient A column on the left, the empty jug in the middle, ingredient B column on the right; an outlined "?" under the asked side; **Check the answer**. |
| Feedback | Cup by cup, batch by batch: a full cup appears on its side in that batch's row, tips toward the jug and empties, and its layer drops into the jug (0.55 s per cup). A dark line marks the top of each batch; rows are labelled batch 1…n. At the end both totals show and the "?" becomes the answer. Stops. |

Same `<details>` + `:has` mechanism and fallback as V03. Ingredient A layers are solid; ingredient B layers are striped, so the two differ by pattern as well as colour. Reduced motion: opened state (empty cups, full jug) appears at once.

## 2 · Data fields

| Field | Rule |
|---|---|
| `A`, `B` | Cups of each ingredient in one batch. One layer = one cup. |
| `n` | Number of batches, 2–5. Jug height = (A + B) × n × 26 px. |
| `unknown` | Which ingredient total is asked (a or b). |
| `skin` | lemonade \| paint \| redwhite (ingredient names and colours). |
| Captions | question, feedback sentence. |

Tested: 2:3 × 3, 1:2 × 4, 2:3 × 3 (pink paint). Claimed: A + B ≤ 6, total cups ≤ 20.

## 3 · Checklist

| Check | Result |
|---|---|
| Recipe stays at the top by the question | Pass |
| Each colour on its own side; cups show full, then empty | Pass |
| Rendered in Chromium: mid-pour, final | Pass |
| 360 / 768 / 1280 px visual check | Review |
| Visual approval | Approved |
| Open LMS sandbox | Not yet run |
