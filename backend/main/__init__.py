from flask import Flask
from dotenv import load_dotenv

from flask_restful import Api
import os
from flask_sqlalchemy import SQLAlchemy

from resources import (
    OrderResource,
    UserResource,
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
    app.config['SQLALCHEMY_DATABASE_USI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)
    

    api.add_resource(UserResource, "/users/<int:id>")
    api.add_resource(ProductResource, "/products/<int:id>")
    api.add_resource(ProductListResource, "/products")
    api.add_resource(OrderResource, "/orders/<int:id>")
    api.add_resource(OrderListResource, "/orders")
    api.add_resource(RegisterResource, "/register")
    api.add_resource(LoginResource, "/login")
    api.init_app(app)
    return app
