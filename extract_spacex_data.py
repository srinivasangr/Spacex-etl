import requests
import boto3
import json
import csv
from datetime import datetime , timezone

# --- Configuration ---
API_URL = ["https://api.spacexdata.com/v4/launches"]
BUCKET_NAME = "spacex-bucket-s3-api"
FILE_TIMESTAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')

# --- Functions ---
def fetch_spacex_data(apis):
    response = requests.get(apis) # Fetch data from the SpaceX API
    response.raise_for_status()
    return response.json()

def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            # Convert lists to JSON strings or handle as needed
            items.append((new_key, json.dumps(v)))
        else:
            items.append((new_key, v))
    return dict(items)

def save_as_csv(data, filename):
    if not data:
        print("No data to write to CSV.")
        return
    flat_data = [flatten_dict(item) for item in data]
    keys = set()
    for item in flat_data:
        keys.update(item.keys())
    keys = sorted(keys)
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(flat_data)
    print(f"✅ Saved {len(data)} records to {filename}")

def upload_csv_to_s3(filename, s3_key):
    s3 = boto3.client("s3")
    with open(filename, "rb") as f:
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=s3_key,
            Body=f,
            ContentType="text/csv"
        )
    print(f"✅ Uploaded CSV to s3://{BUCKET_NAME}/{s3_key}")

def save_selected_fields_as_csv(data, filename):
    selected = []
    for launch in data:
        selected.append({
            "id": launch.get("id"),
            "name": launch.get("name"),
            "date_utc": launch.get("date_utc"),
            "success": launch.get("success"),
            "rocket": launch.get("rocket"),
            "details": launch.get("details"),
            "flight_number": launch.get("flight_number")
        })
    keys = ["id", "name", "date_utc", "success", "rocket", "details", "flight_number"]
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(selected)
    print(f"✅ Saved {len(selected)} records to {filename}")

# --- Main ---
if __name__ == "__main__":
    print("🚀 Fetching SpaceX data...")
    for api in API_URL:
        data = fetch_spacex_data(api)
        print(f"✅ Fetched {len(data)} records.")
        endpoint = api.split("/")[-1]
        csv_filename = f"spacex_{endpoint}_{FILE_TIMESTAMP}.csv"
        s3_key = f"csv/{csv_filename}"
        save_selected_fields_as_csv(data, csv_filename)
        upload_csv_to_s3(csv_filename, s3_key)













