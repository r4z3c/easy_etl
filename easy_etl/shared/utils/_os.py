import os
from subprocess import call


class OsUtil:
    def __init__(self):
        pass

    @staticmethod
    def install(source, target, files, file_suffix=None, with_sudo=False):
        print('i| installing `{}` from `{}` to `{}`'.format(files, source, target))
        for _file in files:
            source_file = OsUtil.join(source, _file)
            target_file = OsUtil.join(target, _file)

            if file_suffix:
                target_file = '{}{}'.format(target_file, file_suffix)

            if os.path.isfile(target_file):
                print('i| `{}` already exists, skipping'.format(target_file))
            else:
                OsUtil.call('cp {} {}'.format(source_file, target_file), with_sudo=with_sudo)

    @staticmethod
    def chmod(mod, folder, files, with_sudo=False):
        print('i| changing mod of `{}` at `{}` to `{}`'.format(files, folder, mod))
        for _file in files:
            target_file = OsUtil.join(folder, _file)

            OsUtil.call('chmod {} {}'.format(mod, target_file), with_sudo=with_sudo)

    @staticmethod
    def mkdir(args, with_sudo=False):
        OsUtil.call('mkdir {}'.format(args), with_sudo=with_sudo)

    @staticmethod
    def mv(args, with_sudo=False):
        OsUtil.call('mv {}'.format(args), with_sudo=with_sudo)

    @staticmethod
    def call(args, with_sudo=False):
        # print('i| calling `{}` with_sudo? `{}`'.format(args, with_sudo))
        sudo = 'sudo ' if with_sudo else ''
        call('{}{}'.format(sudo, args).split())

    @staticmethod
    def join(*args):
        return '/'.join(str(arg) for arg in args)