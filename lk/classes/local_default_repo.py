from lk.classes.local_config import LocalConfig
from lk.config import app_config
from lk.utils.path_util import full_path


class LocalDefaultRepo(object):

    def __init__(self):
        pass

    @property
    def remote_commands_repo_url(self):

        commands_repo = LocalConfig().default_commands_repo()

        return commands_repo

    @property
    def string_path(self):

        # https://github.com/lk-commands/default

        repo_service = self.remote_commands_repo_url.split('/')[2].split('.')[0]

        repo_user = self.remote_commands_repo_url.split('/')[3]

        commands_repo_name = self.remote_commands_repo_url.split('/')[4]

        commands_repo_local_rel_path = '{local_repos_dir}/{repo_service}/{repo_user}/{commands_repo_name}'.format(
            local_repos_dir=app_config.local_repos_dir,
            repo_service=repo_service,
            repo_user=repo_user,
            commands_repo_name=commands_repo_name
        )

        commands_repo_local_path = full_path(commands_repo_local_rel_path)

        return commands_repo_local_path

    @property
    def commands_dir_string_path(self):

        return self.string_path + '/commands'
