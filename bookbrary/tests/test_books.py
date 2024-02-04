def test_get_all_books(client) -> None:
    response = client.get("/api/books/")
    assert response.status_code == 200

def test_create_book(client, user) -> None:
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
        headers={
            "Authorization": f"Bearer {auth_response.json['access_token']}"
            },
        json={
            "title": "Test Book",
            "author": "Test Author",
            "year": "2021",
            "genre": "Test Genre",
            "created_at": "2021-01-01",
            "updated_at": "2021-01-01",
        },
    )
    assert response.status_code == 201
    assert "id" in response.json