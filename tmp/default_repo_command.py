

import click

from lk.classes.local_config import LocalConfig


@click.command('default-repo')
def cli():

    try:
        default_repo = LocalConfig().default_commands_repo()
        print(default_repo)

    except FileNotFoundError:
        print("Config file doesn't exist.")
