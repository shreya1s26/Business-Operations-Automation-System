import pandas as pd
import mysql.connector
from api_fetch import fetch_api_data
from config import DB_CONFIG
from datetime import datetime

def connect_db():
    return mysql.connector.connect(**DB_CONFIG)

def clean_data(raw_data):
    df = pd.DataFrame(raw_data)
    df.dropna(inplace=True)
    df["revenue"] = df["revenue"].astype(float)
    df["created_at"] = pd.to_datetime(df["created_at"])
    return df

def load_to_db(df):
    conn = connect_db()
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO operations_data (order_id, customer_id, revenue, created_at)
        VALUES (%s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        cursor.execute(insert_query, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()

def generate_report(df):
    report = df.groupby(df["created_at"].dt.date)["revenue"].sum()
    report.to_excel(f"weekly_report_{datetime.now().date()}.xlsx")

def run_pipeline():
    raw_data = fetch_api_data()
    cleaned_df = clean_data(raw_data)
    load_to_db(cleaned_df)
    generate_report(cleaned_df)

if __name__ == "__main__":
    run_pipeline()
