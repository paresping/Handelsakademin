from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.item import Item, ItemList

from security import authenticate, identity
from resources.user import UserRegister
from db import db
from resources.store import Store, StoreList


app = Flask(__name__)  # instantiate app object
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Turn off Flask modification tracker to save resources
app.secret_key = 'jose'
api = Api(app)  # instantiate API object


@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # create a new endpoint /auth and call functions for authentication

# add the resources to the api object and define how they are going to be accessed
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')  # access via http://127.0.0.1:5000/item/<name>
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

# run the app in debug mode
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
