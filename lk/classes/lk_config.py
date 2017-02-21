from lk.classes import yaml
from lk.utils.config_util import ConfigUtil
from pathlib2 import Path


class LKConfig(object):

    def __init__(self):
        pass

    @property
    def path_object(self):

        lk_config_path = ConfigUtil().user_lk_config_file_path

        path_object = Path(lk_config_path)

        return path_object

    @property
    def content(self):

        content = self.path_object.read_text()

        return content

    @property
    def odict(self):

        odict = yaml.load(self.content)

        return odict

    def save(self, odict):

        content = yaml.dump(odict)
        self.path_object.write_text(content.decode('utf-8'))

    def set(self, key, value):

        odict = self.odict
        odict[key] = value

        self.save(odict)
