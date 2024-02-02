from bookbrary.deps import ma

from bookbrary.models.books import Book as BookModel


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel


book_schema = BookSchema()
books_schema = BookSchema(many=True)
