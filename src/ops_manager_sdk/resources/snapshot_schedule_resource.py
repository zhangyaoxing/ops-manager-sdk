from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field
from .base_resource import BaseResource
class SnapshotScheduleResource(BaseResource):
    """Client for SnapshotScheduleResource resource."""
    class GetSchedulePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        cluster_id: str = Field(alias="clusterId")
    class GetScheduleQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class GetScheduleBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
    def get_schedule(self,
        path_params: GetSchedulePathParams,
        query_params: Optional[GetScheduleQueryParams],
        body_params: Optional[GetScheduleBodyParams],
    ) -> dict[str, Any]:
        """API: Get the Snapshot Schedule
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/get-snapshot-schedule/
        Description: No description found."""
        return self._request(
            "GET",
            "/groups/{PROJECT-ID}/backupConfigs/CLUSTER-ID/snapshotSchedule",
            path_params,
            query_params,
            body_params,
        )
    class UpdatePathParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        project_id: str = Field(alias="PROJECT-ID")
        cluster_id: str = Field(alias="clusterId")
    class UpdateQueryParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        pretty: Optional[bool] = Field(False, alias="pretty")
        envelope: Optional[bool] = Field(False, alias="envelope")
    class UpdateBodyParams(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        cluster_checkpoint_interval_min: Optional[float] = Field(alias="clusterCheckpointIntervalMin")
        cluster_id: Optional[str] = Field(alias="clusterId")
        daily_snapshot_retention_days: Optional[float] = Field(alias="dailySnapshotRetentionDays")
        full_incremental_day_of_week: Optional[str] = Field(alias="fullIncrementalDayOfWeek")
        group_id: Optional[str] = Field(alias="groupId")
        links: Optional[list[dict]] = Field(alias="links")
        monthly_snapshot_retention_months: Optional[float] = Field(alias="monthlySnapshotRetentionMonths")
        point_in_time_window_hours: Optional[float] = Field(alias="pointInTimeWindowHours")
        reference_hour_of_day: Optional[float] = Field(alias="referenceHourOfDay")
        reference_minute_of_hour: Optional[float] = Field(alias="referenceMinuteOfHour")
        reference_time_zone_offset: Optional[str] = Field(alias="referenceTimeZoneOffset")
        snapshot_interval_hours: Optional[float] = Field(alias="snapshotIntervalHours")
        snapshot_retention_days: Optional[float] = Field(alias="snapshotRetentionDays")
        weekly_snapshot_retention_weeks: Optional[float] = Field(alias="weeklySnapshotRetentionWeeks")
    def update(self,
        path_params: UpdatePathParams,
        query_params: Optional[UpdateQueryParams],
        body_params: Optional[UpdateBodyParams],
    ) -> dict[str, Any]:
        """API: Update the Snapshot Schedule
        Document: https://www.mongodb.com/docs/ops-manager/current/reference/api/backup/update-one-snapshot-schedule-by-cluster-id/
        Description: No description found."""
        return self._request(
            "PATCH",
            "/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/snapshotSchedule",
            path_params,
            query_params,
            body_params,
        )