from .. import db


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,nullable=False)#Aca tiene que haber una llave externa con el id del user, no se como hacerlo
    product_id=db.Column(db.Integer,nullable=False)
    rating=db.Column(db.Text)
    comment=db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.now())

#Este to_json hay que corregirlo
    def to_json(self):
        product_json = {
        'id': self.id,
        'user_id':self.user_id,
        'product_id':self.product_id,
        'rating':self.rating,
        'comment':self.comment,
        'created_at':self.created_at,

    }
        return product_json