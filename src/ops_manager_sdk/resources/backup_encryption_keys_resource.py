from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class BackupEncryptionKeysResource(BaseResource):
    """Client for BackupEncryptionKeysResource resource."""
    class RetrieveKmipMasterKeyIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
        cluster_id: str = Field("None", serialization_alias="CLUSTER-ID")
    class RetrieveKmipMasterKeyIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def retrieve_kmip_master_key_id(self,
        path_params: RetrieveKmipMasterKeyIdPathParams,
        query_params: Optional[RetrieveKmipMasterKeyIdQueryParams],
    ) -> dict[str, Any]:
        """API: Retrieve the KMIP Master Key ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/kmip-keys/get-master-key/
        Description: Use the GET HTTP method with the same endpoint to retrieve the ID of the current KMIP master key."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/encryptionKey",
            path_params,
            query_params,
            None,
        )
    class RotateKmipMasterKeyIdPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
        cluster_id: str = Field("None", serialization_alias="CLUSTER-ID")
    class RotateKmipMasterKeyIdQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def rotate_kmip_master_key_id(self,
        path_params: RotateKmipMasterKeyIdPathParams,
        query_params: Optional[RotateKmipMasterKeyIdQueryParams],
    ) -> dict[str, Any]:
        """API: Rotate the KMIP Master Key ID
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/kmip-keys/rotate-master-key/
        Description: Use the PUT HTTP method with the following endpoint to rotate the KMIP master key. Issue one PUT request for each shard and another PUT request for the config server replica set."""
        return self._request(
            "PUT",
            "/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/encryptionKey",
            path_params,
            query_params,
            None,
        )