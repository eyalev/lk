

import click

from lk.utils.shell_util import run_and_print


@click.command('hello-world')
def cli():

    run_and_print('''echo "Hello World"''')
