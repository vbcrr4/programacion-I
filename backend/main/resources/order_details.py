from flask_restful import Resource
from flask import request,jsonify
from sqlalchemy import func
from main.models import (OrderDetailsModel)
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import role_required

# Recurso /order_details/<id>: operaciones sobre una línea de pedido concreta.
class OrderDetails(Resource):
    # PENDIENTE: con optional=True responde también sin token.
    @jwt_required(optional=True)
    def get(self,orderdetails_id):
        order_details = db.session.query(OrderDetailsModel).get_or_404(orderdetails_id)
        return order_details.to_json()
    
    @role_required(roles = ["Admin"])
    def delete(self,orderdetails_id):
        order_details = db.session.query(OrderDetailsModel).get_or_404(orderdetails_id)
        db.session.delete(order_details)
        db.session.commit()
        return order_details.to_json(), 200  
    
    # PENDIENTE: no tiene ninguna protección; cualquiera puede modificar una línea de pedido.
    def put(self,orderdetails_id):
        order_details = db.session.query(OrderDetailsModel).get_or_404(orderdetails_id)
        data = request.get_json().items()
        for key, value in data:
            setattr(order_details, key, value)
        db.session.add(order_details)
        db.session.commit()
        return order_details.to_json(), 201
    
# Recurso /order_details: listado (solo Admin, con filtros y paginación) y alta de líneas de pedido.
class OrderDetailsList(Resource):
    @role_required(roles = ["Admin"])
    def get(self):
        page = 1
        per_page = 10
        order_details = db.session.query(OrderDetailsModel)
        if request.args.get('page'):
            page=int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page=int(request.args.get('per_page'))
        # Filtros opcionales por query string: order_id, product_id, nrquantity y price
        
        order_id = request.args.get('order_id')
        if order_id:
            order_id=int(order_id)
            order_details = order_details.filter(OrderDetailsModel.order_id == order_id)
        product_id = request.args.get('product_id')
        if product_id:
            product_id=int(product_id)
            order_details = order_details.filter(OrderDetailsModel.product_id == product_id)

        nrquantity = request.args.get('nrquantity')
        if nrquantity:
            order_details=order_details.group_by(OrderDetailsModel.quantity).having(func.count(OrderDetailsModel.quantity)<= int(nrquantity))
        maxprice =request.args.get('price')
        if maxprice:
            order_details = order_details.order_by(OrderDetailsModel.price <= maxprice)

        order_details = order_details.paginate(page=page, per_page=per_page, error_out=False)

        return jsonify({'order_details':[order_detail.to_json() for order_detail in order_details],
                        'total' : order_details.total,
                        'pages' : order_details.pages,
                        'page' : page})
    
    # PENDIENTE: con optional=True acepta peticiones sin token.
    @jwt_required(optional=True)
    def post(self):
        orders_details = OrderDetailsModel.from_json(request.get_json())
        db.session.add(orders_details)
        db.session.commit()
        return orders_details.to_json(), 201