import requests
import json
from pathlib import Path

def fetch_data():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Saving as .json to parse for loading
    raw_path = Path("data/raw/products.json")
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    with open(raw_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Data saved to {raw_path}")
    return raw_path

if __name__ == "__main__":
    fetch_data()
