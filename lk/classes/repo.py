from lk.classes.lk_config import LKConfig


class Repo(object):

    def __init__(self, repo_name):

        self._repo_name = repo_name

    @property
    def repo_name(self):
        return self._repo_name

    @property
    def url(self):

        repo_url = LKConfig().get_repo_alias(self.repo_name)

        return repo_url

