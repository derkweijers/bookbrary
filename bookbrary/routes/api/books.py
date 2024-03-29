from flask import Blueprint, Response, request, make_response, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

from bookbrary.schemas import book_schema, books_schema
from bookbrary.services import book_service


books = Blueprint(name="books", import_name=__name__, url_prefix="/api/books")


@books.get(rule="/")
def index():
    books = book_service.get_all_books()
    return make_response(books_schema.dump(obj=books), 200)


@books.post(rule="/")
@jwt_required()
def create():
    assert request.json, {
        "message": "Missing JSON in request"
    }  # Will probably never reach this (since Flask handles this), but it makes sure that the JSON type is not None

    # Validate the data with Marshmallow and save the book to the database
    try:
        check_book_exists = book_service.get_book_by_title(
            title=request.json.get("title")
        )

        if check_book_exists:
            return make_response(jsonify({"message": "Book already exists"}), 409)

        validated_book = book_schema.load(data=request.json)
        book = book_service.create_book(**validated_book)

        return make_response(book_schema.dump(obj=book), 201)
    except ValidationError as e:
        return e.messages, 400


@books.get(rule="/<int:book_id>")
def show(book_id: int) -> Response:
    book = book_service.get_book_by_id(book_id=book_id)

    if not book:
        return make_response(jsonify({"message": "Book not found"}), 404)

    return make_response(book_schema.dump(obj=book), 200)
