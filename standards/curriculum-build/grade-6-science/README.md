# Grade 6 science publishing

This folder maintains the approved science planning records and their published views. Curriculum decisions follow the root Curriculum Brain and step guide. The completed Grade 6 project handoff is the project input; the project-creation archive is not used.

Edit `build_content.py`, then run these in order with the bundled Python and Node runtimes:

1. `build_content.py` produces `science.json` from the maintained lesson and standards records.
2. `publish_documents.py` publishes the course map and four detailed project documents under `scope-and-sequence`.
3. `build_workbook.mjs` publishes the five-tab workbook to `6th Grade/Grade_6_Science_Curriculum_Standards.xlsx`, inserts native hyperlinks through the builder-only fallback, renders review ranges and reopens the saved file.
4. `validate.py` independently reads the content, official source extracts, documents and saved workbook. It checks lesson counts and timing, standards destinations, workbook content, panes and local links. It does not modify deliverables.

`node_modules` is a junction to the bundled dependency runtime. Source extracts come from the official PDFs in `reference-standards`; they are supporting records, not alternate curriculum instructions. `previews`, link manifests and inspection diagnostics are build support, not grade deliverables.

Review each affected preview after a rebuild. Numerical checks and planning clocks do not verify actual classroom timing or student mastery. Step 6 still requires student materials, empirical data selection, examples, assessment/scoring guidance, access checks and practical trials.
