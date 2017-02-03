

import click

from lk.utils.shell_util import run_and_print
from lk.utils.string_util import multi_command_template


@click.command('api-project-test')
@click.argument('option')
def cli(option):

    print('Starting command: api-server-test')

    test_base_command = 'RESET_DB=false nosetests -v --rednose --nocapture --logging-level=INFO'

    if option == 'unit':

        commands_template = multi_command_template("""
{test_base_command} api.tests.app_tests.unit_tests
{test_base_command} -a 'unit' api
""")

    elif option == 'functional':

        commands_template = multi_command_template("""
{test_base_command} api.tests.app_tests.functional_tests
{test_base_command} -a 'functional' api
""")

    elif option == 'unit-and-functional':

        commands_template = multi_command_template("""
{test_base_command} api.tests.app_tests.unit_tests
{test_base_command} -a 'unit' api
{test_base_command} api.tests.app_tests.functional_tests
{test_base_command} -a 'functional' api
""")

    elif option == 'all':

        commands_template = multi_command_template("""
{test_base_command} api.tests.app_tests.unit_tests
{test_base_command} -a 'unit' api
{test_base_command} api.tests.app_tests.functional_tests
{test_base_command} -a 'functional' api
{test_base_command} api
""")

    else:
        raise ValueError('Invalid option')

    commands = commands_template.format(
        test_base_command=test_base_command
    )

    run_and_print(commands)

    print('Finished command: api-server-test')

