FROM jk-spark-cluster/spark-base


COPY master.sh /

ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 8080
ENV SPARK_MASTER_LOG /spark/logs
ENV SPARK_MASTER_HOST spark-master

EXPOSE 8080 7077 6066

CMD ["/bin/bash", "/master.sh"]