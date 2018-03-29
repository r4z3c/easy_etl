from easy_etl.shared.utils import SparkUtil


class BaseJob:
    def __init__(self):
        pass

    def run(self):
        SparkUtil.secure_run(self.job_action)

    def job_action(self, spark_context, spark_session):
        e = self.extraction().run(spark_session)
        t = self.transformer().run(e)
        self.loader().run(spark_context, spark_session, t)

    def extraction(self):
        raise NotImplementedError

    def transformer(self):
        raise NotImplementedError

    def loader(self):
        raise NotImplementedError
