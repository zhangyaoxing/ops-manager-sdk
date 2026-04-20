from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class AgentsResource(BaseResource):
    """Client for AgentsResource resource."""
    class CreateApiKeyPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class CreateApiKeyQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    class CreateApiKeyBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        desc: Optional[str] = Field("None", serialization_alias="desc")
    def create_api_key(self,
        path_params: CreateApiKeyPathParams,
        query_params: Optional[CreateApiKeyQueryParams],
        body_params: Optional[CreateApiKeyBodyParams],
    ) -> dict[str, Any]:
        """API: Create One Agent API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/agentapikeys/create-one-agent-api-key/
        Description: No description."""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/agentapikeys",
            path_params,
            query_params,
            body_params,
        )
    class RemoveApiKeyPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        api_agent_key_id: str = Field("None", serialization_alias="API-AGENT-KEY-ID")
    class RemoveApiKeyQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def remove_api_key(self,
        path_params: RemoveApiKeyPathParams,
        query_params: Optional[RemoveApiKeyQueryParams],
    ) -> dict[str, Any]:
        """API: Remove One Agent API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/agentapikeys/delete-one-agent-api-key/
        Description: No description."""
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/agentapikeys/{API-AGENT-KEY-ID}",
            path_params,
            query_params,
            None,
        )
    class GetAllApiKeysPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetAllApiKeysQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_all_api_keys(self,
        path_params: GetAllApiKeysPathParams,
        query_params: Optional[GetAllApiKeysQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Agent API Keys for One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/agentapikeys/get-all-agent-api-keys-for-project/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/agentapikeys",
            path_params,
            query_params,
            None,
        )
    class RetrieveAllVersionsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def retrieve_all_versions(self,
        query_params: Optional[RetrieveAllVersionsQueryParams],
    ) -> dict[str, Any]:
        """API: Retrieve All Agent Versions
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/agents/get-agent-versions-global/
        Description: No description."""
        return self._request(
            "GET",
            "/softwareComponents/versions/",
            None,
            query_params,
            None,
        )
    class RetrieveForOneProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class RetrieveForOneProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def retrieve_for_one_project(self,
        path_params: RetrieveForOneProjectPathParams,
        query_params: Optional[RetrieveForOneProjectQueryParams],
    ) -> dict[str, Any]:
        """API: Retrieve All Agent Versions for One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/agents/get-agent-versions-per-project/
        Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/agents/versions",
            path_params,
            query_params,
            None,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_all(self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
    ) -> dict[str, Any]:
        """API: Get Links to Agent Resources for a Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/agents-get-all/
        Description: Get links to Monitoring, Backup, and Automation Agent resources for a project."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/agents",
            path_params,
            query_params,
            None,
        )
    class GetByTypePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        type: str = Field("None", serialization_alias="TYPE")
    class GetByTypeQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
    def get_by_type(self,
        path_params: GetByTypePathParams,
        query_params: Optional[GetByTypeQueryParams],
    ) -> dict[str, Any]:
        """API: Get Agents by Type for One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/agents-get-by-type/
        Description: Get all agents of a specified type (i.e. Monitoring, Backup, or Automation) for a project."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/agents/{TYPE}",
            path_params,
            query_params,
            None,
        )