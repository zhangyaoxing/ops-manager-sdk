from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class AgentsResource(BaseResource):
    """Client for AgentsResource resource."""
    class CreateApiKeyPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class CreateApiKeyQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class CreateApiKeyBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        desc: Optional[str] = Field("None", alias="desc")
    def create_api_key(self,
        path_params: CreateApiKeyPathParams,
        query_params: Optional[CreateApiKeyQueryParams],
        body_params: Optional[CreateApiKeyBodyParams],
    ) -> dict[str, Any]:
        """API: Create One Agent API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/agentapikeys/create-one-agent-api-key/
        Description: No description found."""
        return self._request(
            "POST",
            "/groups/{PROJECT-ID}/agentapikeys",
            path_params,
            query_params,
            body_params,
        )
    class RemoveApiKeyPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
        api_agent_key_id: str = Field("None", alias="API-AGENT-KEY-ID")
    class RemoveApiKeyQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class RemoveApiKeyBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def remove_api_key(self,
        path_params: RemoveApiKeyPathParams,
        query_params: Optional[RemoveApiKeyQueryParams],
        body_params: Optional[RemoveApiKeyBodyParams],
    ) -> dict[str, Any]:
        """API: Remove One Agent API Key
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/agentapikeys/delete-one-agent-api-key/
        Description: No description found."""
        return self._request(
            "DELETE",
            "/groups/{PROJECT-ID}/agentapikeys/{API-AGENT-KEY-ID}",
            path_params,
            query_params,
            body_params,
        )
    class GetAllApiKeysPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class GetAllApiKeysQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetAllApiKeysBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all_api_keys(self,
        path_params: GetAllApiKeysPathParams,
        query_params: Optional[GetAllApiKeysQueryParams],
        body_params: Optional[GetAllApiKeysBodyParams],
    ) -> dict[str, Any]:
        """API: Get All Agent API Keys for One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/agentapikeys/get-all-agent-api-keys-for-project/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/agentapikeys",
            path_params,
            query_params,
            body_params,
        )
    class RetrieveAllVersionsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    class RetrieveAllVersionsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class RetrieveAllVersionsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def retrieve_all_versions(self,
        path_params: Optional[RetrieveAllVersionsPathParams],
        query_params: Optional[RetrieveAllVersionsQueryParams],
        body_params: Optional[RetrieveAllVersionsBodyParams],
    ) -> dict[str, Any]:
        """API: Retrieve All Agent Versions
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/agents/get-agent-versions-global/
        Description: No description found."""
        return self._request(
            "GET",
            "/softwareComponents/versions/",
            path_params,
            query_params,
            body_params,
        )
    class RetrieveForOneProjectPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class RetrieveForOneProjectQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class RetrieveForOneProjectBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def retrieve_for_one_project(self,
        path_params: RetrieveForOneProjectPathParams,
        query_params: Optional[RetrieveForOneProjectQueryParams],
        body_params: Optional[RetrieveForOneProjectBodyParams],
    ) -> dict[str, Any]:
        """API: Retrieve All Agent Versions for One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/agents/get-agent-versions-per-project/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/agents/versions",
            path_params,
            query_params,
            body_params,
        )
    class GetAllPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
    class GetAllQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetAllBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_all(self,
        path_params: GetAllPathParams,
        query_params: Optional[GetAllQueryParams],
        body_params: Optional[GetAllBodyParams],
    ) -> dict[str, Any]:
        """API: Get Links to Agent Resources for a Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/agents-get-all/
        Description: Get links to Monitoring, Backup, and Automation Agent resources for a project."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/agents",
            path_params,
            query_params,
            body_params,
        )
    class GetByTypePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", alias="PROJECT-ID")
        type: str = Field("None", alias="TYPE")
    class GetByTypeQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        page_num: Optional[float] = Field(1.0, alias="pageNum")
        items_per_page: Optional[float] = Field(100.0, alias="itemsPerPage")
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetByTypeBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_by_type(self,
        path_params: GetByTypePathParams,
        query_params: Optional[GetByTypeQueryParams],
        body_params: Optional[GetByTypeBodyParams],
    ) -> dict[str, Any]:
        """API: Get Agents by Type for One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/agents-get-by-type/
        Description: Get all agents of a specified type (i.e. Monitoring, Backup, or Automation) for a project."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/agents/{TYPE}",
            path_params,
            query_params,
            body_params,
        )