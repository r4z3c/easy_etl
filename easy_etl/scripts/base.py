from easy_etl.paths import Paths


class BaseScript:
    def __init__(self, args):
        self.args = args

    def run(self):
        raise NotImplementedError

    @staticmethod
    def print_folders():
        print('\tframework_folder at: {}'.format(Paths.root()))
        print('\tapp_folder at: {}'.format(Paths.app_root()))
