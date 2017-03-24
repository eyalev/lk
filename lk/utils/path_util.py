
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

    def join_paths(self, path1, path2):

        _full_path = os.path.join(path1, path2)

        return _full_path


def join_paths(path1, path2):
    return PathUtil().join_paths(path1, path2)
