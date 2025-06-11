from flask import request, jsonify, Blueprint
from .. import db
from main.models import UserModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token,set_access_cookies,get_jwt
#importar funcion de envio de mail
from main.mail.functions import sendMail

#Blueprint para acceder a los métodos de autenticación
auth = Blueprint('auth', __name__, url_prefix='/auth')

#datetime para el refresh del token
#from datetime import datetime,timedelta
#Método de logueo
#@auth.after_request
#def refresh_expiring_jwts(response):
#    try:
#        #solo refresca si la ruta es /auth/refresh
#        exp_timestamp = get_jwt()["exp"]
#        now = datetime.now()
#        target_timestamp = datetime.timestamp(now+timedelta(minutes=3))
#        print('HOLA SOY UN TESTEO DEL REFRESH')
#
#        if target_timestamp > exp_timestamp:
#            access_token = create_access_token(identity=get_jwt_identity())
#            set_access_cookies(response, access_token)
#        return response
#    except(RuntimeError,KeyError):
#        return response
@auth.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)  # Solo acepta refresh tokens
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    
    return jsonify({
        'access_token': new_access_token
    }), 200

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
    #Pasa el objeto user como identidad
    data = {
        'id': user.id,
        'email': user.email,
        'access_token': access_token
    }
    response = jsonify(data)
    set_access_cookies(response, access_token)
    #Devolver valores y token
    return response, 200

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