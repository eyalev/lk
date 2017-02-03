

import click

from lk.utils.shell_util import run_and_print


@click.command('test-tag')
@click.argument('tag')
def cli(tag):

    run_and_print("RESET_DB=false nosetests -v --rednose --nocapture --logging-level=INFO -a '{tag}' api".format(tag=tag))

