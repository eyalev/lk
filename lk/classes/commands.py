import os

from lk.utils.config_util import ConfigUtil


class Commands(object):

    def __init__(self):
        pass

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
