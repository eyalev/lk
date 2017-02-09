

import click

from lk.utils.config_util import config_util


@click.command('add-bash-completion')
def cli():

    print('Starting command: add-bash-completion')

    lk_bash_complete_path = config_util.lk_bash_complete_script_path

    bashrc_path = config_util.user_bashrc_path

    print('Finished command: add-bash-completion')

