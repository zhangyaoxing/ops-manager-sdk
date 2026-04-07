from dataclasses import dataclass
from typing import Mapping


@dataclass(slots=True)
class ClientConfig:
    base_url: str
    digest_username: str | None = None
    digest_password: str | None = None
    timeout: float = 30.0
    user_agent: str = "ops-manager-sdk/0.1.0"

    def headers(self) -> Mapping[str, str]:
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
        }
