# Grade 6 Ratio Masters — approved teaching visuals

Approved (visual) 6 Oct 2026. Not frozen: each master still needs the Open LMS sandbox check (see each `BUILD_SHEET.md`).

| Folder | Master | Concept |
|---|---|---|
| `V01-object-groups/` | Object Groups: sort, count, write A : B (part to part, part to whole) | RAT-01, RAT-02 |
| `V02-group-multiplier/` | Group Multiplier: repeated groups side by side (plain, + fraction line, + ratio line) | RAT-03 |
| `V02F-group-multiplier-fractions/` | Group Multiplier, fraction layout | RAT-03 |
| `V03-scale-machine/` | Scale Machine: same × n or ÷ n on both sides, answer on Check | RAT-04 |
| `V04-ratio-table/` | Ratio Table: same factor on both columns, answer on Check | RAT-05 |
| `V05-double-number-line/` | Double Number Line: known line jumps first, then the unknown line | RAT-06 |
| `V06-equal-distributor/` | Equal Distributor: deal a total into see-through containers, read the amount for one | RAT-07 |
| `V07-comparator/` | Comparator: share out two offers, compare per one in a stated direction | RAT-08 |
| `V08-mixture-container/` | Mixture Container: pour complete batches cup by cup, recipe at the top | RAT-09 |
| `V08T-mixture-to-a-total/` | Mixture Container variant: picture recipe, fill to a total, full cup supply on each side | RAT-09 |
| `V09-table-to-graph/` | Table to Graph: plot each table row as a point, read the missing value off the line through (0, 0) | RAT-10 |

## Each example folder

`<master>/examples/<example>/`

- `fragment.html` — the `div.ratio-master` markup only. This is what goes into the LMS page.
- `styles.css` — the stylesheet for that fragment. Every rule is scoped under `.ratio-master`; no global rules.
- `preview.html` — fragment + styles in one page. Open it in a browser to review. Reload to replay the animation.

No JavaScript anywhere. V03–V09 use a native `<details>` "Check the answer" button and CSS `:has()`.

## Rebuilding

`build/generators/v0*.py` hold the data for each example and write canvas-format boards; `build/export.py` turns those into the files above.

```
bash build/build_all.sh
```

Change example data inside the `board(...)` calls at the bottom of a generator, then rebuild. The generators reproduce the approved boards byte for byte.

## Source

- Design canvas (private): https://claude.ai/artifact/Nwo2r6bgb6bKUYXSYpP6KU
- Specification and brief: `spec/`
