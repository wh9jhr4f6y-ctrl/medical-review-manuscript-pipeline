"""Check numeric in-text citation order in a DOCX manuscript.

This script supports bracketed numeric citations such as [1], [2,3], [4-6],
and [4–6]. It reports first-mention order, missing references, and long
citation groups.

Usage:
    python scripts/check_reference_order.py manuscript.docx
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from docx import Document


CITATION_RE = re.compile(r"\[([0-9,\-\u2013\s]+)\]")


def expand_group(group: str) -> list[int]:
    nums: list[int] = []
    for part in re.split(r",\s*", group):
        part = part.strip()
        if not part:
            continue
        if "-" in part or "\u2013" in part:
            pieces = re.split(r"[-\u2013]", part)
            if len(pieces) == 2 and pieces[0].strip().isdigit() and pieces[1].strip().isdigit():
                start, end = int(pieces[0]), int(pieces[1])
                nums.extend(range(start, end + 1))
        elif part.isdigit():
            nums.append(int(part))
    return nums


def reference_numbers(paragraphs: list[str]) -> set[int]:
    refs = set()
    for text in paragraphs:
        match = re.match(r"^\s*(\d+)[\.\)]\s+", text)
        if match:
            refs.add(int(match.group(1)))
    return refs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--max-group-size", type=int, default=3)
    args = parser.parse_args()

    doc = Document(args.docx)
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    ref_heading_index = next((i for i, p in enumerate(paragraphs) if p.lower() in {"references", "reference"}), len(paragraphs))
    body = "\n".join(paragraphs[:ref_heading_index])
    refs = reference_numbers(paragraphs[ref_heading_index + 1 :])

    groups = []
    first_order = []
    for match in CITATION_RE.finditer(body):
        nums = expand_group(match.group(1))
        groups.append((match.group(0), nums))
        for num in nums:
            if num not in first_order:
                first_order.append(num)

    expected = list(range(1, max(first_order or [0]) + 1))
    missing_in_text_order = [n for n in expected if n not in first_order]
    listed_not_cited = sorted(refs - set(first_order))
    cited_not_listed = sorted(set(first_order) - refs) if refs else []
    long_groups = [g for g, nums in groups if len(nums) > args.max_group_size]

    print(f"File: {args.docx}")
    print(f"Citation groups: {len(groups)}")
    print(f"First-mention order: {first_order}")
    print(f"Missing in sequential order: {missing_in_text_order}")
    print(f"References listed but not cited: {listed_not_cited}")
    print(f"Citations missing from reference list: {cited_not_listed}")
    print(f"Long citation groups (> {args.max_group_size} refs): {long_groups}")


if __name__ == "__main__":
    main()

