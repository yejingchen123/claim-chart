# Claim Chart Style Contract

Use this reference for every claim-chart filling task.

## Writing Pattern

Each main-table company-column cell should generally contain:

1. A visible comment block beginning with `[Comment:`.
2. One or more detailed paragraphs mapping the patent row to company technology.
3. A final correspondence sentence:
   `Herein, "{patent content}" corresponds to {company technology content}.]`
4. Evidence screenshots and URL lines.

The patent content inside the `Herein` sentence should be specific to that row, not a generic restatement of the entire claim. The company technology content should name the exact product, module, sensor, cloud service, controller, algorithm, or feature being compared.

## Tone

- Write in English.
- Use formal technical/legal comparison prose.
- Prefer "corresponds to", "implements", "provides", "receives", "uses", "controls", "communicates with", and "is functionally equivalent to" where accurate.
- Avoid overclaiming. If the company's public material is analogous but not identical, say so carefully.
- Do not add unsupported assertions merely to force a match.

## Official Evidence

Use official pages first:

- Company product pages.
- Company support pages.
- Company press/media pages.
- Company technical blogs, manuals, whitepapers, or developer docs.
- Official PDFs, if available.

For each row, collect evidence that directly supports the mapping. A good evidence screenshot shows the relevant page text or feature card. Avoid decorative-only images.

## Evidence Ordering

The required order inside each row is:

```text
<screenshot 1>
[Ref-1] https://official.example/page
<screenshot 2>
[Ref-2] https://official.example/other-page
```

Do not put all URLs before all screenshots. Do not leave a screenshot without the URL directly after it unless the example clearly does something else.

## First Row

The first row's company column is special:

- Fill it last.
- Keep the company name heading.
- Add `References:` and make only that label bold.
- List the URLs that appear in the detailed rows, in first-use order.
- Fill the nested comparison table's second column with short phrases or simple sentences.
- Do not change the nested table's row order, labels, or first-column text.

## Comment Formatting

For each main-table company-column row:

- The opening `[Comment:` label must be bold italic.
- The final `]` closing the comment block must be bold italic.
- The body text between them should remain normal unless the example uses another style.
- `[Ref-*]` URL lines should remain normal unless the example uses another style.

## Layout Preservation

- Preserve all original table structures, row order, first-column patent text, headers, footers, confidentiality footers, page numbering, and nested tables.
- Avoid altering column widths unless text or images clearly break the layout.
- Use image sizes that fit the second column. Around 2.8 to 3.0 inches wide is usually safe for narrow tables.
- Do not introduce extra pages with only one orphaned URL or a tiny leftover image if a modest image-size adjustment can avoid it.

## QA Checklist

Before delivery, verify:

- Every main-table second-column row has detailed text.
- Every main-table comment has a final `Herein...corresponds to...` sentence.
- `[Comment:` is bold italic in every detailed row.
- The final `]` of every comment block is bold italic.
- Evidence order is image then URL for every evidence item.
- `References:` in the first row is bold.
- First-row URL list contains every URL used in the row-level evidence, ordered by first appearance.
- Nested summary table second column is complete and concise.
- DOCX opens cleanly.
- Rendered pages show no clipping, broken tables, or missing images.
