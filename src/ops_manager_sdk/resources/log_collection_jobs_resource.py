from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class LogCollectionJobsResource(BaseResource):
    """Client for LogCollectionJobsResource resource."""
    class DeletePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
        job_id: str = Field("None", serialization_alias="JOB-ID")
    class DeleteQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def delete(self,
        path_params: DeletePathParams,
        query_params: Optional[DeleteQueryParams],
    ) -> dict[str, Any]:
        """API: Delete a Log Collection Job
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-delete-one/
        Description: When you create a log collection job, Ops Manager starts a background job to download the logs from the specified Ops Manager deployment. Use this endpoint to delete a specified log collection job. You can delete both in-progress jobs and completed jobs."""
        return self._request(
            "DELETE",
            "/groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}",
            path_params,
            query_params,
            None,
        )
    class DownloadLogsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
        job_id: str = Field("None", serialization_alias="JOB-ID")
    class DownloadLogsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def download_logs(self,
        path_params: DownloadLogsPathParams,
        query_params: Optional[DownloadLogsQueryParams],
    ) -> dict[str, Any]:
        """API: Download Logs from a Log Collection Job
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-download-job/
        Description: When you create a log collection job, Ops Manager starts a background job to download the logs from the specified Ops Manager deployment. Use this endpoint to download a .tar.gz file stream for all logs associated with the specified job."""
        return self._request(
            "GET",
            "/groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}/download",
            path_params,
            query_params,
            None,
        )
    class GetAllJobsPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
    class GetAllJobsQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        items_per_page: Optional[float] = Field(100.0, serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(1.0, serialization_alias="pageNum")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
        verbose: Optional[bool] = Field(False, serialization_alias="verbose")
    def get_all_jobs(self,
        path_params: GetAllJobsPathParams,
        query_params: Optional[GetAllJobsQueryParams],
    ) -> dict[str, Any]:
        """API: Get All Log Collection Jobs for One Project
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-get-all/
        Description: When you create a log collection job, Ops Manager starts a background job to download the logs from the specified Ops Manager deployment. Use this endpoint to retrieve all log collection jobs for a specified Ops Manager project."""
        return self._request(
            "GET",
            "/groups/{GROUP-ID}/logCollectionJobs",
            path_params,
            query_params,
            None,
        )
    class GetJobPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
        job_id: str = Field("None", serialization_alias="JOB-ID")
    class GetJobQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(serialization_alias="envelope")
        items_per_page: Optional[float] = Field(serialization_alias="itemsPerPage")
        page_num: Optional[float] = Field(serialization_alias="pageNum")
        pretty: Optional[bool] = Field(serialization_alias="pretty")
        verbose: Optional[bool] = Field(serialization_alias="verbose")
    def get_job(self,
        path_params: GetJobPathParams,
        query_params: Optional[GetJobQueryParams],
    ) -> dict[str, Any]:
        """API: Get One Log Collection Job
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-get-one/
        Description: When you create a log collection job, Ops Manager starts a background job to download the logs from the specified Ops Manager deployment. Use this endpoint to retrieve a single log collection job by its unique identifier."""
        return self._request(
            "GET",
            "/groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}",
            path_params,
            query_params,
            None,
        )
    class RetryPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
        job_id: str = Field("None", serialization_alias="JOB-ID")
    class RetryQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def retry(self,
        path_params: RetryPathParams,
        query_params: Optional[RetryQueryParams],
    ) -> dict[str, Any]:
        """API: Retry a Failed Log Collection Job
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-retry/
        Description: When you create a log collection job, Ops Manager starts a background job to download the logs from the specified Ops Manager deployment. Use this endpoint to retry a single failed log collection job."""
        return self._request(
            "PUT",
            "/groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}/retry",
            path_params,
            query_params,
            None,
        )
    class CreatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
    class CreateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class CreateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        log_types: list[Any] = Field(serialization_alias="logTypes")
        redacted: bool = Field(serialization_alias="redacted")
        resource_name: str = Field("None", serialization_alias="resourceName")
        resource_type: str = Field("None", serialization_alias="resourceType")
        size_requested_per_file_bytes: float = Field(serialization_alias="sizeRequestedPerFileBytes")
    def create(self,
        path_params: CreatePathParams,
        query_params: Optional[CreateQueryParams],
        body_params: CreateBodyParams,
    ) -> dict[str, Any]:
        """API: Create a Log Collection Job
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-submit/
        Description: When you create a log collection job, Ops Manager starts a background job to download the logs from the specified Ops Manager deployment. Use this endpoint to create a new log collection job."""
        return self._request(
            "POST",
            "/groups/{GROUP-ID}/logCollectionJobs",
            path_params,
            query_params,
            body_params,
        )
    class ExtendPathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        group_id: str = Field("None", serialization_alias="GROUP-ID")
        job_id: str = Field("None", serialization_alias="JOB-ID")
    class ExtendQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class ExtendBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        expiration_date: str = Field("None", serialization_alias="expirationDate")
    def extend(self,
        path_params: ExtendPathParams,
        query_params: Optional[ExtendQueryParams],
        body_params: ExtendBodyParams,
    ) -> dict[str, Any]:
        """API: Extend a Log Collection Job
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/log-collections/log-collections-update-one/
        Description: When you create a log collection job, Ops Manager starts a background job to download the logs from the specified Ops Manager deployment. Each job is created with a specified expiration date. Use this endpoint to extend the expiration date of an existing log collection job."""
        return self._request(
            "PATCH",
            "/groups/{GROUP-ID}/logCollectionJobs/{JOB-ID}",
            path_params,
            query_params,
            body_params,
        )