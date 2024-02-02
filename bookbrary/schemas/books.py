from bookbrary.deps import ma

from bookbrary.models.books import Book as BookModel

class Book(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel


book_schema = Book()
books_schema = Book(many=True)
