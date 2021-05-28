from global_initiator import *
from util_functions import download_url_file

download_url_file(FLIGHT_DATA_CSV_URL_2015_SUMMARY, FLIGHT_DATA_CSV_LOCAL_2015_SUMMARY)

spark_session = initialize_spark(f"Flight Data 2015 Summary - SQL Way - {CURR_DATE_TIME}")

flight_data_2015_summary_df = spark_session.read.option('inferSchema', 'true').option('header', 'true')\
    .csv(FLIGHT_DATA_CSV_LOCAL_2015_SUMMARY)

tmp_view_name = "flight_data_2015_summary_temp_view"
flight_data_2015_summary_df.createOrReplaceTempView(tmp_view_name)

result = spark_session.sql("""
SELECT DEST_COUNTRY_NAME, COUNT(*) AS COUNTRY_COUNT
FROM flight_data_2015_summary_temp_view
GROUP BY DEST_COUNTRY_NAME
ORDER BY DEST_COUNTRY_NAME
""")

result.show()

shutdown_spark_ctx()
