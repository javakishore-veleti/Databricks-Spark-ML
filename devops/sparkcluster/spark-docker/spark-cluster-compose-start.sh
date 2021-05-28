CURR_DIR=$(dirname $0)

cd ${CURR_DIR}/spark-cluster-docker-compose
./spark-cluster-start.sh
cd ..