---
name: medical-review-manuscript-pipeline
description: Use this skill to draft, expand, polish, audit, and prepare medical review manuscripts, Opinion Reviews, narrative reviews, correspondence articles, and translational biomedical reviews for journal submission. It supports topic framing, literature synthesis, citation integrity checks, Word manuscript audits, SCI-style tables, figure quality checks, language polishing, and reviewer-style pre-submission critique.
---

# Medical Review Manuscript Pipeline

## Use When

Use this skill when the user wants to:

- Draft or expand a medical review manuscript.
- Convert a topic memo into an Opinion Review or narrative review.
- Improve an existing Word manuscript for journal submission.
- Audit in-text citations, references, tables, figures, and formatting.
- Reduce AI-like language and strengthen journal-style academic tone.
- Prepare a pre-submission quality-control report.

## Core Principle

The goal is not to make the manuscript longer. The goal is to make it more publishable:

```text
clinical problem -> knowledge gap -> evidence synthesis -> controversy -> author viewpoint -> future direction
```

## Standard Workflow

1. **Classify the manuscript type**
   Determine whether the work is a Narrative Review, Opinion Review, Commentary, Letter, systematic review-style narrative synthesis, or translational clinical review.

2. **Identify the target journal constraints**
   Check article type, word limit, abstract format, reference style, figure/table limits, ethics requirements, AI-use declaration, and data availability requirements.

3. **Frame the central argument**
   Define the clinical problem, why existing evidence is insufficient, what the manuscript adds, and what a reader should remember.

4. **Build or revise the outline**
   Use a logic-forward structure rather than a literature dump:
   `Introduction -> mechanisms/pathophysiology -> current evidence -> controversies -> clinical implications -> future directions -> conclusion`.

5. **Audit references**
   Ensure every reference is real, relevant, cited in the text, and formatted consistently. Avoid citation dumping such as `[1-15]`.

6. **Improve tables and figures**
   Tables should answer a specific scientific or clinical question. Figures should clarify mechanisms, decision pathways, evidence gaps, or future roadmaps.

7. **Polish language**
   Replace template-like transitions, excessive certainty, and generic AI phrasing with precise, cautious, evidence-aligned academic writing.

8. **Run pre-submission review**
   Check structure, claims, evidence strength, abbreviations, figure quality, table format, references, statements, and journal compliance.

## Manuscript Rules

- Do not fabricate references.
- Do not overstate causal or clinical conclusions.
- Define all abbreviations at first use.
- Keep abstract and conclusion proportional to evidence strength.
- Use cautious language for exploratory, retrospective, small-sample, or non-randomized findings.
- Separate hypothesis-generating claims from validated clinical recommendations.
- Ensure every paragraph has a clear function.
- Place citations precisely; avoid citation dumps.
- Use consistent statistical formatting: `n = 40`, `P < 0.001`, `OR = 1.35`, `95% CI 1.10-1.66`.
- For Word documents, inspect tables, figure DPI, captions, references, and declarations.

## Recommended Outputs

Depending on the user's request, provide one or more of:

- Structured review outline.
- Revised manuscript text.
- Reference audit report.
- Table and figure redesign plan.
- Figure legend edits.
- Pre-submission checklist.
- Reviewer-style critique.
- Submission-readiness rating.

## When More Detail Is Needed

Load only the relevant bundled resources:

- `prompts/` for reusable prompt templates.
- `checklists/` for submission audits.
- `journal_profiles/` for journal-style constraints.
- `scripts/` for DOCX structure, reference, figure, and table checks.
- `examples/` for before/after writing and formatting patterns.

