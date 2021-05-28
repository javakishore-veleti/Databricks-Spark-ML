import pyspark
from pyspark.sql import SparkSession

from global_vars import *

global spark_ctx
global spark_session
spark_session:SparkSession = None


def create_spark_context(app_name: str) -> SparkSession:
    global spark_ctx
    spark_ctx = pyspark.SparkContext(master=SPARK_MASTER_IP, appName=app_name)

    global spark_session
    # spark_session = SparkSession(spark_ctx)
    spark_session = SparkSession.builder.master(SPARK_MASTER_IP).appName(app_name).getOrCreate()

    print(f"Spark Version : {spark_session.sparkContext.version}")
    return spark_session


def initialize_spark(app_name:str = "Undefined App Name") -> SparkSession:
    global spark_session
    spark_session = create_spark_context(app_name)
    return spark_session


def shutdown_spark_ctx():
    global spark_ctx
    if spark_ctx:
        spark_ctx.stop()

    global spark_session
    if spark_session:
        spark_session.stop()
