import re

from markdownify import markdownify as _markdownify


def html_to_markdown(html: str) -> str:
    """Convert an HTML fragment from the docs site to markdown."""
    markdown = _markdownify(
        html,
        bullets="-",
        heading_style="ATX",
        strip=["script", "style"],
    )
    return _clean_markdown(markdown)


def _clean_markdown(markdown: str) -> str:
    lines = [line.rstrip() for line in markdown.splitlines()]
    markdown = "\n".join(lines)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip()
