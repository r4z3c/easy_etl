import pytest

from easy_etl.base import BaseExtractor, BaseTransformer
from easy_etl.db import DbConfig
from easy_etl.util import SparkUtil


def test_base_transformer_init():
    BaseTransformer()


def test_base_transformer_run():
    config_name = 'base_transformer'
    DbConfig.register(
        config_name,
        'jdbc:mysql://mysql:3306/easy_etl',
        'com.mysql.jdbc.Driver',
        'root',
        'mysql'
    )

    def run(_, spark_session):
        class TestExtractor(BaseExtractor):
            def extractions(self):
                return ({
                    'cities': {'config': config_name, 'source': '(select * from cities) cities'}
                })

        class TestTransformer(BaseTransformer):
            def transform(self, extractions):
                return extractions['cities']

        data = TestTransformer().run(
            TestExtractor().run(spark_session)
        )

        assert data.columns == ['id', 'state_id', 'name']

    SparkUtil.secure_run(run)
