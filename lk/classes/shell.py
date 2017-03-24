from pathlib2 import Path


class Shell(object):

    def __init__(self):
        pass

    def current_shell_path(self):

        dir_path = Path.cwd().as_posix()

        return dir_path


current_shell_path = Shell().current_shell_path()
