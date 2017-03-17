
import click

from lk.classes.push_command import PushCommand


@click.command('push-command')
@click.argument('command_name')
@click.option('--repo', required=True)
@click.option('--force-push', is_flag=True, default=False)
@click.option('--only-update-config', is_flag=True, default=False)
# @click.option('--unpushed', is_flag=True, default=False)
def cli(command_name, repo, force_push, only_update_config):

    # print('Starting command: push-command')

    PushCommand(
        command_name=command_name,
        repo=repo
    ).push(
        force_push=force_push,
        only_update_config=only_update_config
    )

    # print('Finished command: push-command')
