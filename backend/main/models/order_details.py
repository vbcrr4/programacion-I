from .. import db


class Order_Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id=db.Column(db.Integer,nullable=False)#Aca tiene que haber una llave externa con el id del user, no se como hacerlo
    product_id=db.Column(db.Integer,nullable=False)
    quantity=db.Column(db.Integer,nullable=False)
    price=db.Column(db.Numeric(10,2),nullable=False)
    subtotal=db.Column(db.Numeric(10,2),nullable=False)

#Este to_json hay que corregirlo
    def to_json(self):
        product_json = {
        'id': self.id,
        'user_id':self.user_id,
        'product_id':self.product_id,
        'quantity':self.quantity,
        'comment':self.price,
        'subtotal':self.subtotal

    }
        return product_json