from easy_etl.shared.db import DbSource


class BaseExtraction:
    @staticmethod
    def load_source(spark_session, config_name, source):
        return DbSource(spark_session, config_name, source).load()

    def __init__(self):
        pass

    def run(self, spark_session):
        result = {}

        for config, options in self.definitions().items():
            for extraction, source in self.definitions()[config].items():
                result[extraction] = BaseExtraction.load_source(spark_session, config, source)

        return result

    def definitions(self):
        # {
        #     'my_mysql_config': {
        #         'my_table': '(select * from my_table) my_table',
        #         'my_other_table': '(select * from my_other_table) my_other_table'
        #     }
        # }
        raise NotImplementedError
