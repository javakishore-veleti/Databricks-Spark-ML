CURR_DIR=$(dirname $0)

export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_291.jdk/Contents/Home
export JRE_HOME=${JAVA_HOME}/jre/
export SPARK_HOME=/usr/local/Cellar/apache-spark/3.1.1/libexec
export PATH=${SPARK_HOME}/3.0.1/bin:$PATH
export PYSPARK_PYTHON=${CURR_DIR}/Databricks-Spark-venv/bin/python
