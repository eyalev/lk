

import click
from click import MultiCommand
import os

from lk.utils.config_util import ConfigUtil

# plugin_folder = os.path.join(ConfigUtil().lk_dir, 'commands/core_commands/group1')


class LKMultiCommand(MultiCommand):

    def __init__(self, commands_dir, **kwargs):
        MultiCommand.__init__(self, **kwargs)

        self._commands_dir = commands_dir

    @property
    def commands_dir(self):
        return self._commands_dir

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(self.commands_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(self.commands_dir, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']

# cli = MyCLI(help='This tool\'s subcommands are loaded from a '
#                  'plugin folder dynamically.')

# if __name__ == '__main__':
#     cli()
