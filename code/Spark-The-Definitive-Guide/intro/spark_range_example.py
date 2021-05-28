from global_initiator import *
import logging

app_name = "Spark Range Example"
spark_ctx = initialize_spark(app_name)

range_rdd = spark_ctx.parallelize(range(1,1000))
total_count = range_rdd.count()

logging.info(f"Total Count {total_count}")




