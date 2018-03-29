from subprocess import call

from easy_etl.scripts import BaseScript


class HelpScript(BaseScript):
    def run(self):
        print()
        call('eetl --help'.split())
