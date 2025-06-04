from .. import db


class Order_Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id=db.Column(db.Integer, db.ForeignKey('order.id'),nullable=False)
    product_id=db.Column(db.Integer,db.ForeignKey('product.id'),nullable=False)
    quantity=db.Column(db.Integer,nullable=False)
    price=db.Column(db.Numeric(10,2),nullable=False)
    subtotal=db.Column(db.Numeric(10,2),nullable=False)

    order = db.relationship('Order', backref=db.backref('order_details', lazy=True))
    product = db.relationship('Product', backref=db.backref('order_details', lazy=True))

   
    def __repr__(self):
        return '<Order_Detail %r Order: %r Product %r >' % (self.id,self.order_id,self.product_id)


    def to_json(self):
        order_detail_json = {
        'id': self.id,
        'order_id':int(self.order_id),
        'product_id':int(self.product_id),
        'quantity':int(self.quantity),
        'price':(self.price) if self.price is not None else None,
        'subtotal':(self.subtotal) if self.subtotal is not None else None

    }
        return order_detail_json
    
    def to_json_complete(self):
        order_details_json={
        'id': self.id,
        'order_id':int(self.order_id),
        'product_id':int(self.product_id),
        'quantity':int(self.quantity),
        'price':(self.price) if self.price is not None else None,
        'subtotal':(self.subtotal) if self.subtotal is not None else None,
        'order':self.order.to_json(),
        'product':self.product.to_json()

        }

        return order_details_json  
    
    def to_json_short(self):
        order_details_json = {
            'id': self.id,
            'product':int(self.product_id)
        }
        return order_details_json
    @staticmethod
    def from_json(order_detail_json):
        id = order_detail_json.get('id')
        order_id = order_detail_json.get('order_id')
        product_id = order_detail_json.get('product_id')
        quantity = order_detail_json.get('quantity')
        price = order_detail_json.get('price')
        subtotal = order_detail_json.get('subtotal')
        
        return Order_Details(id=id,order_id=order_id,product_id=product_id,price=price,quantity=quantity
                       ,subtotal=subtotal,
                    )