from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from app.config import Config

mongo = PyMongo()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    print(app.config['MONGO_URI'])
    mongo.init_app(app=app, uri=Config.MONGO_URI)
    jwt.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
