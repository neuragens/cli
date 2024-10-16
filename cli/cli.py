import click
import pkg_resources
import platform

@click.group()
def cli():
    """Cli NeuraGen Framework"""


@click.command()
@click.option('--path', default='.', help='Set Path to save project')
def create_project(path):
    """Creates a new NeuraGens workspace."""
    click.echo("Download the application...")

cli.add_command(create_project)

@cli.command()
def version():
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

if __name__ == '__main__':
    cli()

