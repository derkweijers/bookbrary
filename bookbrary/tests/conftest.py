from typing import Any, Generator
from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner
import pytest

from bookbrary.app import create_app
from bookbrary.services import user_service, book_service
from bookbrary.deps import db
from bookbrary.models import Book, User


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


@pytest.fixture
def runner(app: Flask) -> FlaskCliRunner:
    return app.test_cli_runner()


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture()
def user(app: Flask) -> User:
    with app.app_context():
        return user_service.create_user("testuser", "validpassword")


@pytest.fixture()
def book(app: Flask) -> Book:
    with app.app_context():
        book = book_service.create_book(
            title="Test Book",
            author="Test Author",
            year=2021,
            genre="Test Genre",
            created_at="2021-01-01",
            updated_at="2021-01-01",
        )

        return book
