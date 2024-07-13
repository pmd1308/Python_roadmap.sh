import requests
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_data(endpoint):
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        os.makedirs('data/raw', exist_ok=True)
        with open('data/raw/audit_dataset.csv', 'wb') as file:
            file.write(response.content)
        logging.info("Data fetched successfully")
    except requests.RequestException as e:
        logging.error(f"Failed to fetch data: {e}")

if __name__ == "__main__":
    fetch_data("https://dataset.api.hub.geosphere.at/v1/datasets")