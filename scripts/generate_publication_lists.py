#!/usr/bin/env python3
"""Generate publication list HTML from CV BibTeX files."""

from __future__ import annotations

import re
from pathlib import Path

from pybtex.database.input import bibtex

CV_DIR = Path("/Users/rivas/Downloads/_alia__Curriculum_Vitae")
PUBS_HTML = Path(__file__).resolve().parent.parent / "_pages" / "publications.html"

BIB_CONFIG = [
    ("jlist", "j-counter", CV_DIR / "Papers_Journals.bib", "journal"),
    ("plist", "p-counter", CV_DIR / "Papers_preprint.bib", "preprint"),
    ("clist", "c-counter", CV_DIR / "Papers_indexConf.bib", "conference"),
    ("wlist", "w-counter", CV_DIR / "Papers_nonIndexConf.bib", "workshop"),
]


def clean_latex(text: str) -> str:
    text = text.replace("{", "").replace("}", "")
    text = re.sub(r"\\textbf\s*", "", text)
    text = re.sub(r"\\underline\s*", "", text)
    text = re.sub(r"\\emph\s*", "", text)
    text = re.sub(r"\\textit\s*", "", text)
    text = re.sub(r"\\textsc\s*", "", text)
    text = re.sub(r"\\&", "&", text)
    text = re.sub(r"\\'", "'", text)
    text = re.sub(r'\\"o', "ö", text)
    text = re.sub(r"\\o", "ø", text)
    text = re.sub(r"\\pi-", "π-", text)
    text = re.sub(r"\$[^$]*\$", "", text)
    text = re.sub(r"\\[a-zA-Z]+\*?", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def format_author(person) -> str:
    first = " ".join(person.first_names) if person.first_names else ""
    last = " ".join(person.last_names) if person.last_names else ""
    name = clean_latex(f"{first} {last}".strip())
    normalized = name.lower().replace(".", "")
    if normalized in {"stefano riva", "s riva"}:
        return "Stefano Riva"
    if normalized.startswith("j ") and "kutz" in normalized:
        return "J. Nathan Kutz"
    if normalized.startswith("in ") and "bang" in normalized:
        return "In Cheol Bang"
    if normalized == "matteo verso":
        return "Matteo Lo Verso"
    if normalized == "m verso":
        return "M. Lo Verso"
    if normalized == "amy rude":
        return "Amy Sara Rude"
    if normalized == "judah goldfeder":
        return "Judah A. Goldfeder"
    if normalized == "philippe wyder":
        return "Philippe M. Wyder"
    if normalized == "jan williams":
        return "Jan P. Williams"
    return name


def format_authors(entry) -> str:
    authors = [format_author(person) for person in entry.persons.get("author", [])]
    if len(authors) == 1:
        return authors[0]
    if len(authors) == 2:
        return f"{authors[0]} and {authors[1]}"
    return ", ".join(authors[:-1]) + f", and {authors[-1]}"


def linkify(text: str) -> str:
    return re.sub(
        r"(https?://[^\s<]+)",
        r'<a href="\1">\1</a>',
        text,
    )


def field(entry, key: str, default: str = "") -> str:
    return clean_latex(entry.fields.get(key, default))


def format_journal(entry) -> str:
    authors = format_authors(entry)
    title = field(entry, "title")
    journal = field(entry, "journal")
    year = field(entry, "year")
    volume = field(entry, "volume")
    number = field(entry, "number")
    pages = field(entry, "pages")
    doi = field(entry, "doi").replace("https://doi.org/", "")
    url = field(entry, "url")

    parts = [f"{authors}, “{title},” {journal}"]
    if volume:
        parts.append(f", vol. {volume}")
    if number and number != "0":
        parts.append(f", no. {number}")
    if pages:
        parts.append(f", pp. {pages}" if "-" in pages or "–" in pages else f", p. {pages}")
    parts.append(f", {year}.")
    text = "".join(parts)

    if url:
        text += f' <a href="{url}">URL</a>'
    if doi:
        sep = ", " if url else " "
        text += f"{sep}doi:{doi}."
    elif not text.endswith("."):
        text += "."
    return text


def format_preprint(entry) -> str:
    authors = format_authors(entry)
    title = field(entry, "title")
    year = field(entry, "year")
    url = field(entry, "url")
    note = field(entry, "note")
    eprint = field(entry, "eprint")

    text = f"{authors}, “{title},” {year}."
    if note:
        text = f"{authors}, “{title},” {note}, {year}."
    if url:
        label = f"arXiv:{eprint}" if eprint else "URL"
        text += f' <a href="{url}">{label}</a>.'
    return text


def format_conference(entry) -> str:
    authors = format_authors(entry)
    title = field(entry, "title")
    booktitle = field(entry, "booktitle")
    address = field(entry, "address")
    year = field(entry, "year")
    month = field(entry, "month")
    pages = field(entry, "pages")
    doi = field(entry, "doi").replace("https://doi.org/", "").replace("doi.org/", "")
    url = field(entry, "url")
    note = field(entry, "note")

    location = f", ({address})" if address else ""
    when = f", {month} {year}" if month else f", {year}"
    page_text = ""
    if pages:
        page_text = f", pp. {pages}" if "-" in pages or "–" in pages else f", p. {pages}"

    if note:
        text = f"{authors}, “{title},” {note}, {year}."
    else:
        text = f"{authors}, “{title},” in {booktitle}{location}{page_text}{when}."

    if url:
        text += f' URL: <a href="{url}">link</a>.'
    if doi:
        text += f" doi:{doi}."
    return text


def format_entry(entry, kind: str) -> str:
    if kind == "journal":
        return format_journal(entry)
    if kind == "preprint":
        return format_preprint(entry)
    return format_conference(entry)


def load_entries(path: Path):
    parser = bibtex.Parser()
    data = parser.parse_file(str(path))
    return list(data.entries.values())


def build_list(class_name: str, counter_name: str, entries, kind: str) -> str:
    items = "\n".join(f"  <li>{format_entry(entry, kind)}</li>" for entry in entries)
    return (
        f'<ol class="{class_name}">\n'
        f"{items}\n"
        f"</ol>"
    )


def replace_ol_block(content: str, class_name: str, new_block: str) -> str:
    pattern = rf'<ol class="{class_name}">.*?</ol>'
    return re.sub(pattern, new_block, content, count=1, flags=re.DOTALL)


def main() -> None:
    html = PUBS_HTML.read_text(encoding="utf-8")

    for class_name, counter_name, bib_path, kind in BIB_CONFIG:
        entries = load_entries(bib_path)
        block = build_list(class_name, counter_name, entries, kind)
        html = replace_ol_block(html, class_name, block)

    PUBS_HTML.write_text(html, encoding="utf-8")
    print(f"Updated {PUBS_HTML}")


if __name__ == "__main__":
    main()
