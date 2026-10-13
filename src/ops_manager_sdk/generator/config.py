"""Configuration of the Ops Manager SDK generator.

The values are read from the environment, or from a `.env` file in the project
root, and fall back to the defaults defined here. This module must not import
`ops_manager_sdk.generator.utils` or `ops_manager_sdk.generator.crawler_factory`:
both of them import it, so importing them back would create an import cycle.
"""

from typing import Optional
from pathlib import Path
from importlib.metadata import version as distribution_version
import os

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 ships no tomllib in the standard library.
    import tomli as tomllib

from dotenv import load_dotenv
from loguru import logger

from ops_manager_sdk.generator.version import Version


PROJECT_ROOT: Path = Path(__file__).resolve().parents[3]


def _load_env_file() -> Optional[Path]:
    """Load configuration variables from a .env file.
    The project root .env is preferred, the current working directory is used as a
    fallback for installations outside the source tree. Variables that are already
    exported in the environment are never overridden.
    Returns:
        The path of the loaded .env file, or None when no file was found.
    """
    for candidate in (PROJECT_ROOT / ".env", Path.cwd() / ".env"):
        if candidate.is_file():
            load_dotenv(candidate, override=False)
            return candidate
    return None


ENV_FILE: Optional[Path] = _load_env_file()


def _read_project_version() -> str:
    """Read the version declared in the project's pyproject.toml.
    The installed distribution metadata is used as a fallback, so the version can
    still be resolved when the source tree is not available.
    Returns:
        The version string, for example "8.0.0".
    """
    pyproject_file: Path = PROJECT_ROOT / "pyproject.toml"
    if pyproject_file.is_file():
        with pyproject_file.open("rb") as file:
            declared_version = tomllib.load(file).get("project", {}).get("version")
        if declared_version is not None:
            return str(declared_version)
    return distribution_version("ops-manager-sdk-generator")


PROJECT_VERSION: Version = Version.parse(_read_project_version())
# The documentation is versioned by major and minor only, for example "v8.0".
DOCS_VERSION: str = f"v{PROJECT_VERSION.major_version}.{PROJECT_VERSION.minor_version}"


def _get_int_env(name: str, default: int) -> int:
    """Read an integer configuration variable, falling back to the default value."""
    raw_value: Optional[str] = os.getenv(name)
    if raw_value is None or raw_value.strip() == "":
        return default
    try:
        return int(raw_value)
    except ValueError:
        logger.warning(f"Invalid value for {name}: {raw_value!r}. Using default: {default}")
        return default


# Configuration variables are read from .env or from exported environment variables.
# The default values are the ones that used to be hard-coded in the generator. The
# documentation URLs follow the project version declared in pyproject.toml.
SITEMAP_URL: str = os.getenv(
    "SITEMAP_URL", f"https://www.mongodb.com/docs/ops-manager/{DOCS_VERSION}/sitemap-0.xml"
)
API_BASE_URL: str = os.getenv(
    "API_BASE_URL", f"https://www.mongodb.com/docs/ops-manager/{DOCS_VERSION}/reference/api/"
)
# A relative HOME_DIR is resolved against the working directory the command starts in.
HOME_DIR: Path = Path(os.getenv("HOME_DIR", str(Path.cwd() / ".data"))).expanduser().absolute()
EXPIRE_DAYS: int = _get_int_env("EXPIRE_DAYS", 7)
