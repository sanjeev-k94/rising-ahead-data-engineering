from dagster import ScheduleDefinition


daily_materialization_schedule = ScheduleDefinition(
    job_name="__ASSET_JOB",
    cron_schedule="0 9 * * *",
)