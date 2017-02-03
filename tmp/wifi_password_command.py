

import click

from lk.utils.shell_util import run_and_print


@click.command('wifi-password')
def cli():

    run_and_print('''sudo grep psk= /etc/NetworkManager/system-connections/topsy | cut -d '=' -f2''')
