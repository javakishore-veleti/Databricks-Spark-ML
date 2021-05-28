CURR_DIR=$(dirname $0)

docker build --no-cache -t spark-docker-master -f ${CURR_DIR}/Dockerfile ${CURR_DIR}