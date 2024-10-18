import click
from click_aliases import ClickAliasedGroup

from cli.commands.create_project.command import CreateProjectCommand
from cli.commands.version.command import VersionCommand


@click.group(cls=ClickAliasedGroup)
def cli():
    """Cli NeuraGens Frameworks"""


cli.add_command(CreateProjectCommand.command)
cli.add_command(VersionCommand.command, aliases=["v"])

if __name__ == "__main__":
    cli()
