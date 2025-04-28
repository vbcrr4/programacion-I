from datetime import datetime
from .. import db


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,nullable=False)#Aca tiene que haber una llave externa con el id del user, no se como hacerlo
    product_id=db.Column(db.Integer,nullable=False)
    rating=db.Column(db.Integer,nullable=False)
    comment=db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now())

#Este to_json hay que corregirlo
    def to_json(self):
        rating_json = {
        'id': self.id,
        'user_id':self.user_id,
        'product_id':self.product_id,
        'rating':float(self.rating) if self.rating is not None else None,
        'comment':self.comment,
        'created_at':self.created_at.isoformat() if self.created_at else None

    }
        return rating_json
    
    @staticmethod
    def from_json(rating_json):
        id = rating_json.get('id')
        user_id = rating_json.get('user_id')
        product_id = rating_json.get('product_id')
        rating = rating_json.get('rating')
        comment = rating_json.get('comment')
        created_at = rating_json.get('created_at')


        return Rating(id=id,user_id=user_id,product_id=product_id,rating=rating,comment=comment
                       ,created_at=created_at
                    )