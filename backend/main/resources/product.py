from flask_restful import Resource
from flask import request,jsonify
from main.models import (ProductModel)
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import role_required


# Recurso /products/<id>: operaciones sobre un producto concreto.
class Product(Resource):
    @role_required(roles = ["Admin",'Client','Empleado'])
    def get(self, product_id):
        product = db.session.query(ProductModel).get_or_404(product_id)
        return product.to_json()
    
    @role_required(roles = ["Admin"])
    def delete(self, product_id):
        
        product = db.session.query(ProductModel).get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return product.to_json(), 200
    
    @role_required(roles = ["Admin"])
    def put(self, product_id):
        product = db.session.query(ProductModel).get_or_404(product_id)
        data = request.get_json().items()
        for key, value in data:
            setattr(product, key, value)
        db.session.add(product)
        db.session.commit()
        return product.to_json(), 201

    # Admin y Empleado pueden cambiar solo la disponibilidad del producto
    @role_required(roles = ["Admin", "Empleado"])
    def patch(self, product_id):
        product = db.session.query(ProductModel).get_or_404(product_id)
        data = request.get_json()
        if 'available' not in data:
            return 'Solo se puede modificar available', 400
        product.available = bool(data['available'])
        db.session.commit()
        return product.to_json(), 200


# Recurso /products: listado (con filtros y paginación) y creación de productos.
class ProductList(Resource):
    @role_required(roles = ["Admin",'Client','Empleado'])
    def get(self):
        page = 1
        per_page = 10

        products = db.session.query(ProductModel)

        # Los clientes solo ven los productos disponibles
        if get_jwt().get('role') == 'Client':
            products = products.filter(ProductModel.available == True)

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        
        # Filtros opcionales por query string: name, price (máximo), available y category
        if request.args.get('name'):
            name = request.args.get('name')
            products = products.filter(ProductModel.name.ilike(f'%{name}%'))
        if request.args.get('price'):
            price = float(request.args.get('price'))
            products = products.filter(ProductModel.price <= price)
        if request.args.get('available'):
            available = request.args.get('available').lower() == 'true'
            products = products.filter(ProductModel.available == available)
        if request.args.get('category'):
            category = request.args.get('category')
            products = products.filter(ProductModel.category.ilike(f'%{category}%'))


        products = products.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({ 'products': [product.to_json() for product in products],
                        'total' : products.total,
                         'pages' : products.pages,
                         'page' : page
                         })
    @role_required(roles = ["Admin"])
    def post(self):
        product = ProductModel.from_json(request.get_json())
        db.session.add(product)
        db.session.commit()
        return product.to_json(), 201