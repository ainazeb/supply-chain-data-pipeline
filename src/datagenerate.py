import csv
import random
from datetime import datetime, timedelta

# Define the output file name
output_file = "supply_chain_data.csv"

# Define the number of rows you want to generate
num_rows = 5000000  # You can change this to any number of rows you need

# Define the warehouses and products
warehouses = ["WH1", "WH2", "WH3", "WH4", "WH5"]
products = [1, 2, 3, 4, 5]


# Function to generate random dates
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


# Generate the data
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(
        ["order_id", "product_id", "quantity", "order_date", "delivery_date", "warehouse_id", "stock_level"])

    # Generate rows
    for order_id in range(1, num_rows + 1):
        product_id = random.choice(products)
        quantity = random.randint(1, 20)  # Random quantity between 1 and 20
        order_date = random_date(datetime(2025, 1, 1), datetime(2025, 12, 31))
        delivery_date = order_date + timedelta(days=random.randint(1, 10))  # Delivery within 1-10 days
        warehouse_id = random.choice(warehouses)
        stock_level = random.randint(50, 500)  # Random stock level between 50 and 500

        # Write the row
        writer.writerow(
            [order_id, product_id, quantity, order_date.strftime("%Y-%m-%d"), delivery_date.strftime("%Y-%m-%d"),
             warehouse_id, stock_level])

print(f"Generated {num_rows} rows of supply chain data in '{output_file}'")
