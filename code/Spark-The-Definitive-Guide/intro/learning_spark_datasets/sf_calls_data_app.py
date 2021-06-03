import os
import requests
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import *
import pyspark.sql.functions as f
from time import sleep
from global_vars import logging

sf_fire_calls_dataset_url_path = "https://raw.githubusercontent.com/databricks/LearningSparkV2/master/chapter3/data/sf-fire-calls.csv"
sf_fire_calls_dataset_local_path = "/tmp/sf_fire_calls.csv"

global spark_session
global sf_fire_calls_df
spark_session: SparkSession = None
sf_fire_calls_df:DataFrame = None


def download_sf_first_calls_dataset():
    if not os.path.exists(sf_fire_calls_dataset_local_path):
        logging.info(f"Downloading the SFO Fire Calls Dataset from {sf_fire_calls_dataset_url_path}")
        r = requests.get(sf_fire_calls_dataset_url_path, allow_redirects=True)
        with open(sf_fire_calls_dataset_local_path, 'wb') as f:
            f.write(r.content)

    logging.info(f"SFO Fire Calls Dataset is located at {sf_fire_calls_dataset_url_path}")
    return


def create_spark_session(app_name: str = "SFO Fire Calls Data Analytics App"):
    global spark_session
    logging.info(f"Creating the Spark Session with app_name as {app_name}")
    spark_session = SparkSession.builder.appName(app_name).getOrCreate()


def stop_spark_session(sleep_time: int = 10):
    sleep(sleep_time)
    global spark_session

    logging.info(f"Stopping the Spark Session")
    spark_session.stop()


def load_sf_first_dataframe() -> DataFrame:
    global spark_session
    logging.info(f"Spark Reading the CSV for SFO Fire Calls Dataset")
    sf_fire_calls_df = spark_session.read.option("header", "true").option("inferSchema", "true").csv(
        sf_fire_calls_dataset_local_path)
    sf_fire_calls_df = sf_fire_calls_df.withColumn("CallDate_Year", f.year(f.to_timestamp('CallDate', 'dd/MM/yyyy')))
    sf_fire_calls_df.cache()
    return sf_fire_calls_df


def sol_1_diff_types_of_fire_calls_2018():
    logging.info(f"Use Case 01: sol_1_diff_types_of_fire_calls_2018 Enter")
    global sf_fire_calls_df
    sf_fire_calls_df.select("CallType").where(col("CallType").isNotNull()).filter(
        expr("CallDate_Year == 2018 ")).distinct().orderBy("CallType").show(
        n=100, truncate=False)
    logging.info(f"Use Case 01: sol_1_diff_types_of_fire_calls_2018 Exit")


def sol_1_diff_types_of_fire_calls_2018_count():
    logging.info(f"Use Case 01: sol_1_diff_types_of_fire_calls_2018_count Enter")

    global sf_fire_calls_df

    count = sf_fire_calls_df.select("CallType").where(col("CallType").isNotNull()).filter(
        expr("CallDate_Year == 2018 ")).distinct().orderBy("CallType").count()
    logging.info(f"Count {count}")
    logging.info(f"Use Case 01: sol_1_diff_types_of_fire_calls_2018_count Exit")


def sol_2_Find_out_all_response_or_delayed_times_greater_than_5_mins():
    logging.info(f"Use Case 02: sol_2_Find_out_all_response_or_delayed_times_greater_than_5_mins Exit")
    global sf_fire_calls_df

    sf_fire_calls_df.select("Delay").where(expr("Delay > 5")).withColumnRenamed("Delay", "ResponseDelayedinMins").show(n=10000, truncate=False)
    logging.info(f"Use Case 02: sol_2_Find_out_all_response_or_delayed_times_greater_than_5_mins Exit")


def sol_3_what_were_the_most_common_call_types():
    logging.info(f"Use Case 03: sol_3_what_were_the_most_common_call_types Exit")
    global sf_fire_calls_df
    sf_fire_calls_df.select("CallType").groupBy("CallType").count().orderBy("count", ascending=False).show(n=1000, truncate=False)
    logging.info(f"Use Case 03: sol_3_what_were_the_most_common_call_types Exit")


download_sf_first_calls_dataset()
create_spark_session()

sf_fire_calls_df = load_sf_first_dataframe()

sol_1_diff_types_of_fire_calls_2018()
sol_1_diff_types_of_fire_calls_2018_count()
sol_2_Find_out_all_response_or_delayed_times_greater_than_5_mins()
sol_3_what_were_the_most_common_call_types()

stop_spark_session()
