#!/bin/bash

export SPARK_HOME=/spark

# Moved below env variable to Dockerfile
# export SPARK_MASTER_HOST=`hostname`

. "/spark/sbin/spark-config.sh"

. "/spark/bin/load-spark-env.sh"

mkdir -p $SPARK_HISTORY_SERVER_LOG

ln -sf /dev/stdout $SPARK_HISTORY_SERVER_LOG/spark-history-server.out

cd /spark && ./sbin/start-history-server.sh >> $SPARK_HISTORY_SERVER_LOG/spark-history-server.out
