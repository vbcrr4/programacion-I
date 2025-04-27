from .. import db


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,nullable=False)#Aca tiene que haber una llave externa con el id del user, no se como hacerlo
    message=db.Column(db.Text)
    sent_date=db.Column(db.DateTime, nullable=False,default=db.func.now())
    status = db.Column(db.Enum('pending','sent','failed'))

#Este to_json hay que corregirlo
    def to_json(self):
        product_json = {
        'id': self.id,
        'user_id':self.user_id,
        'message':self.message,
        'sent_date':self.sent_date,
        'status':self.status,

    }
        return product_json