import pandas as pd


def test_customers_csv_not_empty():

    df = pd.read_csv("data/customers.csv")

    assert len(df) > 0


def test_accounts_csv_not_empty():

    df = pd.read_csv("data/accounts.csv")

    assert len(df) > 0


def test_transactions_csv_not_empty():

    df = pd.read_csv("data/transactions.csv")

    assert len(df) > 0


def test_loans_csv_not_empty():

    df = pd.read_csv("data/loans.csv")

    assert len(df) > 0


def test_customer_id_column_exists():

    df = pd.read_csv("data/customers.csv")

    assert "customer_id" in df.columns


def test_no_null_customer_ids():

    df = pd.read_csv("data/customers.csv")

    assert df["customer_id"].isnull().sum() == 0