#!/usr/bin/env python
"""Polish and validate common DOCX claim-chart formatting.

This helper is intentionally narrow:
- bolds the top-cell "References:" label,
- makes each main-row "[Comment:" label bold italic,
- makes the final closing bracket of each comment block bold italic,
- reorders evidence blocks from URL-then-image to image-then-URL when needed.

It does not write claim text or invent evidence.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt


FONT = "Times New Roman"


def set_font(run, size=10, bold=None, italic=None):
    run.font.name = FONT
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.rFonts
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    rfonts.set(qn("w:ascii"), FONT)
    rfonts.set(qn("w:hAnsi"), FONT)
    run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic


def clear_paragraph(paragraph):
    for child in list(paragraph._p):
        paragraph._p.remove(child)


def format_references_label(document):
    changed = 0
    if not document.tables:
        return changed
    for paragraph in document.tables[0].rows[0].cells[1].paragraphs:
        if paragraph.text.strip() == "References:":
            if len(paragraph.runs) == 1 and paragraph.runs[0].bold is True:
                return changed
            clear_paragraph(paragraph)
            run = paragraph.add_run("References:")
            set_font(run, bold=True, italic=False)
            changed += 1
            return changed
    return changed


def format_comment_opening(cell):
    if not cell.paragraphs:
        return 0
    paragraph = cell.paragraphs[0]
    text = paragraph.text
    label = "[Comment:"
    if not text.startswith(label):
        return 0
    if paragraph.runs and paragraph.runs[0].text == label and paragraph.runs[0].bold and paragraph.runs[0].italic:
        return 0

    style = paragraph.style
    alignment = paragraph.alignment
    fmt = paragraph.paragraph_format
    keep = {
        "left_indent": fmt.left_indent,
        "right_indent": fmt.right_indent,
        "first_line_indent": fmt.first_line_indent,
        "space_before": fmt.space_before,
        "space_after": fmt.space_after,
        "line_spacing": fmt.line_spacing,
    }
    clear_paragraph(paragraph)
    paragraph.style = style
    paragraph.alignment = alignment
    for key, value in keep.items():
        setattr(paragraph.paragraph_format, key, value)

    opening = paragraph.add_run(label)
    set_font(opening, bold=True, italic=True)
    body = paragraph.add_run(text[len(label) :])
    set_font(body, bold=False, italic=False)
    return 1


def format_comment_closing(cell):
    candidates = [p for p in cell.paragraphs if p.text.strip().endswith("]") and "Herein," in p.text]
    if not candidates:
        return 0
    paragraph = candidates[-1]
    for run in reversed(paragraph.runs):
        if not run.text.endswith("]"):
            continue
        if run.text == "]":
            if run.bold and run.italic:
                return 0
            set_font(run, bold=True, italic=True)
            return 1
        run.text = run.text[:-1]
        closing = paragraph.add_run("]")
        set_font(closing, bold=True, italic=True)
        return 1
    closing = paragraph.add_run("]")
    set_font(closing, bold=True, italic=True)
    return 1


def reorder_evidence(cell):
    changed = 0
    paragraphs = list(cell.paragraphs)
    i = 0
    while i < len(paragraphs) - 1:
        paragraph = paragraphs[i]
        next_paragraph = paragraphs[i + 1]
        is_ref = paragraph.text.strip().startswith("[Ref-")
        next_is_image = bool(next_paragraph._p.xpath(".//w:drawing"))
        if is_ref and next_is_image:
            parent = paragraph._p.getparent()
            parent.remove(next_paragraph._p)
            parent.insert(parent.index(paragraph._p), next_paragraph._p)
            changed += 1
            paragraphs = list(cell.paragraphs)
            i += 2
        else:
            i += 1
    return changed


def collect_issues(document):
    issues = []
    if len(document.tables) < 2:
        issues.append("Expected at least two tables: summary table and main claim table.")
        return issues

    summary_cell = document.tables[0].rows[0].cells[1]
    ref_paras = [p for p in summary_cell.paragraphs if p.text.strip() == "References:"]
    if not ref_paras:
        issues.append('Missing "References:" label in the first row second column.')
    elif not any(run.bold for run in ref_paras[0].runs):
        issues.append('"References:" is not bold.')

    for row_index, row in enumerate(document.tables[1].rows):
        cell = row.cells[1]
        if not cell.text.strip():
            issues.append(f"Row {row_index}: second column is empty.")
            continue
        if not cell.paragraphs[0].text.startswith("[Comment:"):
            issues.append(f"Row {row_index}: first paragraph does not start with [Comment:.")
        elif not (cell.paragraphs[0].runs and cell.paragraphs[0].runs[0].bold and cell.paragraphs[0].runs[0].italic):
            issues.append(f"Row {row_index}: [Comment: is not bold italic.")
        closers = [p for p in cell.paragraphs if p.text.strip().endswith("]") and "Herein," in p.text]
        if not closers:
            issues.append(f"Row {row_index}: missing Herein closing paragraph ending in ].")
        else:
            closing_run = None
            for run in reversed(closers[-1].runs):
                if run.text.endswith("]"):
                    closing_run = run
                    break
            if closing_run is None or not (closing_run.bold and closing_run.italic):
                issues.append(f"Row {row_index}: final ] is not bold italic.")

        sequence = []
        for paragraph in cell.paragraphs:
            if paragraph._p.xpath(".//w:drawing"):
                sequence.append("IMG")
            elif paragraph.text.strip().startswith("[Ref-"):
                sequence.append("REF")
        for seq_index in range(0, len(sequence), 2):
            pair = sequence[seq_index : seq_index + 2]
            if pair and pair != ["IMG", "REF"]:
                issues.append(f"Row {row_index}: evidence sequence should be image then ref, got {pair}.")
                break
    return issues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--check", action="store_true", help="Report issues without modifying the file.")
    args = parser.parse_args()

    document = Document(str(args.docx))
    if args.check:
        issues = collect_issues(document)
        if issues:
            print("\n".join(issues))
            raise SystemExit(1)
        print("No claim-chart polish issues found.")
        return

    changes = {
        "references_label": format_references_label(document),
        "comment_openings": 0,
        "comment_closings": 0,
        "evidence_reordered": 0,
    }
    if len(document.tables) >= 2:
        for row in document.tables[1].rows:
            cell = row.cells[1]
            changes["comment_openings"] += format_comment_opening(cell)
            changes["comment_closings"] += format_comment_closing(cell)
            changes["evidence_reordered"] += reorder_evidence(cell)

    document.save(str(args.docx))
    print("Saved:", args.docx)
    for key, value in changes.items():
        print(f"{key}: {value}")

    issues = collect_issues(Document(str(args.docx)))
    if issues:
        print("Remaining issues:")
        print("\n".join(issues))
        raise SystemExit(1)
    print("No claim-chart polish issues found.")


if __name__ == "__main__":
    main()
