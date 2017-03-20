from lk.classes.python_util import P
from lk.utils.shell_util import run, run_and_return_output, run_and_get_return_code


class App(object):

    def __init__(self, app):
        self._app = app

    @property
    def app(self):
        return self._app

    @property
    def installed(self):

        # return_code = run_and_get_return_code('lk check-installed {app} --script-format'.format(app=self.app))
        return_code = run_and_get_return_code('dpkg -l | grep {app}'.format(app=self.app))

        if P(return_code).is_bash_success_code:
            return True
        else:
            return False

    @property
    def not_installed(self):

        return not self.installed
