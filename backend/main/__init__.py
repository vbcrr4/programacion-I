from flask import Flask
from dotenv import load_dotenv

from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

#importar flask mail
from flask_mail import Mail

api = Api()

#Inicializamos la db con sqlalchemy
db = SQLAlchemy()
#Inicializa Migrate
migrate = Migrate()
# Inicializamos JWT de flask
jwt = JWTManager()
#inicializamos mail
mailsender = Mail()

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
    api.add_resource(resources.NotificationResource, "/notifications/<int:rating_id>")
    api.add_resource(resources.NotificationListResource, "/notifications")
    api.add_resource(resources.OrderDetailResource, "/orderdetails/<int:orderdetails_id>")
    api.add_resource(resources.OrderDetailListResource, "/orderdetails")
    api.add_resource(resources.RatingResource, "/ratings/<int:rating_id>")
    api.add_resource(resources.RatingListResource, "/ratings")
    api.init_app(app)
    #Cargar la secret key de jwt
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    #cargar el tiempo de expiración del token
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 86400
    #Configuración de cookies para refresh de JWTs
    app.config["JWT_COOKIE_SECURE"] = True
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    app.config['JWT_ACCESS_COOKIE_NAME'] = 'access_token_cookie'
    app.config['JWT_REFRESH_COOKIE_NAME'] = 'refresh_token_cookie'
    app.config['JWT_REFRESH_COOKIE_PATH'] = '/api/v1/auth/refresh'
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False #desactiva csrf protection para testing
    app.config['JWT_SESSION_COOKIE'] = False #permite cookies en multiplees rutas
    jwt.init_app(app)
    
    from main.auth import routes
    app.register_blueprint(routes.auth) 
    """Creamos carpetas del blueprint, inicializamos blueprints
    """
    #cofiguracion de mail
    app.config['MAIL_HOSTNAME'] = os.getenv('MAIL_HOSTNAME')
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['FLASKY_MAIL_SENDER'] = os.getenv('FLASKY_MAIL_SENDER')
    #inicializar en app
    mailsender.init_app(app)
    
    return app