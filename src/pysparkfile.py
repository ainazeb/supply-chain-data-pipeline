# src/process_data.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, datediff

spark = SparkSession.builder.appName("SupplyChainDataProcessing").getOrCreate()

input_path = "download_from_s3/supply_chain_data.csv"
df = spark.read.csv(input_path, header=True, inferSchema=True)

df = df.withColumn("leadtime", datediff(col("delivery_date"), col("order_date")))

inventory_turnover = df.groupBy("product_id").sum("quantity")
order_fulfillment_rate = df.filter(col("quantity") > 0).count() / df.count()

print("\n📊 Inventory Turnover by Product:")
inventory_turnover.show()
print(f"\n✅ Order Fulfillment Rate: {order_fulfillment_rate:.2f}")

output_path = "processed_data/Processed_supply_chain_data.csv"
df.write.mode("overwrite").csv(output_path, header=True)

print(f"\n📁 Processed data saved to: {output_path}")
spark.stop()
