CURR_DIR=$(dirname $0)

docker build --no-cache -t jk-spark-cluster/spark-base -f ${CURR_DIR}/Dockerfile ${CURR_DIR}