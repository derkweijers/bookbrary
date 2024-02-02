from os import path
from flask import Flask

from bookbrary.deps import ma, db, migrate, jwt
from bookbrary.models import *  # noqa - needed to detect migrations

from bookbrary.routes.api import books as books_blueprint, auth as auth_blueprint
from bookbrary.cli import user_cli


def create_app() -> Flask:
    app = Flask(import_name=__name__)
    app.config.from_prefixed_env()

    # Initialize extensions
    db.init_app(app=app)
    ma.init_app(app=app)
    migrate.init_app(
        app=app, db=db, directory=path.join(path.dirname(__file__), "migrations")
    )

    jwt.init_app(app=app)

    # Register blueprints
    app.register_blueprint(blueprint=auth_blueprint)
    app.register_blueprint(blueprint=books_blueprint)

    app.cli.add_command(cmd=user_cli)

    return app
