# Claim Chart Style Contract

Use this reference for every claim-chart filling task.

## Template Authority

Inspect the actual reference, including its Word runs. Record the opening sequence, font family/size, body italics, emphasized phrases, reference placement and evidence order before authoring. Preserve these choices unless the user requests a change. Do not interpret general permission to improve quality as permission to add a cover summary, change body typography or introduce inline citation tags.

## Writing Pattern

Each main-table company-column cell should generally contain:

1. A visible comment block beginning with `[Comment:`.
2. One or more detailed paragraphs mapping the patent row to company technology.
3. A final correspondence sentence:
   `Herein, "{patent content}" corresponds to {company technology content}.]`
4. Evidence screenshots and URL lines.

The patent content inside the `Herein` sentence should reproduce the complete relevant phrase for that row, not a generic restatement of the entire claim or an ellipsis that hides a limitation. The company technology content should name the exact product, module, sensor, cloud service, controller, algorithm, or feature being compared. Preserve substantive conditions and unconfirmed deployment details in the sentence or immediately adjacent prose.

If the reference emphasizes the correspondence, reproduce two distinct bold spans:

> Herein, “**a sensing module provided in an AV**” corresponds to **the identified vehicle sensor and perception subsystem**, which collects the surrounding road information.]

In Word, apply actual run formatting to both phrases; do not insert literal Markdown markers. Keep `Herein,`, quotation marks and `corresponds to` in the surrounding body style. In an italic template, both highlighted phrases are bold italic while the connecting text stays italic. The helper checks that the claim is bold and the mapped element starts with bold text; human review must verify the full intended product phrase is emphasized.

When the reference has no inline citations, do not append `[Ref-1; Ref-2]`, footnote markers or similar tags to Comment paragraphs. Keep the row's complete source trail in the evidence/reference area below the comment. Supplementary sources without a screenshot may have their own URL lines there.

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

An official supplier page is evidence about that supplier. Its applicability to the named target depends on the product/deployment connection; follow [research and evidence boundaries](research-evidence.md). Keep company roles and unresolved mappings equally clear in the detailed rows and nested summary.

## Evidence Ordering

The required order inside each row is:

```text
<screenshot 1>
[Ref-1] https://official.example/page
<screenshot 2>
[Ref-2] https://official.example/other-page
```

Do not put all URLs before all screenshots. Do not leave a screenshot without its own URL directly after it unless the example clearly does something else. Preserve source identity when moving blocks: the URL after screenshot 1 must not be moved with screenshot 2. Never infer a pairing solely because a URL happens to precede the next image.

Match the reference's evidence fields exactly. When it has only screenshots and `[Ref-*] URL` lines, do not add source titles, image captions, descriptions such as “excerpt identifying…”, `Published`/`Accessed` dates, or plain-text PDF page notes. This applies both to separate paragraphs and to extra prose appended to a reference line. Metadata belongs in local source notes. A PDF `#page=18` fragment can stay in the URL without creating another visible field. Include captions or other fields only when the reference shows them or the user explicitly asks for them; perceived usefulness alone is not a reason to add them.

## First Row

The first row's company column is special:

- Fill it last.
- Keep the company name heading.
- When the reference has no intervening prose, proceed directly to `References:`. Do not add a comparison title, date, assessed-service paragraph or access-date note above the references or nested table. Put necessary scope qualifications inside the existing detailed Comment cells; keep access dates in local source notes unless the reference or user requires a visible date field.
- Add `References:` and make only that label bold.
- List the URLs that appear in the detailed rows, in first-use order.
- Fill the nested comparison table's second column with short phrases or simple sentences.
- Do not change the nested table's row order, labels, or first-column text.

## Comment Formatting

For each main-table company-column row:

- The opening `[Comment:` label must be bold italic.
- The final `]` closing the comment block must be bold italic.
- The body text between them should remain normal unless the example uses another style.
- Match the body font, size and italic treatment to the reference. Preserve selective bold emphasis, hyperlinks and paragraph properties when adjusting only the opening or closing marker.
- Bold the claim phrase and corresponding product phrase in every `Herein` paragraph when this is the reference's convention. Do not bold the entire paragraph as a shortcut.
- `[Ref-*]` URL lines should remain normal unless the example uses another style.

## Layout Preservation

- Preserve all original table structures, row order, first-column patent text, headers, footers, confidentiality footers, page numbering, and nested tables.
- Keep column widths and page geometry fixed unless the user authorizes a change. First shorten repetitive prose, adjust paragraph spacing or size evidence to fit.
- Use image sizes that fit the actual second column and remain legible at final scale.
- Do not introduce extra pages with only one orphaned URL or a tiny leftover image if a modest image-size adjustment can avoid it.

## QA Checklist

Before delivery, verify:

- The opening sequence matches the reference, with no added preamble.
- Comment prose contains no inline reference tags when the reference has none.
- Every main-table second-column row has detailed text.
- Every main-table comment has a final `Herein...corresponds to...` sentence.
- `[Comment:` is bold italic in every detailed row.
- The final `]` of every comment block is bold italic.
- Both correspondence phrases have the reference's emphasis; the connecting text retains the body style.
- Evidence order is image then URL for every evidence item.
- Evidence fields match the reference: no added captions, source titles, excerpt explanations, dates or prose after URL lines when the reference contains only screenshots and references.
- `References:` in the first row is bold.
- First-row URL list contains every URL used in the row-level evidence, ordered by first appearance.
- Nested summary table second column is complete and concise.
- Target-company, supplier and deployment attribution is accurate, and summary certainty matches the detailed evidence.
- Protected left-column text, table properties and nested labels match the original target; headers, footers and field codes are preserved.
- DOCX opens cleanly.
- Every rendered page has been inspected for clipping, broken tables, missing images, orphaned fragments and incorrect page totals.
