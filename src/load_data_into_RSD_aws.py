# src/load_data.py
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

db_endpoint = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT", 3306)

connection_string = f"mysql+pymysql://{username}:{password}@{db_endpoint}:{port}/{db_name}"
engine = create_engine(connection_string)

file_path = "processed_data/Processed_supply_chain_data.csv"

try:
    df = pd.read_csv(file_path)
    print(f"✅ Loaded processed file: {file_path}")
except Exception as e:
    print(f"❌ Failed to load CSV file: {e}")
    exit()

try:
    df.to_sql("supply_chain_data", engine, if_exists="append", index=False)
    print("✅ Data inserted into the RDS database successfully!")
except Exception as e:
    print(f"❌ Failed to insert data into RDS: {e}")
