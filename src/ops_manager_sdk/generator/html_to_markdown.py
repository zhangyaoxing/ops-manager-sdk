import re

from bs4 import BeautifulSoup
from markdownify import markdownify as _markdownify

_BASIC_MARKDOWN_TAGS = [
    "a",
    "blockquote",
    "br",
    "code",
    "em",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "i",
    "li",
    "ol",
    "p",
    "pre",
    "strong",
    "table",
    "tbody",
    "td",
    "th",
    "thead",
    "tr",
    "ul",
]


def html_to_markdown(html: str) -> str:
    """Convert an HTML fragment from the docs site to basic markdown."""
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()

    markdown = _markdownify(
        str(soup),
        bullets="-",
        convert=_BASIC_MARKDOWN_TAGS,
        heading_style="ATX",
    )
    return _clean_markdown(markdown)


def _clean_markdown(markdown: str) -> str:
    lines = [line.rstrip() for line in markdown.splitlines()]
    markdown = "\n".join(lines)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip()
