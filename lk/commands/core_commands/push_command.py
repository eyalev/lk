
import click

from lk.classes.push_command import PushCommand


@click.command('push')
@click.argument('command_name')
@click.option('--force-push/--no-force-push', default=False)
def cli(command_name, force_push):

    print('Starting command: push-command')

    PushCommand(command_name).push(force_push=force_push)

    print('Finished command: push-command')
