from flask.testing import FlaskCliRunner
from bookbrary.cli import create_user


def test_create_user(runner: FlaskCliRunner):
    result = runner.invoke(create_user, ["testuser", "testpassword"])

    assert result.exit_code == 0
    assert "User testuser created successfully." in result.output
