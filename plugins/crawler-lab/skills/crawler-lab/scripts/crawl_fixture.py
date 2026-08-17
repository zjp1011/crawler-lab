#!/usr/bin/env python3
"""Parse the bundled local catalog fixture into CSV and JSON outputs.

This demo intentionally performs no network requests. It is meant for interviews,
skill validation, and parser testing where repeatability matters.
"""


from __future__ import annotations


import argparse
import csv
import json
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable




@dataclass
class CatalogRecord:
    title: str
    url: str
    category: str
    date: str
    summary: str




class CatalogParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.records: list[CatalogRecord] = []
        self._current: dict[str, str] | None = None
        self._field: str | None = None
        self._chunks: list[str] = []


    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {key: value or "" for key, value in attrs}
        if tag == "article" and "result-card" in attrs_dict.get("class", "").split():
            self._current = {"category": attrs_dict.get("data-category", "")}
        elif self._current is not None and tag == "a" and "url" not in self._current:
            self._current["url"] = attrs_dict.get("href", "")
            self._start_text("title")
        elif self._current is not None and tag == "time":
            self._current["date"] = attrs_dict.get("datetime", "")
        elif self._current is not None and tag == "p" and "summary" in attrs_dict.get("class", "").split():
            self._start_text("summary")


    def handle_data(self, data: str) -> None:
        if self._field is not None:
            self._chunks.append(data)


    def handle_endtag(self, tag: str) -> None:
        if self._field == "title" and tag == "a":
            self._finish_text()
        elif self._field == "summary" and tag == "p":
            self._finish_text()
        elif tag == "article" and self._current is not None:
            record = CatalogRecord(
                title=self._current.get("title", "").strip(),
                url=self._current.get("url", "").strip(),
                category=self._current.get("category", "").strip(),
                date=self._current.get("date", "").strip(),
                summary=self._current.get("summary", "").strip(),
            )
            if record.title and record.url:
                self.records.append(record)
            self._current = None
            self._field = None
            self._chunks = []


    def _start_text(self, field: str) -> None:
        self._field = field
        self._chunks = []


    def _finish_text(self) -> None:
        if self._current is not None and self._field is not None:
            self._current[self._field] = " ".join(" ".join(self._chunks).split())
        self._field = None
        self._chunks = []




def parse_catalog(html: str) -> list[CatalogRecord]:
    parser = CatalogParser()
    parser.feed(html)
    return parser.records




def write_csv(records: Iterable[CatalogRecord], output_path: Path) -> None:
    rows = [asdict(record) for record in records]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["title", "url", "category", "date", "summary"])
        writer.writeheader()
        writer.writerows(rows)




def write_json(records: Iterable[CatalogRecord], output_path: Path) -> None:
    rows = [asdict(record) for record in records]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")




def main() -> int:
    skill_root = Path(__file__).resolve().parents[1]
    default_input = skill_root / "assets" / "fixtures" / "sample_catalog.html"
    default_output = skill_root / "tmp" / "sample_catalog"


    parser = argparse.ArgumentParser(description="Parse the bundled local catalog fixture.")
    parser.add_argument("--input", type=Path, default=default_input, help="HTML fixture path")
    parser.add_argument("--output", type=Path, default=default_output, help="Output path without extension")
    args = parser.parse_args()


    html = args.input.read_text(encoding="utf-8")
    records = parse_catalog(html)
    write_csv(records, args.output.with_suffix(".csv"))
    write_json(records, args.output.with_suffix(".json"))
    print(f"Parsed {len(records)} records")
    print(f"CSV: {args.output.with_suffix('.csv')}")
    print(f"JSON: {args.output.with_suffix('.json')}")
    return 0




if __name__ == "__main__":
    raise SystemExit(main())
