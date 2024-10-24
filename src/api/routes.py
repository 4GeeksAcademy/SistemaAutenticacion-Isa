"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


#Funcion de registro de usuario
@api.route('/register', methods=['POST'])
def register():
    request_body= request.get_json()
    if request_body is None:
        return jsonify({"msg": "JSON no encontrado"}), 400
    if "email" not in request_body:
        return jsonify({"msg": "Falta el campo e-mail"}), 400
    if "password" not in request_body:
        return jsonify({"msg": "Falta el campo contraseña"}), 400
    user = User()
    user.create_user(request_body["email"],request_body["password"])
    return jsonify(user.serialize()), 200

#Funcion de login
@api.route('/login', methods=['POST'])
def login():
    request_body= request.get_json()
    if request_body is None:
        return jsonify({"msg": "JSON no encontrado"}), 400
    if "email" not in request_body:
        return jsonify({"msg": "Falta el campo e-mail"}), 400
    if "password" not in request_body:
        return jsonify({"msg": "Falta el campo contraseña"}), 400
    
    user = User.query.filter_by(email=request_body["email"]).first()
     
    if user and user.check_password(request_body["password"]) is True:
        access_token = create_access_token(identity=user.serialize())

        return jsonify({"msg": "Te has logueado", "user": user.serialize(), "access_token": access_token}), 200
    else:
        return jsonify({"msg": "email o contraseña incorrectos"}), 401