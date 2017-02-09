import git

import click

from lk.classes.Dir import current_dir


@click.command('pull-source')
def cli():

    print('Starting command: pull-source')

    if current_dir.is_git_repo:

        g = git.cmd.Git(current_dir.path)
        g.pull()

    print('Finished command: pull-source')

