

import click


@click.command('list')
def cli():

    print('Starting command: list')

    commands = Commands().get_commands()

    print('Finished command: list')

