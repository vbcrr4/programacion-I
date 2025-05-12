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
    
    def __repr__(self):
        return '<Product: %r Name: %r >' % (self.id,self.name)

    def to_json(self):
        product_json = {
        'id': self.id,
        'name':self.name,
        'description':self.description,
        'price':int(self.price) if self.price is not None else None,
        'available':self.available,
        'category': self.category,
        'image_url':self.image_url,
        'popularity':int(self.popularity)if self.price is not None else None,
    }
        return product_json
    def to_json_short(self):
        product_json = {
            'id': self.id,
            'name': str(self.name),
        }
        return product_json
    @staticmethod
    def from_json(product_json):
        id = product_json.get('id')
        name = product_json.get('name')
        description = product_json.get('description')
        price = product_json.get('price')
        available = product_json.get('available')
        category = product_json.get('category')
        image_url = product_json.get('image_url')
        popularity = product_json.get('popularity')

        return Product(id=id,name=name,description=description,price=price,available=available
                       ,category=category,image_url=image_url,popularity=popularity
                    )