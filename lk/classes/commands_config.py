from collections import OrderedDict as odict

# from lk.classes.command import Command
from lk.classes.commands_config_keys import commands_dir_key, commands_key, relative_path_key, repo_url_key, \
    local_path_key, local_repo_path_key, local_repo_command_path_key, info_key, file_name_key, last_push_key
from lk.classes.dict_util import Dict
from lk.classes.file_util import File
from lk.utils.config_util import ConfigUtil
from lk.utils.string_util import String, print_util
from pathlib2 import Path

import pyaml


class CommandsConfig(object):

    def __init__(self):

        self._odict = odict()

        self.create_config_if_needed()

    def create_config_if_needed(self):

        self.yaml_file.touch()
        self.json_file.touch()

        if not self.odict:

            odict_object = odict()
            odict_object[commands_dir_key] = ConfigUtil().user_commands_directory
            odict_object[commands_key] = None

            self.update_config(odict_object=odict_object)

    def set_config(self, yaml_string):

        self.yaml_file.write(yaml_string)

    def update_config(self, odict_object):

        json_string = Dict(odict_object).to_pretty_json_string()
        yaml_string = pyaml.dumps(odict_object)

        self.json_file.write(json_string)
        self.yaml_file.write(yaml_string)

    @property
    def json_file_path(self):

        commands_config_json_file_path = ConfigUtil().commands_config_json_file_path
        return commands_config_json_file_path

    @property
    def json_file(self):

        file = File(self.json_file_path)
        return file

    @property
    def yaml_file(self):
        yaml_file = File(self.yaml_path)
        return yaml_file

    @property
    def yaml_path(self):
        return str(self.yaml_path_object)

    @property
    def yaml_path_object(self):

        commands_config_file_path = ConfigUtil().commands_config_yaml_file_path

        commands_config_path_object = Path(commands_config_file_path)

        return commands_config_path_object

    def user_output(self, command_name=None):

        commands_dict = self.odict[commands_key]

        if command_name:
            command_data = commands_dict.get(command_name, {})
            command_dict = odict()
            command_dict[command_name] = command_data
            output = Dict(command_dict).to_pretty_yaml_string()

        else:
            output = self.yaml_file.content

        return output

    @property
    def yaml_file_content(self):

        content = self.yaml_file.content

        return content

    @property
    def json_file_content(self):

        content = self.json_file.content

        return content

    @property
    def odict(self):

        json_odict = String(self.json_file_content).to_odict()

        return json_odict

    @property
    def commands_odict(self):
        """
        :rtype: collections.OrderedDict
        """

        return self.odict[commands_key]

    def add_command(self,
                    command_name,
                    repo_url=None,
                    file_name=None,
                    local_path=None,
                    local_repo_command_path=None,
                    local_repo_path=None,
                    override=False):

        commands_dict = self.commands_odict

        if override is False and command_name in commands_dict:
            print_util('Command {command} already exists.'.format(command=command_name))
            return

        info_odict = self.get_info_odict(command_name)

        command_odict = odict()
        command_odict[repo_url_key] = repo_url
        command_odict[file_name_key] = file_name
        command_odict[local_path_key] = local_path
        command_odict[local_repo_path_key] = local_repo_path
        command_odict[local_repo_command_path_key] = local_repo_command_path

        command_odict.update(info_odict)

        if commands_dict is None:
            commands_dict = odict()

        commands_dict[command_name] = command_odict

        self.update_commands(commands_dict=commands_dict)

    def update_command(self,
                       command_name,
                       repo_url=None,
                       local_path=None,
                       file_name=None,
                       local_repo_path=None,
                       local_repo_command_path=None,
                       last_push=None
                       ):

        commands_odict = self.commands_odict

        command_odict = commands_odict.get(command_name)

        if repo_url:
            command_odict[repo_url_key] = repo_url

        if local_path:
            command_odict[local_path_key] = local_path

        if file_name:
            command_odict[file_name_key] = file_name

        if local_repo_path:
            command_odict[local_repo_path_key] = local_repo_path

        if local_repo_command_path:
            command_odict[local_repo_command_path_key] = local_repo_command_path

        if last_push:
            command_odict[last_push_key] = last_push
        else:
            if last_push_key not in command_odict:
                command_odict[last_push_key] = None

        info_odict = self.get_info_odict(command_name=command_name)

        command_odict.update(info_odict)

        command_config_keys_order = [
            file_name_key,
            repo_url_key,
            last_push_key,
            local_path_key,
            local_repo_path_key,
            local_repo_command_path_key,
        ]

        ordered_command_odict = odict((key, command_odict[key]) for key in command_config_keys_order)

        commands_odict[command_name] = ordered_command_odict

        self.update_commands(commands_dict=commands_odict)

    def update_commands(self, commands_dict):

        config_dict = self.odict
        config_dict[commands_key] = commands_dict

        self.update_config(config_dict)

    def remove_command(self, command_name):

        commands_odict = self.commands_odict

        Dict(commands_odict).remove(command_name, allow_missing_key=True)

        self.update_commands(commands_odict)

    def get_info_odict(self, command_name):

        command_data = self.get_command_data(command_name)

        info_odict_data = command_data.get(info_key)

        if info_odict_data:

            command_not_pushed_key = 'command_not_pushed'

            if command_not_pushed_key in info_odict_data:

                if command_data[repo_url_key] is None:
                    info_odict_data[command_not_pushed_key] = "Command has not been pushed yet11."

                else:
                    info_odict_data.pop(command_not_pushed_key)

        if info_odict_data:
            info_odict = odict()
            info_odict[info_key] = info_odict_data
        else:
            info_odict = odict()

        return info_odict

    def get_command_data(self, command_name):

        commands_odict = self.commands_odict

        command_data = commands_odict.get(command_name)

        return command_data











