from datetime import datetime
from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False,unique=True)
    cellphone = db.Column(db.String(20),nullable=False,unique=True)
    email = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(255),nullable=False)
    address = db.Column(db.String(255),)
    role=db.Column(db.Enum('Client','Admin'))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.now())

    orders = db.relationship("Order", back_populates="user",cascade="all, delete-orphan")                   # Relacion de 1 : n
    notification = db.relationship("notification",back_populates="user",cascade="all, delete-orphan")         # Relacion de 1: n Creo que hay que meterla en la rama relaciones



    def to_json(self):
        user_json = {
        'id': self.id,
        'name':self.name,
        'cellphone':self.cellphone,
        'email':self.email,
        'password':self.password,
        'address':self.address,
        'role': self.role,
        'is_active':self.is_active,
        'created_at':self.created_at.isoformat() if self.created_at else None,
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
        role = user_json.get('role')
        is_active = user_json.get('is_active')
        created_at = user_json.get('created_at')
        return User(id=id,name=name,cellphone=cellphone,email=email,password=password,address=address,role=role,is_active=is_active,
                    created_at=created_at
                    )
    
    