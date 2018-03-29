from pyspark.sql.functions import *

from easy_etl import DbConfig, BaseJob, BaseExtraction, BaseTransformer, S3Loader

from app.util import DbConfigUtil


DbConfigUtil.register_all()


class {job}Job(BaseJob):
    def extraction(self):
        return {job}Extraction()

    def transformer(self):
        return {job}Transformer()

    def loader(self):
        return S3Loader('bucket', 'path')


class {job}Extraction(BaseExtraction):
    def extractions(self):
        return ({
            'states': {'config': 'mysql', 'source': '(select * from states) states'},
            'cities': {'config': 'mysql', 'source': '(select * from cities) cities'}
        })


class {job}Transformer(BaseTransformer):
    def transform(self, extractions):
        states = self.rename(extractions['states'], {'id': 'state_id', 'name': 'state_name'})
        cities = self.rename(extractions['cities'], {'id': 'city_id', 'name': 'city_name'})

        return (
            states.join(cities, states.state_id == cities.state_id, 'inner')
                  .drop(cities.state_id)
                  .select('state_id', 'state_name', 'city_id', 'city_name')
        )
