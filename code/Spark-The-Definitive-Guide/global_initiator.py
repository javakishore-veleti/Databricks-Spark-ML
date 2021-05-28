import pyspark
from pyspark import SparkContext

import global_vars

global spark_ctx


def create_spark_context(app_name: str) -> SparkContext:
    global spark_ctx
    spark_ctx = pyspark.SparkContext(master=global_vars.SPARK_MASTER_IP, appName=app_name)
    return spark_ctx


def initialize_spark(app_name:str) -> SparkContext:
    global spark_ctx
    spark_ctx = create_spark_context(app_name)
    return spark_ctx


def shutdown_spark_ctx():
    global spark_ctx
    if spark_ctx:
        spark_ctx.stop()
