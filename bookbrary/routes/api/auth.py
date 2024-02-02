from flask import Blueprint, make_response, Response, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from bookbrary.models.users import User

auth = Blueprint(name="auth", import_name=__name__, url_prefix="/api/auth")


@auth.post(rule="/login")
def login() -> Response:
    if not request.json:
        return make_response(jsonify({"msg": "Missing JSON in request"}), 400)
    

    username = request.json.get("username")
    password = request.json.get("password")

    check_for_user = User.query.filter_by(username=username).first()

    if not check_for_user or not check_password_hash(pwhash=check_for_user.password, password=password):
        return make_response(jsonify({"msg": "Invalid credentials"}), 400)

    access_token = create_access_token(identity=username)
    return make_response(jsonify(access_token=access_token), 200)
