from flask_restful import Resource
from flask import request,jsonify
from main.models import (ProductModel)
from .. import db
#PRODUCTS = {
#    1: {"name": "burger", "price": 5000},
#    2: {"name": "french fries", "price": 2000},
#    3: {"name": "nuggets", "price": 3000},
#}


class Product(Resource):
    def get(self, product_id):
        product = db.session.query(ProductModel).get_or_404(product_id)
        return product.to_json()
        #product = PRODUCTS.get(int(product_id))
        #if product:
        #    return product, 200
        #return {"message": "Product ID not found"}, 404

    def delete(self, product_id):
        
        product = db.session.query(ProductModel).get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return product.to_json(), 200

    def put(self, product_id):
        product = db.session.query(ProductModel).get_or_404(product_id)
        data = request.get_json().items()
        for key, value in data:
            setattr(product, key, value)
        db.session.add(product)
        db.session.commit()
        return product.to_json(), 201


class ProductList(Resource):
    def get(self):
        page = 1
        per_page = 10

        products = db.session.query(ProductModel)

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        
        #Buscamos por nombre
        if request.args.get('name'):
            name = request.args.get('name')
            products = products.filter(ProductModel.name.ilike(f'%{name}%'))
        #Buscamos por precio
        if request.args.get('price'):
            price = float(request.args.get('price'))
            products = products.filter(ProductModel.price <= price)
        #Buscamos por disponibilidad
        if request.args.get('available'):
            available = request.args.get('available').lower() == 'true'
            products = products.filter(ProductModel.available == available)
        #Buscamos por categoria
        if request.args.get('category'):
            category = request.args.get('category')
            products = products.filter(ProductModel.category.ilike(f'%{category}%'))

        #fin filtros

        products = products.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({ 'products': [product.to_json() for product in products],
                        'total' : products.total,
                         'pages' : products.pages,
                         'page' : page
                         })

    def post(self):
        product = ProductModel.from_json(request.get_json())
        db.session.add(product)
        db.session.commit()
        return product.to_json(), 201