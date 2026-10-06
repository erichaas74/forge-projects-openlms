# V06 Equal Distributor: build sheet

Concept RAT-07, unit rates. Share a total equally, then read the amount for one. Status: **Approved (visual), 6 Oct 2026.** Freeze after the Open LMS sandbox check.

## 1 · Two states

| State | On screen |
|---|---|
| Question | Question; the total as a pile of items in a grey tray (2 rows, not aligned to the groups); one see-through container per group, drawn as the group object (notebook, bag, box); "1 … = ?"; **Check the answer**. |
| Feedback | Items are dealt in rounds: round r starts at 0.3 + 0.9r s, one item to each container left to right (0.08 s apart, 0.6 s slide), settling from the bottom. After the last round a dashed box marks container 1 and the "?" becomes the amount for one. Stops. |

Items move with the CSS `translate` property and a transition, triggered by `:has(.rm-check[open])`. Containers sit above the items with a translucent fill so items read as inside. Reduced motion: no transition; items appear in place.

## 2 · Data fields

| Field | Rule |
|---|---|
| `total`, `groups` | Whole numbers; total must divide exactly by groups. Discrete items only; continuous amounts need a bar variant (not built). |
| `item` | coin \| apple \| block (item artwork). |
| `group` | notebook \| bag \| box (container shape). |
| Captions | Pile caption (e.g. "$18"), group caption ("6 notebooks"), answer line ("1 notebook costs $ ?"), feedback sentence. |

Tested: 18 ÷ 6 (coins, notebooks), 20 ÷ 5 (apples, bags), 18 ÷ 6 (blocks, boxes). Claimed: total ≤ 24, groups 2–6, amount per group ≤ 5.

## 3 · Checklist

| Check | Result |
|---|---|
| Answer hidden until Check | Pass |
| Equal dealing in rounds; one group highlighted | Pass |
| Rendered in Chromium: all three, final state | Pass |
| 360 / 768 / 1280 px visual check | Review |
| Visual approval | Approved |
| Open LMS sandbox: also check the `translate` property is kept in inline styles | Not yet run |
