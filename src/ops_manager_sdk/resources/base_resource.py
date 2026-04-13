from typing import Any, Optional
from httpx import Client


class BaseResource:
    def __init__(self, client: Client) -> None:
        self._client = client

    def request(
        self,
        method: str,
        path: str,
        query_params: Optional[dict[str, Any]] = None,
        body_params: Optional[dict[str, Any] | list[Any]] = None,
    ) -> Any:
        response = self._client.request(
            method=method, url=path, params=query_params, json=body_params
        )

        if not response.content:
            return None
        return response.json()
