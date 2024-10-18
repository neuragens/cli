import os
from unittest import mock

import pytest
from click.testing import CliRunner

from cli.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


@mock.patch("os.makedirs")
def test_create_project_integration(mock_makedirs, runner):
    """Integration test for the create_project command"""

    result = runner.invoke(cli, ["create-project", "--path", "/tmp/project"])

    assert result.exit_code == 0
    assert "Download the application..." in result.output

    mock_makedirs.assert_called_once_with("/tmp/project", exist_ok=True)

    assert not os.path.exists("/tmp/project")
