
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
    def user_lk_data_dir(self):

        user_lk_config_dir = '{user_shared_data_dir}/lk'.format(
            user_shared_data_dir=self.user_shared_data_dir
        )

        return user_lk_config_dir

    @property
    def user_home_path(self):
        home_path = str(Path.home())
        return home_path

    @property
    def current_dir(self):
        current_dir = str(Path.cwd())
        return current_dir

    @property
    def user_data_dir(self):

        user_data_dir = '{home_path}/.local/share'.format(
            home_path=self.user_home_path
        )

        return user_data_dir

    @property
    def user_lk_dir(self):

        user_lk_dir = '{user_data_dir}/lk'.format(
            user_data_dir=self.user_data_dir
        )

        return user_lk_dir

    @property
    def lk_config_dir(self):

        user_config_dir = '{user_lk_dir}/config'.format(
            user_lk_dir=self.user_lk_dir
        )

        return user_config_dir

    @property
    def user_lk_config_file_path(self):

        lk_config_file_path = '{lk_config_dir}/lk_config.yaml'.format(
            lk_config_dir=self.lk_config_dir
        )

        return lk_config_file_path

    # @property
    # def add_command_prompt_enabled(self):



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
    def lk_dir(self):

        lk_dir = app_config.lk_path

        return lk_dir

    @property
    def user_commands_directory_in_lk_dir(self):

        user_commands_directory = '{lk_dir}/commands/user_commands'.format(
            lk_dir=self.lk_dir
        )

        return user_commands_directory

    @property
    def core_commands_directory(self):

        core_commands_directory = '{lk_project_path}/commands/core_commands'.format(
            lk_project_path=self.lk_project_path
        )

        return core_commands_directory

    @property
    def dev_commands_directory(self):

        dev_commands_directory = '{lk_project_path}/commands/dev_commands'.format(
            lk_project_path=self.lk_project_path
        )

        return dev_commands_directory

    @property
    def commands_config_file_path(self):

        file_name = 'lk_commands_config.yaml'

        commands_config_file_path = self.join_paths_string(self.lk_config_dir, file_name)

        return commands_config_file_path

    @property
    def lk_project_path(self):

        return LK_ROOT

    def join_paths(self, first_path, *args):

        combined_path = Path(first_path).joinpath(*args)

        return combined_path

    def join_paths_string(self, first_path, *args):

        combined_path = self.join_paths(first_path, *args)

        return str(combined_path)

    @property
    def lk_bash_complete_script_path(self):

        relative_path = 'scripts/lk_bash_complete.sh'

        # full_path = Path(self.lk_project_path).joinpath(relative_path)
        full_path = self.join_paths(self.lk_project_path, relative_path)

        return full_path

    @property
    def user_bashrc_path(self):

        bashrc_path = Path(self.user_home_path).joinpath('.bashrc')
        return str(bashrc_path)


config_util = ConfigUtil()
