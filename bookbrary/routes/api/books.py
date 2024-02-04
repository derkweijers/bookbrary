from flask import Blueprint, request, current_app as app
from marshmallow import ValidationError
from bookbrary.deps import db
from flask_jwt_extended import jwt_required

from bookbrary.models.books import Book
from bookbrary.schemas import books_schema, BookSchema, book_schema


books = Blueprint(name="books", import_name=__name__, url_prefix="/api/books")


@books.get(rule="/")
def index() -> list[BookSchema]:
    return books_schema.dump(obj=Book.query.all())


@books.post(rule="/")
@jwt_required()
def create():
    if request.json is None:
        return {"message": "Request must be in JSON format"}, 400

    # Validate the data with Marshmallow and save the book to the database
    try:
        check_book_exists = Book.query.filter_by(title=request.json["title"]).first()

        if check_book_exists:
            return {"message": "Book already exists"}, 409

        validated_book = BookSchema().load(data=request.json)
        book = Book(**validated_book)

        db.session.add(instance=book)
        db.session.commit()

        return book_schema.dump(obj=book), 201
    except ValidationError as e:
        return e.messages, 400
    except Exception as e:
        app.logger.error(msg=f"{type(e).__name__}: {e}")
        return {"message": "An error occurred while processing the request"}, 500
