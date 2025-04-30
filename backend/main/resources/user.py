from flask_restful import Resource
from flask import request,jsonify
from main.models import (UserModel)
from .. import db
#USERS = {
#    1: {"name": "Nehuen", "role": "admin"},
#    2: {"name": "Franco", "role": "client"},
#    3: {"name": "Valentin", "role": "owner"},
#}


class User(Resource):
    def get(self, user_id):
        user=db.session.query(UserModel).get_or_404(user_id)
        return user.to_json()
 #       user_id = int(user_id)
 #       user = USERS.get(user_id)
 #       if user:
 #           return user, 200 # 200 OK
 #       return {"message": "User ID not found"}, 404 # 404 NOT FOUND    

    def delete(self, user_id):
        user_id = int(user_id)
        user = db.session.query(UserModel).get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return user.to_json(), 200
#        if user_id in USERS:
#            del USERS[user_id]
#            return {"message": "User deleted successfully"}, 200
#        return {"message": "User ID not found for deletion"}, 404

    def put(self, user_id):
        user = db.session.query(UserModel).get_or_404(user_id)
        data = request.get_json().items()
        for key, value in data:
            setattr(user, key, value)
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201
    

class UserList(Resource):
    def  get(self):
        users = db.session.query(UserModel).all()
        return jsonify([user.to_json() for user in users])
#        return USERS, 200
    
    def post(self):

        user = UserModel.from_json(request.get_json())
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201
        #Pide la data para agregar la info nueva a users
        
        #data = request.get_json()
        #new_id = max(USERS.keys())+1
        #USERS[new_id] = data
        #return {'message': 'User created successfully','product_id':new_id}, 201
