from collections import OrderedDict as odict

import click
from lk.classes.commands import Commands
from lk.classes.commands_config_keys import repo_url_key
from lk.classes.dict_util import Dict
from lk.utils.string_util import cli_print


@click.command('list-commands')
@click.option('--include-no-config', is_flag=True, default=False)
def cli(include_no_config):

    print('Starting command: list')

    commands = Commands().get_commands()

    commands_odict = odict()

    for command_name, command in sorted(commands.iteritems()):
        command_data = odict()

        if command.has_config:
            command_data[repo_url_key] = command.repo_url
            commands_odict[command_name] = command_data
        elif include_no_config:
            command_data['status'] = 'no_config'
            commands_odict[command_name] = command_data

    yaml_string = Dict(commands_odict).to_pretty_yaml_string()

    cli_print(yaml_string)

    print('Finished command: list')

