CURR_DIR=$(dirname $0)

cd ${CURR_DIR}/spark-docker-base
./base-docker-build.sh

cd ..
cd ${CURR_DIR}/spark-docker-master
./master-docker-build.sh

cd ..
cd ${CURR_DIR}/spark-docker-worker
./worker-docker-build.sh

cd ..
cd ${CURR_DIR}/spark-docker-submit
./submit-docker-build.sh
