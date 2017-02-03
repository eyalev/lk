
import os

from lk import definitions

from pathlib2 import Path

# Bash

bash_success_code = 0

# Local repo

local_repos_dir = 'repos'

# Commands

current_dir_path = str(Path.cwd())

lk_path = definitions.LK_ROOT

commands_directory = os.path.join(lk_path, 'commands')

repos_directory = os.path.join(current_dir_path, 'repos')

# commands_local_repo_dir_path = os.path.join(current_dir_path, 'repos/bitbucket/breezometer/lk-commands/commands')

# commands_repo_git_url = 'git@bitbucket.org:breezometer/lk-commands.git'

# repo_hosting_service = commands_repo_git_url.split('@')[1].split('.')[0]

# organization = commands_repo_git_url.split(':')[1].split('/')[0]

# organization_repos_dir = '{repos_dir}/{repo_hosting_service}/{organization}'.format(
#     repos_dir=repos_directory,
#     repo_hosting_service=repo_hosting_service,
#     organization=organization
# )

DEFAULT_COMMANDS_REPO = 'https://github.com/lk-commands/default'
