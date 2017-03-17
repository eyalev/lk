from lk.config import app_config
from lk.utils.string_util import String


class PythonUtil(object):

    def __init__(self, input):
        self._input = input

    @property
    def input(self):
        return self._input

    def get_first_line_with(self, string):

        lines = self.input.split('\n')

        for line in lines:
            if string in line:
                return line

        return None

    @property
    def is_shell_success_code(self):

        if self.input == '0' or self.input == 0:
            return True

        else:
            return False

    @property
    def is_yaml_true(self):

        if self.input == 'true' or self.input is True:
            return True

        else:
            return False

    @property
    def is_url(self):
        is_url = String(self.input).is_url
        return is_url

    @property
    def is_not_a_url(self):
        return not self.is_url

    @property
    def is_bash_success_code(self):
        if str(self.input) == str(app_config.bash_success_code):
            return True
        else:
            return False

    @property
    def is_bash_error_code(self):
        return not self.is_bash_success_code


P = PythonUtil
