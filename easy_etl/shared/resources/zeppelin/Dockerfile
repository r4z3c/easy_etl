FROM dylanmei/zeppelin

LABEL maintainer="r4z3c <cezar.almeidajr@gmail.com>"

RUN pip install pyspark

RUN pip install pytest==3.4.2 envparse==0.2.0 simple-settings==0.12.1 pprint==0.1 Django==2.0.3

ENV SPARK_JARS $SPARK_HOME/jars

ADD https://search.maven.org/remotecontent?filepath=com/amazonaws/aws-java-sdk/1.7.4/aws-java-sdk-1.7.4.jar $SPARK_JARS/
ADD https://search.maven.org/remotecontent?filepath=org/apache/hadoop/hadoop-aws/2.7.2/hadoop-aws-2.7.2.jar $SPARK_JARS/
ADD https://search.maven.org/remotecontent?filepath=mysql/mysql-connector-java/5.1.45/mysql-connector-java-5.1.45.jar $SPARK_JARS/

ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH

RUN echo "cd $ZEPPELIN_HOME/ && bin/zeppelin.sh" > /usr/local/bin/zeppelin

RUN chmod +x /usr/local/bin/zeppelin

WORKDIR /app

CMD bash -c "pip install -r requirements.txt && eetl --docker && /usr/local/bin/zeppelin"
