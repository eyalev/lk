import xerox

from lk.utils.string_util import print_not_implemented, cli_print


class ClickUtil(object):

    def __init__(self):
        pass

    def not_implemented(self):

        print_not_implemented()

        return None


def not_implemented():

    return ClickUtil().not_implemented()


def abort_command():

    print('Command aborted.')
    return None


def copy_to_clipboard(text):

    xerox.copy(text)
    cli_print('[Result copied to clipboard]')


def do_copy_to_clipboard(text):

    copy_to_clipboard(text)
