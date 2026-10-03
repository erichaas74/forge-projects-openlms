# Grade 6 history scope-and-sequence build

The completed Grade 6 handoff and root curriculum guide govern this build. This is Steps 1–4, with block outlines. Detailed teaching procedures and source selections remain Step 5; student materials and classroom validation remain Step 6.

Use the bundled Python and Node runtimes. Edit `build_content.py`, then run `build_content.py`, `publish.py`, `build_workbook.mjs`, and the read-only `validate.py` in that order. `history.json` is the maintained data view; the Markdown course/project outlines and workbook are synchronized outputs. Review affected preview ranges after a rebuild.

`extract_sources.py` extracts the official local Tennessee PDF pages 81–98. The official C3 PDF was reviewed online; local download was unavailable. C3 summaries are interpretive and selected, not the complete grade band. NCSS theme labels are local navigation labels and do not certify the proprietary middle-grades performance expectations. TN 6.39 chronology is explicitly Unverified.

`node_modules` points to the bundled dependency runtime. The builder uses `@oai/artifact-tool`; `write_native_links.py` is a builder-only fallback for the native hyperlink feature missing from that API. Validation reads outputs without modifying them. Preview files, source extracts and manifests belong here, outside grade deliverables.
