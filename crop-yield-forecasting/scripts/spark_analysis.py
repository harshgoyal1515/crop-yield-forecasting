import findspark
findspark.init("C:\\spark-3.4.1-bin-hadoop3")

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# Start Spark session
spark = SparkSession.builder \
    .appName("CropYieldSparkAnalysis") \
    .getOrCreate()

# ✅ Load CSV into Spark DataFrame
df = spark.read.csv("clean_crop_weather_historical.csv", header=True, inferSchema=True)

# ✅ Show schema and a few rows
df.printSchema()
df.show(5)

# ✅ Select all yield columns (end with "_yield_kg_per_ha")
yield_cols = [col_name for col_name in df.columns if col_name.endswith("_yield_kg_per_ha")]

# ✅ Compute average yield per crop (ignoring nulls)
for crop_col in yield_cols:
    crop_name = crop_col.replace("_yield_kg_per_ha", "")
    print(f"\n📈 Average yield for {crop_name}:")
    df.select(avg(col(crop_col)).alias("avg_yield")).show()

# ✅ Stop Spark session
spark.stop()
