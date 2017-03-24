import click
from pathlib2 import Path

from lk.utils.config_util import ConfigUtil


@click.command('add-dev-command')
@click.argument('name')
def cli(name):

    print('# Adding dev command: ' + name)

    template = """

import click


@click.command('{command_name}')
def cli():

    print('Starting command: {command_name}')

    print('Finished command: {command_name}')

"""

    command_source = template.format(
        command_name=name
    )

    command_path = '{commands_directory}/{command_name}_command.py'.format(
        commands_directory=ConfigUtil().dev_commands_directory,
        command_name=name.replace('-', '_')
    )

    Path(command_path).write_text(command_source.decode('utf-8'))

    print('# Command path: ' + command_path)

    print('# Finished adding dev command: ' + name)
