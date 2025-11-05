from flask_restful import Resource
from flask import request,jsonify
from main.models import (OrderModel, OrderDetailsModel, ProductModel)
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
    @role_required(roles = ["Admin", "Client"])
    def get(self):
        claims = get_jwt()
        page = 1
        per_page = 10

        orders = db.session.query(OrderModel).order_by(OrderModel.created_at.desc())
        
        if claims['role'] == 'Client':
            orders = orders.filter_by(user_id=claims['id'])
        else: # Admin
            if request.args.get('user_id'):
                user_id = int(request.args.get('user_id'))
                orders = orders.filter(OrderModel.user_id == user_id)

        #paginacion
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

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

        return jsonify({'orders': [order.to_json_complete() for order in orders.items],
            'total': orders.total,
            'pages': orders.pages,
            'page': page
        })
    
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        # Check if there is an active order for the user
        order = db.session.query(OrderModel).filter_by(user_id=user_id, status='pending').first()
        if not order:
            # Create a new order
            order = OrderModel(user_id=user_id, status='pending', total=0)
            db.session.add(order)
            db.session.commit()

        # Get product details from the request
        product_id = request.get_json().get('product_id')
        quantity = request.get_json().get('quantity')

        # Get product from DB
        product = db.session.query(ProductModel).get_or_404(product_id)

        # Check if the product is already in the order
        order_detail = db.session.query(OrderDetailsModel).filter_by(order_id=order.id, product_id=product_id).first()

        if order_detail:
            # Update quantity
            order_detail.quantity += quantity
            order_detail.subtotal = order_detail.quantity * order_detail.price
        else:
            # Add new product to the order
            order_detail = OrderDetailsModel(
                order_id=order.id,
                product_id=product_id,
                quantity=quantity,
                price=product.price,
                subtotal=product.price * quantity
            )
            db.session.add(order_detail)

        db.session.commit()
        # Recalculate order total
        order.total = sum([item.subtotal for item in order.order_details])
        db.session.commit()

        return order.to_json_complete(), 201