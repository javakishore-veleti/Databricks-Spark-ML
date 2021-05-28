FROM spark-docker-base


COPY worker.sh /

ENV SPARK_WORKER_WEBUI_PORT 8081
ENV SPARK_WORKER_LOG /spark/logs
ENV SPARK_MASTER "spark://spark-docker-master:7077"
ENV SPARK_WORKER_IP "127.0.0.1"

EXPOSE 8081

CMD ["/bin/bash", "/worker.sh"]