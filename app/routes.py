from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from app import mongo
from app.models import User

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def home():
    return "Service is up."


@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print(username, password)

    password_hash = generate_password_hash(password)
    print(password_hash)
    user = User(username, password_hash)

    mongo.db.users.insert_one(user.to_mongo())
    return jsonify({"msg": "User registered successfully"}), 201


@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_data = mongo.db.users.find_one({"username": username})
    if not user_data or not check_password_hash(user_data['password_hash'], password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@main.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"msg": "You are viewing protected content!"}), 200
