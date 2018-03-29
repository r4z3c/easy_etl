import datetime

from easy_etl.loaders import BaseLoader


class S3Loader(BaseLoader):
    def __init__(self, bucket, path, _format='json'):
        self.bucket = bucket
        self.path = path
        self.format = _format

    def run(self, _, __, data_frame):
        data_frame.write\
            .format(self.format)\
            .save('s3a://{}/{}/{}'.format(self.bucket, self.path, datetime.datetime.now()))
