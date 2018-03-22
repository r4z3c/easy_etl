from pyspark.sql.functions import *

from easy_etl.db import DbConfig
from easy_etl.base import BaseExtractor, BaseTransformer, BaseJob
from easy_etl.loader import S3Loader


def test_full():
    # 1: register DB connection

    config_name = 'test_full'

    DbConfig.register(
        config_name,
        'jdbc:mysql://mysql:3306/easy_etl',
        'com.mysql.jdbc.Driver',
        'root',
        'mysql'
    )

    # 2: create an Extraction

    class GeoreferenceExtractor(BaseExtractor):
        def extractions(self):
            return ({
                'states': {'config': config_name, 'source': '(select * from states) states'},
                'cities': {'config': config_name, 'source': '(select * from cities) cities'}
            })

    # 3: create an Transformer

    class GeoreferenceTransformer(BaseTransformer):
        def transform(self, extractions):
            states = self.rename(extractions['states'], {'id': 'state_id', 'name': 'state_name'})
            cities = self.rename(extractions['cities'], {'id': 'city_id', 'name': 'city_name'})

            return (
                states.join(cities, states.state_id == cities.state_id, 'inner')
                    .drop(cities.state_id)
                    .select('state_id', 'state_name', 'city_id', 'city_name')
            )

    # 4: create an Loader

    class TestLoader(S3Loader):
        def run(self, data_frame):
            assert data_frame.columns == ['state_id', 'state_name', 'city_id', 'city_name']
            # super().run(data_frame) # uncomment to upload files

    # 5: wrap all in a job

    class GeoreferenceJob(BaseJob):
        def extractor(self):
            return GeoreferenceExtractor()

        def transformer(self):
            return GeoreferenceTransformer()

        def loader(self):
            return TestLoader('bucket', 'path')

    # 6: run

    GeoreferenceJob().run()
