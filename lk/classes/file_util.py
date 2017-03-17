import json

from lk.utils.config_util import ConfigUtil
from lk.utils.path_util import join_paths
from lk.utils.shell_util import run
from lk.utils.string_util import cli_print
from pathlib2 import Path
from utils2.datetime_util import DatetimeUtil


class FileUtil(object):

    def __init__(self, path):
        self._path = path

    @property
    def path(self):
        return self._path

    @property
    def path_object(self):

        return Path(self.path)

    @property
    def content(self):

        return self.path_object.read_text()

    def write(self, text):
        text_utf8 = text.decode('utf-8')
        self.path_object.write_text(text_utf8)

    def to_dict(self):

        try:
            with open(self.path) as json_data:
                dict_data = json.load(json_data)

            return dict_data

        except ValueError as e:
            message = '\n\nJSON could be invalid.'
            raise ValueError(e.message + message)

    def touch(self):
        self.path_object.touch()

    def exists(self):

        if self.path == '':
            return False

        return self.path_object.exists()

    def delete(self):

        self.path_object.unlink()

    @property
    def file_name(self):

        file_name = self.path_object.name
        return file_name

    def delete_with_backup(self):

        now_datetime_string = DatetimeUtil().now_iso_string()
        new_suffix = '.{timestamp}'.format(timestamp=now_datetime_string)
        new_file_name = self.file_name + new_suffix

        home_path = ConfigUtil().user_home_path
        tmp_dir = join_paths(home_path, 'tmp')

        new_file_path = join_paths(tmp_dir, new_file_name)

        if self.exists():
            try:
                self.path_object.rename(new_file_path)
            except OSError as e:
                cli_print(e.message)
                cli_print('Trying with sudo')
                command = 'sudo mv {source_path} {target_path}'.format(
                    source_path=self.path,
                    target_path=new_file_path
                )
                run(command)

        else:
            cli_print("File doesn't exists.")


File = FileUtil

