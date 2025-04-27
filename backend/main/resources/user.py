from flask_restful import Resource
from flask import request

USERS = {
    1: {"name": "Nehuen", "role": "admin"},
    2: {"name": "Franco", "role": "client"},
    3: {"name": "Valentin", "role": "owner"},
}


class User(Resource):
    def get(self, user_id):
        user_id = int(user_id)
        user = USERS.get(user_id)
        if user:
            return user, 200 # 200 OK
        return {"message": "User ID not found"}, 404 # 404 NOT FOUND    

    def delete(self, user_id):
        user_id = int(user_id)
        if user_id in USERS:
            del USERS[user_id]
            return {"message": "User deleted successfully"}, 200
        return {"message": "User ID not found for deletion"}, 404

    def put(self, user_id):
        user_id = int(user_id)
        if user_id in USERS:
            data = request.get_json()

            # Optionally, validate input here
            USERS[user_id].update(data)

            return {"message": "User updated successfully"}, 200
        return {"message": "User ID not found for update"}, 404
    
class UserList(Resource):
    def  get(self):
        return USERS, 200
    
    def post(self):
        #Pide la data para agregar la info nueva a users
        data = request.get_json()
        new_id = max(USERS.keys())+1
        USERS[new_id] = data
        return {'message': 'User created successfully','product_id':new_id}, 201
