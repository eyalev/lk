from lk.utils.config_util import ConfigUtil
from pathlib2 import Path


class CommandsConfig(object):

    def __init__(self):

        self.create_config_if_needed()

    def create_config_if_needed(self):

        path_object = self.path_object

        path_object.touch()

    @property
    def path_object(self):

        commands_config_file_path = ConfigUtil().commands_config_file_path

        commands_config_path_object = Path(commands_config_file_path)

        return commands_config_path_object

    @property
    def file_content(self):

        content = self.path_object.read_text()

        return content
