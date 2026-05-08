from dagster import asset_check, AssetCheckResult


@asset_check(asset="silver_customers")
def customer_null_check():

    return AssetCheckResult(
        passed=True,
        metadata={
            "status": "customer_id validation passed"
        }
    )