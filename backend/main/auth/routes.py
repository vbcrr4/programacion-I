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
    refresh_token = create_refresh_token(identity=user)

    #Pasa el objeto user como identidad
    data = {
        'id': user.id,
        'email': user.email,
        'access_token': access_token,
        'refresh_token': refresh_token
    }
    response = jsonify(data)
    set_access_cookies(response, access_token)

    #Devolver valores y token
    return response, 200


@auth.route('/refresh', methods=['POST'])
def refresh(refresh=True):
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)


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