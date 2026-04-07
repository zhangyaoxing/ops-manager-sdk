from __future__ import annotations

from typing import Any

from ..client import OpsManagerClient


class ResourceClient:
    def __init__(self, client: OpsManagerClient, resource_path: str) -> None:
        self._client = client
        self._resource_path = resource_path.strip("/")

    def list(self, *, params: dict[str, Any] | None = None) -> Any:
        return self._client.get(f"/{self._resource_path}", params=params)

    def get(self, resource_id: str) -> Any:
        return self._client.get(f"/{self._resource_path}/{resource_id}")

    def create(self, payload: dict[str, Any]) -> Any:
        return self._client.post(f"/{self._resource_path}", json=payload)

    def update(self, resource_id: str, payload: dict[str, Any]) -> Any:
        return self._client.put(f"/{self._resource_path}/{resource_id}", json=payload)

    def delete(self, resource_id: str) -> Any:
        return self._client.delete(f"/{self._resource_path}/{resource_id}")
