from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class PerformanceAdvisorResource(BaseResource):
    """Client for PerformanceAdvisorResource resource."""
    class GetSlowQueryLogsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        host_id: str = Field("None", serialization_alias="HOST-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetSlowQueryLogsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        duration: Optional[int] = Field(serialization_alias="duration")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        n_logs: Optional[int] = Field(serialization_alias="nLogs")
        namespaces: Optional[str] = Field("None", serialization_alias="namespaces")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        since: Optional[int] = Field(serialization_alias="since")
    def get_slow_query_logs(self,
        path_params: GetSlowQueryLogsPathParams,
        query_params: Optional[GetSlowQueryLogsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Slow Query Logs
        - Document: [Get Slow Query Logs](https://www.mongodb.com/docs/ops-manager/current/reference/api/performance-advisor/get-slow-queries/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/slowQueryLogs`
        - Description: Retrieves log lines for slow queries as determined by the Performance Advisor."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/slowQueryLogs",
            path_params,
            query_params,
            None,
        )
    class GetSuggestedIndexesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        host_id: str = Field("None", serialization_alias="HOST-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetSuggestedIndexesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        duration: Optional[int] = Field(serialization_alias="duration")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        n_examples: Optional[int] = Field(serialization_alias="nExamples")
        n_indexes: Optional[int] = Field(serialization_alias="nIndexes")
        namespaces: Optional[str] = Field("None", serialization_alias="namespaces")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        since: Optional[int] = Field(serialization_alias="since")
    def get_suggested_indexes(self,
        path_params: GetSuggestedIndexesPathParams,
        query_params: Optional[GetSuggestedIndexesQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Suggested Indexes
        - Document: [Get Suggested Indexes](https://www.mongodb.com/docs/ops-manager/current/reference/api/performance-advisor/get-suggested-indexes/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/suggestedIndexes`
        - Description: Retrieves suggested indexes as determined by the Performance Advisor."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/suggestedIndexes",
            path_params,
            query_params,
            None,
        )
    class GetNamespacesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        host_id: str = Field("None", serialization_alias="HOST-ID")
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
    class GetNamespacesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        duration: Optional[int] = Field(serialization_alias="duration")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        since: Optional[int] = Field(serialization_alias="since")
    def get_namespaces(self,
        path_params: GetNamespacesPathParams,
        query_params: Optional[GetNamespacesQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Namespaces for a Project
        - Document: [Get Namespaces](https://www.mongodb.com/docs/ops-manager/current/reference/api/performance-advisor/pa-namespaces-get-all/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/namespaces`
        - Description: Retrieve namespaces for collections experiencing slow queries on a specified host. Namespaces appear in the following format: {database}.{collection}."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/namespaces",
            path_params,
            query_params,
            None,
        )