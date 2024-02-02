def test_login_invalid_credentials(client) -> None:
    response = client.post(
        "/api/auth/login",
        json={
            "username": "testuser",
            "password": "password",
        },
    )
    assert response.status_code == 400


def test_login_valid_credentials(client, user) -> None:
    response = client.post(
        "/api/auth/login",
        json={
            "username": "testuser",
            "password": "validpassword",
        },
    )
    assert response.status_code == 200
    assert "access_token" in response.json
