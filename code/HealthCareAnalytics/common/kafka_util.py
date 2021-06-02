from pyspark.sql.session import SparkSession
from pyspark.sql.streaming import DataStreamReader

from common import kafka_config


def spark_streaming_subscribe_to_topic(topic_name: str, spark_session: SparkSession) -> DataStreamReader:
    kafka_data_source: DataStreamReader = spark_session.readStream.format('kafka'). \
        option('kafka.bootstrap.servers', kafka_config.KAFKA_BROKERS).option("subscribe", topic_name)
    return kafka_data_source
