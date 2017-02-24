
import click

from lk.classes.push_command import PushCommand


@click.command('push-command')
@click.argument('command_name')
@click.option('--repo')
@click.option('--force-push/--no-force-push', default=False)
def cli(command_name, repo, force_push):

    # print('Starting command: push-command')

    PushCommand(
        command_name=command_name,
        repo=repo
    ).push(
        force_push=force_push
    )

    # print('Finished command: push-command')
