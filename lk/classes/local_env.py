

# from share.file_util import FileUtil
from lk.classes.file_util import FileUtil, File
from lk.utils.config_util import ConfigUtil


class LocalEnv(object):

    def __init__(self, file_path=None, name=None):

        self._file_path = self.init_file_path(file_path_param=file_path, name=name)
        self._env_dict = self.init_env_dict()

    @property
    def file_path(self):
        return self._file_path

    @property
    def dict(self):
        return self._env_dict

    def init_file_path(self, file_path_param, name):

        if name:
            file_path = ConfigUtil().lk_dir + '/env/{name}.json'.format(name=name)

        elif file_path_param is None:
            file_path = ConfigUtil().lk_dir + '/env/env.json'

        else:
            file_path = file_path_param

        return file_path

    def init_env_dict(self):

        try:
            return File(self.file_path).to_dict()

        except IOError:
            print(self.file_path + ' not found.')
            return {}

    def get(self, name, default=None):

        try:
            value = self.dict[name]
            return value

        except KeyError:
            return default


