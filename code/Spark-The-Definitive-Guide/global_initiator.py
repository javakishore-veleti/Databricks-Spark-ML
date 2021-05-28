import pyspark
from pyspark import SparkContext

import global_vars

spark_ctx: SparkContext = None


def create_spark_context(app_name: str) -> SparkContext:
    spark_ctx = pyspark.SparkContext(master=global_vars.SPARK_MASTER_IP, appName=app_name)
    return spark_ctx


def initialize_spark(app_name:str) -> SparkContext:
    spark_ctx = create_spark_context(app_name)
    return spark_ctx
