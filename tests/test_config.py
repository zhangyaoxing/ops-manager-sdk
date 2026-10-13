import importlib
import os
import re

import pytest

from ops_manager_sdk.generator import utils
from ops_manager_sdk.generator.version import Version


PYPROJECT_FILE = utils.PROJECT_ROOT / "pyproject.toml"


def test_docs_version_uses_major_and_minor_of_project_version() -> None:
    declared = re.search(
        r'^version = "([^"]+)"', PYPROJECT_FILE.read_text(encoding="utf-8"), re.MULTILINE
    )
    assert declared is not None, "pyproject.toml declares no [project] version"

    project_version = Version.parse(declared.group(1))

    assert utils.DOCS_VERSION == f"v{project_version.major_version}.{project_version.minor_version}"
    assert re.fullmatch(r"v\d+\.\d+", utils.DOCS_VERSION)

    # The project version itself must still be parsed into the same object.
    assert utils.PROJECT_VERSION == project_version


@pytest.mark.skipif(
    "SITEMAP_URL" in os.environ or "API_BASE_URL" in os.environ,
    reason="the documentation URLs are overridden in the environment",
)
def test_documentation_urls_default_to_the_docs_version() -> None:
    reloaded = importlib.reload(utils)
    docs_base_url = f"https://www.mongodb.com/docs/ops-manager/{utils.DOCS_VERSION}"

    assert reloaded.SITEMAP_URL == f"{docs_base_url}/sitemap-0.xml"
    assert reloaded.API_BASE_URL == f"{docs_base_url}/reference/api/"
