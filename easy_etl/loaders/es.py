from easy_etl.loaders import BaseLoader


class EsLoader(BaseLoader):
    def __init__(self, options={}, _format='org.elasticsearch.spark.sql'):
        default_options = {
            'es.nodes': 'elasticsearch:9200',
            'es.nodes.wan.only': 'false'
        }

        self.format = _format
        self.options = default_options.copy()
        self.options.update(options)

    def run(self, spark_context, spark_session, data_frame):
        writer = data_frame.write.format(self.format)
        for key, value in self.options.items():
            writer = writer.option(key, value)
        writer.save()

    def resource(self):
        return '{}/{}'.format(self.index, self.type)
