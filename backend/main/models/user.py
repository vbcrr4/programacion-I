from datetime import datetime
from .. import db
#Acá importamos werkzeug para hashear la contraseña
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False,unique=True)
    cellphone = db.Column(db.Integer,nullable=False,unique=True)
    #añadir que el mail sea unico en la DB
    email = db.Column(db.String(100),nullable=False,unique=True)
    #La pass será un hash de la contraseña en texto
    password = db.Column(db.String(255),nullable=False)
    address = db.Column(db.String(255),)
    #Agregar un Default al rol, para poder usarlo más adelante con la seguridad
    role=db.Column(db.Enum('Client','Admin', 'Empleado'), default='Client') #######ELEGIDO UN DEFAULT PARA ESTE COMMIT
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.now())

    orders = db.relationship("Order", back_populates="user",cascade="all, delete-orphan")

    @property
    def plain_password(self):
        raise AttributeError('Password cant be read')
    
    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)
    
    #Método que compara una contraseña en texto plano con el hash guardado en la db
    def validate_pass(self,password):
        return check_password_hash(self.password, password)
    """Se utilizan tokens de cookies en el front, para enviar usuario contraseña
    Cabecera: dice que tipo y algoritmo de cifrado
    Payload: contiene la info de usuario o entidad que se quiere autenticar, No mandar contraseña en el payload(NO HAY CIFRADO)
    Firma/Signature: Hash creado por la cabecera y el payload para chequear la integridad del token
    
    Como se accede a los recursos:
        El cliente envía el token(GET,POST,etc)
        Se chequea la validez del token 
        Se chequea la validez de los permisos del cliente
        El server responde"""
    
    def __repr__(self):
        return '<User: %r >' % (self.id)

    def to_json(self):
        user_json = {
        'id': self.id,
        'name':str(self.name),
        'cellphone':int(self.cellphone),
        'email':str(self.email),
        'address':str(self.address),
        'role': str(self.role),
        'is_active':self.is_active,
        'created_at':str(self.created_at.strftime("%d-%m-%Y")),
        #'created_at':self.created_at.isoformat() if self.created_at else None,
    }
        return user_json
    
    def to_json_complete(self):
        orders = [order.to_json() for order in self.orders]
        user_json = {
        'id': self.id,
        'name':str(self.name),
        'cellphone':str(self.cellphone),
        'email':str(self.email),
        'address':str(self.address),
        'role': str(self.role),
        'is_active':self.is_active,
        'created_at':str(self.created_at.strftime("%d-%m-%Y")),
        #'created_at':self.created_at.isoformat() if self.created_at else None,
        'orders':orders,}
        return user_json

    def to_json_short(self):
        user_json = {
            'id': self.id,
            'name': str(self.name),
        }
        return user_json


    @staticmethod
    def from_json(user_json):
        id = user_json.get('id')
        name = user_json.get('name')
        cellphone = user_json.get('cellphone')
        email = user_json.get('email')
        password = user_json.get('password')
        address = user_json.get('address')
        role = user_json.get('role') or 'Client'
        is_active = user_json.get('is_active') if user_json.get('is_active') is not None else True

        #No devolver al crear la contraseña en texto plano
        return User(id=id
                    ,name=name
                    ,cellphone=cellphone,
                    email=email,
                    plain_password=password,
                    address=address
                    ,role=role,
                    is_active=is_active
                    )