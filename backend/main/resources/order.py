from flask_restful import Resource
from flask import request,jsonify
from main.models import (OrderModel, OrderDetailsModel, ProductModel, UserModel)
from .. import db
from sqlalchemy import func, desc
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import role_required


# Recurso /orders/<id>: operaciones sobre un pedido concreto.
class Order(Resource):
    @jwt_required()
    def get(self,order_id):
        order = db.session.query(OrderModel).get_or_404(order_id)
        if get_jwt().get('role') == 'Client' and str(order.user_id) != get_jwt_identity():
            return "No tenes permiso para ver este pedido", 403
        return order.to_json()
    
    @role_required(roles = ["Admin"])
    def delete(self, order_id):
        order = db.session.query(OrderModel).get_or_404(order_id)
        db.session.delete(order)
        db.session.commit()
        return order.to_json(), 200        
    
    # PENDIENTE: aplica cualquier campo recibido, sin una lista de campos permitidos.
    @role_required(roles=["Admin", "Empleado"])
    def patch(self, order_id):
        order = db.session.query(OrderModel).get_or_404(order_id)
        data = request.get_json().items()
        for key, value in data:
            setattr(order, key, value)
        db.session.add(order)
        db.session.commit()
        return order.to_json(), 201
        
# Recurso /orders: listado de pedidos (con filtros y paginación) y alta de productos en un pedido.
class OrderList(Resource):
    # El Cliente solo ve sus propios pedidos; Admin y Empleado ven todos y pueden filtrar por user_id.
    @role_required(roles = ["Admin", "Client", "Empleado"])
    def get(self):
        claims = get_jwt()
        page = 1
        per_page = 10

        orders = db.session.query(OrderModel).order_by(OrderModel.created_at.desc())
        
        if claims['role'] == 'Client':
            orders = orders.filter_by(user_id=claims['id'])
        else:
            if request.args.get('user_id'):
                user_id = int(request.args.get('user_id'))
                orders = orders.filter(OrderModel.user_id == user_id)

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        # Filtros opcionales por query string: created_at, status, total_min y total_max
        if request.args.get('created_at'):
            created_at = request.args.get('created_at')
            orders = orders.filter(OrderModel.created_at == created_at)
        if request.args.get('status'):
            status = request.args.get('status')
            orders = orders.filter(OrderModel.status == status)


        if request.args.get('total_min'):
            total_min = float(request.args.get('total_min'))
            orders = orders.filter(OrderModel.total >= total_min)


        if request.args.get('total_max'):
            total_max = float(request.args.get('total_max'))
            orders = orders.filter(OrderModel.total <= total_max)

        
        orders = orders.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'orders': [order.to_json_complete() for order in orders.items],
            'total': orders.total,
            'pages': orders.pages,
            'page': page
        })
    
    # Agrega un producto al pedido pendiente del usuario (lo crea si no existe) y recalcula el total.
    # PENDIENTE: no se valida que quantity sea un entero positivo.
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        # Admin y Empleado pueden crear el pedido a nombre de un cliente
        if get_jwt().get('role') in ['Admin', 'Empleado'] and request.get_json().get('user_id'):
            user_id = request.get_json().get('user_id')
            db.session.query(UserModel).get_or_404(user_id)
        # No se puede pedir un producto no disponible (se valida antes de crear el pedido)
        requested_product = db.session.query(ProductModel).get_or_404(request.get_json().get('product_id'))
        if not requested_product.available:
            return 'El producto no está disponible', 400
        order = db.session.query(OrderModel).filter_by(user_id=user_id, status='pending').first()
        if not order:
            order = OrderModel(user_id=user_id, status='pending', total=0)
            db.session.add(order)
            db.session.commit()

        product_id = request.get_json().get('product_id')
        quantity = request.get_json().get('quantity')

        product = db.session.query(ProductModel).get_or_404(product_id)

        order_detail = db.session.query(OrderDetailsModel).filter_by(order_id=order.id, product_id=product_id).first()

        if order_detail:
            order_detail.quantity += quantity
            order_detail.subtotal = order_detail.quantity * order_detail.price
        else:
            order_detail = OrderDetailsModel(
                order_id=order.id,
                product_id=product_id,
                quantity=quantity,
                price=product.price,
                subtotal=product.price * quantity
            )
            db.session.add(order_detail)

        db.session.commit()
        order.total = sum([item.subtotal for item in order.order_details])
        db.session.commit()

        return order.to_json_complete(), 201