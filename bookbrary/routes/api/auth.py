from flask import Blueprint, make_response, Response, request, jsonify
from flask_jwt_extended import create_access_token

auth = Blueprint(name="auth", import_name=__name__, url_prefix="/api/auth")


@auth.post(rule="/login")
def login() -> Response:
    if not request.json:
        return make_response(jsonify({"msg": "Missing JSON in request"}), 400)

    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username != "test" or password != "test":
        return make_response(jsonify({"msg": "Bad username or password"}), 401)
    
    access_token = create_access_token(identity=username)
    return make_response(jsonify(access_token=access_token), 200)