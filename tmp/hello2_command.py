

import click

from lk.utils.shell_util import run_and_print


@click.command('hello2')
def cli():

    run_and_print('''echo hello2''')
