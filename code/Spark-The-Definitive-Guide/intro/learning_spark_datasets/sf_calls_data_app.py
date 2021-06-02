import os
import requests
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import *
import pyspark.sql.functions as f
from time import sleep

sf_fire_calls_dataset_url_path = "https://raw.githubusercontent.com/databricks/LearningSparkV2/master/chapter3/data/sf-fire-calls.csv"
sf_fire_calls_dataset_local_path = "/tmp/sf_fire_calls.csv"


def download_sf_first_calls_dataset():
    if not os.path.exists(sf_fire_calls_dataset_local_path):
        r = requests.get(sf_fire_calls_dataset_url_path, allow_redirects=True)
        with open(sf_fire_calls_dataset_local_path, 'wb') as f:
            f.write(r.content)
    return


def create_spark_session(app_name: str) -> SparkSession:
    spark_session = SparkSession.builder.appName(app_name).getOrCreate()
    return spark_session


def stop_spark_session(spark_session: SparkSession, sleep_time: int = 50):
    sleep(sleep_time)
    spark_session.stop()


def load_sf_first_dataframe(spark_session: SparkSession) -> DataFrame:
    sf_fire_calls_df = spark_session.read.option("header", "true").option("inferSchema", "true").csv(
        sf_fire_calls_dataset_local_path)
    sf_fire_calls_df = sf_fire_calls_df.withColumn("CallDate_Year", f.year(f.to_timestamp('CallDate', 'dd/MM/yyyy')))
    return sf_fire_calls_df


def sol_1_diff_types_of_fire_calls_2018():
    spark_session = create_spark_session(app_name="Sol 1 - Different Types of Fire Calls in 2018")
    sf_fire_calls_df = load_sf_first_dataframe(spark_session)
    sf_fire_calls_df.filter(expr("CallDate_Year == 2018 ")).select("CallType").distinct().orderBy("CallType").show(
        n=100, truncate=False)
    stop_spark_session(spark_session)


def sol_2_months_within_2018_highest_no_of_first_calls():
    pass


def sol_3_neighborhood_in_sfo_most_fire_calls_2018():
    pass


download_sf_first_calls_dataset()
sol_1_diff_types_of_fire_calls_2018()
