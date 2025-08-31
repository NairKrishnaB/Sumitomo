import json
import pandas as pd
from pathlib import Path

def transform_data(raw_path="data/raw/products.json"):
    # Loading data
    with open(raw_path, "r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    # Converting exchange rate USD to GBP
    usd_to_gbp = 0.8 
    df["price_gbp"] = df["price"] * usd_to_gbp

    # Categorise expensive products
    df["expensive_flag"] = df["price_gbp"] > 100

    # Save processed data as parquet
    processed_path = Path("data/processed/products.parquet")
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(processed_path, index=False)

    print(f"Data transformed and saved to {processed_path}")
    return processed_path

# Run directly when script executed
if __name__ == "__main__":
    transform_data()
