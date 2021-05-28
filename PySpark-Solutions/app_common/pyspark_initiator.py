from global_initiator import *
import pyspark


def create_spark_ctxt(app_name: str):
    sparkCtx = pyspark.SparkContext(appName="$app_name", master=SPARK_MASTER_URL)
    return sparkCtx
