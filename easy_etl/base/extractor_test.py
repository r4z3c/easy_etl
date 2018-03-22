import pytest

from easy_etl.base import BaseExtractor
from easy_etl.db import DbConfig
from easy_etl.util import SparkUtil


def test_base_extractor_init():
    BaseExtractor()


def test_base_extractor_run():
    config_name = 'base_extractor'
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

        extractions = TestExtractor().run(spark_session)

        assert extractions['cities'].columns == ['id', 'state_id', 'name']

    SparkUtil.secure_run(run)
