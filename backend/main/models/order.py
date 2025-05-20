from datetime import datetime
from .. import db
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,db.ForeingKey('user.id'),nullable=False)#Aca tiene que haber una llave externa con el id del user, no se como hacerlo
    created_at = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.Enum('pending','preparing','ready','delivered','canceled'))
    total = db.Column(db.Float,nullable=False)

    def to_json(self):
        product_json = {
        'id': self.id,
        'user_id':self.user_id,
        'created_at':self.created_at.isoformat() if self.created_at else None,
        'status':self.status,
        'total':self.total,

    }
        return product_json
    @staticmethod
    def from_json(product_json):
        id = product_json.get('id')
        user_id = product_json.get('user_id')
        created_at = product_json.get('created_at')
        status = product_json.get('status')
        total = product_json.get('total')


        return Order(id=id,user_id=user_id,created_at=created_at,status=status,total=total
                    )