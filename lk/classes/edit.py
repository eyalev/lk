from lk.utils.config_util import ConfigUtil
from lk.utils.shell_util import run, execute
from lk.utils.string_util import print_with_space


class Edit(object):

    def __init__(self):
        pass

    def edit_command(self, command_name):

        commands_dir = ConfigUtil().user_commands_directory_in_lk_dir
        command_file_name = '{command_name}_command.py'.format(command_name=command_name.replace('-', '_'))
        command_path_object = ConfigUtil().join_paths(commands_dir, command_file_name)
        command_path = str(command_path_object)
        print_with_space('Command path:\n\n' + command_path)
        execute('charm {command_path}'.format(command_path=command_path))
