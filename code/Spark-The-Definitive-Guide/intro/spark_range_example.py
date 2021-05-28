from pyspark import Row

from global_initiator import *
import logging

logging.info("Enter")

app_name = "Spark Range Example"
spark_session: SparkSession = initialize_spark(app_name)

# Step 1: Create a RDD by paralleling ta range of numbers
range_rdd = spark_session.sparkContext.parallelize(range(1, 1000))

# Step 2: Count Action
total_count = range_rdd.count()
logging.info(f"Total Count {total_count}")

# Step 3: Convert to a Dataframe
row = Row("number")
range_df = range_rdd.map(row).toDF()

divided_by_2 = range_df.where(" number % 2 = 0")
divided_by_2.show(100)

shutdown_spark_ctx()

logging.info("Exit")