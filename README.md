# Medical Review Manuscript Pipeline

An AI-assisted workflow for drafting, revising, auditing, and preparing medical review manuscripts for journal submission.

This is not another academic prompt collection. It is a submission-oriented workflow for medical reviews: citation-aware, table-aware, figure-aware, and reviewer-aware.

## Why This Exists

Many AI-assisted medical reviews fail for predictable reasons:

- The manuscript reads like a literature dump rather than a clinical argument.
- Citations are out of order, overpacked, or poorly matched to claims.
- Tables are long, repetitive, or formatted like office documents.
- Figures are visually attractive but too low-resolution for submission.
- Conclusions overstate the strength of exploratory evidence.
- Required submission statements are missing.

This project turns those recurring problems into a reusable workflow.

## What It Does

- Frames the review around a clinical problem and knowledge gap.
- Builds an Opinion Review or narrative review structure.
- Audits in-text citation order and reference consistency.
- Helps redesign tables and figures for SCI-style submission.
- Checks Word manuscripts for structure, tables, and embedded image DPI.
- Reduces AI-like transitions and overconfident academic phrasing.
- Produces reviewer-style pre-submission critiques.

## Quick Start

Use the skill with a manuscript or topic:

```text
Use medical-review-manuscript-pipeline to evaluate this manuscript for SCI submission readiness.
```

For Word documents:

```bash
python scripts/extract_docx_structure.py manuscript.docx --out structure.md
python scripts/check_reference_order.py manuscript.docx
python scripts/check_image_dpi.py manuscript.docx --out image_report.csv
python scripts/format_three_line_tables.py manuscript.docx --out manuscript_three_line_tables.docx
```

## Example Audit Report

See a real anonymized manuscript audit example:

- [`examples/example_manuscript_audit_report.md`](examples/example_manuscript_audit_report.md)

## Repository Structure

```text
medical-review-manuscript-pipeline/
  SKILL.md
  README.md
  LICENSE
  requirements.txt
  prompts/
  checklists/
  journal_profiles/
  scripts/
  examples/
  agents/
```

## Best Use Cases

- Medical narrative reviews.
- Opinion Reviews.
- Clinical translational reviews.
- Biomedical mechanism-focused reviews.
- Letters and correspondence needing concise peer-review style.
- Manuscripts requiring Word, reference, table, and figure audits.

## Core Workflow

```text
Topic -> Knowledge gap -> Outline -> Literature synthesis -> Draft -> Tables/Figures -> Reference audit -> Language polish -> Pre-submission review
```

## Differentiators

- **Citation-aware**: checks citation order and citation density.
- **Evidence-aware**: separates validated claims from hypothesis-generating claims.
- **Table-aware**: turns office-style tables into publication-style evidence matrices.
- **Figure-aware**: checks embedded image DPI and recommends replacement.
- **Reviewer-aware**: evaluates the manuscript as a skeptical journal reviewer would.

## Disclaimer

This project supports academic writing and manuscript preparation only. It does not provide medical advice, diagnosis, or treatment recommendations. All references, factual claims, journal requirements, and clinical statements must be independently verified before submission.
