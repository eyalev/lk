from lk.classes.python_util import P
from lk.classes.urls import URLs
from lk.utils.shell_util import execute, run_and_return_output, run, run_and_get_return_code


class Chrome(object):

    def __init__(self):
        pass

    def get_url(self, url_input):

        if url_input is None:
            raise NotImplementedError

        if not url_input.startswith('http'):
            url = URLs().get_url(url_input)

        else:
            url = url_input

        return url

    def open_multiple_tabs(self, urls):

        urls_string = ''

        all_exist = True

        for url in urls:
            if not self.tab_exists(url):
                all_exist = False
            urls_string += ' {url}'.format(url=url)

        if all_exist:
            self.focus(urls[-1])

        else:
            execute('google-chrome-stable --new-window {urls_string}'.format(urls_string=urls_string))

    def open(self, url_input, focus=True):

        if focus:
            self.open_or_focus(url_input)

        else:
            url = self.get_url(url_input)
            self.open_url(url)

    def open_or_focus(self, url_input):

        url = self.get_url(url_input)

        if self.tab_exists(url=url):
            self.focus(url)

        else:
            self.open_url(url)

    def tab_exists(self, url):

        tabs = self.tabs()

        for tab in tabs:
            if url in tab:
                return True

        return False

    def focus(self, url):

        run('chromix-too focus {url}'.format(url=url))

    def tabs(self):

        code = run_and_get_return_code('chromix-too ls')
        if P(code).is_bash_error_code:
            print('Chromix not working.')
            return []

        output = run_and_return_output('chromix-too ls')

        tabs = output.split('\n')

        return tabs

    def open_url(self, url):

        execute('google-chrome-stable --new-window {url}'.format(url=url))
