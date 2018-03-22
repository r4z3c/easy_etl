from pyspark.sql import DataFrameReader

class DbConfig:
    configs = {}

    # TODO implement register_all method to register multiple configs

    @staticmethod
    def register_all(configs):
        for config in configs:
            DbConfig.register(
                config['name'],
                config['url'],
                config['driver'],
                config['user'],
                config['password']
            )

    @staticmethod
    def register(name, url, driver, user, password):
        if name in DbConfig.configs:
            raise(Exception(f'config `{name}` already exists'))

        DbConfig.configs[name] = config = DbConfig(url, driver, user, password)
        return config

    @staticmethod
    def get(name):
        if name in DbConfig.configs:
            return DbConfig.configs[name]

        raise(Exception(f'config `{name}` not found'))

    def __init__(self, url, driver, user, password):
        self.url = url
        self.driver = driver
        self.user = user
        self.password = password

    def format_reader(self, reader, table_name):
        if not isinstance(reader,  DataFrameReader):
            raise(TypeError(f'`reader` must be a DataFrameReader'))

        reader.format('jdbc')\
            .option('url', self.url)\
            .option('driver', self.driver)\
            .option('user', self.user)\
            .option('password', self.password)\
            .option('dbtable', table_name)
