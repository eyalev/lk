
import click


@click.command('example2')
@click.option('--project-id', required=True)
def cli(project_id):

    print('Another command')
    print(project_id)

