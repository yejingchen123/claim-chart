---
name: claim-chart
description: Fill professional patent comparison claim-chart Word documents. Use when the user provides a DOCX claim chart, an example/reference DOCX, a target company name, and asks Codex to fill the company-comparison column with detailed English technical/product mapping, official-source screenshots, references, and Word-format preservation.
---

# Claim Chart

## Objective

Produce a high-quality Word claim chart. The final output is the filled `.docx`, with the original table structure preserved, the target company's column completed in English, official-source evidence inserted, and render QA completed.

Use the document/DOCX workflow available in the environment for authoring and rendering. Read [the style contract](references/style-contract.md) before editing. The supplied reference controls the document's design; generic document advice about titles, introductory summaries, fonts or citations must not add structures absent from that reference. Explicit user instructions take precedence.

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
   - Record the actual opening sequence, inline-citation convention, comment font/size/italics, bold spans in the `Herein` sentence, and screenshot/URL order in a short local style inventory.
   - Copy those conventions. A request for high quality is not, by itself, a request to redesign the template.

2. Inspect the target DOCX.
   - Confirm which cells are blank and which structures must remain.
   - Preserve all first-column patent text and all table geometry unless the user asks otherwise.
   - Fill only the target-company column and summary comparison cells.

3. Research the company from official sources.
   - First identify the concrete product or service being assessed, its provider, deployment and relevant period. Read [research and evidence boundaries](references/research-evidence.md), especially for partner technology, acquired/divested businesses or historical sources.
   - Prefer the company website, official support pages, official news/media pages, official product pages, official whitepapers, or official documentation.
   - Use non-official sources only if official sources cannot establish a necessary fact; disclose that choice in the work notes, not inside the claim chart unless appropriate.
   - For modern companies and products, browse live sources. Do not rely on memory.
   - Capture clear screenshots of relevant official page sections. Screenshots should show the relevant text or product feature, not just decorative hero images.

4. Map each claim row.
   - Read the patent text in the first-column row carefully.
   - Identify a supported corresponding element within the assessed product or service. Do not force a match to a merely similar feature or silently substitute another company's general platform.
   - Write detailed English prose in the company column. Be specific about how the company feature performs the same or analogous function.
   - End the substantive text with `Herein, “{patent content}” corresponds to {company technology content}.`, using the reference's punctuation and emphasis. Bold both correspondence phrases when the reference does, including the complete relevant claim phrase.
   - Keep material qualifications next to the mapping. Distinguish documented deployment facts, partner-platform disclosures and unconfirmed inferences. A summary must retain the same qualifications.
   - When the reference has no inline citation tags, keep `[Ref-*]` out of the Comment prose. Put traceable source lines below the comment, alongside the evidence.

5. Fill evidence for each main-table row.
   - Select enough focused screenshots to substantiate the mapping; do not fill an image quota with weak or repetitive evidence.
   - Follow the reference's evidence order. For the standard image-first layout, each screenshot is followed by its own URL; additional supporting URL lines may follow the evidence blocks.
   - Match the evidence fields as well as their order. If the reference has only screenshots and `[Ref-*] URL` lines, include only those after the Comment. Do not add source titles, captions, excerpt explanations, publication/access dates or plain-text page notes. Keep that metadata in local work notes; a PDF page fragment may remain part of its URL.
   - Reuse the same official source in multiple rows when it supports multiple claim elements.
   - Keep screenshots readable at the final document scale; size them to the actual cell width. Retain original captures and source/page locators in local work notes.

6. Fill the opening summary row last.
   - Add `References:` followed by all official URLs used in the other company-column rows, ordered by first appearance.
   - `References:` must be bold.
   - If the reference goes from the company heading directly to `References:`, do the same. Do not insert an extra comparison title, date, scope paragraph or executive summary. Explain the assessed scope in the existing first detailed Comment instead.
   - Fill the nested summary table without changing its structure. Use short phrases or simple sentences, not long prose.
   - Keep the summary table's first column unchanged.

7. Apply final formatting.
   - In each main-table company cell, the visible opening label `[Comment:` must be bold italic.
   - The final closing bracket `]` of the comment block must also be bold italic.
   - Match the example's comment body style and correspondence emphasis separately. An italic body still needs distinct bold claim and product spans in `Herein` when shown in the reference.
   - Do not bold or italicize `[Ref-*]` URL lines unless the example requires it.
   - Preserve the example's font family and size; solve layout problems with content length, paragraph spacing and evidence sizing before changing typography.

8. Run the bundled polish helper.
   - Check without modifying the document:
     `python scripts/polish_claim_chart_docx.py path/to/file.docx --check --template path/to/reference.docx`
   - To repair only `References:`, `[Comment:` and the final `]`, use `--fix-labels --output path/to/polished.docx`. The helper preserves the other runs and the input file.
   - Evidence is never reordered by default. Use `--reorder-url-first --output path/to/polished.docx` only after confirming that the whole evidence sequence consists of URL/image pairs. Mixed or ambiguous layouts require manual pairing.
   - The checker targets the common two-outer-table, company-in-column-two, image-first layout. It detects structural/style problems, not factual correspondence or full template fidelity. Review intentional user overrides separately; do not reorder a different reference convention to satisfy this checker.

9. Render and visually verify.
   - Render the final DOCX to page images using the document skill renderer.
   - If LibreOffice is unavailable and Microsoft Word is available on Windows, export to PDF with Word and rasterize the PDF with Poppler.
   - Inspect every rendered page at a readable scale. A contact sheet is an index, not a substitute for page inspection.
   - Fix clipping, broken tables, image overflow, unreadable screenshots, missing URLs, wrong evidence ordering, or style drift before delivery.
   - Inspect all visible text after each Comment, not just headings and bold spans. In a screenshot-and-URL-only reference, there must be no added evidence prose, including text appended to a URL line.
   - Compare protected left-column text, table geometry, nested labels, headers/footers and field codes against the target baseline. Check the rendered page count and cached page total.
   - Deliver only the requested final document. Keep originals, evidence captures and QA files outside the deliverable and out of the public skill repository.

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
- `references/research-evidence.md`: Product scope, partner attribution, source timing and evidence strength.
- `scripts/polish_claim_chart_docx.py`: Deterministic post-processing and validation helper for common claim-chart DOCX formatting details.
