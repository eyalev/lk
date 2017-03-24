from lk.classes.python_util import P
from lk.classes.shell import Shell
from lk.utils.shell_util import run_and_return_output, run_and_get_return_code, run
import git


class SourceControl(object):

    def __init__(self):
        pass

    @property
    def current_path(self):

        path = Shell().current_shell_path()

        return path

    @property
    def is_git(self):

        try:
            _ = git.Repo(self.current_path).git_dir
            return True
        except git.exc.InvalidGitRepositoryError:
            return False

    @property
    def is_hg(self):

        return_code = run_and_get_return_code('hg root')

        if P(return_code).is_shell_success_code:
            return True
        else:
            return False

    @property
    def current_branch(self):

        if self.is_git:
            current_branch = run_and_return_output('git rev-parse --abbrev-ref HEAD')
            return current_branch

        elif self.is_hg:
            current_branch = run_and_return_output('hg identify -b')
            return current_branch

        else:
            raise NotImplementedError
