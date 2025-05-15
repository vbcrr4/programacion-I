from datetime import datetime
from .. import db
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)#Aca tiene que haber una llave externa con el id del user, no se como hacerlo
    created_at = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.Enum('pending','preparing','ready','delivered','canceled'))
    total = db.Column(db.Float,nullable=False)
    user = db.relationship("User", back_populates="orders")


    def __repr__(self):
        return '<Order:%r User: %r >' % (self.id,self.user_id)

    def to_json(self):
        order_json = {
        'id': self.id,
        'user_id':self.user_id,
        'created_at':self.created_at.isoformat() if self.created_at else None,
        'status':self.status,
        'total':self.total,

    }
        return order_json
    
    def to_json_complete(self):
        order_json={
        'id': self.id,
        'user_id':self.user_id,
        'created_at':self.created_at.isoformat() if self.created_at else None,
        'status':self.status,
        'total':self.total,
        'user':self.user.to_json(),
        }

        return order_json
    
    def to_json_short(self):
        order_json = {
            'id': self.id,
            'status': str(self.status),
        }
        return order_json
    @staticmethod
    def from_json(order_json):
        id = order_json.get('id')
        user_id = order_json.get('user_id')
        created_at = order_json.get('created_at')
        status = order_json.get('status')
        total = order_json.get('total')


        return Order(id=id,user_id=user_id,created_at=created_at,status=status,total=total
                    )