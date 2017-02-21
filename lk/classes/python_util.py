

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


P = PythonUtil
