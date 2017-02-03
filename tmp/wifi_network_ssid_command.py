

import click

from lk.utils.shell_util import run_and_print


@click.command('wifi-network-ssid')
def cli():

    run_and_print('''iwgetid -r''')
