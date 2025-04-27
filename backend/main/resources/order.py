from flask_restful import Resource
from flask import request

ORDERS = {
    1: {
        "user_id": 1,
        "created_at": "2025-02-01",
        "status": "delivered",
        "total": 10000,
    },
    2: {
        "user_id": 2,
        "created_at": "2025-02-01",
        "status": "delivered",
        "total": 20000,
    },
    3: {
        "user_id": 3,
        "created_at": "2025-02-01",
        "status": "delivered",
        "total": 30000,
    },
}


class Order(Resource):
    def get(self, order_id):
        order = ORDERS.get(int(order_id))
        if not order:
            return {"message": "Order id not found"}, 404
        return order, 200

    def delete(self, order_id):
        order_id = int(order_id)
        if order_id in ORDERS:
            del ORDERS[order_id]
            return {"message": "Order deleted successfully"}, 200
            return {"message": "Order ID not found for deletion"}, 404

    def put(self, order_id):
        order_id = int(order_id)
        if order_id in ORDERS:
            data = request.get_json()
            ORDERS[order_id].update(data)
            return {"message": "Order updated successfully"}, 200
        return {"message": "Order ID not found for update"}, 404


class OrderList(Resource):
    def get(self):
        return ORDERS, 200

    def post(self):
        data = request.get_json()
        new_id = max(ORDERS.keys()) + 1
        ORDERS[new_id] = data
        return {"message": "Order created successfully", "order_id": new_id}, 201
