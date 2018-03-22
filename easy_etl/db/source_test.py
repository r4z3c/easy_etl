import pytest

from easy_etl.db import DbSource
from easy_etl.db import DbConfig
from easy_etl.util import SparkUtil


def test_db_table_init():
    config_name = 'db_table'
    DbConfig.register(config_name, 'url', 'driver', 'user', 'password')

    def run(_, spark_session):
        DbSource(spark_session, config_name, 'table')

    SparkUtil.secure_run(run)
