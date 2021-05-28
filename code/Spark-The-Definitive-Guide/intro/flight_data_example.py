from global_initiator import *
from util_functions import download_url_file

logging.info("Enter")

# https://github.com/databricks/Spark-The-Definitive-Guide/blob/master/code/A_Gentle_Introduction_to_Spark-Chapter_2_A_Gentle_Introduction_to_Spark.py
download_url_file(FLIGHT_DATA_CSV_URL_2015_SUMMARY, FLIGHT_DATA_CSV_LOCAL_2015_SUMMARY)

spark_session = initialize_spark(f"Flight Data 2015 Summary - {CURR_DATE_TIME}")

flight_data_summary_2015_df = spark_session.read\
    .option("inferSchema", "true").option("header", "true").csv(FLIGHT_DATA_CSV_LOCAL_2015_SUMMARY)

flight_data_summary_2015_df.createOrReplaceTempView("flight_data_summary_2015_tmp_view")

sqlWay = spark_session.sql("""
SELECT DEST_COUNTRY_NAME, count(1)
FROM flight_data_summary_2015_tmp_view
GROUP BY DEST_COUNTRY_NAME
""")

sqlWay.show()

dataframe_way = flight_data_summary_2015_df.groupby("DEST_COUNTRY_NAME").count()
dataframe_way.show()

sqlWay.explain()
dataframe_way.explain()

from pyspark.sql.functions import max
result = flight_data_summary_2015_df.select(max("count")).take(1)
logging.info(f"flight_data_summary_2015_df max(count).take(1) {result}")

shutdown_spark_ctx()

logging.info("Exit")