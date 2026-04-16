from httpx import Auth, DigestAuth, Client
from .config import ClientConfig
from .resources import *


class OpsManagerClient:
    def __init__(self, cfg: ClientConfig) -> None:
        self._config = cfg
        assert (
            cfg.digest_username is not None and cfg.digest_password is not None
        ), "Digest credentials must be provided"
        auth: Auth = DigestAuth(cfg.digest_username, cfg.digest_password)
        self._client = Client(
            base_url=f"{cfg.base_url.rstrip('/')}/api/public/v1.0",
            headers=cfg.headers,
            timeout=cfg.timeout,
            auth=auth,
        )
