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
# Inicializa la API
api = Api()

#Inicializamos la db con sqlalchemy
db = SQLAlchemy()

def create_app():                   # Configura el entorno y usa dotenv para cargar configuraciones sensibles
    app = Flask(__name__)
    load_dotenv()


    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_USI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME') # Aca configuramos la DB en este caso SQL lite
    db.init_app(app)
    

    api.add_resource(UserResource, "/users/<int:id>")
    api.add_resource(ProductResource, "/products/<int:id>")
    api.add_resource(ProductListResource, "/products")
    api.add_resource(OrderResource, "/orders/<int:id>")         # Todo esto define las rutas de la API y las vincula a clases en resources.py
    api.add_resource(OrderListResource, "/orders")
    api.add_resource(RegisterResource, "/register")
    api.add_resource(LoginResource, "/login")
    api.init_app(app)
    return app


# Este archivo en teoria es el corazon del backend. Se encarga de Ensamblar la app Flask. Configura la base de datos. Registra los endpoints y garantiza el funcionamiento