from __future__ import annotations

from typing import Any

import httpx

from .config import ClientConfig
from .exceptions import ApiError, AuthenticationError, RequestError


class OpsManagerClient:
    def __init__(self, config: ClientConfig) -> None:
        self._config = config
        auth = self._build_auth(config)

        self._client = httpx.Client(
            base_url=config.base_url.rstrip("/"),
            headers=config.headers,
            timeout=config.timeout,
            auth=auth,
        )

    @staticmethod
    def _build_auth(config: ClientConfig) -> httpx.Auth | None:
        if config.digest_username and config.digest_password:
            return httpx.DigestAuth(config.digest_username, config.digest_password)
        return None

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "OpsManagerClient":
        return self

    def __exit__(self, _exc_type: Any, _exc_value: Any, _traceback: Any) -> None:
        self.close()

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | list[Any] | None = None,
    ) -> Any:
        try:
            response = self._client.request(method=method, url=path, params=params, json=json)
        except httpx.HTTPError as exc:
            raise RequestError(str(exc)) from exc

        if response.status_code in (401, 403):
            raise AuthenticationError(response.status_code, response.text)
        if response.is_error:
            raise ApiError(response.status_code, response.text)

        if not response.content:
            return None
        return response.json()

    def get(self, path: str, *, params: dict[str, Any] | None = None) -> Any:
        return self.request("GET", path, params=params)

    def post(self, path: str, *, json: dict[str, Any] | list[Any] | None = None) -> Any:
        return self.request("POST", path, json=json)

    def put(self, path: str, *, json: dict[str, Any] | list[Any] | None = None) -> Any:
        return self.request("PUT", path, json=json)

    def patch(self, path: str, *, json: dict[str, Any] | list[Any] | None = None) -> Any:
        return self.request("PATCH", path, json=json)

    def delete(self, path: str) -> Any:
        return self.request("DELETE", path)
