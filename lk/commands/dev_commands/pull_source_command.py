import click

from lk.classes.Dir import current_dir
from lk.classes.shell_commands import shell_commands


@click.command('pull-source')
def cli():

    print('Starting command: pull-source')

    if current_dir.is_git_repo:

        shell_commands.git_pull_current_branch()

    print('Finished command: pull-source')

