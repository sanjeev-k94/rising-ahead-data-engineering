from dagster import asset, get_dagster_logger
import pandas as pd
from connectors.postgres_connector import engine
import hashlib


def generate_hash(row):

    return hashlib.md5(
        str(row.values).encode()
    ).hexdigest()


def clean_dataframe(df):

    df = df.drop_duplicates()

    df.columns = [col.lower() for col in df.columns]

    df = df.fillna("unknown")

    df["row_hash"] = df.apply(
        generate_hash,
        axis=1
    )

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

    logger = get_dagster_logger()

    logger.info(
        "Starting silver_transactions pipeline"
    )

    df = pd.read_sql(
        "SELECT * FROM bronze_transactions",
        engine
    )

    df = clean_dataframe(df)

    logger.info(
        f"Rows after cleaning: {len(df)}"
    )

    try:

        existing_df = pd.read_sql(
            "SELECT * FROM silver_transactions",
            engine
        )

        new_records = df[
            ~df["row_hash"].isin(
                existing_df["row_hash"]
            )
        ]

        logger.info(
            f"New records detected: {len(new_records)}"
        )

    except:

        new_records = df

        logger.info(
            "No existing silver table found"
        )

    try:

        new_records.to_sql(
            "silver_transactions",
            engine,
            if_exists="append",
            index=False
        )

        logger.info(
            "silver_transactions loaded successfully"
        )

    except Exception as e:

        logger.error(
            f"Pipeline failed: {e}"
        )

        raise

    return new_records


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