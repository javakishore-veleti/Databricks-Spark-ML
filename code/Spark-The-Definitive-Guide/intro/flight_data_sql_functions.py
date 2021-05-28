from global_initiator import *
from util_functions import download_url_file

# https://github.com/databricks/Spark-The-Definitive-Guide/blob/master/code/A_Gentle_Introduction_to_Spark-Chapter_2_A_Gentle_Introduction_to_Spark.py
download_url_file(FLIGHT_DATA_CSV_URL_2015_SUMMARY, FLIGHT_DATA_CSV_LOCAL_2015_SUMMARY)

spark_session = initialize_spark(f"Flight Data 2015 Summary - SQL Functions - {CURR_DATE_TIME}")
flight_data_2015_summary = spark_session.read.option('header', 'true').option('inferSchema', 'true').csv(FLIGHT_DATA_CSV_LOCAL_2015_SUMMARY)

flight_data_2015_summary.createOrReplaceTempView("flight_data_2015_summary_temp_view")

sql_result = spark_session.sql("""
SELECT 
    DEST_COUNTRY_NAME, min(count) AS MIN_COUNT
FROM flight_data_2015_summary_temp_view
GROUP BY DEST_COUNTRY_NAME
ORDER BY MIN_COUNT
""")

sql_result.show(10000)
logging.info(f"sql_result -> {sql_result}")

shutdown_spark_ctx()

logging.info("Exit")