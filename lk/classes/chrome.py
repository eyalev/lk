from lk.utils.shell_util import execute


class Chrome(object):

    def __init__(self):
        pass

    def open_url(self, url):

        execute('google-chrome-stable --new-window {url}'.format(url=url))
