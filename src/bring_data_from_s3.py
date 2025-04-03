# src/download_from_s3.py
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
AWS_REGION = os.getenv('AWS_REGION')

def download_from_s3(bucket_name, file_key, download_path):
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )
    s3 = session.client('s3')
    s3.download_file(bucket_name, file_key, download_path)
    print(f"✅ Downloaded {file_key} from {bucket_name} to {download_path}")

if __name__ == "__main__":
    os.makedirs("download_from_s3", exist_ok=True)
    download_from_s3("supply-chain-data-2024", "supply_chain_data.csv", "download_from_s3/supply_chain_data.csv")
