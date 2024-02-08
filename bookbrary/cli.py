import click
from flask.cli import AppGroup
from bookbrary.services import user_service


user_cli = AppGroup(name="user", help="User related commands.")


@user_cli.command(name="create", help="Create a new user.")
@click.argument("username")
@click.argument("password")
def create_user(username: str, password: str) -> None:
    user_service.create_user(username=username, password=password)

    return click.echo(f"User {username} created successfully.")
