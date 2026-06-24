---
name: claim-chart
description: Fill professional patent comparison claim-chart Word documents. Use when the user provides a DOCX claim chart, an example/reference DOCX, a target company name, and asks Codex to fill the company-comparison column with detailed English technical/product mapping, official-source screenshots, references, and Word-format preservation.
---

# Claim Chart

## Objective

Produce a high-quality Word claim chart. The final output is the filled `.docx`, with the original table structure preserved, the target company's column completed in English, official-source evidence inserted, and render QA completed.

Always use this skill together with the document/DOCX workflow available in the environment. Read `references/style-contract.md` before editing the DOCX.

## Inputs To Identify

- Target DOCX to fill.
- Example/reference DOCX that shows the desired writing tone, evidence layout, typography, and table behavior.
- Target company name.
- Patent row text in the first column.
- Any explicit user preferences that override the example.

If an input is missing, infer it from the current folder when obvious. Ask only when ambiguity could cause editing the wrong file or comparing the wrong company.

## Workflow

1. Inspect the example DOCX first.
   - Identify the top summary table, the main claim table, row count, column count, nested tables, image layout, and special formatting.
   - Do not assume visible `[Comment: ...]` text is a Word comment. Inspect the DOCX structure.
   - Copy the example's style before applying general preferences.

2. Inspect the target DOCX.
   - Confirm which cells are blank and which structures must remain.
   - Preserve all first-column patent text and all table geometry unless the user asks otherwise.
   - Fill only the target-company column and summary comparison cells.

3. Research the company from official sources.
   - Prefer the company website, official support pages, official news/media pages, official product pages, official whitepapers, or official documentation.
   - Use non-official sources only if official sources cannot establish a necessary fact; disclose that choice in the work notes, not inside the claim chart unless appropriate.
   - For modern companies and products, browse live sources. Do not rely on memory.
   - Capture clear screenshots of relevant official page sections. Screenshots should show the relevant text or product feature, not just decorative hero images.

4. Map each claim row.
   - Read the patent text in the first-column row carefully.
   - Decide which company product, feature, service, cloud system, vehicle module, sensor, controller, or workflow is the closest corresponding element.
   - Write detailed English prose in the company column. Be specific about how the company feature performs the same or analogous function.
   - End the substantive text with: `Herein, "{patent content}" corresponds to {company technology content}.`

5. Fill evidence for each main-table row.
   - Use about two relevant screenshots per row when possible; three is acceptable for complex rows.
   - The required order is image first, then its URL, then image, then URL, continuing in that pattern.
   - Reuse the same official source in multiple rows when it supports multiple claim elements.
   - Keep screenshots readable after insertion. A width around 2.8 to 3.0 inches often matches narrow claim-chart cells.

6. Fill the first row last.
   - Add `References:` followed by all official URLs used in the other company-column rows, ordered by first appearance.
   - `References:` must be bold.
   - Fill the nested summary table without changing its structure. Use short phrases or simple sentences, not long prose.
   - Keep the summary table's first column unchanged.

7. Apply final formatting.
   - In each main-table company cell, the visible opening label `[Comment:` must be bold italic.
   - The final closing bracket `]` of the comment block must also be bold italic.
   - The comment body itself should not be bold italic unless the example uses that style.
   - Do not bold or italicize `[Ref-*]` URL lines unless the example requires it.
   - Preserve the example's font family and size as closely as possible.

8. Run the bundled polish helper.
   - After editing, run:
     `python scripts/polish_claim_chart_docx.py path/to/file.docx`
   - Use `--check` first if you only want a report.
   - This helper formats `[Comment:` and final `]`, bolds `References:`, and enforces image-before-URL evidence ordering for common DOCX structures.

9. Render and visually verify.
   - Render the final DOCX to page images using the document skill renderer.
   - If LibreOffice is unavailable and Microsoft Word is available on Windows, export to PDF with Word and rasterize the PDF with Poppler.
   - Inspect every page or at minimum a contact sheet plus all dense evidence pages.
   - Fix clipping, broken tables, image overflow, unreadable screenshots, missing URLs, wrong evidence ordering, or style drift before delivery.

## Quality Bar

The result should read like a polished legal/technical claim chart, not a rough extraction:

- Detailed company-side technical analysis for every row.
- Official sources only where feasible.
- Screenshots and URLs paired in the correct order.
- First-row references and summary table completed after row-level work.
- Original table structure preserved.
- Word opens cleanly and rendered pages are visually acceptable.

## Useful Resources

- `references/style-contract.md`: Exact writing, evidence, and formatting rules.
- `scripts/polish_claim_chart_docx.py`: Deterministic post-processing and validation helper for common claim-chart DOCX formatting details.
