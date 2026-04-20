from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class VersionManifestResource(BaseResource):
    """Client for VersionManifestResource resource."""
    class RetrieveQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def retrieve(self,
        query_params: Optional[RetrieveQueryParams],
    ) -> dict[str, Any]:
        """API: Retrieve the Ops Manager Version Manifest
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/version-manifest/get-om-version-manifest/
        Description: Use this resource to retrieve the version manifest that Ops Manager is configured to use."""
        return self._request(
            "GET",
            "/unauth/versionManifest",
            None,
            query_params,
            None,
        )
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    def update(self,
        query_params: Optional[UpdateQueryParams],
    ) -> dict[str, Any]:
        """API: Update the Version Manifest
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/version-manifest/update-version-manifest/
        Description: Use this resource to upload the latest version manifest from MongoDB, Inc."""
        return self._request(
            "PUT",
            "/versionManifest",
            None,
            query_params,
            None,
        )