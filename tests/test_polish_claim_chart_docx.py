"""Synthetic DOCX regressions. No client documents or web evidence are fixtures."""

from copy import deepcopy
from io import BytesIO
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile
import zlib

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import polish_claim_chart_docx as polish


SCRIPT = Path(polish.__file__)


def png(color):
    def chunk(kind, data):
        return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data))
    header = struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0)
    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', header) + chunk(b'IDAT', zlib.compress(b'\0' + bytes(color))) + chunk(b'IEND', b'')


def hyperlink(paragraph, url, label=None):
    element = OxmlElement('w:hyperlink')
    element.set(qn('r:id'), paragraph.part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True))
    run = OxmlElement('w:r')
    text = OxmlElement('w:t')
    text.text = label or url
    run.append(text)
    element.append(run)
    paragraph._p.append(element)
    return element


def reference(cell, number, fragment=''):
    paragraph = cell.add_paragraph(f'[Ref-{number}] ')
    hyperlink(paragraph, f'https://example.com/source-{number}' + fragment)
    return paragraph


def chart(order='image-first', broken_labels=False):
    doc = Document()
    doc.styles['Normal'].font.name = 'Calibri'
    doc.styles['Normal'].font.size = Pt(12)
    body_style = doc.styles.add_style('Comparison Body', WD_STYLE_TYPE.PARAGRAPH)
    body_style.base_style = doc.styles['Normal']
    body_style.font.italic = True
    summary = doc.add_table(rows=1, cols=2)
    summary.cell(0, 0).text = 'Synthetic claim chart'
    top = summary.cell(0, 1)
    top.paragraphs[0].text = 'Example Supplier'
    label = top.add_paragraph().add_run('References:')
    label.bold = not broken_labels
    reference(top, 1)
    reference(top, 2)
    nested = top.add_table(rows=2, cols=2)
    nested.cell(0, 0).text = 'Claim Feature'
    nested.cell(0, 1).text = 'Corresponding Element'
    nested.cell(1, 0).text = 'Sensing module'
    nested.cell(1, 1).text = 'Example perception subsystem'
    main = doc.add_table(rows=1, cols=2)
    main.cell(0, 0).text = 'a sensing module that collects road information;'
    cell = main.cell(0, 1)
    opening = cell.paragraphs[0]
    opening.style = body_style
    opening.paragraph_format.keep_with_next = True
    opening.paragraph_format.space_after = Pt(7)
    if broken_labels:
        opening.add_run('[Com').bold = False
        opening.add_run('ment: The published system has ').bold = False
    else:
        marker = opening.add_run('[Comment: ')
        marker.bold = marker.italic = True
        opening.add_run('The published system has ')
    opening.add_run('selective emphasis').bold = True
    opening.add_run(' and a ')
    hyperlink(opening, 'https://example.com/explanation', 'technical description')
    opening.add_run('.')
    herein = cell.add_paragraph()
    herein.style = body_style
    herein.add_run('Herein, “')
    herein.add_run('a sensing module that collects road information').bold = True
    herein.add_run('” corresponds to ')
    herein.add_run('the Example perception subsystem').bold = True
    if broken_labels:
        herein.add_run(', which senses traffic.]   ')
    else:
        herein.add_run(', which senses traffic.')
        marker = herein.add_run(']')
        marker.bold = marker.italic = True
    for number in (1, 2):
        if order == 'url-first':
            reference(cell, number)
        image = cell.add_paragraph()
        shape = image.add_run().add_picture(BytesIO(png((number * 80, 0, 0))), width=Inches(1))
        shape._inline.docPr.set('descr', f'Synthetic image for source {number}')
        if order == 'image-first':
            reference(cell, number)
    doc.sections[0].footer.paragraphs[0].text = 'Synthetic footer, retained verbatim'
    return doc


def codes(document, template=None):
    return {issue.code for issue in polish.collect_issues(document, template)}


class EvidenceTests(unittest.TestCase):
    def test_already_correct_pairs_are_unchanged_on_repeated_repairs(self):
        doc = chart()
        cell = doc.tables[1].cell(0, 1)
        original = cell._tc.xml
        self.assertEqual(polish.reorder_evidence(cell), 0)
        self.assertEqual(polish.reorder_evidence(cell), 0)
        self.assertEqual(cell._tc.xml, original)
        self.assertEqual(codes(doc), set())

    def test_explicit_url_first_repair_keeps_source_image_identity(self):
        doc = chart('url-first')
        cell = doc.tables[1].cell(0, 1)
        events = polish.evidence_events(cell)
        before = [(events[i][1]._p.xml, events[i + 1][1]._p.xml) for i in (0, 2)]
        self.assertIn('EVIDENCE_ORDER', codes(doc))
        self.assertEqual(polish.reorder_evidence(cell), 2)
        events = polish.evidence_events(cell)
        after = [(events[i + 1][1]._p.xml, events[i][1]._p.xml) for i in (0, 2)]
        self.assertEqual(before, after)
        self.assertEqual(polish.reorder_evidence(cell), 0)
        self.assertEqual(codes(doc), set())

    def test_mixed_evidence_is_rejected_without_moving_anything(self):
        doc = chart('url-first')
        cell = doc.tables[1].cell(0, 1)
        reference(cell, 3)
        original = cell._tc.xml
        with self.assertRaises(polish.UnsafeRepair):
            polish.reorder_evidence(cell)
        self.assertEqual(original, cell._tc.xml)

    def test_caption_between_url_and_image_requires_manual_pairing(self):
        doc = chart('url-first')
        cell = doc.tables[1].cell(0, 1)
        events = polish.evidence_events(cell)
        caption = cell.add_paragraph('Caption belongs to an evidence block.')
        events[1][1]._p.addprevious(caption._p)
        original = cell._tc.xml
        with self.assertRaises(polish.UnsafeRepair):
            polish.reorder_evidence(cell)
        self.assertEqual(original, cell._tc.xml)

    def test_supplementary_references_and_pdf_page_fragments_are_valid(self):
        doc = chart()
        reference(doc.tables[0].cell(0, 1), 3)
        reference(doc.tables[1].cell(0, 1), 3, '#page=18')
        self.assertEqual(codes(doc), set())


class FormattingTests(unittest.TestCase):
    def test_marker_repairs_preserve_body_typography_hyperlinks_and_properties(self):
        doc = chart(broken_labels=True)
        cell = doc.tables[1].cell(0, 1)
        paragraphs = polish.comment_paragraphs(cell)
        text_before = [polish.paragraph_text(p) for p in paragraphs]
        opening = paragraphs[0]
        ppr = opening._p.pPr.xml
        link = opening._p.xpath('.//w:hyperlink')[0].xml
        emphasis = next(r for r in opening.runs if r.text == 'selective emphasis')
        emphasis_xml = emphasis._r.xml
        left = doc.tables[1].cell(0, 0)._tc.xml
        self.assertEqual(polish.format_references_label(doc), 1)
        self.assertEqual(polish.format_comment_opening(cell), 1)
        self.assertEqual(polish.format_comment_closing(cell), 1)
        self.assertEqual([polish.paragraph_text(p) for p in polish.comment_paragraphs(cell)], text_before)
        self.assertEqual(opening._p.pPr.xml, ppr)
        self.assertEqual(opening._p.xpath('.//w:hyperlink')[0].xml, link)
        self.assertEqual(emphasis._r.xml, emphasis_xml)
        self.assertEqual(doc.tables[1].cell(0, 0)._tc.xml, left)
        body = next(r for r in opening.runs if 'The published system' in r.text)
        self.assertFalse(polish.effective(body, opening, 'bold'))
        self.assertTrue(polish.effective(body, opening, 'italic'))
        self.assertIsNone(body.font.name)
        self.assertEqual(doc.styles['Normal'].font.name, 'Calibri')
        self.assertEqual(doc.styles['Normal'].font.size.pt, 12)
        self.assertEqual(codes(doc), set())
        before_second = doc.element.xml
        self.assertEqual(polish.format_references_label(doc), 0)
        self.assertEqual(polish.format_comment_opening(cell), 0)
        self.assertEqual(polish.format_comment_closing(cell), 0)
        self.assertEqual(doc.element.xml, before_second)

    def test_character_style_inheritance_is_recognized(self):
        doc = chart()
        style = doc.styles.add_style('Comment Marker', WD_STYLE_TYPE.CHARACTER)
        style.font.bold = style.font.italic = True
        opening = doc.tables[1].cell(0, 1).paragraphs[0]
        opening.runs[0].style = style
        opening.runs[0].bold = opening.runs[0].italic = None
        before = opening._p.xml
        self.assertEqual(polish.format_comment_opening(doc.tables[1].cell(0, 1)), 0)
        self.assertEqual(opening._p.xml, before)
        self.assertNotIn('COMMENT_OPENING', codes(doc))

    def test_three_reported_template_regressions_are_detected(self):
        reference_doc = chart()
        doc = chart()
        doc.tables[0].cell(0, 1).add_paragraph('Comparison as of a new date; extra scope prose.')
        cell = doc.tables[1].cell(0, 1)
        cell.paragraphs[0].add_run(' [Ref-1; Ref-2]')
        herein = polish.comment_paragraphs(cell)[-1]
        for run in herein.runs:
            if run.text not in (']',):
                run.bold = False
        self.assertTrue({'SUMMARY_PROSE', 'INLINE_REFERENCE', 'CLAIM_EMPHASIS', 'MAPPING_EMPHASIS'} <= codes(doc, reference_doc))

    def test_template_can_explicitly_use_prose_inline_refs_and_plain_correspondence(self):
        doc = chart()
        doc.tables[0].cell(0, 1).add_paragraph('Scope required by this reference.')
        cell = doc.tables[1].cell(0, 1)
        cell.paragraphs[0].add_run(' [Ref-1]')
        for run in polish.comment_paragraphs(cell)[-1].runs:
            if run.text != ']':
                run.bold = False
        self.assertEqual(codes(doc, deepcopy(doc)), set())

    def test_entire_herein_bold_is_not_a_substitute_for_two_spans(self):
        doc = chart()
        for run in polish.comment_paragraphs(doc.tables[1].cell(0, 1))[-1].runs:
            run.bold = True
        self.assertIn('CORRESPONDENCE_FRAME', codes(doc))

    def test_abbreviated_claim_is_detected_against_same_limitation(self):
        reference_doc = chart()
        doc = chart()
        herein = polish.comment_paragraphs(doc.tables[1].cell(0, 1))[-1]
        herein.runs[1].text = 'a sensing module ... road information'
        self.assertIn('CLAIM_PHRASE', codes(doc, reference_doc))

    def test_empty_nested_summary_and_missing_source_are_reported(self):
        doc = chart()
        doc.tables[0].cell(0, 1).tables[0].cell(1, 1).text = ''
        reference(doc.tables[1].cell(0, 1), 3)
        self.assertTrue({'SUMMARY_EMPTY', 'REFERENCE_MISSING', 'REFERENCE_ORDER'} <= codes(doc))

    def test_source_number_cannot_silently_point_to_a_different_url(self):
        doc = chart()
        cell = doc.tables[1].cell(0, 1)
        paragraph = polish.evidence_events(cell)[1][1]
        link = paragraph._p.xpath('.//w:hyperlink')[0]
        # Keep the top line intact and change only the row's hyperlink target.
        link.set(qn('r:id'), paragraph.part.relate_to('https://example.com/third', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True))
        self.assertIn('REFERENCE_MISMATCH', codes(doc))

    def test_missing_hereins_do_not_misclassify_source_lines_as_inline_tags(self):
        doc = chart()
        cell = doc.tables[1].cell(0, 1)
        herein = polish.comment_paragraphs(cell)[-1]
        herein._p.getparent().remove(herein._p)
        self.assertIn('HEREIN', codes(doc))
        self.assertNotIn('INLINE_REFERENCE', codes(doc))

    def test_unsupported_layout_returns_diagnostic(self):
        doc = Document()
        doc.add_table(rows=1, cols=1)
        doc.add_table(rows=1, cols=1)
        self.assertEqual(codes(doc), {'LAYOUT'})


class FileTests(unittest.TestCase):
    def test_default_cli_is_read_only(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'source.docx'
            chart().save(source)
            original = source.read_bytes()
            result = subprocess.run([sys.executable, str(SCRIPT), str(source)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(source.read_bytes(), original)

    def test_repaired_output_preserves_original_and_all_other_package_parts(self):
        with tempfile.TemporaryDirectory() as directory:
            source, output = [Path(directory) / name for name in ('source.docx', 'output.docx')]
            chart(broken_labels=True).save(source)
            with ZipFile(source, 'a') as archive:
                archive.writestr('opaque-fixture.bin', b'Preserve this unrelated package part.')
            original = source.read_bytes()
            result = subprocess.run([sys.executable, str(SCRIPT), str(source), '--fix-labels', '--output', str(output)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(source.read_bytes(), original)
            with ZipFile(source) as old, ZipFile(output) as new:
                self.assertEqual(old.namelist(), new.namelist())
                self.assertEqual([name for name in old.namelist() if old.read(name) != new.read(name)], ['word/document.xml'])
            self.assertEqual(codes(Document(output)), set())

    def test_repairs_require_separate_output_and_reject_in_place_path(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'source.docx'
            chart().save(source)
            original = source.read_bytes()
            for extra in (['--fix-labels'], ['--fix-labels', '--output', str(source)]):
                result = subprocess.run([sys.executable, str(SCRIPT), str(source), *extra], capture_output=True, text=True)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(source.read_bytes(), original)


if __name__ == '__main__':
    unittest.main()
