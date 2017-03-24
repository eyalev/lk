
import libtmux


class Tmux(object):

    def __init__(self):
        pass

    @property
    def server(self):
        server = libtmux.Server()
        return server

    @property
    def session(self):
        session = self.server.find_where({'session_name': 'main'})
        return session

    @property
    def window(self):
        return self.session.attached_window

    def select_window(self, window_name):

        window = self.session.select_window(window_name)

        return window

    @property
    def pane(self):
        return self.window.attached_pane

    def run(self, command):
        print('Start run')
        self.pane.send_keys(command, suppress_history=False)
        print('Finish run')

    def focus_on(self, window_name):

        window = self.select_window(window_name)
        pane = window.list_panes()[0]
        pane.select_pane()

    def create_window(self, window_name):

        window = self.session.new_window(attach=False, window_name=window_name)
        return window

    def create_window_if_needed(self, window_name):

        if self.window_not_exists(window_name):
            window = self.create_window(window_name)

        else:
            window = self.get_window(window_name)

        return window

    def get_window(self, window_name):

        return self.windows_dict[window_name]

    @property
    def windows_dict(self):

        windows_dict = {}

        for window in self.windows:
            windows_dict[window.name] = window

        return windows_dict

    def window_not_exists(self, window_name):
        return not self.window_exists(window_name)

    @property
    def window_list(self):

        window_list = self.session.list_windows()
        return window_list

    @property
    def windows(self):
        return self.window_list

    @property
    def window_names(self):

        names = [window.name for window in self.window_list]

        return names

    def window_exists(self, window_name):

        if window_name in self.window_names:
            return True

        else:
            return False
