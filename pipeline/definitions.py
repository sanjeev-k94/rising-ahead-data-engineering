from dagster import Definitions

from pipeline.assets.bronze import (
    bronze_customers,
    bronze_accounts,
    bronze_transactions,
    bronze_loans
)

from pipeline.assets.silver import (
    silver_customers,
    silver_accounts,
    silver_transactions,
    silver_loans
)

from pipeline.assets.gold import gold_customer_summary

from pipeline.assets.gold_analytics import gold_monthly_analytics
from pipeline.assets.gold_risk import gold_risk_scoring

from pipeline.schedules.daily_schedule import daily_materialization_schedule

from pipeline.checks.customer_checks import customer_null_check

from pipeline.sensors.file_sensor import csv_update_sensor


defs = Definitions(
    assets=[
        bronze_customers,
        bronze_accounts,
        bronze_transactions,
        bronze_loans,

        silver_customers,
        silver_accounts,
        silver_transactions,
        silver_loans,

        gold_customer_summary,
        gold_monthly_analytics,
        gold_risk_scoring
    ],

    schedules=[
        daily_materialization_schedule
    ],

    sensors=[
        csv_update_sensor
    ],

    asset_checks=[
        customer_null_check
    ]
)