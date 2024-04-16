import click
import cvScore.commands as commands


@click.group()
def cli():
    pass


cli.add_command(commands.scoreCV)
