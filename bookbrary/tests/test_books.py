from flask.testing import FlaskClient
import pytest
from bookbrary.models.books import Book

from bookbrary.models.users import User


class TestBooks:
    def test_get_all_books(self, client: FlaskClient) -> None:
        response = client.get("/api/books/")
        assert response.status_code == 200

    @pytest.mark.parametrize(
        "test_title,test_created_at, expected",
        [
            ("Test Book 1", "2021-01-01", 201),
            ("Test Book 2", True, 400),
            ("Test Book", "2021-01-01", 409),
        ],
    )
    def test_create_book(
        self,
        client: FlaskClient,
        user: User,
        book: Book,
        test_title,
        test_created_at,
        expected,
    ) -> None:
        auth_response = client.post(
            "/api/auth/login",
            json={
                "username": "testuser",
                "password": "validpassword",
            },
        )
        assert auth_response.status_code == 200
        assert auth_response.json
        assert auth_response.json["access_token"]

        response = client.post(
            "/api/books/",
            headers={"Authorization": f"Bearer {auth_response.json['access_token']}"},
            json={
                "title": test_title,
                "author": "Test Author",
                "year": "2021",
                "genre": "Test Genre",
                "created_at": test_created_at,
                "updated_at": "2021-01-01",
            },
        )
        assert response.status_code == expected

    def test_no_data(self, client: FlaskClient, user: User) -> None:
        auth_response = client.post(
            "/api/auth/login",
            json={
                "username": "testuser",
                "password": "validpassword",
            },
        )
        assert auth_response.status_code == 200
        assert auth_response.json
        assert auth_response.json["access_token"]

        response = client.post(
            "/api/books/",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {auth_response.json['access_token']}",
            },
        )
        assert response.status_code == 400

    # def test_get_single_book(self, client: FlaskClient, book: Book) -> None:
    #     response = client.get(f"/api/books/{book.id}")
    #     assert response.status_code == 200
