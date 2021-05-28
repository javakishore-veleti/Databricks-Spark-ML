CURR_DIR=$(dirname $0)

docker build --no-cache -t jk-spark-cluster/spark-master -f ${CURR_DIR}/Dockerfile ${CURR_DIR}

docker build --no-cache -t jk-spark-cluster/spark-history-server -f ${CURR_DIR}/Dockerfile-history-server ${CURR_DIR}