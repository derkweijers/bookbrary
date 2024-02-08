from bookbrary.models import Book
from bookbrary.deps import db


class BookService:
    def create_book(
        self,
        title: str,
        author: str,
        year: int,
        genre: str,
        created_at: str,
        updated_at: str,
    ) -> Book:
        book = Book()
        book.title = title
        book.author = author
        book.year = year
        book.genre = genre
        book.created_at = created_at
        book.updated_at = updated_at

        db.session.add(instance=book)
        db.session.commit()

        return book

    def get_all_books(self) -> list[Book]:
        return Book.query.all()

    def get_book_by_title(self, title: str) -> Book | None:
        return Book.query.filter_by(title=title).first()

    def get_book_by_id(self, book_id: int) -> Book | None:
        return Book.query.filter_by(id=book_id).first()
