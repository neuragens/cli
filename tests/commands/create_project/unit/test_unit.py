import os

from click.testing import CliRunner

from cli.commands.create_project.command import CreateProjectCommand


def test_create_project():
    """[1][Command][create_project] - Download scaffolding app"""
    runner = CliRunner()

    test_path = "/tmp/neurages"
    test_name = "test-project"

    result = runner.invoke(
        CreateProjectCommand.command, ["--path", test_path, "--name", test_name]
    )

    assert result.exit_code == 0
    assert "Download the application..." in result.output
    assert f"NeuraGens create the path: {test_path}/{test_name}" in result.output
    assert (
        f"Neuragens app create successful in {test_path}/{test_name}" in result.output
    )

    assert os.path.exists(f"{test_path}/{test_name}")

    if os.path.exists(f"{test_path}/{test_name}"):
        os.rmdir(f"{test_path}/{test_name}")
    if os.path.exists(test_path):
        os.rmdir(test_path)
