
import click

from lk.helpers.global_context import app_context


def app_confirm(message, default=True):

    if app_context.skip_confirm:
        return True

    confirm = click.confirm(message, default)

    return confirm
