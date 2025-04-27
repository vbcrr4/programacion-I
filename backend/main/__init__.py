from flask import Flask
from dotenv import load_dotenv

from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os

from .resources import (
    OrderResource,
    UserResource,
    UserListResource,
    OrderListResource,
    ProductListResource,
    ProductResource,
    LoginResource,
    RegisterResource,
)

api = Api()

#Inicializamos la db con sqlalchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    load_dotenv()


    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)
    

    api.add_resource(UserResource, "/users/<int:user_id>")
    api.add_resource(UserListResource, "/users")
    api.add_resource(ProductResource, "/products/<int:product_id>")
    api.add_resource(ProductListResource, "/products")
    api.add_resource(OrderResource, "/orders/<int:order_id>")
    api.add_resource(OrderListResource, "/orders")
    api.add_resource(RegisterResource, "/register")
    api.add_resource(LoginResource, "/login")
    api.init_app(app)
    return app
