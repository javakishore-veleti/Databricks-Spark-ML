from global_initiator import *
from util_functions import download_url_file

logging.info("Enter")

# https://github.com/databricks/Spark-The-Definitive-Guide/blob/master/code/A_Gentle_Introduction_to_Spark-Chapter_2_A_Gentle_Introduction_to_Spark.py
download_url_file(FLIGHT_DATA_CSV_URL_2015_SUMMARY, FLIGHT_DATA_CSV_LOCAL_2015_SUMMARY)

spark_session = initialize_spark(f"Flight Data 2015 Summary - DF Way Functions - {CURR_DATE_TIME}")

flight_data_2015_summary_df = spark_session.read.option("header", "true").option("inferSchema", "true").csv(FLIGHT_DATA_CSV_LOCAL_2015_SUMMARY)

from pyspark.sql.functions import window, col, desc, sum

flight_data_group_by_df = flight_data_2015_summary_df.groupby("DEST_COUNTRY_NAME").sum("count")\
    .withColumnRenamed("sum(count)","destination_total")\
    .sort(desc("destination_total"))

flight_data_group_by_df.show()
flight_data_group_by_df.explain(extended=True)

shutdown_spark_ctx()

logging.info("Exit")