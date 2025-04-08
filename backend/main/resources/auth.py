from flask_restful import Resource
from flask import request

USERS = {}


class Register(Resource):
    def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return {"message": "Username and password are required"}, 400

        if username in USERS:
            return {"message": "Username already exists"}, 409

        USERS[username] = password
        return {"message": f"User '{username}' registered successfully"}, 201


class Login(Resource):
    def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return {"message": "Username and password are required"}, 400

        if USERS.get(username) == password:
            return {"message": f"Welcome, {username}!"}, 200

        return {"message": "Invalid credentials"}, 401
