from dagster import asset
import pandas as pd
from connectors.postgres_connector import engine
from datetime import datetime
import hashlib

from dagster import asset
import pandas as pd
from connectors.postgres_connector import engine
from datetime import datetime
import hashlib


def add_metadata(df):

    df["ingestion_time"] = datetime.now()

    df["row_hash"] = df.astype(str).apply(
        lambda x: hashlib.md5(
            ''.join(map(str, x)).encode()
        ).hexdigest(),
        axis=1
    )

    return df


@asset
def bronze_customers():

    df = pd.read_csv("data/customers.csv")

    df = add_metadata(df)

    df.to_sql(
        "bronze_customers",
        engine,
        if_exists="replace",
        index=False
    )

    return df


@asset
def bronze_accounts():

    df = pd.read_csv("data/accounts.csv")

    df = add_metadata(df)

    df.to_sql(
        "bronze_accounts",
        engine,
        if_exists="replace",
        index=False
    )

    return df


@asset
def bronze_transactions():

    df = pd.read_csv("data/transactions.csv")

    df = add_metadata(df)

    df.to_sql(
        "bronze_transactions",
        engine,
        if_exists="replace",
        index=False
    )

    return df


@asset
def bronze_loans():

    df = pd.read_csv("data/loans.csv")

    df = add_metadata(df)

    df.to_sql(
        "bronze_loans",
        engine,
        if_exists="replace",
        index=False
    )

    return df