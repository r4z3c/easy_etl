from pyspark.sql import DataFrame


class BaseTransformer:
    def __init__(self):
        pass

    def run(self, extractions):
        result_data_frame = self.transform(extractions)

        if not isinstance(result_data_frame, DataFrame):
            raise TypeError('`transform` method must return a `DataFrame` instance')

        return result_data_frame

    def transform(self, extractions):
        raise NotImplementedError

    def rename(self, data_frame, mapping):
        df = data_frame
        for old, new in mapping.items():
            df = df.withColumnRenamed(old, new)
        return df
