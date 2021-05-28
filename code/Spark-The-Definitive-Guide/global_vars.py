import os

import logging
this_file_path = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename=f'{this_file_path}/Spark-Solutions-Logs.log', encoding='utf-8', level=logging.INFO)

SPARK_MASTER_IP = os.getenv("SPARK_DEF_GUIDE_SPARK_MASTER_IP", "spark://localhost:7077")