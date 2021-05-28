import os

import logging

this_file_path = os.path.dirname(os.path.realpath(__file__))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("{0}/{1}.log".format(this_file_path, "Spark-Solutions-Logs")),
        logging.StreamHandler()
    ]
)

# logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
# rootLogger = logging.getLogger()

# fileHandler = logging.FileHandler("{0}/{1}.log".format(this_file_path, "Spark-Solutions-Logs"))
# fileHandler.setFormatter(logFormatter)
# fileHandler.setLevel(logging.INFO)
# rootLogger.addHandler(fileHandler)

# consoleHandler = logging.StreamHandler()
# consoleHandler.setFormatter(logFormatter)
# consoleHandler.setLevel(logging.INFO)
# rootLogger.addHandler(consoleHandler)

# logging.basicConfig(filename=f'{this_file_path}/Spark-Solutions-Logs.log', encoding='utf-8', level=logging.DEBUG)
# CAUTION: Below logger setLevel is required to resolve the issue "pyspark Message: 'Answer received: !yv'"
logging.getLogger('pyspark').setLevel(logging.ERROR)
logging.getLogger("py4j").setLevel(logging.ERROR)
logging.getLogger("matplotlib").setLevel(logging.ERROR)

SPARK_MASTER_IP = os.getenv("SPARK_DEF_GUIDE_SPARK_MASTER_IP", "spark://localhost:7077")

# CAUTION: /tmp/docker-mount folder is created in the spark-cluster-start.sh docker compose UP script in this project
TMP_BASE_PATH_DOWNLOAD = '/tmp/docker-mount/Spark-The-Definitive-Guide/Downloads'

FLIGHT_DATA_CSV_BASE_URL = 'http://raw.githubusercontent.com/databricks/Spark-The-Definitive-Guide/master/data' \
                           '/flight-data/csv'

# Columns -> DEST_COUNTRY_NAME	ORIGIN_COUNTRY_NAME	count
FLIGHT_DATA_CSV_FILE_NAME_2015_SUMMARY = "2015-summary.csv"

FLIGHT_DATA_CSV_URL_2015_SUMMARY = f"{FLIGHT_DATA_CSV_BASE_URL}/{FLIGHT_DATA_CSV_FILE_NAME_2015_SUMMARY}"
FLIGHT_DATA_CSV_LOCAL_2015_SUMMARY = f"{TMP_BASE_PATH_DOWNLOAD}/{FLIGHT_DATA_CSV_FILE_NAME_2015_SUMMARY}"

if not os.path.exists(TMP_BASE_PATH_DOWNLOAD):
    os.makedirs(TMP_BASE_PATH_DOWNLOAD)

from datetime import datetime

CURR_DATE_TIME = datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
