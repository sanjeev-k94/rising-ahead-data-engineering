from dagster import asset_check, AssetCheckResult
import pandas as pd


@asset_check(asset="silver_customers")
def customer_null_check():

    df = pd.read_csv("data/customers.csv")

    passed = df["customer_id"].isnull().sum() == 0

    return AssetCheckResult(
        passed=passed,
        metadata={
            "null_customer_ids": int(df["customer_id"].isnull().sum())
        }
    )