import git

from lk.classes.shell import current_shell_path


class Dir(object):

    def __init__(self, path):

        self._path = path

    @property
    def path(self):
        return self._path

    def is_git_repo(self):

        try:
            _ = git.Repo(self.path).git_dir
            return True
        except git.exc.InvalidGitRepositoryError:
            return False


current_dir = Dir(current_shell_path)

