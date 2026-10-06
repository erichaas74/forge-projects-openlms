# V01 Object Groups: build sheet

Concepts RAT-01 (write A : B) and RAT-02 (part to part, part to whole). Status: **Approved (visual), 6 Oct 2026.** Freeze after the Open LMS sandbox check.

## 1 · Sequence

| Time | On screen |
|---|---|
| 0 s | Question, and the unsorted string (stays visible the whole time). Empty answer box below. |
| 0.8 s, every 0.2 s | A copy of each object drops from the string into the answer box: A objects left, B objects right (part to part), or all objects right (part to whole). Each move takes 1 s. |
| Last landing | ":" and the labels appear (A label, B label or "all"). Part to whole: the copy of the A objects fades in on the left first. |
| +0.7 s, end | The count of each side drops in under it: `A : B` or `A : whole`. Motion stops. |

Reduced motion: no animation, the sorted answer shows at once. Text equivalent: one screen-reader sentence per board.

## 2 · Data fields and substitution

| Field / token | Rule |
|---|---|
| `sequence` | Order of objects in the string, e.g. `a b a b a`. Counts of a and b give A and B. |
| `ratioKind` | part_to_part \| part_to_whole. Whole = A + B, derived. |
| `labelA`, `labelB`, `noun`, `question` | Question names A first. |
| Slots `n` | A + 1 + (B or whole). Stage width = min(100%, n × 60 px). Every object's `left`/`width` = slot × 100/n %. |
| Move keyframes | One per distinct shift: `translate(dx%, calc(-100% - 72px))` → none, where dx = (string slot − sorted slot) × 100. |
| `skin` | Object SVG, colours, thread (transparent for blocks). |

Range: tested 3/2, 3/5, 4/5. Claimed: each count 1–9, string ≤ 12 objects so beads stay ≥ 26 px at 360 px.

## 3 · Checklist

| Check | Result |
|---|---|
| Counts match each string | Pass |
| A and B share structure; skin changes artwork only | Pass |
| Rendered in Chromium: end states, mid-animation | Pass (3 of 4 boards) |
| 360 / 768 / 1280 px visual check | Review |
| Visual approval | Approved |
| Open LMS sandbox (same checks as V02) | Not yet run |
| Freeze | After sandbox |
