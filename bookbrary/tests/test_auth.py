from flask.testing import FlaskClient

from bookbrary.models.users import User


class TestAuth:
    def test_login_invalid_credentials(self, client: FlaskClient) -> None:
        response = client.post(
            "/api/auth/login",
            json={
                "username": "testuser",
                "password": "password",
            },
        )
        assert response.status_code == 400

    def test_login_valid_credentials(self, client: FlaskClient, user: User) -> None:
        response = client.post(
            "/api/auth/login",
            json={
                "username": "testuser",
                "password": "validpassword",
            },
        )
        assert response.status_code == 200
        assert response.json
        assert "access_token" in response.json

    def test_login_no_data(self, client: FlaskClient) -> None:
        response = client.post(
            "/api/auth/login", headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 400
