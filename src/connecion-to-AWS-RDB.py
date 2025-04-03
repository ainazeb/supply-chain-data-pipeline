# src/create_db.py
import pymysql
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT", 3306))
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

try:
    connection = pymysql.connect(host=host, user=username, password=password, port=port)
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")
    cursor.execute(f"USE `{db_name}`;")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS supply_chain_data (
            order_id INT,
            product_id INT,
            quantity INT,
            order_date DATE,
            delivery_date DATE,
            warehouse_id VARCHAR(10),
            stock_level INT,
            leadtime INT,
            inventory_turnover INT,
            order_fulfillment_rate INT
        );
    """)
    print("✅ Database and table created successfully!")
    connection.close()
except Exception as e:
    print(f"❌ Error creating database/table: {e}")

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}")
try:
    with engine.connect() as conn:
        result = conn.execute(text("DESCRIBE supply_chain_data"))
        print("\n📌 Columns in 'supply_chain_data':")
        for row in result:
            print(row)
except Exception as e:
    print(f"❌ Error describing table: {e}")
