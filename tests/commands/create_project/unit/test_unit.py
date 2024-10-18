from click.testing import CliRunner

from cli.commands.create_project.command import CreateProjectCommand


def test_create_project():
    """[1][Command][create_project] - Download scaffolding app"""
    runner = CliRunner()
    result = runner.invoke(CreateProjectCommand.command, ["--path", "/tmp/neurages"])
    assert result.exit_code == 0
    assert "Download the application..." in result.output
