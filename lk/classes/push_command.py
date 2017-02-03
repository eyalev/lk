import os
from distutils.file_util import copy_file

import click
from pathlib2 import Path

from lk.classes import helpers
from lk.classes.helpers import get_local_config
from lk.classes.local_config import LocalConfig
from lk.classes.source_code_repo import SourceCodeRepo
from lk.config import app_config
from lk.utils.shell_util import run_and_confirm, run_and_return_output, run_and_print
from lk.utils.string_util import multi_command_template


class PushCommand(object):

    def __init__(self, command_name):

        self._command_name = command_name

    def push(self, force_push):

        print('Command for push: {command_name}'.format(command_name=self.command_name))

        self.init_local_repo()

        if self.command_file_destination_path.exists():
            print('File: {file_path} already exists.'.format(file_path=self.command_file_destination_path_string))
        else:
            # import pdb; pdb.set_trace()
            copy_file(
                os.path.join(app_config.lk_path, self.command_file_string_path),
                os.path.join(app_config.lk_path, self.local_repo_commands_dir_string_path)
            )

        if self.changes_exist():
            self.show_git_status()
            self.commit_changes()
            self.push_changes()
        elif force_push:
            self.push_changes()
        else:
            print('No changes in commands repo.')

    @property
    def command_file_string_path(self):

        command_file_string_path = 'commands/{command_name}_command.py'.format(
            command_name=self.command_path_name
        )

        return command_file_string_path

    @property
    def command_file_destination_path_string(self):

        command_file_destination_path_string = '{local_commands_dir}/{command_name}_command.py'.format(
            local_commands_dir=self.local_repo_commands_dir_string_path,
            command_name=self.command_path_name
        )

        return command_file_destination_path_string

    @property
    def command_file_destination_path(self):

        command_file_destination_path = Path(self.command_file_destination_path_string)

        return command_file_destination_path

    def init_local_repo(self):

        local_config = get_local_config()

        if local_config.not_found:
            remote_repo_url = self.get_remote_repo_url_from_user()
            local_config.add_remote_repo(remote_repo_url)

        if self.local_repo_exists:
            print('Repository {commands_repo_name} already exists.'.format(commands_repo_name=self.commands_repo_name))
        else:
            self.clone_lk_repo()

        if not self.local_repo_commands_dir_path.exists():
            self.local_repo_commands_dir_path.mkdir()

    def get_remote_repo_url_from_user(self):

        print("""
# Configuring commands repository
# Create one if needed. Example: https://github.com/your-user-name/lk-commands
""")

        remote_repo = click.prompt('# Enter repository URL')

        return remote_repo

    @property
    def local_repo_exists(self):

        commands_repo_local_path = Path(self.local_repo_string_path)

        return commands_repo_local_path.is_dir()

    @property
    def command_name(self):

        return self._command_name

    @property
    def command_path_name(self):

        command_path_name = self._command_name.replace('-', '_')

        return command_path_name

    @property
    def local_repo_commands_dir_string_path(self):

        local_commands_dir_path_string = self.local_repo_string_path + '/commands'

        return local_commands_dir_path_string

    @property
    def local_repo_commands_dir_path(self):

        return Path(self.local_repo_commands_dir_string_path)

    @property
    def remote_commands_repo(self):

        commands_repo = LocalConfig().default_commands_repo()

        return commands_repo

    @property
    def local_repo_string_path(self):

        local_default_repo = helpers.get_local_default_repo()

        return local_default_repo.string_path

    def commands_repo_name(self):

        commands_repo_name = self.remote_commands_repo.split('/')[4]

        return commands_repo_name

    def push_changes(self):

        commands_template = multi_command_template("""
cd {commands_repo_string_path}
git push
""")

        commands = commands_template.format(
            commands_repo_string_path=self.local_repo_string_path,
        )

        run_and_confirm(commands)

    def show_git_status(self):

        commands_template = multi_command_template("""
cd {commands_repo_string_path}
git status
""")

        commands = commands_template.format(
            commands_repo_string_path=self.local_repo_string_path,
        )

        run_and_print(commands)

    def changes_exist(self):

        commands_template = multi_command_template("""
cd {commands_repo_string_path}
git status --porcelain
""")

        commands = commands_template.format(
            commands_repo_string_path=self.local_repo_string_path,
        )

        output = run_and_return_output(commands)

        if output:
            return True
        else:
            return False

    def commit_changes(self):

        print('# Committing changes')

        commands_template = multi_command_template("""
cd {commands_repo_string_path}
git add .
git commit -am "Adding command '{command_name}'"
""")

        commands = commands_template.format(
            commands_repo_string_path=self.local_repo_string_path,
            command_name=self.command_name
        )

        run_and_confirm(commands)

    def clone_lk_repo(self):

        print('# Cloning lk-repo')

        # git@github.com:lk-commands/default.git

        clone_command = SourceCodeRepo(self.remote_commands_repo).clone_command

        # command = 'git clone git@bitbucket.org:breezometer/lk-commands.git {local_commands_dir_path}'.format(
        command = '{clone_command} {local_repo_path}'.format(
            clone_command=clone_command,
            local_repo_path=self.local_repo_string_path
        )

        run_and_confirm(command)
