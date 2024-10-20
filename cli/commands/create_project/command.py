import os

import click


class CreateProjectCommand:
    """Class  to command create project"""

    @staticmethod
    @click.command(name="new")
    @click.option("--path", default=".", help="Set Path to save project")
    @click.option("--name", help="Set Name your project", required=True, type=str)
    def command(path, name):
        """Creates a new NeuraGens workspace."""
        click.echo("Download the application...")

        full_path = f"{path}/{name}"
        if path != ".":
            click.secho(f"NeuraGens create the path: {full_path}", fg="green")
            os.makedirs(full_path, exist_ok=True)
        else:
            click.echo("2")

        click.echo(f"Neuragens app create successful in {full_path}")
