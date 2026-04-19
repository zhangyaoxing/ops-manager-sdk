from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class PerformanceAdvisorResource(BaseResource):
    """Client for PerformanceAdvisorResource resource."""
    class GetSlowQueryLogsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        host_id: str = Field("None", serialization_alias="HOST-ID")
    class GetSlowQueryLogsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        since: Optional[int] = Field(serialization_alias="since")
        duration: Optional[int] = Field(serialization_alias="duration")
        namespaces: Optional[str] = Field("None", serialization_alias="namespaces")
        n_logs: Optional[int] = Field(serialization_alias="nLogs")
    class GetSlowQueryLogsBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_slow_query_logs(self,
        path_params: GetSlowQueryLogsPathParams,
        query_params: Optional[GetSlowQueryLogsQueryParams],
        body_params: Optional[GetSlowQueryLogsBodyParams],
    ) -> dict[str, Any]:
        """API: Get Slow Query Logs
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/performance-advisor/get-slow-queries/
        Description: Retrieves log lines for slow queries as determined by the Performance Advisor."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/slowQueryLogs",
            path_params,
            query_params,
            body_params,
        )
    class GetSuggestedIndexesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        host_id: str = Field("None", serialization_alias="HOST-ID")
    class GetSuggestedIndexesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        since: Optional[int] = Field(serialization_alias="since")
        duration: Optional[int] = Field(serialization_alias="duration")
        namespaces: Optional[str] = Field("None", serialization_alias="namespaces")
        n_indexes: Optional[int] = Field(serialization_alias="nIndexes")
        n_examples: Optional[int] = Field(serialization_alias="nExamples")
    class GetSuggestedIndexesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_suggested_indexes(self,
        path_params: GetSuggestedIndexesPathParams,
        query_params: Optional[GetSuggestedIndexesQueryParams],
        body_params: Optional[GetSuggestedIndexesBodyParams],
    ) -> dict[str, Any]:
        """API: Get Suggested Indexes
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/performance-advisor/get-suggested-indexes/
        Description: Retrieves suggested indexes as determined by the Performance Advisor."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/suggestedIndexes",
            path_params,
            query_params,
            body_params,
        )
    class GetNamespacesPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        host_id: str = Field("None", serialization_alias="HOST-ID")
    class GetNamespacesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        since: Optional[int] = Field(serialization_alias="since")
        duration: Optional[int] = Field(serialization_alias="duration")
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
    class GetNamespacesBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_namespaces(self,
        path_params: GetNamespacesPathParams,
        query_params: Optional[GetNamespacesQueryParams],
        body_params: Optional[GetNamespacesBodyParams],
    ) -> dict[str, Any]:
        """API: Get Namespaces for a Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/performance-advisor/pa-namespaces-get-all/
        Description: Retrieve namespaces for collections experiencing slow queries on a specified host. Namespaces appear in the following format: {database}.{collection}."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/namespaces",
            path_params,
            query_params,
            body_params,
        )