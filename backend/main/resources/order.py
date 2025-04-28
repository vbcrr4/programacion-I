from flask_restful import Resource
from flask import request,jsonify
from main.models import (OrderModel)
from .. import db

#ORDERS = {
#    1: {
#        "user_id": 1,
#        "created_at": "2025-02-01",
#        "status": "delivered",
#        "total": 10000,
#    },
#    2: {
#        "user_id": 2,
#        "created_at": "2025-02-01",
#        "status": "delivered",
#        "total": 20000,
#    },
#    3: {
#        "user_id": 3,
#        "created_at": "2025-02-01",
#        "status": "delivered",
#        "total": 30000,
#    },
#}


class Order(Resource):
    def get(self, order_id):
        order = db.session.query(OrderModel).get_or_404(order_id)
        return order.to_json()

    def delete(self, order_id):
        order = db.session.query(OrderModel).get_or_404(order_id)
        db.session.delete(order)
        db.session.commit()
        return order.to_json(), 200        
        
    def put(self, order_id):
        
        order = db.session.query(OrderModel).get_or_404(order_id)
        data = request.get_json().items()
        for key, value in data:
            setattr(order, key, value)
        db.session.add(order)
        db.session.commit()
        return order.to_json(), 201
        
class OrderList(Resource):
    def get(self):
        orders = db.session.query(OrderModel).all()
        return jsonify([order.to_json() for order in orders])

    def post(self):
        order = OrderModel.from_json(request.get_json())
        db.session.add(order)
        db.session.commit()
        return order.to_json(), 201