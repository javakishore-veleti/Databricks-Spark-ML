CURR_DIR=$(dirname $0)

# CAREFUL - This folder name changes will impact the Python PySpark code in this Git Repo. Look at global_vars.py in the Spark Definitive Guide examples codebase of this project
mkdir -p /tmp/docker-mount

docker-compose -f $CURR_DIR/docker-compose.yml up &
