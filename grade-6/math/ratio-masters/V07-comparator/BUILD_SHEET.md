# V07 Comparator: build sheet

Concept RAT-08, compare rates. Both offers are shared out to "per one", then compared in a stated direction. Status: **Approved (visual), 6 Oct 2026.** Freeze after the Open LMS sandbox check.

## 1 · Two states

| State | On screen |
|---|---|
| Question | Question; a basis line saying which direction is better ("Less money per pencil is better."); two panels, each with name, offer, pile, one see-through container per unit (unit pictured inside), and "? per unit"; **Check the answer**. |
| Feedback | Both panels deal at once in rounds (as V06). Then a dashed box marks container 1 in each panel and both "?" become the per-one amounts. The winner gets a tag ("Better buy" / "Faster") and a verdict line states the comparison. Stops. |

Same `<details>` + `:has` + `translate` mechanism as V06. Reduced motion: opened state appears at once.

## 2 · Data fields

| Field | Rule |
|---|---|
| Per panel: `name`, `offer`, `total`, `units` | total must divide exactly by units. |
| `item` | coin \| toy \| block (what is shared). |
| `unit` | pencil \| hour \| apple (pictured inside each container). |
| `better` | less \| more. Always shown as the basis line; the winner is computed, never typed. |
| Captions | "$ ? per pencil" / "? toys per hour", verdict sentence, feedback sentence. |

Tested: $8/4 vs $9/3 (less is better), 12/3 vs 10/2 toys per hour (more is better), apples skin. Do not use equal rates without a "same" verdict (not built).

## 3 · Checklist

| Check | Result |
|---|---|
| Comparison direction explicit | Pass |
| Same unit ("per one") before comparing | Pass |
| Rendered in Chromium: question (A), final (B) | Pass |
| 360 / 768 / 1280 px visual check (panels stack on phones) | Review |
| Visual approval | Approved |
| Open LMS sandbox | Not yet run |
