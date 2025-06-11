from flask import request, jsonify, Blueprint
from .. import db
from main.models import UserModel
from flask_jwt_extended import create_access_token,set_access_cookies,create_refresh_token,get_jwt_identity,get_jwt
from datetime import datetime,timedelta
#importar funcion de envio de mail
from main.mail.functions import sendMail

#Blueprint para acceder a los métodos de autenticación
auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['POST'])
def login():
    #Busca al user en la db por mail
    user = db.session.query(UserModel).filter(UserModel.email == request.get_json().get("email")).first()
    ## Devuelvo error si no existe el user o si la contraseña no coincide
    if (user is None) or not (user.validate_pass(request.get_json().get("password"))):
        #print(user.validate_pass(request.get_json().get("password"))) DEBUGGEO
        return 'Invalid user or password', 401 
    #Valida la contraseña
    # if user.validate_pass(request.get_json().get("password")):
    #Genera un nuevo token
    access_token = create_access_token(identity=user)
    print('ACCESSTOKEN: ',access_token)
    #Pasa el objeto user como identidad
    data = {
        'id': user.id,
        'email': user.email,
        'access_token': access_token,
    }
    response = jsonify(data)
    set_access_cookies(response, access_token)
    print('SET_ACCESS_COOKIES: ',set_access_cookies(response,access_token))
    #Devolver valores y token
    return response, 200

@auth.after_request
def refresh_expiring_jwts(response):
    print('REFRESH CHECK AFTER REQUEST')
    if request.path == '/auth/login':
        return response
    try:
        expiracion_timestamp = get_jwt()["exp"]
        now = datetime.now()
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > expiracion_timestamp:
            user = db.session.query(UserModel).filter(UserModel.id == get_jwt_identity()).first()
            access_token = create_access_token(identity=user)
            print(access_token)
            set_access_cookies(response, access_token)
            print(set_access_cookies(response,access_token))
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response

#Método de registro
@auth.route('/register', methods=['POST'])
def register():
    #Obtener user
    user = UserModel.from_json(request.get_json())
    #Verificar si el mail ya existe en la db, scalar() para saber la cantidad de ese email
    exists = db.session.query(UserModel).filter(UserModel.email == user.email).scalar() is not None
    if exists:
        return 'Duplicated mail', 409
    else:
        try:
            #Agregar user a DB
            db.session.add(user)
            db.session.commit()
            #Enviar mail de bienvenida
            send = sendMail([user.email],"Bienvenido/a", 'register', user = user)
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return user.to_json() , 201