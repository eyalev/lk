
from lk.classes.local_config import LocalConfig
from lk.classes.local_default_repo import LocalDefaultRepo
from lk.classes.source_code_repo import SourceCodeRepo


def get_remote_default_repo():

    remote_default_repo_url = LocalConfig().default_commands_repo()
    remote_default_repo = SourceCodeRepo(url=remote_default_repo_url)

    return remote_default_repo


def get_local_default_repo():

    local_default_repo = LocalDefaultRepo()

    return local_default_repo


def get_local_config():

    local_config = LocalConfig()

    return local_config

