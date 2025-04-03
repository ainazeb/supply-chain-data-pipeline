# 📦 Supply Chain Data Pipeline

A complete end-to-end data engineering project for simulating, processing, and serving large-scale supply chain data using PySpark, AWS S3, MySQL (RDS), and Flask API.

---

## 🧩 What This Project Does

 Generates 5 million synthetic supply chain records  
 Uploads and downloads data via AWS S3  
 Cleans and enriches data using PySpark (lead time, KPIs)  
 Stores processed data in AWS RDS (MySQL)  
 Exposes a REST API using Flask for data access  

---



---

## ⚙️ Technologies Used

- Python — core language  
- PySpark — large-scale data processing  
- AWS S3 — cloud storage  
- AWS RDS (MySQL)— relational database  
- Flask — REST API framework  
- SQLAlchemy / Pandas — DB + file operations  
- dotenv — secure credential loading  

---

## 🔐 Environment Setup

### 1. Install Requirements

```bash
pip install -r requirements.txt


add a .env file:
DB_HOST=your-db-hostname
DB_PORT=3306
DB_USERNAME=your-db-user
DB_PASSWORD=your-db-password
DB_NAME=supply-chain

AWS_ACCESS_KEY=your-aws-key
AWS_SECRET_KEY=your-aws-secret
AWS_REGION=your-region
-------

🔁 Run the Pipeline

# 1. Generate fake supply chain data (5M rows) ( I uploaded it my S3 storage)
python src/generate_data.py

# 2. Download the dataset from S3
python src/download_from_s3.py

# 3. Process the data with Spark (leadtime, KPIs)
python src/process_data.py

# 4. Create database & table on AWS RDS
python src/create_db.py

# 5. Load processed data into MySQL RDS
python src/load_data.py

# 6. Start Flask API
python src/api.py
-----------

Then go to:

http://localhost:5000/data

------------------------

📊 KPIs Processed
Metric	Description
leadtime	delivery_date - order_date
inventory_turnover	Sum of quantity per product
order_fulfillment_rate	Ratio of successful orders over total orders
-----------------------

Sample API Response:

[
  {
    "order_id": 1,
    "product_id": 3,
    "quantity": 10,
    "order_date": "2025-05-10",
    "delivery_date": "2025-05-13",
    "leadtime": 3,
    "warehouse_id": "WH3",
    "stock_level": 120,
    "inventory_turnover": 9870,
    "order_fulfillment_rate": 0.98
  },
  ...
]

--------------------

BY: Ainaz Ebrahimi






