

import click
from pathlib2 import Path

from lk.config import app_config


@click.command('create-shell-command')
@click.argument('command')
@click.option('--content')
def cli(command, content):

    print('# Creating shell command: ' + command)

    if content:
        shell_command_to_run = content
    else:
        shell_command_to_run = click.prompt('# Enter shell command')

    if shell_command_to_run.endswith("'"):
        quotes = '"""'
    else:
        quotes = "'''"

    template = """

import click

from lk.utils.shell_util import run_and_print


@click.command('{command_name}')
def cli():

    run_and_print({quotes}{command_to_run}{quotes})
"""

    command_source = template.format(
        command_name=command,
        command_to_run=shell_command_to_run,
        quotes=quotes
    )

    command_path = '{commands_directory}/{command_name}_command.py'.format(
        commands_directory=app_config.commands_directory,
        command_name=command.replace('-', '_')
    )

    # import pdb; pdb.set_trace()
    # Path(command_path).write_text(unicode(command_source))
    Path(command_path).write_text(command_source.decode("utf-8"))

    print('# Finished creating shell command: ' + command)
