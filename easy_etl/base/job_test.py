import pytest

from easy_etl.base import BaseJob


def test_base_job_abstract_methods():
    class InvalidTestJob(BaseJob):
        pass

    class ValidTestJob(BaseJob):
        def job_action(self, spark_context, spark_session):
            pass

    with pytest.raises(NotImplementedError):
        InvalidTestJob().run()

    ValidTestJob().run()
