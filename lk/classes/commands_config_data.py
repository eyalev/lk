from lk.classes.commands_config import CommandsConfig


class CommandsConfigData(object):

    def __init__(self):
        pass

    @property
    def odict(self):

        commands_config_odict = CommandsConfig().odict

        return commands_config_odict
