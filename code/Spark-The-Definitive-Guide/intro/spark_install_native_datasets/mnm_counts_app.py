from __future__ import print_function

import os
from time import sleep

import requests
from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame

mnm_dataset_url_path = "https://raw.githubusercontent.com/databricks/LearningSparkV2/master/chapter2/py/src/data/mnm_dataset.csv"
mnm_dataset_local_path = "/tmp/mnm_dataset.csv"


def download_mnm_dataset():
    if not os.path.exists(mnm_dataset_local_path):
        r = requests.get(mnm_dataset_url_path, allow_redirects=True)
        with open(mnm_dataset_local_path, 'wb') as f:
            f.write(r.content)
    return


def create_spark_session() -> SparkSession:
    return SparkSession.builder.appName("MnM Counts App").getOrCreate()


def count_all_colors(mnm_dataset_raw_df: DataFrame):
    order_by_df = mnm_dataset_raw_df.select("State", "Color", "Count").groupBy("State", "Color").sum("Count").orderBy(
        "sum(Count)", ascending=False)
    no_of_rows = order_by_df.count()
    print(f"No of Rows {no_of_rows}")
    order_by_df.show(n=500, truncate=False)
    return


download_mnm_dataset()
spark_session = create_spark_session()

mnm_dataset_raw_df = spark_session.read.option("inferSchema", "true").option("header", "true").csv(mnm_dataset_local_path)
count_all_colors(mnm_dataset_raw_df)


sleep(100)