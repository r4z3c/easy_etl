from easy_etl.db import DbSource


class BaseExtractor:
    @staticmethod
    def load_source(spark_session, config_name, source):
        return DbSource(spark_session, config_name, source).load()

    def __init__(self):
        pass

    def run(self, spark_session):
        result = {}

        for name, options in self.extractions().items():
            result[name] = BaseExtractor.load_source(
                spark_session,
                options['config'],
                options['source']
            )

        return result

    def extractions(self):
        raise NotImplementedError
