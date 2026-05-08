from dagster import sensor, RunRequest
import os


@sensor(job_name="__ASSET_JOB")
def csv_update_sensor():

    if os.path.exists("data/customers.csv"):
        yield RunRequest(run_key=None)