from flask import Flask
from dotenv import load_dotenv

from flask_restful import Api

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


def create_app():
    app = Flask(__name__)
    load_dotenv()

    api.add_resource(UserResource, "/users/<int:id>")
    api.add_resource(ProductResource, "/products/<int:id>")
    api.add_resource(ProductListResource, "/products")
    api.add_resource(OrderResource, "/orders/<int:id>")
    api.add_resource(OrderListResource, "/orders")
    api.add_resource(RegisterResource, "/register")
    api.add_resource(LoginResource, "/login")
    api.init_app(app)
    return app
