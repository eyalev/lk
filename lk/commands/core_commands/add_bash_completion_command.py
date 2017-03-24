

import click

from lk.utils.config_util import config_util


@click.command('add-bash-completion')
def cli():

    print('Starting command: add-bash-completion')

    lk_bash_complete_file_path = config_util.lk_bash_complete_script_path

    bashrc_path = config_util.user_bashrc_path

    text_to_append_template = '''

# lk completion [https://github.com/eyalev/lk]
source {lk_bash_complete_file_path}
'''

    text_to_append = text_to_append_template.format(
        lk_bash_complete_file_path=lk_bash_complete_file_path
    )

    with open(bashrc_path, 'a') as _file:
        _file.write(text_to_append)

    print('Finished command: add-bash-completion')

