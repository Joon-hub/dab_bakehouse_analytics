# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,NYC Taxi Analysis Header
# MAGIC %md
# MAGIC # NYC Taxi Analysis
# MAGIC
# MAGIC This notebook analyzes NYC taxi trip data and is executed using a Lakeflow job similar to customer_360.

# COMMAND ----------

# DBTITLE 1,Setup Catalog and Schema
# Set default catalog and schema

# The following code creates interactive text input widgets in Databricks notebooks.
# Users can specify the catalog and schema names for their analysis.
# The first argument is the widget name, the second is the default value, and the third is the widget label.

dbutils.widgets.text("catalog", "bakehouse_analytics_dev", "Catalog")
dbutils.widgets.text("schema", "default", "Schema")

# Set the catalog and schema
catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

# Create the schema if it doesn't exist
spark.sql(f"USE CATALOG {catalog}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {schema}")
spark.sql(f"USE SCHEMA {schema}")

# COMMAND ----------

# DBTITLE 1,Load NYC Taxi Data
# Read NYC taxi sample data
df = spark.table("samples.nyctaxi.trips")
display(df.limit(5))

# COMMAND ----------

# DBTITLE 1,Analyze Trip Data
from pyspark.sql import functions as F

# Business logic: Analyze trips by pickup location
trip_analysis = df \
  .groupBy("pickup_zip") \
  .agg(
    F.count("*").alias("total_trips"),
    F.avg("fare_amount").alias("avg_fare"),
    F.avg("trip_distance").alias("avg_distance"),
    F.sum("fare_amount").alias("total_revenue")
  ) \
  .orderBy(F.desc("total_trips"))

# Write to Unity Catalog
trip_analysis.write.mode("overwrite") \
  .saveAsTable(f"{catalog}.{schema}.nyc_taxi_analysis")

# COMMAND ----------

# DBTITLE 1,Display Results
display(spark.table(f"{catalog}.{schema}.nyc_taxi_analysis"))

# COMMAND ----------


