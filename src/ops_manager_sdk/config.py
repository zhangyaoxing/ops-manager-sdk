from dataclasses import dataclass
from typing import Mapping


@dataclass(slots=True)
class ClientConfig:
    base_url: str
    api_token: str | None = None
    timeout: float = 30.0
    user_agent: str = "ops-manager-sdk/0.1.0"

    def headers(self) -> Mapping[str, str]:
        headers: dict[str, str] = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
        }
        if self.api_token:
            headers["Authorization"] = f"Bearer {self.api_token}"
        return headers
