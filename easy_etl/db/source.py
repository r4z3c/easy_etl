from easy_etl.db import DbConfig


class DbSource:
    def __init__(self, spark_session, config_name, source):
        self.config = DbConfig.get(config_name)
        self.source = source
        self.reader = spark_session.read
        self.config.format_reader(self.reader, self.source)

    def load(self):
        return self.reader.load()
