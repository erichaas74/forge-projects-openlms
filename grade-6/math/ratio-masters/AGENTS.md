# Instructions for Codex: Grade 6 Ratio Masters

These teaching masters are visually approved. Your job is production, not design.

## Do

- Preserve each master's appearance, structure, timing and class names exactly.
- Make new problems by changing only the data documented in that master's `BUILD_SHEET.md` (counts, labels, noun, question, skin, unknown side). Use the `board(...)` calls in `build/generators/` as the reference for how data maps to markup.
- Validate the math before rendering, as each build sheet states (whole-number outputs, equal factor on both quantities, counts match the sequence).
- Generate two variants of a master for human inspection before producing a batch.
- Ship `fragment.html` + `styles.css` per problem. Keep all CSS under `.ratio-master`.
- Keep the screen-reader sentence (`p.rm-sr`) accurate for the new data.
- Keep `prefers-reduced-motion` behaviour: the final state must show with no animation.

## Do not

- Add JavaScript, script tags, event-handler attributes, frameworks, web fonts or CDN links.
- Redesign, restyle, add text, add numbers, or add controls.
- Invent H5P libraries or package fields. These masters are teaching visuals; H5P practice is separate.
- Claim LMS grading or reporting works without a real student-role test in the sandbox.
- Exceed the supported ranges in each build sheet without asking.

## Ask before continuing when

- The Open LMS editor or filter strips `<style>`, inline `<svg>`, `class`/`style` attributes or `<details>` (route the CSS through an approved stylesheet; never disable HTML filtering site-wide).
- Platform details (Moodle/Open LMS version, editor, filter settings) block packaging. Continue independent work meanwhile.

Specification: `spec/RATIO_MASTER_SPECIFICATION.md`. Design brief: `spec/CLAUDE_RATIO_MASTER_PROMPT.md`.
