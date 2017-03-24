
import shutil

import git
from pathlib2 import Path

from lk.classes.python_util import P
from lk.classes.shell import current_shell_path
from lk.utils.shell_util import run_and_get_return_code


class Dir(object):

    def __init__(self, path):

        self._path = path

    @property
    def path(self):
        return self._path

    @property
    def path_object(self):
        path_object = Path(self.path)
        return path_object

    @property
    def is_git_repo(self):

        try:
            _ = git.Repo(self.path).git_dir
            return True
        except git.exc.InvalidGitRepositoryError:
            return False

    def create_if_needed(self):

        self.path_object.mkdir(parents=True, exist_ok=True)

    @property
    def is_hg_repo(self):

        return_code = run_and_get_return_code('hg root')

        if P(return_code).is_shell_success_code:
            return True
        else:
            return False

    def remove(self):

        shutil.rmtree(self.path)

    @property
    def exists(self):
        return self.path_object.exists()


current_dir = Dir(current_shell_path)

