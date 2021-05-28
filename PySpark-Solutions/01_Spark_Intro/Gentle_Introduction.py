from app_common.pyspark_initiator import *
import logging

logging.info('Enter')

app_name = "Gentle Introduction"
sparkCtx = create_spark_ctxt(app_name)

numbers_rdd = sparkCtx.parallelize(range(1,1000))
count_value = numbers_rdd.count()
logging.info(f'count_value {count_value}')

logging.info('Exit')


