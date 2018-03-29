import os
from easy_etl.shared.utils import OsUtil


class Paths:
    def __init__(self):
        pass

    @staticmethod
    def root():
        return OsUtil.join(os.path.dirname(__file__))

    @staticmethod
    def app_root():
        return os.getcwd()

    @staticmethod
    def spark_path():
        return os.environ['SPARK_HOME']

    @staticmethod
    def spark_conf_path():
        return OsUtil.join(Paths.spark_path(), 'conf')

    @staticmethod
    def resources_path():
        return OsUtil.join(Paths.root(), 'shared', 'resources')
