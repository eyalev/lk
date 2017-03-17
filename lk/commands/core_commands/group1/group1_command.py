import os

import click
from lk.classes.multi_command import LKMultiCommand

from lk.utils.config_util import ConfigUtil

commands_dir = os.path.join(ConfigUtil().lk_dir, 'commands/core_commands/group1/commands')


@click.command('group1', cls=LKMultiCommand, commands_dir=commands_dir)
def cli():

    print('Starting command: group1')

    print('Finished command: group1')

