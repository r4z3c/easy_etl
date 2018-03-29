from easy_etl.scripts import BaseScript, HelpScript


class MainScript(BaseScript):
    def run(self):
        (self.args.action if self.args.action else HelpScript)(self.args).run()
