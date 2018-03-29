from easy_etl.scripts import InitScript
from easy_etl.shared.utils import OsUtil
from easy_etl.paths import Paths


class DockerScript(InitScript):
    def __init__(self, args):
        InitScript.__init__(self,
                            args=args,
                            source=OsUtil.join(Paths.app_root(), 'shared', 'resources', 'spark'),
                            target=Paths.spark_conf_path(),
                            start_message='i| running DockerScript')

    def install(self):
        self.install_hdfs_xml()

    def install_hdfs_xml(self):
        OsUtil.install(source=self.source, target=self.target, files=['hdfs-site.xml'], with_sudo=True)
