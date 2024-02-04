from typing import Any, Generator
from flask import Flask
from flask.testing import FlaskClient
import pytest

from bookbrary.app import create_app
from bookbrary.services import user_service
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
        book = Book()
        book.title = "Test Book"
        book.author = "Test Author"
        book.year = 2021
        book.genre = "Test Genre"
        book.created_at = "2021-01-01"
        book.updated_at = "2021-01-01"

        db.session.add(instance=book)
        db.session.commit()

        return book
