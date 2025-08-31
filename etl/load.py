import sqlite3
import pandas as pd
from pathlib import Path

def load_to_db(processed_path="data/processed/products.parquet"):
    conn = sqlite3.connect("products.db")
    df = pd.read_parquet(processed_path)

    ## Renaming price column as per the instruction
    if "price" in df.columns:
        df.rename(columns={"price": "price_usd"}, inplace=True)

    ## Dropping unsupported columns
    if "rating" in df.columns:
        df = df.drop(columns=["rating"])

    ## Load the data to SQLite
    df.to_sql("products", conn, if_exists="replace", index=False)

    conn.close()
    ## print(f"Data loaded into SQLite database 'products.db', total rows: {len(df)}")

## Run directly when script executed
if __name__ == "__main__":
    load_to_db()
