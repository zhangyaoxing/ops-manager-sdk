from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource


class PerformanceAdvisorResource(BaseResource):
    """Client for PerformanceAdvisorResource resource."""

    class GetSlowQueryLogsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        host_id: str = Field("None", serialization_alias="HOST-ID")
        """(Required.) Unique identifier of the host for the MongoDB process.
        """

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """(Required.) Unique identifier of the project that owns this MongoDB process.
        """

    class GetSlowQueryLogsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        duration: Optional[int] = Field(serialization_alias="duration")
        """up to the present time
        """

        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """false
        """

        n_logs: Optional[int] = Field(serialization_alias="nLogs")
        """20000
        """

        namespaces: Optional[str] = Field("None", serialization_alias="namespaces")
        """all
        """

        pretty: Optional[bool] = Field(serialization_alias="pretty")
        """false
        """

        since: Optional[int] = Field(serialization_alias="since")
        """previous 24 hours
        """

    def get_slow_query_logs(
        self,
        path_params: GetSlowQueryLogsPathParams,
        query_params: Optional[GetSlowQueryLogsQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Slow Query Logs
        - Document: [Get Slow Query Logs](https://www.mongodb.com/docs/ops-manager/current/reference/api/performance-advisor/get-slow-queries/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/slowQueryLogs`
        - Description: Retrieves log lines for slow queries as determined by the Performance Advisor.
        """
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
        """(Required.) Unique identifier of the host for the MongoDB process.
        """

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """(Required.) Unique identifier of the project that owns this MongoDB process.
        """

    class GetSuggestedIndexesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        duration: Optional[int] = Field(serialization_alias="duration")
        """up to the present time
        """

        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """false
        """

        n_examples: Optional[int] = Field(serialization_alias="nExamples")
        """5
        """

        n_indexes: Optional[int] = Field(serialization_alias="nIndexes")
        """unlimited
        """

        namespaces: Optional[str] = Field("None", serialization_alias="namespaces")
        """all
        """

        pretty: Optional[bool] = Field(serialization_alias="pretty")
        """false
        """

        since: Optional[int] = Field(serialization_alias="since")
        """previous 24 hours
        """

    def get_suggested_indexes(
        self,
        path_params: GetSuggestedIndexesPathParams,
        query_params: Optional[GetSuggestedIndexesQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Suggested Indexes
        - Document: [Get Suggested Indexes](https://www.mongodb.com/docs/ops-manager/current/reference/api/performance-advisor/get-suggested-indexes/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/suggestedIndexes`
        - Description: Retrieves suggested indexes as determined by the Performance Advisor.
        """
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
        """No description.
        """

        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        """No description.
        """

    class GetNamespacesQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)

        duration: Optional[int] = Field(serialization_alias="duration")
        """Length of time from the since parameter, in milliseconds, for which you want to receive results. If you do not also specify the since parameter, the endpoint returns results from the number of milliseconds specified by duration before the current time until now.
        """

        envelope: Optional[bool] = Field(serialization_alias="envelope")
        """Specifies whether or not to wrap the response in an envelope. The default is false.
        """

        pretty: Optional[bool] = Field(serialization_alias="pretty")
        """Indicates whether the response body should be in a prettyprint format. The default value is false.
        """

        since: Optional[int] = Field(serialization_alias="since")
        """Point in time, specified as milliseconds since the Unix Epoch, from which you want to receive results. If you do not also specify the duration parameter, the endpoint returns results from since until the current time.
        """

    def get_namespaces(
        self,
        path_params: GetNamespacesPathParams,
        query_params: Optional[GetNamespacesQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get Namespaces for a Project
        - Document: [Get Namespaces](https://www.mongodb.com/docs/ops-manager/current/reference/api/performance-advisor/pa-namespaces-get-all/)
        - Resource: `GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/namespaces`
        - Description: Retrieve namespaces for collections experiencing slow queries on a specified host. Namespaces appear in the following format: {database}.{collection}.
        """
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/namespaces",
            path_params,
            query_params,
            None,
        )
