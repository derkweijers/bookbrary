from flask import Flask
from bookbrary.models import Book, User
from bookbrary.services import user_service, book_service


class TestService:
    def test_create_user_service(self, app: Flask) -> None:
        with app.app_context():
            user = user_service.create_user("testuser", "testpassword")
            assert user.username == "testuser"
            assert user.password != "testpassword"

    def test_get_user_by_username(self, app: Flask, user: User) -> None:
        with app.app_context():
            user_from_database = user_service.get_user_by_username("testuser")
            if user_from_database:
                assert user_from_database.username == "testuser"


class TestBookService:
    def test_create_book_service(self, app: Flask) -> None:
        with app.app_context():
            book = book_service.create_book(
                title="Test Book",
                author="Test Author",
                year=2021,
                genre="Test Genre",
                created_at="2021-01-01",
                updated_at="2021-01-01",
            )
            assert book.title == "Test Book"
            assert book.author == "Test Author"
            assert book.year == 2021
            assert book.genre == "Test Genre"
            assert book.created_at == "2021-01-01"
            assert book.updated_at == "2021-01-01"

    def test_get_book_by_title(self, app: Flask, book: Book) -> None:
        with app.app_context():
            book_from_database = book_service.get_book_by_title("Test Book")
            if book_from_database:
                assert book_from_database.title == "Test Book"
                assert book_from_database.author == "Test Author"
                assert book_from_database.year == 2021
                assert book_from_database.genre == "Test Genre"
                assert book_from_database.created_at == "2021-01-01"
                assert book_from_database.updated_at == "2021-01-01"

    def test_get_all_books(self, app: Flask, book: Book) -> None:
        with app.app_context():
            books = book_service.get_all_books()
            assert len(books) == 1

    def test_get_book_by_id(self, app: Flask, book: Book) -> None:
        with app.app_context():
            book_from_database = book_service.get_book_by_id(book.id)
            if book_from_database:
                assert book_from_database.title == "Test Book"
                assert book_from_database.author == "Test Author"
                assert book_from_database.year == 2021
                assert book_from_database.genre == "Test Genre"
                assert book_from_database.created_at == "2021-01-01"
                assert book_from_database.updated_at == "2021-01-01"
