class SparkUtil:
    @staticmethod
    def secure_run(func, spark_context=None, spark_session=None):
        from pyspark import SparkContext
        from pyspark.sql import SparkSession

        if not spark_context:
            spark_context = SparkContext()

        if not spark_session:
            spark_session = SparkSession(spark_context)

        try:
            func(spark_context, spark_session)
        finally:
            spark_session.stop()

    def __init__(self):
        pass
