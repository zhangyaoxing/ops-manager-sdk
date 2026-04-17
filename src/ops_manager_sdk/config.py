from dataclasses import dataclass, field
from importlib.metadata import PackageNotFoundError, version


def _default_user_agent() -> str:
    try:
        sdk_version = version("ops-manager-sdk")
    except PackageNotFoundError:
        # Fallback for source-only usage before package metadata is installed.
        sdk_version = "0.0.0"
    return f"ops-manager-sdk/{sdk_version}"


@dataclass(slots=True)
class ClientConfig:
    base_url: str
    digest_username: str | None = None
    digest_password: str | None = None
    timeout: float = 30.0
    user_agent: str = field(default_factory=_default_user_agent)

    @property
    def headers(self) -> dict[str, str]:
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
        }
