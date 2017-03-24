from lk.utils import shell_util


class TestUbuntu:

    def test_1(self):

        a = 'one'

        print(a)

        self.run_docker()

        assert 1 == 1

    def run_docker(self):

        output = shell_util.run_and_return_output('ls')

        print(output)

        # assert False
