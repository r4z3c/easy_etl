FROM jupyter/pyspark-notebook

LABEL maintainer="r4z3c <cezar.almeidajr@gmail.com>"

USER root

RUN apt update -y
RUN apt install -y iputils-ping sudo mysql-client
RUN echo "jovyan ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers

ENV SPARK_JARS $SPARK_HOME/jars

ADD http://central.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4/aws-java-sdk-1.7.4.jar $SPARK_JARS/
ADD http://central.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.7.2/hadoop-aws-2.7.2.jar $SPARK_JARS/
ADD http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.45/mysql-connector-java-5.1.45.jar $SPARK_JARS/
ADD http://central.maven.org/maven2/org/elasticsearch/elasticsearch-hadoop/6.0.0/elasticsearch-hadoop-6.0.0.jar $SPARK_JARS/

RUN chmod 555 $SPARK_JARS/aws-java-sdk-1.7.4.jar
RUN chmod 555 $SPARK_JARS/hadoop-aws-2.7.2.jar
RUN chmod 555 $SPARK_JARS/mysql-connector-java-5.1.45.jar
RUN chmod 555 $SPARK_JARS/elasticsearch-hadoop-6.0.0.jar

USER jovyan

ENV APP_PATH /app/

WORKDIR $APP_PATH

RUN pip install pytest==3.4.2 envparse==0.2.0 simple-settings==0.12.1 pprint==0.1 Django==2.0.3
RUN pip install ipyparallel==6.1.1

CMD bash -c "pip install -r requirements.txt && eetl --docker && jupyter notebook"
