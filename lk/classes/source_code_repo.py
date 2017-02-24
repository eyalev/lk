from lk.utils.config_util import ConfigUtil
from lk.utils.shell_util import run_and_confirm

from furl import furl


class SourceCodeRepo(object):

    def __init__(self, url):

        self._url = url

    @property
    def url(self):
        return self._url

    @property
    def hosting_service_host(self):

        hosting_service_host = self._url.split('/')[2]

        return hosting_service_host

    @property
    def hosting_service(self):

        hosting_service = self.hosting_service_host.split('.')[0]

        return hosting_service

    @property
    def user(self):

        user = self._url.split('/')[3]

        return user

    @property
    def repo_name(self):

        repo_name = self._url.split('/')[4]

        return repo_name

    @property
    def clone_command(self):

        # https://github.com/lk-commands/default
        # git@github.com:lk-commands/default.git

        # git clone git@bitbucket.org:eyalev/lk-commands.git

        # clone_command = 'git clone git@{hosting_service_host}:{user}/{repo_name}.git'.format(
        # clone_command = 'git clone {repo_url}.git'.format(
        clone_command = 'git clone {git_url}'.format(
            git_url=self.git_url
        )

        return clone_command

    @property
    def git_url(self):

        url = self.url

        _furl = furl(url)

        git_url = 'git@{host}:{user}/{repo}.git'.format(
            host=_furl.host,
            user=str(_furl.path).split('/')[1],
            repo=str(_furl.path).split('/')[2]
        )

        return git_url

    def clone(self):

        print('# Cloning lk-repo')

        clone_command = SourceCodeRepo(self.url).clone_command

        command = '{clone_command} {local_repo_path}'.format(
            clone_command=clone_command,
            local_repo_path=self.local_repo_string_path
        )

        run_and_confirm(command)

    @property
    def local_repo_string_path(self):

        commands_repo_local_path = '{local_repos_dir}/{repo_service}/{repo_user}/{commands_repo_name}'.format(
            local_repos_dir=ConfigUtil().local_repos_dir,
            repo_service=self.hosting_service,
            repo_user=self.user,
            commands_repo_name=self.repo_name
        )

        # from pathlib2 import Path
        #
        # user_data_dir = ConfigUtil().user_lk_data_dir
        # commands_repo_local_path = Path(user_data_dir).joinpath(commands_repo_local_rel_path)
        #
        # commands_repo_local_path_string = str(commands_repo_local_path)
        # # commands_repo_local_path = full_path(commands_repo_local_rel_path)

        # return commands_repo_local_path_string
        return commands_repo_local_path











