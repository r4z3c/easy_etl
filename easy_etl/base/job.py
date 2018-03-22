from easy_etl.util import SparkUtil


class BaseJob:
    def __init__(self):
        pass

    def run(self):
        SparkUtil.secure_run(self.job_action)

    def job_action(self, spark_context, spark_session):
        self.loader().run(
            self.transformer().run(
                self.extractor().run(spark_session)
            )
        )

    def extractor(self):
        raise NotImplementedError

    def transformer(self):
        raise NotImplementedError

    def loader(self):
        raise NotImplementedError
