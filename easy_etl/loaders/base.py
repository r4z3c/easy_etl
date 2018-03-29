class BaseLoader:
    def __init__(self):
        pass

    def run(self, spark_context, spark_session, data_frame):
        raise NotImplementedError
