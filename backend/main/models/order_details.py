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
        'order_id':self.order_id,
        'product_id':self.product_id,
        'quantity':self.quantity,
        'price':float(self.price) if self.price is not None else None,
        'subtotal':float(self.subtotal) if self.subtotal is not None else None

    }
        return product_json
    
    @staticmethod
    def from_json(product_json):
        id = product_json.get('id')
        order_id = product_json.get('order_id')
        product_id = product_json.get('product_id')
        quantity = product_json.get('quantity')
        price = product_json.get('price')
        subtotal = product_json.get('subtotal')
        
        return Order_Details(id=id,order_id=order_id,product_id=product_id,price=price,quantity=quantity
                       ,subtotal=subtotal,
                    )