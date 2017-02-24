import os

from lk.classes.command import Command
from lk.utils.config_util import ConfigUtil
from lk.utils.shell_util import run_and_confirm


class Commands(object):

    def __init__(self):
        pass

    def get_empty_command(self, click_format):

        if click_format:
            command = self.get_click_command('empty-command')
        else:
            raise NotImplementedError

        return command

    def get_click_command(self, command_name):

        command = Command(command_name)

        with open(str(command.path)) as _file:
            args = {}
            code = compile(_file.read(), command.file_name, 'exec')
            eval(code, args, args)

        command = args['cli']

        return command

    def remove_command(self, command_name):

        command_path = Command(command_name).path

        run_and_confirm('rm {command_path}'.format(command_path=command_path))

    def get_commands(self):

        commands = []

        commands_dirs = [ConfigUtil().user_commands_directory, ConfigUtil().core_commands_directory]

        for command_dir in commands_dirs:

            for file_name in os.listdir(command_dir):

                if file_name.endswith('.py') and file_name != '__init__.py':

                    file_path = os.path.join(command_dir, file_name)

                    with open(file_path) as _file:
                        code = compile(_file.read(), file_name, 'exec')
                        eval(code, args, args)

                    command = args['cli']
                    commands[command.name] = command

        return []
