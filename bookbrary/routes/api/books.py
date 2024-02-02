from flask import Blueprint

from bookbrary.models.books import Book
from bookbrary.schemas import books_schema


books = Blueprint(name="books", import_name=__name__, url_prefix="/api/books")

@books.route(rule="/", methods=["GET"])
def index():
    return books_schema.dump(obj=Book.query.all())
