
import os

from lk.config import app_config


def full_path(relative_path):

    return PathUtil.full_path(relative_path)


class PathUtil(object):

    def __init__(self):
        pass

    @staticmethod
    def full_path(relative_path):

        _full_path = os.path.join(app_config.lk_path, relative_path)

        return _full_path
