from flask.testing import FlaskClient


def test_login_invalid_credentials(client: FlaskClient) -> None:
    response = client.post(
        "/api/auth/login",
        json={
            "username": "testuser",
            "password": "password",
        },
    )
    assert response.status_code == 400


def test_login_valid_credentials(client: FlaskClient, user) -> None:
    response = client.post(
        "/api/auth/login",
        json={
            "username": "testuser",
            "password": "validpassword",
        },
    )
    assert response.status_code == 200
    assert "access_token" in response.json


def test_login_no_data(client: FlaskClient) -> None:
    response = client.post(
        "/api/auth/login", headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 400
