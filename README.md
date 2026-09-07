<a id="top"></a>

<p align="center">
  <img src="assets/readme/hero-handdrawn.png" alt="Claim Chart — a hand-drawn journey from patent claims, through technical evidence, to a completed comparison document" width="100%">
</p>

<h1 align="center">Claim Chart</h1>

<p align="center">
  <strong>From patent language to a carefully sourced comparison.</strong><br>
  A Codex skill for researching, writing, and polishing claim charts in Word.
</p>

<p align="center">
  <img src="assets/readme/badges.svg" alt="Codex skill · Word documents · Official-source research" width="432">
</p>

<p align="center">
  <a href="#quick-start"><strong>Get started</strong></a> &nbsp;·&nbsp;
  <a href="SKILL.md">Read the skill</a> &nbsp;·&nbsp;
  <a href="https://github.com/yejingchen123/claim-chart/issues">Report an issue</a>
</p>

<p align="center">
  <strong>English</strong> &nbsp; / &nbsp; <a href="README.zh-CN.md">简体中文</a>
</p>

---

<p align="center">
  <a href="#overview">Overview</a> &nbsp; / &nbsp;
  <a href="#quick-start">Quick start</a> &nbsp; / &nbsp;
  <a href="#workflow">Workflow</a> &nbsp; / &nbsp;
  <a href="#docx-helper">DOCX helper</a> &nbsp; / &nbsp;
  <a href="#inside-the-repository">Repository</a>
</p>

<a id="overview"></a>

## A research workflow with an eye for the details

Bring a claim-chart draft, a completed reference, and a company to assess. The skill guides Codex through the company-side analysis: identify the relevant product, connect each claim element to technical evidence, and assemble a finished `.docx` in the reference's style.

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="assets/readme/template.svg" width="36" alt=""><br>
      <strong>Your template sets the design</strong><br>
      Preserve patent text, table geometry, typography, opening structure, and the reference's evidence layout.
    </td>
    <td width="50%" valign="top">
      <img src="assets/readme/evidence.svg" width="36" alt=""><br>
      <strong>Evidence you can trace</strong><br>
      Research official product pages and technical documents, then pair relevant source captures with their URLs.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="assets/readme/mapping.svg" width="36" alt=""><br>
      <strong>Careful technical correspondence</strong><br>
      Distinguish confirmed deployment facts, partner-platform disclosures, and mappings that remain unconfirmed.
    </td>
    <td width="50%" valign="top">
      <img src="assets/readme/review.svg" width="36" alt=""><br>
      <strong>Review down to the page</strong><br>
      Check common DOCX issues, render the document, and inspect every page for layout and evidence readability.
    </td>
  </tr>
</table>

> **The reference is the design contract.** If it has no introductory paragraph, inline citation tags, or evidence captions, the completed chart should not add them.

<a id="quick-start"></a>

## Start with three inputs

| Bring | What it provides |
| :--- | :--- |
| **Target `.docx`** | The claim rows and company column to complete. |
| **Reference `.docx`** | A finished example that defines wording, formatting, and evidence placement. |
| **Target company** | The company to assess, plus a product, deployment, or period if you have one in mind. |

### 1. Make the skill available

In Codex, ask the built-in skill installer:

```text
Use $skill-installer to install the claim-chart skill from
https://github.com/yejingchen123/claim-chart (the skill is at the repository root).
```

<details>
<summary><strong>Prefer a manual installation?</strong></summary>

For a personal installation on macOS or Linux:

```sh
mkdir -p ~/.agents/skills
git clone https://github.com/yejingchen123/claim-chart.git ~/.agents/skills/claim-chart
```

Codex discovers personal skills in `~/.agents/skills`. If the new skill does not appear, restart Codex. See the [official skills guide](https://learn.chatgpt.com/docs/build-skills) for installation locations and invocation details.

</details>

### 2. Open your working folder

Place the two Word files in a private working folder and open it in Codex. The workflow needs access to web research, source screenshots, DOCX editing, and a document renderer. Use the document tools available in your environment; this repository supplies the claim-chart instructions and a Python checking helper.

### 3. Give Codex the task

Replace the example names below with your files and company:

```text
Use $claim-chart to complete target.docx for ExampleCo.
Use reference.docx as the formatting and writing reference.

Fill the company column in English with official-source evidence.
Preserve the patent text and table structure. Match the reference's
opening, emphasis, citation style, and screenshot/URL layout.
Keep any unconfirmed correspondence explicit, inspect every rendered
page, and save the finished document as completed.docx.
```

**Your deliverable:** a completed Word claim chart. Original documents, source captures, research notes, and render checks stay in the private working folder.

<a id="workflow"></a>

## From reference to finished chart

| Step | Focus | Result |
| :---: | :--- | :--- |
| **01** | **Read the reference** | Record its structure, writing style, emphasis, and evidence conventions. |
| **02** | **Establish the scope** | Identify the actual product or service, provider, deployment, and relevant period. |
| **03** | **Research and map** | Write the row-level comparison; connect each mapping to attributable evidence. |
| **04** | **Assemble in Word** | Insert screenshots and URLs; finish the opening references and nested summary. |
| **05** | **Check and review** | Run the helper, inspect every rendered page, and correct layout or style drift. |

### What a correspondence sentence looks like

The shape of a typical mapping, using placeholders:

> Herein, “**[complete claim phrase]**” corresponds to **[supported product feature]**.

Both sides receive the reference's emphasis. The supporting prose explains the connection and keeps material limitations beside it.

<details>
<summary><strong>How partner evidence is handled</strong></summary>

A company may offer a service powered by a partner's technology. The research must establish that connection and retain the partner's attribution.

| Evidence supports… | The comparison should say… |
| :--- | :--- |
| The feature in the assessed service or configuration | **Deployment confirmed** |
| The feature in a supplier's platform, without deployment-specific confirmation | **Platform disclosed** |
| A plausible match that still depends on an assumption or missing implementation detail | **Correspondence inferred or unconfirmed** |

These distinctions guide the existing prose; they do not require a new table in the delivered chart. Read the [research and evidence boundaries](references/research-evidence.md).

</details>

<a id="docx-helper"></a>

## A small helper for the finishing work

The bundled Python script checks common structural and formatting problems. **Checks are read-only by default; repairs require a separate output file.**

Run these commands from the skill's repository folder, with `python-docx` installed in your Python environment:

```sh
python -m pip install python-docx
```

**Inspect a chart against its reference**

```sh
python scripts/polish_claim_chart_docx.py chart.docx --check --template reference.docx
```

**Repair the `References:`, `[Comment:`, and closing `]` labels**

```sh
python scripts/polish_claim_chart_docx.py chart.docx --fix-labels --output polished.docx
```

<details>
<summary><strong>Options and supported layout</strong></summary>

| Option | Behavior |
| :--- | :--- |
| `--check` | Validate without changing the input. This is the default. |
| `--template reference.docx` | Check conventions inferred from the supplied reference. |
| `--fix-labels` | Repair only the reference and comment markers, preserving other run formatting. |
| `--reorder-url-first` | Explicitly convert a confirmed, uniform URL/image sequence to image/URL order. |
| `--output polished.docx` | Write repairs to a separate file; in-place overwrites are refused. |

The checker targets the common layout with two outer tables, the company in column two, and image-first evidence. Mixed or ambiguous evidence sequences need manual pairing. A different reference convention may require manual review.

The helper does not research sources, determine factual correspondence, or replace a visual review of the Word document.

</details>

<a id="inside-the-repository"></a>

## Inside the repository

```text
claim-chart/
├── SKILL.md                         The complete agent workflow
├── agents/openai.yaml               Skill name and invocation metadata
├── references/
│   ├── style-contract.md            Writing, formatting, and evidence layout
│   └── research-evidence.md         Scope, attribution, and evidence strength
├── scripts/
│   └── polish_claim_chart_docx.py   Read-only checks and explicit repairs
├── tests/
│   └── test_polish_claim_chart_docx.py
└── assets/readme/                   Illustrated README artwork
```

<a id="contributing"></a>

## Help refine the craft

Issues and pull requests are welcome, especially for reproducible formatting problems, clearer evidence rules, and additional template conventions. Include the expected behavior and a small **synthetic** example when reporting a bug.

Run the regression tests after changing the helper:

```sh
python -m unittest discover -s tests -v
```

Keep client documents, actual evidence captures, and QA output out of this public repository. The test suite builds its own synthetic DOCX fixtures.

---

<p align="center">
  Made with care by <a href="https://github.com/yejingchen123">yejingchen123</a>.<br>
  Layout inspiration: <a href="https://github.com/othneildrew/Best-README-Template">Best-README-Template</a>.<br>
  <sub>The hand-drawn cover is AI-generated conceptual artwork. <a href="assets/readme/ARTWORK.md">Artwork notes</a>.</sub>
</p>

<p align="center"><a href="#top">↑ Back to top</a></p>
