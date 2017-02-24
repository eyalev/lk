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
    def exists(self):
        path_object = self.path_object
        if path_object.exists():
            return True
        else:
            return False

    @property
    def path_object(self):

        user_commands_dir_path = Path(ConfigUtil().user_commands_directory)

        command_path = user_commands_dir_path.joinpath(self.file_name)

        return command_path

    @property
    def path(self):
        return str(self.path_object)

    @property
    def file_name(self):
        command_file_name = '{command_name_underscore}_command.py'.format(
            command_name_underscore=self.name_underscore
        )
        return command_file_name

    @property
    def source_code(self):

        if self.path_object.exists():
            source = self.path_object.read_text()
            output = '\n' + source + '\n'
            return output

        else:
            return 'Command source was not found.'
