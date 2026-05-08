from dagster import asset
import pandas as pd
from connectors.postgres_connector import engine


@asset
def gold_risk_scoring():

    df = pd.read_sql(
        "SELECT * FROM silver_transactions",
        engine
    )

    df["amount"] = pd.to_numeric(
        df["amount"],
        errors="coerce"
    )

    df = df.dropna(subset=["amount"])

    risk = (
        df.groupby("customer_id")
        .agg(
            transaction_count=("transaction_id", "count"),
            total_spend=("amount", "sum"),
            average_spend=("amount", "mean")
        )
        .reset_index()
    )

    risk.to_sql(
        "gold_risk_scoring",
        engine,
        if_exists="replace",
        index=False
    )

    return risk