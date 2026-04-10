from dataclasses import dataclass


@dataclass(slots=True)
class ClientConfig:
    base_url: str
    digest_username: str | None = None
    digest_password: str | None = None
    timeout: float = 30.0
    user_agent: str = "ops-manager-sdk/0.1.0"

    @property
    def headers(self) -> dict[str, str]:
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
        }
