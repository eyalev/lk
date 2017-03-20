
import platform


class OS(object):

    def __init__(self):
        pass

    @property
    def platform_info(self):

        platform_info = platform.platform()

        return platform_info

    @property
    def platform_info_lowercase(self):
        return self.platform_info.lower()

    @property
    def ubuntu(self):

        if 'ubuntu' in self.platform_info_lowercase:
            return True

        else:
            return False
