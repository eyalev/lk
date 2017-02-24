from lk.classes.local_config import LocalConfig
from lk.config import app_config
from lk.utils.config_util import ConfigUtil
from lk.utils.path_util import full_path


class LocalRepo(object):

    def __init__(self, remote_url):
        self._remote_url = remote_url

    @property
    def remote_url(self):
        return self._remote_url

    @property
    def remote_commands_repo_url(self):

        # commands_repo = LocalConfig().default_commands_repo()
        commands_repo = self.remote_url

        return commands_repo

    @property
    def path(self):

        # https://github.com/lk-commands/default

        repo_service = self.remote_commands_repo_url.split('/')[2].split('.')[0]

        repo_user = self.remote_commands_repo_url.split('/')[3]

        commands_repo_name = self.remote_commands_repo_url.split('/')[4]

        commands_repo_local_rel_path = '{local_repos_dir}/{repo_service}/{repo_user}/{commands_repo_name}'.format(
            local_repos_dir=ConfigUtil().local_repos_dir,
            repo_service=repo_service,
            repo_user=repo_user,
            commands_repo_name=commands_repo_name
        )

        commands_repo_local_path = full_path(commands_repo_local_rel_path)

        return commands_repo_local_path

    @property
    def commands_dir_string_path(self):

        return self.string_path + '/commands'
