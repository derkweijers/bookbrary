from typing import Any, Generator
from flask import Flask
import pytest
from bookbrary.app import create_app
from bookbrary.services import user_service


@pytest.fixture
def app() -> Generator[Flask, Any, None]:
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def user(app) -> Any:
    with app.app_context():
        return user_service.create_user("testuser", "validpassword")
