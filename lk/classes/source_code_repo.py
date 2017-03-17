from lk.utils.config_util import ConfigUtil
from lk.utils.shell_util import run_and_confirm, run, run_and_return_output

from furl import furl

bitbucket = 'bitbucket'
bitbucket_domain = 'bitbucket.org'
github = 'github'
github_domain = 'github.com'


class SourceCodeRepo(object):

    def __init__(self, url=None, service=None, user=None, repo_name=None):

        self._url = url

        self._service = service
        self._user = user
        self._repo_name = repo_name

    @property
    def url(self):

        if self._url:
            return self._url

        else:

            url = 'https://{service_domain}/{user}/{repo}'.format(
                service_domain=self.service_domain,
                user=self.user,
                repo=self.repo_name
            )
            return url

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

        if self._user:
            return self._user

        else:
            user = self._url.split('/')[3]
            return user

    @property
    def repo_name(self):

        if self._repo_name:
            return self._repo_name

        else:
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

        if 'github' in url:
            return url

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
    def commands_dir_string_path(self):
        return self.local_repo_string_path + '/commands'

    @property
    def local_repo_string_path(self):

        commands_repo_local_path = '{local_repos_dir}/{repo_service}/{repo_user}/{commands_repo_name}'.format(
            local_repos_dir=ConfigUtil().local_repos_dir,
            repo_service=self.hosting_service,
            repo_user=self.user,
            commands_repo_name=self.repo_name
        )

        return commands_repo_local_path

    @property
    def service(self):

        if self._service:
            return self._service

        if 'bitbucket.org' in self.url:
            return bitbucket

        elif 'github.com' in self.url:
            return github

        else:
            raise NotImplementedError

    @property
    def bitbucket(self):
        return self.service == bitbucket

    @property
    def github(self):
        return self.service == github

    @property
    def service_domain(self):

        if self.bitbucket:
            return bitbucket_domain

        if self.github:
            return github_domain

        else:
            raise NotImplementedError

    def remote_file_source(self, file_name):

        if self.bitbucket:
            shell_command = 'git archive --remote=git@{service_domain}:{user}/{repo}.git HEAD commands/{file_name} | tar -x -O'.format(
                service_domain=self.service_domain,
                user=self.user,
                repo=self.repo_name,
                file_name=file_name
            )
            output = run_and_return_output(shell_command)
            return output

        elif self.github:
            raise NotImplementedError

        else:
            raise NotImplementedError










