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
        products = db.session.query(ProductModel).all()
        return jsonify([product.to_json() for product in products])
    
    def post(self):
        product = ProductModel.from_json(request.get_json())
        db.session.add(product)
        db.session.commit()
        return product.to_json(), 201