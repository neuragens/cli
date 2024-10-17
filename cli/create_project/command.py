import click


class CreateProjectCommand:
    """Class  to command create project"""

    @staticmethod
    @click.command(name="create-project")
    @click.option("--path", default=".", help="Set Path to save project")
    def command(path):
        """Creates a new NeuraGens workspace."""
        click.echo("Download the application...")
