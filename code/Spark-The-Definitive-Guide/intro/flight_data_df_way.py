from global_initiator import *
from util_functions import download_url_file

logging.info("Enter")

# https://github.com/databricks/Spark-The-Definitive-Guide/blob/master/code/A_Gentle_Introduction_to_Spark-Chapter_2_A_Gentle_Introduction_to_Spark.py
download_url_file(FLIGHT_DATA_CSV_URL_2015_SUMMARY, FLIGHT_DATA_CSV_LOCAL_2015_SUMMARY)

spark_session = initialize_spark(f"Flight Data 2015 Summary - DF Way - {CURR_DATE_TIME}")

flight_data_2015_summary_df = spark_session.read.option("inferSchema", "true").option("header", "true").csv(FLIGHT_DATA_CSV_LOCAL_2015_SUMMARY)

dest_country_count = flight_data_2015_summary_df.groupby("DEST_COUNTRY_NAME").count().take(1)
logging.info(f"Exit dest_country_count {dest_country_count}")

shutdown_spark_ctx()

logging.info("Exit")