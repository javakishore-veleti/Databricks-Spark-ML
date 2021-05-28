CURR_DIR=$(dirname $0)

docker build --no-cache -t jk-spark-cluster/spark-master -f ${CURR_DIR}/Dockerfile ${CURR_DIR}