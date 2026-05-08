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

        gold_customer_summary
    ]
)