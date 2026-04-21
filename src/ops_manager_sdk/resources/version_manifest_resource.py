from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource


class VersionManifestResource(BaseResource):
    """Client for VersionManifestResource resource."""

    class RetrieveQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        pretty: Optional[bool] = Field(serialization_alias="pretty")
        """false
        """

    def retrieve(
        self,
        query_params: Optional[RetrieveQueryParams],
    ) -> dict[str, Any]:
        """
        ## Retrieve the Ops Manager Version Manifest
        - Document: [Retrieve](https://www.mongodb.com/docs/ops-manager/current/reference/api/version-manifest/get-om-version-manifest/)
        - Resource: `GET /unauth/versionManifest`
        - Description: Use this resource to retrieve the version manifest that Ops Manager is configured to use.
        """
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
        """false
        """

    def update(
        self,
        query_params: Optional[UpdateQueryParams],
    ) -> dict[str, Any]:
        """
        ## Update the Version Manifest
        - Document: [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/version-manifest/update-version-manifest/)
        - Resource: `PUT /versionManifest`
        - Description: Use this resource to upload the latest version manifest from MongoDB, Inc.
        """
        return self._request(
            "PUT",
            "/versionManifest",
            None,
            query_params,
            None,
        )
