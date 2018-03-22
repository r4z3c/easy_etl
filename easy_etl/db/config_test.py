import pytest

from easy_etl.db import DbConfig
from easy_etl.util import SparkUtil


def test_db_config_init():
    config = DbConfig('url', 'driver', 'user', 'password')

    assert config.url == 'url'
    assert config.driver == 'driver'
    assert config.user == 'user'
    assert config.password == 'password'


def test_db_config_static_register():
    config = DbConfig.register('name1', 'url', 'driver', 'user', 'password')
    assert isinstance(config, DbConfig)

    with pytest.raises(Exception, message='config `name` already exists'):
        DbConfig.register('name1', 'url', 'driver', 'user', 'password')


def test_db_config_static_get():
    config = DbConfig.register('name2', 'url', 'driver', 'user', 'password')
    assert isinstance(config, DbConfig)

    config2 = DbConfig.get('name2')
    assert isinstance(config2, DbConfig)

    assert config == config2

    with pytest.raises(Exception, message='config `name3` not found'):
        DbConfig.get('name3')


def test_db_config_format_reader():
    def run(_, spark_session):
        reader = spark_session.read
        config = DbConfig.get('name1')
        config.format_reader(reader, 'table')

    SparkUtil.secure_run(run)
