"""Check embedded DOCX image size and effective DPI.

Usage:
    python scripts/check_image_dpi.py manuscript.docx --out image_report.csv
"""

from __future__ import annotations

import argparse
import csv
import zipfile
from io import BytesIO
from pathlib import Path

from lxml import etree
from PIL import Image


EMU_PER_INCH = 914400
NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}


def classify(min_dpi: float) -> str:
    if min_dpi >= 600:
        return "excellent"
    if min_dpi >= 300:
        return "acceptable for color/grayscale"
    if min_dpi >= 200:
        return "borderline"
    return "high risk"


def relationship_map(zf: zipfile.ZipFile) -> dict[str, str]:
    rels = etree.fromstring(zf.read("word/_rels/document.xml.rels"))
    mapping = {}
    for rel in rels.xpath("//rel:Relationship", namespaces=NS):
        rid = rel.get("Id")
        target = rel.get("Target")
        if rid and target and target.startswith("media/"):
            mapping[rid] = "word/" + target
    return mapping


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    rows = []
    with zipfile.ZipFile(args.docx) as zf:
        rels = relationship_map(zf)
        doc_xml = etree.fromstring(zf.read("word/document.xml"))
        drawings = doc_xml.xpath("//w:drawing", namespaces=NS)
        for idx, drawing in enumerate(drawings, 1):
            blips = drawing.xpath(".//a:blip", namespaces=NS)
            extents = drawing.xpath(".//wp:extent", namespaces=NS)
            if not blips or not extents:
                continue
            rid = blips[0].get(f"{{{NS['r']}}}embed")
            target = rels.get(rid)
            if not target or target not in zf.namelist():
                continue
            cx = int(extents[0].get("cx"))
            cy = int(extents[0].get("cy"))
            width_in = cx / EMU_PER_INCH
            height_in = cy / EMU_PER_INCH
            with Image.open(BytesIO(zf.read(target))) as image:
                dpi_x = image.width / width_in
                dpi_y = image.height / height_in
                min_dpi = min(dpi_x, dpi_y)
                rows.append(
                    {
                        "image_use": idx,
                        "media_file": Path(target).name,
                        "pixel_width": image.width,
                        "pixel_height": image.height,
                        "display_width_in": round(width_in, 2),
                        "display_height_in": round(height_in, 2),
                        "effective_dpi_x": round(dpi_x, 1),
                        "effective_dpi_y": round(dpi_y, 1),
                        "min_effective_dpi": round(min_dpi, 1),
                        "assessment": classify(min_dpi),
                    }
                )

    fieldnames = list(rows[0].keys()) if rows else []
    if args.out:
        with args.out.open("w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    else:
        for row in rows:
            print(row)


if __name__ == "__main__":
    main()

