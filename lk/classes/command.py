from pathlib2 import Path

from lk.utils.config_util import ConfigUtil


class Command(object):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def name_underscore(self):
        name_underscore = self.name.replace('-', '_')
        return name_underscore

    @property
    def source_code(self):

        user_commands_dir_path = Path(ConfigUtil().user_commands_directory)
        command_name = '{command_name_underscore}_command.py'.format(
            command_name_underscore=self.name_underscore
        )
        command_path = user_commands_dir_path.joinpath(command_name)

        if command_path.exists():
            source = command_path.read_text()
            output = '\n' + source + '\n'
            return output

        else:
            return 'Command source was not found.'
