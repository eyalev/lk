import click
from lk.classes.commands_config_data import CommandsConfigData
from lk.classes.commands_config_keys import repo_url_key, commands_key
from lk.classes.dir import Dir
from pathlib2 import Path

from lk.classes.file_util import File
from lk.classes.source_code_repo import SourceCodeRepo
from lk.config import app_config
from lk.utils.config_util import ConfigUtil
from lk.utils.path_util import join_paths
from lk.utils.string_util import print_lines, print_util


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
    def relative_path(self):
        return self.file_name

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

    @property
    def user_command_path(self):

        return self.path

    @property
    def user_command_file(self):

        """
        :rtype: lk.classes.file_util.File
        """

        user_command_path = self.user_command_path

        user_command_file = File(user_command_path)

        return user_command_file

    @property
    def user_command_source(self):

        user_command_file = self.user_command_file

        source = user_command_file.content

        return source

    @property
    def repo_command_path(self):

        repos_path = ConfigUtil().local_repos_dir_path

        file_name = self.file_name

        import fnmatch
        import os

        matches = []
        for root, dirnames, filenames in os.walk(repos_path):
            for filename in fnmatch.filter(filenames, file_name):
                matches.append(os.path.join(root, filename))

        if len(matches) > 1:
            print_lines(matches)
            raise ValueError('More than one repo found for file {file}'.format(file=file_name))

        elif len(matches) == 0:
            raise ValueError('No repo found for file {file}'.format(file=file_name))

        elif len(matches) == 1:
            return matches[0]

        else:
            raise NotImplementedError

    @property
    def has_config(self):

        if self.name in self.commands_config_data:
            return True

        else:
            return False

    @property
    def commands_config_data(self):

        commands_config_dict = self.commands_config_dict
        commands_config_data = commands_config_dict[commands_key]

        return commands_config_data

    @property
    def repo_url(self):

        command_config = self.command_config

        return command_config[repo_url_key]

    @property
    def command_config(self):

        commands_data = self.commands_config_data

        if self.has_config:
            command_config = commands_data[self.name]
            return command_config

        else:
            raise NotImplementedError

    @property
    def commands_config_dict(self):

        commands_config = CommandsConfigData().odict

        return commands_config

    @property
    def repo(self):

        """
        :rtype: SourceCodeRepo
        """

        file_name = self.file_name

        repos_path = ConfigUtil().local_repos_dir_path

        import fnmatch
        import os

        matches = []
        for root, dirnames, filenames in os.walk(repos_path):
            for filename in fnmatch.filter(filenames, file_name):
                matches.append(os.path.join(root, filename))

        if len(matches) > 1:
            print_lines(matches)
            raise ValueError('More than one repo found for file {file}'.format(file=file_name))

        elif len(matches) == 0:
            raise ValueError('No repo found for file {file}'.format(file=file_name))

        elif len(matches) == 1:

            match = matches[0]
            split_list = match.split('/')
            repos_index = split_list.index(app_config.local_repos_dir)
            new_list = split_list[repos_index + 1:]
            service = new_list[0]
            user = new_list[1]
            repo_name = new_list[2]

            repo = SourceCodeRepo(
                service=service,
                user=user,
                repo_name=repo_name
            )
            return repo

        else:
            raise NotImplementedError

    @property
    def repo_command_file(self):

        repo_command_path = self.repo_command_path

        repo_command_file = File(repo_command_path)

        return repo_command_file

    @property
    def local_repo_command_source(self):

        repo_command_file = self.repo_command_file

        source = repo_command_file.content

        return source

    @property
    def local_path(self):

        path = self.user_command_path

        return path

    @property
    def local_repo_command_path(self):
        return self.repo_command_path

    @property
    def local_repo_path(self):

        repo_command_path = self.repo_command_path
        splits = repo_command_path.split('/')
        local_repo_path = '/'.join(splits[0:-3])
        return local_repo_path

        # return 'temp'

    @property
    def remote_repo_command_source(self):

        repo = self.repo

        if repo:
            source = repo.remote_file_source(self.file_name)
            return source

        else:
            raise ValueError('Remote file not found.')

    def remove_from_user_commands_dir(self):

        file = self.user_command_file

        if file.exists():
            print_util('File path: {path}'.format(path=file.path))
            if click.confirm('Are you sure you want to this file?', default=False):
                file.delete()
            else:
                print_util('Deletion aborted.')

        else:
            print_util('File {path} does not exists.'.format(path=file.path))

    def remove_local_repo(self):

        local_repo_path = self.local_repo_path

        print_util(local_repo_path, name='Local repo path')

        if click.confirm('Do you want to remove this directory?', default=False):

            Dir(local_repo_path).remove()

