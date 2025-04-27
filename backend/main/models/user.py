from multiprocessing.util import is_abstract_socket_namespace
from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False,unique=True)
    cellphone = db.Column(db.String(20),nullable=False,unique=True)
    email = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(255),nullable=False)
    address = db.Column(db.String(255))
    role=db.Column(db.Enum('Client','Admin'))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def to_json(self):
        user_json = {
        'id': self.id,
        'name':self.name,
        'cellphone':self.cellphone,
        'email':self.email,
        'password':self.password,
        'role': self.role,
        'is_active':self.is_active,
        'created_at':self.created_at,
    }
        return user_json
    
    @staticmethod
    def from_json(user_json):
        id = user_json.get('id')
        name = user_json.get('name')
        cellphone = user_json.get('cellphone')
        email = user_json.get('email')
        password = user_json.get('password')
        role = user_json.get('role')
        is_active = user_json.get('is_active')
        created_at = user_json.get('created_at')
        return User(id=id,name=name,cellphone=cellphone,email=email,password=password,role=role,is_active=is_active,
                    created_at=created_at
                    )