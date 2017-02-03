# import sys
# import os
# sys.path.insert(1, os.path.join(sys.path[0], '..'))
# sys.path.insert(1, '/home/eyalev/workspace/github/lk3')

import os
from distutils.file_util import copy_file

from click import MultiCommand
from pathlib2 import Path

from lk.classes import helpers
from lk.classes.local_default_repo import LocalDefaultRepo
# from lk.config.app_config import commands_directory
from lk.utils.config_util import ConfigUtil


class MyCLI(MultiCommand):

    def __init__(self, **kwargs):

        MultiCommand.__init__(self, **kwargs)

        self.user_commands_dir = ConfigUtil().user_commands_directory
        self.core_commands_dir = ConfigUtil().core_commands_directory

        self.commands = self._init_commands()

    def _init_commands(self):

        commands = {}

        commands_dirs = [self.user_commands_dir, self.core_commands_dir]

        for command_dir in commands_dirs:

            for file_name in os.listdir(command_dir):

                if file_name.endswith('.py') and file_name != '__init__.py':

                    args = {}
                    file_path = os.path.join(command_dir, file_name)

                    with open(file_path) as _file:
                        code = compile(_file.read(), file_name, 'exec')
                        eval(code, args, args)

                    command = args['cli']
                    commands[command.name] = command

        return commands

    def list_commands(self, ctx):
        return sorted(self.commands)

    def get_command(self, ctx, name):

        command = self.commands.get(name)

        if command:
            return command

        command_found = False

        print('''Couldn't find local command: "{name}"'''.format(name=name))
        print('Checking commands repository.')

        command_file_name = '{command_name}_command.py'.format(
            command_name=name.replace('-', '_')
        )

        local_default_repo = helpers.get_local_default_repo()

        local_repo_command_path = Path(local_default_repo.commands_dir_string_path + '/' + command_file_name)

        if local_repo_command_path.exists():

            print('Found command in commands repository (local cache).')
            print('Adding command to local commands.')

            copy_file(str(local_repo_command_path), self.user_commands_dir)

            command_found = True

        else:

            if self.local_commands_repo_not_exists():

                self.clone_commands_repo()

                if local_repo_command_path.exists():

                    print('Found command in commands repository (remote).')
                    print('Adding command to local commands.')

                    copy_file(str(local_repo_command_path), self.user_commands_dir)

                    command_found = True

                else:
                    print('Command not found in repo local copy.')

            # if self.local_commands_repo_not_in_sync():
            #
            #     self.sync_local_commands_repo()
            #
            #     if self.command_found_in_local_repo():
            #
            #         self.copy_command_to_commands_master_directory()
            #
            #         command_found = True

        if command_found:

            command_path = self.user_commands_dir + '/' + command_file_name

            with open(str(command_path)) as _file:
                args = {}
                code = compile(_file.read(), command_file_name, 'exec')
                eval(code, args, args)

            command = args['cli']

            return command

        else:
            return None

    @property
    def local_default_repo_string_path(self):
        return LocalDefaultRepo().string_path

    def local_commands_repo_not_exists(self):

        # if not Path(app_config.organization_repos_dir).exists():
        # local_default_repo_dir_path = Util().local_default_repo_dir_path()

        if not Path(self.local_default_repo_string_path).exists():
            return True

        else:
            return False

    def clone_commands_repo(self):

        remote_default_repo = helpers.get_remote_default_repo()

        remote_default_repo.clone()

cli = MyCLI()


if __name__ == '__main__':
    cli()
