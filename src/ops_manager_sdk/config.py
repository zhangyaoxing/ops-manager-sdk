from importlib.metadata import PackageNotFoundError, version
from typing import Optional
import os
from pydantic import BaseModel, Field


def _default_user_agent() -> str:
    try:
        sdk_version = version("ops-manager-sdk")
    except PackageNotFoundError:
        # Fallback for source-only usage before package metadata is installed.
        sdk_version = "0.0.0"
    return f"ops-manager-sdk/{sdk_version}"


class ClientConfig(BaseModel):
    base_url: str
    public_key: str
    private_key: str
    timeout: float = 30.0
    user_agent: str = Field(default_factory=_default_user_agent)

    @property
    def headers(self) -> dict[str, str]:
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
        }
