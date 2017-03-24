from git import Repo

from lk.classes.shell import current_shell_path
from lk.utils.shell_util import run_and_print, run


class ShellCommands(object):

    def __init__(self):
        pass

    def git_pull_current_branch(self):

        repo = Repo(current_shell_path)
        current_branch = repo.active_branch

        command = 'git pull origin {current_branch}'.format(current_branch=current_branch)

        run_and_print(command)

    def hg_pull_current_branch(self):

        run('hg pull -u')


shell_commands = ShellCommands()
