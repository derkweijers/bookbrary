from typing import Any, Generator
from flask import Flask
from flask.testing import FlaskClient
import pytest
from bookbrary.app import create_app
from bookbrary.services import user_service
from bookbrary.deps import db


@pytest.fixture
def app() -> Generator[Flask, Any, None]:
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture()
def user(app: Flask) -> Any:
    with app.app_context():
        return user_service.create_user("testuser", "validpassword")
