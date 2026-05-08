from dagster import asset
import pandas as pd
from connectors.postgres_connector import engine


@asset
def gold_monthly_analytics():

    df = pd.read_sql(
        "SELECT * FROM silver_transactions",
        engine
    )

    analytics = (
        df.groupby("merchant")
        .agg(
            total_transactions=("transaction_id", "count"),
            total_amount=("amount", "sum")
        )
        .reset_index()
    )

    analytics.to_sql(
        "gold_monthly_analytics",
        engine,
        if_exists="replace",
        index=False
    )

    return analytics