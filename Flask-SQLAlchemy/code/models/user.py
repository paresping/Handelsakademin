import sqlite3
from db import db


# Below is a sort of API that exposes two endpoints/methods/interfaces
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)  # Id is automatically generated and added to the object
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()  # return an UserModel object

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()  # return an UserModel object
