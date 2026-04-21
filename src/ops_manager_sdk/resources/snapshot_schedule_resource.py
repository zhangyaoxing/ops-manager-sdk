from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class SnapshotScheduleResource(BaseResource):
    """Client for SnapshotScheduleResource resource."""
    class GetSchedulePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class GetScheduleQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    def get_schedule(self,
        path_params: GetSchedulePathParams,
        query_params: Optional[GetScheduleQueryParams],
    ) -> dict[str, Any]:
        """
        ## Get the Snapshot Schedule
        - Document: [Get Schedule](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/get-snapshot-schedule/)
        - Resource: `GET /groups/{PROJECT-ID}/backupConfigs/CLUSTER-ID/snapshotSchedule`
        - Description: No description."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/backupConfigs/CLUSTER-ID/snapshotSchedule",
            path_params,
            query_params,
            None,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field("None", serialization_alias="PROJECT-ID")
        cluster_id: str = Field("None", serialization_alias="clusterId")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        envelope: Optional[bool] = Field(False, serialization_alias="envelope")
        pretty: Optional[bool] = Field(False, serialization_alias="pretty")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        cluster_checkpoint_interval_min: Optional[float] = Field(serialization_alias="clusterCheckpointIntervalMin")
        cluster_id: Optional[str] = Field("None", serialization_alias="clusterId")
        daily_snapshot_retention_days: Optional[float] = Field(serialization_alias="dailySnapshotRetentionDays")
        full_incremental_day_of_week: Optional[str] = Field("None", serialization_alias="fullIncrementalDayOfWeek")
        group_id: Optional[str] = Field("None", serialization_alias="groupId")
        links: Optional[list[dict]] = Field(serialization_alias="links")
        monthly_snapshot_retention_months: Optional[float] = Field(serialization_alias="monthlySnapshotRetentionMonths")
        point_in_time_window_hours: Optional[float] = Field(serialization_alias="pointInTimeWindowHours")
        reference_hour_of_day: Optional[float] = Field(serialization_alias="referenceHourOfDay")
        reference_minute_of_hour: Optional[float] = Field(serialization_alias="referenceMinuteOfHour")
        reference_time_zone_offset: Optional[str] = Field("None", serialization_alias="referenceTimeZoneOffset")
        snapshot_interval_hours: Optional[float] = Field(serialization_alias="snapshotIntervalHours")
        snapshot_retention_days: Optional[float] = Field(serialization_alias="snapshotRetentionDays")
        weekly_snapshot_retention_weeks: Optional[float] = Field(serialization_alias="weeklySnapshotRetentionWeeks")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """
        ## Update the Snapshot Schedule
        - Document: [Update](https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/update-one-snapshot-schedule-by-cluster-id/)
        - Resource: `PATCH /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/snapshotSchedule`
        - Description: No description."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/snapshotSchedule",
            path_params,
            query_params,
            body_params,
        )