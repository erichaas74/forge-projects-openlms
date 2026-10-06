# V10 Necklace shortage hook: build sheet

A hook problem: someone claims a number of necklaces; building them from the beads available shows which colour runs out. Status: **Approved (visual), 6 Oct 2026.** Freeze after the Open LMS sandbox check.

## 1 · Two states

| State | On screen |
|---|---|
| Question | The claim ("Each necklace needs A blue and B yellow beads. Maya has … Maya says that makes C necklaces. Is that right?"); a recipe chip; two trays with the beads available; C empty necklaces (dashed bead spaces); "Maya can make ? necklaces."; **Check the answer**. |
| Feedback | Beads are placed one at a time (0.22 s), necklace by necklace: each tray bead fades as its copy fills a space. A full necklace gets a **complete** tag. When a colour runs out, its empty spaces get red dashed rings and the necklace gets **not enough …**. Trays show "… left"; the "?" becomes the real number. Stops. |

Same `<details>` + `:has` mechanism and fallback as V03. Shortage is shown by dashed red rings and the tag text, not colour alone. Reduced motion: opened state appears at once.

## 2 · Data fields

| Field | Rule |
|---|---|
| `A`, `B` | Beads of each colour per necklace. |
| `haveA`, `haveB` | Beads available. |
| `claim` | Claimed necklaces; must be more than min(haveA ÷ A, haveB ÷ B), which is the answer. |
| `who`, `item` | Name and object ("necklace", "bracelet"). |
| `cols` | Tray grid columns. |
| `labelA`, `labelB`, `skin` | As V02. |

Tested: 8 blue / 9 yellow, claim 4 (yellow runs out); 10 red / 8 white, claim 4 (red runs out); blocks as bracelets.

## 3 · Checklist

| Check | Result |
|---|---|
| Shows why the claim fails, at the necklace where it fails | Pass |
| Limiting colour identified in text and visual | Pass |
| Rendered in Chromium: question, final (A and B) | Pass |
| 360 / 768 / 1280 px visual check | Review |
| Visual approval | Approved |
| Open LMS sandbox | Not yet run |
