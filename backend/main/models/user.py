from email.policy import default
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
        'Name':self.name,
        'Cellphone':self.cellphone,
        'Email':self.email,
        'Password':self.password,
        'Role': self.role,
        'is_active':self.is_active,
        'Created_at':self.created_at,
    }
        return user_json