import json
import subprocess

import click
from bash import bash

from lk.config.app_config import bash_success_code
from lk.utils.confirm_util import app_confirm


def run_and_return_output(command, command_for_print=None, print_command=False, confirm_prompt=False, print_output=False):

    if command_for_print:
        print('\n> Running command:\n')
        print(command_for_print + '\n')

    if print_command:
        print('\n> Running command:\n')
        print(command + '\n')

    if confirm_prompt:

        if app_confirm('>> Do you want to continue?'):
            pass
        else:
            print('## Command did not run.')
            return

    result = bash(command)
    output = result.value()

    if print_output:
        print('\n## Output:')
        print('\n' + 44 * '-')

        print('')
        print(output)

        print('\n' + 44 * '-')

    return output


def run_confirm_and_return_dict(command):

    json_output = run_and_return_output(
        command,
        print_command=True,
        confirm_prompt=True,
        print_output=True
    )

    return json.loads(json_output)


def run_and_return_json_object(command, print_command=False):

    json_output = run_and_return_output(command, print_command)

    json_object = json.loads(json_output)

    return json_object


def run_print_and_return_output(command):

    print('\n> Running command:\n')
    print(command)

    output = run_and_return_output(command)

    return output


def run_and_print(command,
                  verbose=False,
                  confirm_prompt=False,
                  skip_confirm=True,
                  hide_echo=True,
                  decorate_command=False,
                  allow_error=False):

    if confirm_prompt or not skip_confirm:
        print('\n>> Confirm command:\n')
    elif verbose:
        print('\n> Running command:\n')

    custom_command = customize_command(command, hide_echo)

    if decorate_command:
        print('--------------------------------\n')

    if verbose or confirm_prompt:
        print(custom_command + '\n')

    if decorate_command:
        print('--------------------------------\n')

    if confirm_prompt or not skip_confirm:
        if app_confirm('>> Do you want to continue?'):
            pass
        else:
            print('## Command did not run.')
            return

    if verbose:
        print('\n## Output:')
        print('\n' + 44*'-')

        print('')

    return_code = subprocess.call(command, shell=True)

    if verbose:
        print('\n' + 44 * '-')

    if not allow_error and return_code != bash_success_code:
        print('\n[ERROR] Command failed with code:', return_code, '\n')
        raise click.Abort

    return return_code


def run_and_get_return_code(command):

    command_result = bash(command)

    return_code = command_result.code

    return return_code


def customize_command(command, hide_echo):

    if hide_echo:
        command_parts = command.split('\n')

        custom_command_parts = []
        for part in command_parts:
            if part.startswith('echo'):
                continue
            custom_command_parts.append(part)

        custom_command = '\n'.join(custom_command_parts)

    else:
        custom_command = command

    return custom_command


def run_and_confirm(command, allow_error=False):

    return_code = run_and_print(command, confirm_prompt=True, allow_error=allow_error)

    return return_code


def run_interactive(command):

    run_and_print(command, verbose=True)


run_command = run_and_return_output
run = run_and_print
# run_interactive = run_and_print
execute = run_and_return_output
get_output = run_and_return_output

