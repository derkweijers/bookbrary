from os import path
from flask import Flask

from bookbrary.deps import ma,db,migrate

from bookbrary.routes.api import books as books_blueprint

def create_app() -> Flask:
    app = Flask(import_name=__name__)
    app.config.from_prefixed_env()

    # Initialize extensions
    db.init_app(app=app)
    ma.init_app(app=app)
    migrate.init_app(app=app,db=db, directory=path.join(path.dirname(__file__), 'migrations'))
    from bookbrary.models import books  # noqa: F401 - Needed to register models

    # Register blueprints
    app.register_blueprint(blueprint=books_blueprint)

    return app
