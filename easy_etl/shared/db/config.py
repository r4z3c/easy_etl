class DbConfig:
    configs = {}

    @staticmethod
    def register_all(configs):
        for name, options in configs.items():
            DbConfig.register(
                name,
                options['url'],
                options['driver'],
                options['user'],
                options['password']
            )

    @staticmethod
    def register(name, url, driver, user, password):
        # if name in DbConfig.configs:
        #     raise(Exception('config `{}` already exists'.format(name)))

        DbConfig.configs[name] = config = DbConfig(url, driver, user, password)
        return config

    @staticmethod
    def get(name):
        if name in DbConfig.configs:
            return DbConfig.configs[name]

        raise(Exception('config `{}` not found'.format(name)))

    def __init__(self, url, driver, user, password):
        self.url = url
        self.driver = driver
        self.user = user
        self.password = password

    def format_reader(self, reader, table_name):
        from pyspark.sql import DataFrameReader

        if not isinstance(reader,  DataFrameReader):
            raise(TypeError('`reader` must be a DataFrameReader'))

        reader.format('jdbc')\
            .option('url', self.url)\
            .option('driver', self.driver)\
            .option('user', self.user)\
            .option('password', self.password)\
            .option('dbtable', table_name)
