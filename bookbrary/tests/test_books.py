def test_get_all_books(client) -> None:
    response = client.get("/api/books/")
    assert response.status_code == 200
