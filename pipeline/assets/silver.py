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