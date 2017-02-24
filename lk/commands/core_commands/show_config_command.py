

import click

from lk.classes.lk_config import LKConfig
from lk.utils.string_util import print_with_space, print_with_bottom_space, print_with_separators


@click.command('show-config')
def cli():

    lk_config = LKConfig()
    lk_config_path = lk_config.path

    print_with_space('Path:\n' + lk_config_path)
    print('Content:')
    print_with_separators(lk_config.content, top_space=False)
