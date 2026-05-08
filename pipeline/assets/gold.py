from dagster import asset
import pandas as pd
from connectors.postgres_connector import engine

@asset
def gold_customer_summary():

    df = pd.read_sql(
        "SELECT * FROM silver_customers",
        engine
    )

    summary = pd.DataFrame()

    summary["total_customers"] = [len(df)]

    summary["unique_cities"] = [df["city"].nunique() if "city" in df.columns else 0]

    summary.to_sql(
        "gold_customer_summary",
        engine,
        if_exists="replace",
        index=False
    )

    return summary