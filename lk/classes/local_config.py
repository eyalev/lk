import yaml
from collections import OrderedDict as odict

import click
from pathlib2 import Path

from lk.classes.exceptions import LocalConfigNotFound
from lk.config import app_config
from lk.utils.confirm_util import app_confirm


class LocalConfig(object):

    def __init__(self):

        self.lk_config_dir_string = str(Path.home()) + '/' + '.config/lk'
        self.lk_config_dir_path = Path(self.lk_config_dir_string)

        self.lk_config_file_path_string = self.lk_config_dir_string + '/' + 'lk_config.yaml'
        self.lk_config_file_path = Path(self.lk_config_file_path_string)

    @property
    def not_found(self):

        if not self.lk_config_file_path.exists():
            return True

        else:
            return False

    @property
    def config_dict(self):

        config_string = self.lk_config_file_path.read_text()
        config_dict = yaml.load(config_string)

        return config_dict

    def add_remote_repo(self, remote_repo):

        self.create_config(remote_repo=remote_repo)

    def default_commands_repo(self):

        try:
            return self.config_dict['default_commands_repo']

        except IOError:

            self.create_config()
            return self.config_dict['default_commands_repo']

            # raise LocalConfigNotFound

    def create_config(self, remote_repo=None):

        if not self.lk_config_dir_path.exists():
            Path.mkdir(self.lk_config_dir_path, parents=True, exist_ok=True)

        if self.lk_config_file_path.exists():

            print('# Config file exists at: {config_file_path}'.format(config_file_path=self.lk_config_file_path_string))

            if app_confirm('Do you want to override?'):
                pass
            else:
                click.Abort()

        if remote_repo is None:
            remote_repo_value = app_config.DEFAULT_COMMANDS_REPO
        else:
            remote_repo_value = remote_repo

        config_odict = odict([
            ('default_commands_repo', remote_repo_value)
        ])

        setup_yaml()

        config_yaml_string = yaml.dump(config_odict, default_flow_style=False)

        self.lk_config_file_path.write_text(config_yaml_string.decode('utf-8'))


def setup_yaml():

    """ http://stackoverflow.com/a/8661021 """

    represent_dict_order = lambda self, data:  self.represent_mapping('tag:yaml.org,2002:map', data.items())
    yaml.add_representer(odict, represent_dict_order)

