from flask_pymongo import ObjectId


class User:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

    @staticmethod
    def from_mongo(data):
        return User(username=data.get('username'), password_hash=data.get('password_hash'))

    def to_mongo(self):
        return {
            "username": self.username,
            "password_hash": self.password_hash
        }
