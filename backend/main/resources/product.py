from flask_restful import Resource
from flask import request

PRODUCTS = {
    1: {"name": "burger", "price": 5000},
    2: {"name": "french fries", "price": 2000},
    3: {"name": "nuggets", "price": 3000},
}


class Product(Resource):
    def get(self, product_id):
        product = PRODUCTS.get(int(product_id))
        if product:
            return product, 200
        return {"message": "Product ID not found"}, 404

    def delete(self, product_id):
        product_id = int(product_id)
        if product_id in PRODUCTS:
            del PRODUCTS[product_id]
            return {"message": "Product deleted successfully"}, 200
        return {"message": "Product ID not found"}, 404

    def put(self, product_id):
        product_id = int(product_id)
        if product_id in PRODUCTS:
            data = request.get_json()
            PRODUCTS[product_id].update(data)
            return {"message": "Product updated successfully"}, 200
        return {"message": "Product ID not found"}, 404


class ProductList(Resource):
    def get(self):
        return PRODUCTS, 200

    def post(self):
        data = request.get_json()
        new_id = max(PRODUCTS.keys()) + 1
        PRODUCTS[new_id] = data
        return {"message": "Product created successfully", "product_id": new_id}, 201
