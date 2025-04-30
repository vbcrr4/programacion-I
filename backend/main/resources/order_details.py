from flask_restful import Resource
from flask import request,jsonify
from main.models import (OrderDetailsModel)
from .. import db

class OrderDetails(Resource):
    def get(self,orderdetails_id):
        order_details = db.session.query(OrderDetailsModel).get_or_404(orderdetails_id)
        return order_details.to_json()
    
    def delete(self,orderdetails_id):
        order_details = db.session.query(OrderDetailsModel).get_or_404(orderdetails_id)
        db.session.delete(order_details)
        db.session.commit()
        return order_details.to_json(), 200  
    
    def put(self,orderdetails_id):
        order_details = db.session.query(OrderDetailsModel).get_or_404(orderdetails_id)
        data = request.get_json().items()
        for key, value in data:
            setattr(order_details, key, value)
        db.session.add(order_details)
        db.session.commit()
        return order_details.to_json(), 201
    
class OrderDetailsList(Resource):
    def get(self):
        order_details = db.session.query(OrderDetailsModel).all()
        return jsonify([order_details.to_json() for order_details in order_details])
    
    def post(self):
        orders_details = OrderDetailsModel.from_json(request.get_json())
        db.session.add(orders_details)
        db.session.commit()
        return orders_details.to_json(), 201