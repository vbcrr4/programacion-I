from flask_restful import Resource
from flask import request,jsonify
from main.models import (OrderModel)
from .. import db
from sqlalchemy import func, desc
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import role_required


class Order(Resource):
    @jwt_required(optional=True)
    def get(self, order_id):
        order = db.session.query(OrderModel).get_or_404(order_id)
        return order.to_json()
    
    @role_required(roles = ["Admin"])
    def delete(self, order_id):
        order = db.session.query(OrderModel).get_or_404(order_id)
        db.session.delete(order)
        db.session.commit()
        return order.to_json(), 200        
    
    @jwt_required()
    def put(self, order_id):
        
        order = db.session.query(OrderModel).get_or_404(order_id)
        data = request.get_json().items()
        for key,value in data :
            setattr (order, key, value)
        db.session.add(order)
        db.session.commit()
        return order.to_json(), 201
        
class OrderList(Resource):
    @role_required(roles = ["Admin"])
    def get(self):
        page = 1
        per_page = 10

        orders = db.session.query(OrderModel)
        
        #paginacion
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        #filtro por id usuario
        if request.args.get('user_id'):
            user_id = int(request.args.get('user_id'))
            orders = orders.filter(OrderModel.user_id == user_id)
        #filtro por fecha de creacion
        if request.args.get('created_at'):
            created_at = request.args.get('created_at')
            orders = orders.filter(OrderModel.created_at == created_at)
        #filtro por estado
        if request.args.get('status'):
            status = request.args.get('status')
            orders = orders.filter(OrderModel.status == status)
        #filtro por mayor subtotal
        if request.args.get('total'):
            total = float(request.args.get('total'))
            orders = orders.filter(OrderModel.total >= total)
        #filtro por menor subtotal
        if request.args.get('total_min'):
            total_min = float(request.args.get('total_min'))
            orders = orders.filter(OrderModel.total <= total_min)
        
        #fin filtros
        orders = orders.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'orders': [order.to_json() for order in orders],
            'total': orders.total,
            'pages': orders.pages,
            'page': page
        })
    
    @jwt_required()
    def post(self):
        order = OrderModel.from_json(request.get_json())
        db.session.add(order)
        db.session.commit()
        return order.to_json,201