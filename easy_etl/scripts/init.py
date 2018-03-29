import os
from easy_etl.paths import Paths
from easy_etl.scripts import BaseScript
from easy_etl.shared.utils import OsUtil


class InitScript(BaseScript):
    def __init__(self, args, source=None, target=None, start_message=None):
        BaseScript.__init__(self, args)
        self.source = source if source else Paths.resources_path()
        self.target = target if target else Paths.app_root()
        self.start_message = start_message if start_message else \
            'i| initializing EasyETL framework'

    def run(self):
        print(self.start_message)
        BaseScript.print_folders()
        self.install()

    def install(self):
        OsUtil.mkdir('-p {}/{}'.format(self.target, 'etls'))
        self.install_requirements_file()
        # self.install_dockerfile()
        self.install_docker_compose()
        self.install_hdfs_xml()

    def install_requirements_file(self):
        print('i| installing requirements')

        with open(OsUtil.join(self.target, 'requirements.txt'), 'a') as _file:
            _file.write("\neasy_etl==0.1.0\n")

    def install_dockerfile(self):
        target = OsUtil.join(self.target, 'shared', 'resources', 'jupyter')

        OsUtil.mkdir('-p {}'.format(target))
        OsUtil.install(source=OsUtil.join(self.source, 'jupyter'),
                       target=target,
                       files=['Dockerfile'],
                       file_suffix='.example')

    def install_docker_compose(self):
        OsUtil.install(source=OsUtil.join(self.source, 'jupyter'),
                       target=self.target,
                       files=['docker-compose.yml'],
                       file_suffix='.example')

    def install_hdfs_xml(self):
        target = OsUtil.join(self.target, 'shared', 'resources', 'spark')

        OsUtil.mkdir('-p {}'.format(target))
        OsUtil.install(source=OsUtil.join(self.source, 'spark'),
                       target=target,
                       files=['hdfs-site.xml'],
                       file_suffix='.example')
