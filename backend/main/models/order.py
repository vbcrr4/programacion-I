from .. import db
from user import User
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column()#Aca tiene que haber una llave externa con el id del user, no se como hacerlo
    created_at = db.Column(db.DateTime, default=db.func.now())
    is_active = db.Column(db.Boolean, default=True)
    available = db.Column()

#Este to_json hay que corregirlo
    def to_json(self):
        product_json = {
        'id': self.id,
        'Name':self.name,
        'Description':self.description,
        'Price':self.price,
        'Available':self.available,
        'Category': self.category,
        'Image_url':self.image_url,
        'Popularity':self.popularity,
    }
        return product_json