import platform

import click
import pkg_resources


class VersionCommand:
    """Class Version Command"""

    @staticmethod
    @click.command(name="version")
    def command():
        """Outputs NeuraGens CLI version."""
        version_info = pkg_resources.get_distribution("neuragens-cli").version
        click.echo(f"""
\033[32m  _   _                       _____
 | \\ | |                     / ____|
 |  \\| | ___ _   _ _ __ __ _| |  __  ___ _ __  ___
 | . ` |/ _ \\ | | | '__/ _` | | |_ |/ _ \\ '_ \\/ __|
 | |\\  |  __/ |_| | | | (_| | |__| |  __/ | | \\__ \\
 |_| \\_|\\___|\\__,_|_|  \\__,_|\\_____|\___|_| |_|___/
\033[0m
NeuraGens CLI: {version_info}
Python: {platform.python_version()}
OS: {platform.system()} {platform.release()}
""")
