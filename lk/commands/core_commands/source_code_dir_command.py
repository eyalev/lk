

import click

from lk.utils.config_util import ConfigUtil


@click.command('source-code-dir')
def cli():

    print('')

    source_code_dir = ConfigUtil().lk_project_path

    print('lk source code directory: {}'.format(source_code_dir))

    print('')
