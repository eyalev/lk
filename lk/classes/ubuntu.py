from lk.utils.shell_util import run_and_return_output


class Ubuntu(object):

    def __init__(self):
        pass

    def get_executable_path(self, program):

        command = 'which {program}'.format(program=program)

        output = run_and_return_output(command)

        return output
