import os
import logging

this_file_path = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename=f'{this_file_path}/PySpark-Solutins-Logs.log', encoding='utf-8', level=logging.INFO)

SPARK_MASTER_URL = os.getenv("MY_PYSPARK_SOL_SPARK_MASTER_URL", "spark://localhost:7077")