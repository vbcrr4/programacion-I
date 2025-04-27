from .. import db

class Product(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    description = db.Column(db.Text)
    price=db.Column(db.DECIMAL(10,2))
    available = db.Column(db.Boolean, default=False)
    category=db.Column(db.String(50),nullable=False)
    image_url=db.Column(db.String(255),nullable=False)
    popularity=db.Column(db.Integer)

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