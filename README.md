# claim-chart

Codex skill for producing high-quality patent comparison claim charts in Word.

Use this skill when you have:

- a target `.docx` claim-chart file to fill,
- a completed example `.docx` to imitate,
- a target company name,
- and a requirement to fill the company-comparison column in English with official-source evidence, screenshots, references, and preserved Word formatting.

The skill output is a polished Word document. Publishing or uploading the skill itself is an external distribution step and is not part of the claim-chart workflow.

The supplied reference controls opening content, citation placement, typography and correspondence emphasis. Partner technical sources require a documented connection to the assessed product or deployment; the skill keeps platform disclosures separate from confirmed deployment facts.

The DOCX helper checks by default and requires an explicit output path for repairs:

```sh
python scripts/polish_claim_chart_docx.py chart.docx --check --template reference.docx
python scripts/polish_claim_chart_docx.py chart.docx --fix-labels --output polished.docx
```

With `python-docx` installed, run the synthetic regression tests using:

```sh
python -m unittest discover -s tests -v
```
