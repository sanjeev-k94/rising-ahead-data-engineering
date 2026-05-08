from dagster import asset
import pandas as pd
from connectors.postgres_connector import engine

from dagster import asset
import pandas as pd
from connectors.postgres_connector import engine


def clean_dataframe(df):

    df = df.drop_duplicates()

    df.columns = [col.lower() for col in df.columns]

    df = df.fillna("unknown")

    return df


@asset
def silver_customers():

    df = pd.read_sql(
        "SELECT * FROM bronze_customers",
        engine
    )

    df = clean_dataframe(df)

    df.to_sql(
        "silver_customers",
        engine,
        if_exists="replace",
        index=False
    )

    return df


@asset
def silver_accounts():

    df = pd.read_sql(
        "SELECT * FROM bronze_accounts",
        engine
    )

    df = clean_dataframe(df)

    df.to_sql(
        "silver_accounts",
        engine,
        if_exists="replace",
        index=False
    )

    return df


@asset
def silver_transactions():

    df = pd.read_sql(
        "SELECT * FROM bronze_transactions",
        engine
    )

    df = clean_dataframe(df)

    df.to_sql(
        "silver_transactions",
        engine,
        if_exists="replace",
        index=False
    )

    return df


@asset
def silver_loans():

    df = pd.read_sql(
        "SELECT * FROM bronze_loans",
        engine
    )

    df = clean_dataframe(df)

    df.to_sql(
        "silver_loans",
        engine,
        if_exists="replace",
        index=False
    )

    return df