

import click


from lk.classes.local_config import LocalConfig


@click.command('create-config')
def cli():

    print('Starting command: create-config')

    LocalConfig().create_config()

    print('Finished command: create-config')



