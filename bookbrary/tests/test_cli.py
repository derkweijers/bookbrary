from flask.testing import FlaskCliRunner
from bookbrary.cli import create_user


class TestCli:
    def test_create_user(self, runner: FlaskCliRunner) -> None:
        result = runner.invoke(cli=create_user, args=["testuser", "testpassword"])

        assert result.exit_code == 0
        assert "User testuser created successfully." in result.output
