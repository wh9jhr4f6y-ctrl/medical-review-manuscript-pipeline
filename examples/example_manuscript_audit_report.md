# Example Manuscript Audit Report

This is an anonymized example generated from a real Word manuscript using the Medical Review Manuscript Pipeline.

## Manuscript Type

Original research-style biomedical manuscript with:

- Public transcriptomic dataset analysis.
- Supportive external dataset analysis.
- Retrospective clinical cohort.
- Tables, figures, references, and prediction-model reporting.

## Overall Submission Readiness

**Recommendation: Major formatting and technical revision before submission.**

The manuscript has a coherent scientific structure and a complete citation chain. However, several submission-facing issues should be corrected before journal upload, especially figure resolution, statistical formatting, table notes, ethics/declaration completeness, and evidence-boundary wording.

## Automated DOCX Structure Summary

- Non-empty paragraphs: 114
- Tables: 6
- Embedded figures detected: 6
- Approximate word count: 4,800-5,000 words
- Reference count: 28

## Citation Integrity Audit

Automated numeric citation check:

```text
Citation groups: 29
First-mention order: [1, 2, 3, ..., 28]
Missing in sequential order: []
References listed but not cited: []
Citations missing from reference list: []
Long citation groups (> 3 refs): []
```

### Interpretation

The reference system is structurally strong. In-text citations appear in sequential order, all listed references are cited, and no excessive citation dumping was detected.

### Remaining Reference Recommendations

- Verify every DOI manually before submission.
- Standardize author truncation rules.
- Standardize journal abbreviations.
- Remove hidden non-breaking spaces around `et al.` if present.
- Replace older non-foundational references with newer evidence where possible.

## Figure Quality Audit

| Figure | Pixel size | Display size | Minimum effective DPI | Assessment |
|---|---:|---:|---:|---|
| Figure 1 | 2155 x 2746 | 7.10 x 9.05 in | 303.3 | Acceptable for color/grayscale |
| Figure 2 | 3268 x 1825 | 6.30 x 3.52 in | 518.7 | Good for combination artwork |
| Figure 3 | 1086 x 1448 | 6.30 x 8.40 in | 172.4 | High risk |
| Figure 4 | 1448 x 1086 | 6.30 x 4.72 in | 229.8 | Borderline |
| Figure 5 | 10860 x 3620 | 6.22 x 2.07 in | 1745.2 | Excellent |
| Figure 6 | 7240 x 5430 | 6.26 x 4.69 in | 1156.6 | Excellent |

### Interpretation

Figures 3 and 4 are the main technical risk. They may appear acceptable on screen but are below typical submission expectations for figures containing labels, heatmaps, plots, or multi-panel scientific content. These figures should be re-exported at higher resolution before submission.

Recommended targets:

- Color/grayscale figure: at least 300 dpi.
- Combination artwork: at least 500 dpi.
- Line art: at least 1000 dpi.

## Table Audit

The manuscript contains six tables. The table count is acceptable for a data-rich manuscript, but submission quality would improve if:

- All table titles use the same capitalization style.
- All table notes define abbreviations consistently.
- `P value` formatting is uniform.
- Statistical expressions use spaces consistently, such as `P < 0.001`.
- Exploratory model rows are clearly separated from primary model rows.
- Tables are formatted as three-line tables when required by the journal.

## Formatting Issues Detected

### High Priority

- Structured abstract labels used non-English full-width punctuation in the source manuscript, e.g., `Background：`. These should be changed to `Background:`.
- Statistical spacing was inconsistent, e.g., `n=6`, `P<0.001`, `OR=16.34`. Use `n = 6`, `P < 0.001`, `OR = 16.34`.
- Greek and spelled-out terminology should be standardized, e.g., use `TGF-β` consistently rather than mixing `TGF-beta` and `TGF-β`.
- Ethics approval and consent/waiver statements should be included for clinical retrospective data.

### Moderate Priority

- Figure legends are generally informative but should ensure every abbreviation is defined.
- Table footnotes should be harmonized.
- Formula lines should be visually separated from ordinary prose.
- The conclusion should be shortened and made more proportional to the exploratory nature of the evidence.

### Minor Priority

- Smart quotes and em dashes should be checked against journal style.
- Non-breaking spaces should be removed from references if they affect formatting.
- Author affiliation superscripts should be formatted consistently.

## Scientific and Methodological Caution

The manuscript uses small public datasets and a retrospective clinical cohort. The following wording principles are recommended:

- Use `supports` rather than `confirms` for supportive external dataset analysis.
- Use `exploratory` for unvalidated scores or nomograms.
- Avoid implying direct clinical adoption before prospective validation.
- State that retrospective adjustment and weighting reduce but do not eliminate residual confounding.

## Suggested Priority Order Before Submission

1. Replace or re-export low-resolution figures.
2. Add ethics approval, consent/waiver, funding, conflict of interest, author contribution, and data availability statements.
3. Standardize statistical formatting.
4. Harmonize table titles, notes, and three-line formatting.
5. Shorten and temper the conclusion.
6. Recheck all DOI and reference formatting.
7. Run final citation-order and image-DPI scripts again.

## Example Final Verdict

The manuscript is scientifically promising and structurally coherent, but it is not yet technically submission-ready. After correcting figure resolution, declarations, table formatting, statistical spacing, and evidence-boundary language, it would be suitable for journal-specific formatting and final submission preparation.

