# src/api.py
from flask import Flask, jsonify
from sqlalchemy import create_engine
import pandas as pd
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

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    query = "SELECT * FROM supply_chain_data LIMIT 10"
    df = pd.read_sql(query, engine)
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
