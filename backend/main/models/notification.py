from datetime import datetime
from .. import db
from . import UserModel


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)#Aca tiene que haber una llave externa con el id del user, no se como hacerlo
    message=db.Column(db.Text)
    sent_date=db.Column(db.DateTime, nullable=False,default=datetime.now())
    status = db.Column(db.Enum('pending','sent','failed'))


    def __repr__(self):
        return '<Notification: %r User: %r Message: %r >' % (self.id,self.user_id,self.message)

#Este to_json hay que corregirlo
    def to_json(self):
        product_json = {
        'id': self.id,
        'user_id':self.user_id,
        'message':str(self.message),
        'created_at':str(self.sent_date.strftime("%H:%M%S %d-%m-%Y")),
        'status':str(self.status),

    }
        return product_json
    
    def to_json_short(self):
        notification_json = {
            'id': self.id,
            'message':str(self.message)
        }
        return notification_json
    @staticmethod
    def from_json(product_json):
        id = product_json.get('id')
        user_id = product_json.get('user_id')
        message = product_json.get('message')
        sent_date = datetime.strptime(product_json.get('sent_date'),"%H:%M%S %d-%m-%Y")
        status = product_json.get('status')

        return Notification(id=id,user_id=user_id,message=message,sent_date=sent_date,status=status)