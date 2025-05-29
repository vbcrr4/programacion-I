from flask_restful import Resource
from flask import request,jsonify
from sqlalchemy import func
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
        page = 1
        per_page = 10
        order_details = db.session.query(OrderDetailsModel)
        if request.args.get('page'):
            page=int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page=int(request.args.get('per_page'))
        ##FILTROS
        #Filtrar por id de orden
        
        order_id = request.args.get('order_id')
        if order_id:
            order_id=int(order_id)
            order_details = order_details.filter(OrderDetailsModel.order_id == order_id)
        #Filtrar por id de producto
        product_id = request.args.get('product_id')
        if product_id:
            product_id=int(product_id)
            order_details = order_details.filter(OrderDetailsModel.product_id == product_id)

        # Filtrar por cantidad de productos o menos
        nrquantity = request.args.get('nrquantity')
        if nrquantity:
            order_details=order_details.group_by(OrderDetailsModel.quantity).having(func.count(OrderDetailsModel.quantity)<= int(nrquantity))
        #filtrar por
        maxprice =request.args.get('price')
        if maxprice:
            order_details = order_details.order_by(OrderDetailsModel.price <= maxprice)

        order_details = order_details.paginate(page=page, per_page=per_page, error_out=False)

        return jsonify({'order_details':[order_detail.to_json() for order_detail in order_details],
                        'total' : order_details.total,
                        'pages' : order_details.pages,
                        'page' : page})
    
    def post(self):
        orders_details = OrderDetailsModel.from_json(request.get_json())
        db.session.add(orders_details)
        db.session.commit()
        return orders_details.to_json(), 201