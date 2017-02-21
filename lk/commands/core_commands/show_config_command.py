

import click
from lk.utils.config_util import ConfigUtil
from lk.utils.string_util import print_with_space, print_with_bottom_space
from utils2.file_util import FileUtil


@click.command('show-config')
def cli():

    print('Starting command: show-config')

    lk_config_path = ConfigUtil().user_lk_config_file_path
    config_file = FileUtil(lk_config_path)

    print_with_space(lk_config_path + ':')
    separator = 90 * '-'
    print_with_bottom_space(separator)
    print_with_bottom_space(config_file.data())
    print_with_bottom_space(separator)

    print('Finished command: show-config')

