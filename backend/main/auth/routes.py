from flask import request, jsonify, Blueprint
from .. import db
from main.models import UserModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

#Blueprint para acceder a los métodos de autenticación
auth = Blueprint('auth', __name__, url_prefix='/auth')

#Método de logueo
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
        'id': str(user.id),
        'email': user.email,
        'access_token': access_token
    }

    #Devolver valores y token
    return data, 200

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
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return user.to_json() , 201