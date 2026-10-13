from ops_manager_sdk.generator.html_to_markdown import html_to_markdown


def test_html_to_markdown_preserves_inline_markup() -> None:
    html = (
        "Create a <strong>project</strong> with <code>groupId</code> "
        'and <a href="/docs">docs</a>.'
    )

    assert html_to_markdown(html) == (
        "Create a **project** with `groupId` and [docs](/docs)."
    )


def test_html_to_markdown_converts_lists() -> None:
    html = "<p>Allowed values:</p><ul><li><code>READ</code></li><li>WRITE</li></ul>"

    assert html_to_markdown(html) == "Allowed values:\n\n- `READ`\n- WRITE"


def test_html_to_markdown_converts_simple_tables() -> None:
    html = (
        "<table><thead><tr><th>Name</th><th>Description</th></tr></thead>"
        "<tbody><tr><td><code>id</code></td><td>Project identifier</td></tr></tbody></table>"
    )

    assert html_to_markdown(html) == (
        "| Name | Description |\n" "| --- | --- |\n" "| `id` | Project identifier |"
    )


def test_html_to_markdown_ignores_css_javascript_and_non_basic_tags() -> None:
    html = (
        '<style>.hidden { display: none; }</style>'
        '<script>alert("x")</script>'
        '<p style="color: red" onclick="doThing()">Use <span>basic</span> '
        '<strong>markdown</strong>.</p>'
    )

    assert html_to_markdown(html) == "Use basic **markdown**."
