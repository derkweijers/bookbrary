from flask.testing import FlaskClient
import pytest


def test_get_all_books(client: FlaskClient) -> None:
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
def test_create_book(client: FlaskClient, user, book, test_title, test_created_at, expected) -> None:
    auth_response = client.post(
        "/api/auth/login",
        json={
            "username": "testuser",
            "password": "validpassword",
        },
    )
    assert auth_response.status_code == 200
    assert "access_token" in auth_response.json

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


def test_no_data(client: FlaskClient, user) -> None:
    auth_response = client.post(
        "/api/auth/login",
        json={
            "username": "testuser",
            "password": "validpassword",
        },
    )
    response = client.post(
        "/api/books/",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth_response.json['access_token']}",
        },
    )
    assert response.status_code == 400
