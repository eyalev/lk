
import os
import sys
import argparse

from lk.classes.commands_config import CommandsConfig
from lk.utils.path_util import join_paths

lk_repo_arg = '--lk-repo'
repo = None


def handle_repo_argument():

    global repo

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(lk_repo_arg, type=str)
    arguments, unknown = parser.parse_known_args()
    repo = arguments.lk_repo
    remove_repo_argument_from_argv()


def remove_repo_argument_from_argv():

    # Handle lk repo option with '='
    if lk_repo_arg in sys.argv:
        index = sys.argv.index(lk_repo_arg)
        sys.argv.pop(index+1)
        sys.argv.pop(index)

    # Handle lk repo option with '='
    sys.argv[:] = [x for x in sys.argv if not x.startswith(lk_repo_arg + '=')]


handle_repo_argument()

from distutils.file_util import copy_file

import click
from click import MultiCommand
from pathlib2 import Path

from lk.classes import helpers
from lk.classes.commands import Commands
from lk.classes.lk_config import LKConfig
from lk.classes.local_default_repo import LocalDefaultRepo
from lk.classes.source_code_repo import SourceCodeRepo
from lk.utils.config_util import ConfigUtil
from lk.utils.shell_util import run


class MyCLI(MultiCommand):

    def __init__(self, **kwargs):

        MultiCommand.__init__(self, **kwargs)

        self.user_commands_dir = ConfigUtil().user_commands_directory
        self.core_commands_dir = ConfigUtil().core_commands_directory

        self.commands = self._init_commands()
        # self.commands = self._init_commands_new()

        self._repo = None

    def get_first_level_dirs(self, parent_dir):

        from glob import glob
        dirs = glob("{parent_dir}/*/".format(parent_dir=parent_dir))

        return dirs

    def _init_commands(self):

        commands = {}

        first_level_dirs = self.get_first_level_dirs(self.core_commands_dir)

        commands_dirs = [self.user_commands_dir, self.core_commands_dir] + first_level_dirs

        self.create_dir_if_needed(directory=self.user_commands_dir)

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

    def _init_commands_new(self):

        command_list = []

        commands_dirs = [self.user_commands_dir, self.core_commands_dir]

        for commands_dir in commands_dirs:

            for file_name in os.listdir(commands_dir):
                if file_name.endswith('.py') and file_name != '__init__.py':
                    command_list.append(file_name[:-3])
            # command_list.sort()

        return command_list

    def list_commands(self, ctx):
        return sorted(self.commands)

    def create_dir_if_needed(self, directory):

        Path(directory).mkdir(parents=True, exist_ok=True)

    def get_command(self, ctx, name):

        command_name = name

        if self.got_repo_argument():

            if self.command_exists(command_name=command_name):
                command = self.get_command_from_source(command_name=command_name)
                return command

            self.clone_repo()

            if self.command_exists(command_name=command_name):
                self.copy_command_to_user_commands_dir(command_name=command_name)
                command = self.get_command_from_source(command_name=command_name)
                return command

        command = self.commands.get(name)

        if command:
            return command

        command_found = False

        print('''Couldn't find user command: "{name}"'''.format(name=name))
        print('Checking commands repository.')

        command_file_name = '{command_name}_command.py'.format(
            command_name=name.replace('-', '_')
        )

        local_default_repo = helpers.get_local_default_repo()

        local_default_repo_command_path_object = Path(local_default_repo.commands_dir_string_path + '/' + command_file_name)

        if not command_found:

            if local_default_repo_command_path_object.exists():

                print('Found command in commands repository (local cache).')
                print('Adding command to local commands.')

                copy_file(str(local_default_repo_command_path_object), self.user_commands_dir)

                command_found = True

            else:

                if self.local_commands_repo_not_exists():

                    self.clone_commands_repo()

                    if local_default_repo_command_path_object.exists():

                        print('Found command in commands repository (remote).')
                        print('Adding command to local commands.')

                        local_default_repo_command_path = str(local_default_repo_command_path_object)

                        copy_file(local_default_repo_command_path, self.user_commands_dir)

                        CommandsConfig().add_command(
                            command_name=command_name,
                            repo_url=self.remote_repo.url,
                            file_name=command_file_name,
                            local_path=self.get_local_command_path(command_name),
                            local_repo_command_path=local_default_repo_command_path,
                            local_repo_path=self.local_default_repo_string_path
                        )

                        command_found = True

                    else:
                        print('Command not found in repo local copy.')

        if not command_found:
            print('Command not found in repository.')

        if command_found:

            command_path = self.user_commands_dir + '/' + command_file_name

            with open(str(command_path)) as _file:
                args = {}
                code = compile(_file.read(), command_file_name, 'exec')
                eval(code, args, args)

            command = args['cli']

            return command

        elif LKConfig().add_command_prompt_enabled:

            if click.confirm('Would you like to add this command?', default=True):
                run('lk add-command {command}'.format(command=name))

                if click.confirm('Would you like to edit this command?', default=True):
                    run('lk edit-command {command_name}'.format(command_name=name))

                empty_command = Commands().get_empty_command(click_format=True)

                return empty_command

        else:
            return None

    def get_local_command_path(self, command_name):

        commands_dir = self.user_commands_dir

        file_name = self.get_command_file_name(command_name)

        local_command_path = join_paths(commands_dir, file_name)

        return local_command_path

    def get_command_from_source(self, command_name):

        command_file_name = self.get_command_file_name(command_name=command_name)
        # command_file_name = self.get_command_file_name_new(command_name=command_name)

        command_path = self.user_commands_dir + '/' + command_file_name

        with open(str(command_path)) as _file:
            args = {}
            code = compile(_file.read(), command_file_name, 'exec')
            eval(code, args, args)

        command = args['cli']

        return command

    def copy_command_to_user_commands_dir(self, command_name):

        command_repo_path = self.get_command_repo_path(command_name=command_name)

        print('Found command in commands repository (remote).')
        print('Adding command to local commands.')

        copy_file(command_repo_path, self.user_commands_dir)

    def get_command_repo_path(self, command_name):

        command_path_object = self.get_command_path_object(command_name)

        return str(command_path_object)

    def command_exists(self, command_name):

        command_path_object = self.get_command_path_object(command_name=command_name)

        return command_path_object.exists()

    def get_command_file_name(self, command_name):

        command_file_name = '{command_name}_command.py'.format(
            command_name=command_name.replace('-', '_')
        )

        return command_file_name

    def get_command_file_name_new(self, command_name):

        command_file_name = '{command_name}.py'.format(
            command_name=command_name.replace('-', '_')
        )

        return command_file_name

    def get_command_path_object(self, command_name):

        command_file_name = self.get_command_file_name(command_name=command_name)

        repo_object = self.get_repo_object()

        local_repo_command_path = Path(repo_object.commands_dir_string_path + '/' + command_file_name)

        return local_repo_command_path

    def got_repo_argument(self):

        repo = self.get_repo_argument()

        if repo:
            return True
        else:
            return False

    # def remove_repo_argument_from_argv(self):
    #
    #     import sys
    #     sys.argv[:] = [x for x in sys.argv if not x.startswith('--repo')]
    #     # import ipdb; ipdb.set_trace()
    #     # a = ''

    def get_repo_object(self):

        """
        :rtype: SourceCodeRepo
        """

        repo_url = self.get_repo_argument()

        repo_object = SourceCodeRepo(url=repo_url)

        return repo_object

    def clone_repo(self):

        repo_object = self.get_repo_object()

        repo_object.clone()

    def get_repo_argument(self):

        return repo

    #
    #     if self._repo:
    #         return self._repo
    #
    #     import argparse
    #     parser = argparse.ArgumentParser()
    #     parser.add_argument('--repo', type=str)
    #     arguments, unknown = parser.parse_known_args()
    #     self._repo = arguments.repo
    #     self.remove_repo_argument_from_argv()
    #
    #     return self._repo

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

    # def clone_repo_temp(self, repo):
    #
    #     remote_repo = helpers.get_remote_default_repo()
    #
    #     remote_repo.clone()

    @property
    def remote_repo(self):

        remote_repo = helpers.get_remote_default_repo()

        return remote_repo

    def clone_commands_repo(self):

        self.remote_repo.clone()


# env_option = click.Option(param_decls=['-e', '--env'], default='prod', help='Environment config')

# version_option = click.Option(param_decls=['--version'], is_flag=True, default=False)
# params = [version_option]

# cli = MyCLI(params=params)
# @click.option('--debug/--no-debug', default=False)
# @click.option('--version', is_flag=True, default=False)

# version = click.version_option

# cli = MyCLI()
# cli = MyCLI(params=params)


lk_version = '0.01'

temp = click.help_option


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(lk_version)
    ctx.exit()


@click.command(cls=MyCLI)
@click.option('--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def cli():

    pass


if __name__ == '__main__':
    cli()
