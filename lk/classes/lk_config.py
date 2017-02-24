from collections import OrderedDict as odict

import click

from lk.classes import yaml
from lk.classes.local_config import setup_yaml
from lk.classes.python_util import P
from lk.config import app_config
from lk.utils.config_util import ConfigUtil
from pathlib2 import Path


# lk config keys
from lk.utils.confirm_util import app_confirm

default_push_repo = 'default_push_repo'
default_pull_repo = 'default_commands_repo'
create_command_prompt = 'create_command_prompt'


class LKConfig(object):

    def __init__(self):

        self.init_config_if_needed()

    def init_config_if_needed(self):

        if not self.config_exists:
            self.create_config()

    @property
    def config_exists(self):

        if self.path_object.exists():
            return True

        else:
            return False

    @property
    def path(self):

        path = ConfigUtil().user_lk_config_file_path

        return path

    @property
    def path_object(self):

        path_object = Path(self.path)

        return path_object

    @property
    def content(self):

        content = self.path_object.read_text()

        return content

    @property
    def odict(self):

        odict = yaml.load(self.content)

        return odict

    def save(self, odict):

        content = yaml.dump(odict)
        self.path_object.write_text(content.decode('utf-8'))

    def set(self, key, value):

        odict = self.odict
        odict[key] = value

        self.save(odict)

    def _get_repo_alias_key(self, alias):

        key = 'repo_alias_{alias}'.format(alias=alias)

        return key

    def set_repo_alias(self, alias, repo_url):

        self.set(key=self._get_repo_alias_key(alias), value=repo_url)

    def get_repo_alias(self, alias):

        key = self._get_repo_alias_key(alias)

        value = self.get(key)

        return value

    def alias_exists(self, alias):

        try:
            key = self._get_repo_alias_key(alias)
            self.get(key)
            return True

        except KeyError:
            return False

    def get(self, key):

        value = self.odict[key]

        return value

    def key_enabled(self, key):

        if key in self.odict:
            value = self.odict[key]
            if P(value).is_yaml_true:
                return True

        return False

    @property
    def default_push_repo(self):
        return self.odict[default_push_repo]

    @property
    def default_pull_repo(self):
        return self.odict[default_pull_repo]

    def update_default_push_repo(self, repo_url):

        self.set(default_push_repo, repo_url)

    @property
    def add_command_prompt_enabled(self):

        return self.key_enabled(create_command_prompt)

    # def update_push_repo(self, remote_repo):
    #
    #     self.create_config(remote_repo=remote_repo)

    # def default_commands_repo(self):
    #
    #     try:
    #         return self.config_dict['default_commands_repo']
    #
    #     except IOError:
    #
    #         self.create_config()
    #         return self.config_dict['default_commands_repo']
    #
    #         # raise LocalConfigNotFound

    @property
    def lk_config_dir_string(self):

        lk_config_dir_string = ConfigUtil().lk_config_dir

        return lk_config_dir_string

    @property
    def lk_config_dir_path_object(self):

        lk_config_dir_path_object = Path(self.lk_config_dir_string)

        return lk_config_dir_path_object

    @property
    def lk_config_file_path_string(self):
        lk_config_file_path_string = ConfigUtil().user_lk_config_file_path
        return lk_config_file_path_string

    @property
    def lk_config_file_path_object(self):

        lk_config_file_path = Path(self.lk_config_file_path_string)

        return lk_config_file_path

    def create_config(self, remote_repo=None):

        if not self.lk_config_dir_path_object.exists():
            Path.mkdir(self.lk_config_dir_path_object, parents=True, exist_ok=True)

        if self.lk_config_file_path_object.exists():

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

        config_yaml_string = yaml.dump(config_odict)

        self.lk_config_file_path_object.write_text(config_yaml_string.decode('utf-8'))
