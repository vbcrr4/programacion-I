import os
from flask import Flask
from dotenv import load_dotenv

from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

api = Api()

#Inicializamos la db con sqlalchemy
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    load_dotenv()


    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)
    migrate.init_app(app,db)
    
    import main.resources as resources
    api.add_resource(resources.UserResource, "/users/<int:user_id>")
    api.add_resource(resources.UserListResource, "/users")
    api.add_resource(resources.ProductResource, "/products/<int:product_id>")
    api.add_resource(resources.ProductListResource, "/products")
    api.add_resource(resources.OrderResource, "/orders/<int:order_id>")
    api.add_resource(resources.OrderListResource, "/orders")
    api.add_resource(resources.RegisterResource, "/register")
    api.add_resource(resources.LoginResource, "/login")
    api.add_resource(resources.NotificationResource, "/notifications/<int:rating_id>")
    api.add_resource(resources.NotificationListResource, "/notifications")
    api.add_resource(resources.OrderDetailResource, "/orderdetails/<int:orderdetails_id>")
    api.add_resource(resources.OrderDetailListResource, "/orderdetails")
    api.add_resource(resources.RatingResource, "/ratings/<int:rating_id>")
    api.add_resource(resources.RatingListResource, "/ratings")

    #app.register_blueprint(routes.auth) 
    """Creamos carpetas del blueprint, inicializamos blueprints
    """
    
    api.init_app(app)

    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCES_TOKEN_EXPIRES'] = os.getenv['JWT_ACCES_TOKEN_EXPIRES']
    jwt.init_app(app)
    from main.auth import routes

    app.register_blueprint(routes.auth)




    return app