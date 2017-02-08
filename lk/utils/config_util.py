
from pathlib2 import Path

from lk.config import app_config
from lk.definitions import LK_ROOT


class ConfigUtil(object):

    def __init__(self):
        pass

    @property
    def local_repos_dir(self):

        local_repos_dir = Path(self.user_lk_data_dir).joinpath(app_config.local_repos_dir)

        return local_repos_dir

    @property
    def user_lk_config_dir(self):

        user_lk_config_dir = '{user_config_dir}/lk'.format(
            user_config_dir=self.user_config_dir
        )

        return user_lk_config_dir

    @property
    def user_lk_data_dir(self):

        user_lk_config_dir = '{user_shared_data_dir}/lk'.format(
            user_shared_data_dir=self.user_shared_data_dir
        )

        return user_lk_config_dir

    @property
    def user_config_dir(self):

        user_config_dir = '{home_path}/.config'.format(
            home_path=str(Path.home())
        )

        return user_config_dir

    @property
    def user_shared_data_dir(self):

        user_config_dir = '{home_path}/.local/share'.format(
            home_path=str(Path.home())
        )

        return user_config_dir

    @property
    def user_commands_directory(self):

        user_commands_directory = '{user_lk_data_dir}/user_commands'.format(
            user_lk_data_dir=self.user_lk_data_dir
        )

        return user_commands_directory

    @property
    def core_commands_directory(self):

        core_commands_directory = '{lk_project_path}/commands/core_commands'.format(
            lk_project_path=self.lk_project_path
        )

        return core_commands_directory

    @property
    def lk_project_path(self):

        return LK_ROOT
