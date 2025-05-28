from flask_restful import Resource
from flask import request,jsonify
from main.models import (UserModel, OrderModel)
from .. import db
from sqlalchemy import func, desc



class User(Resource):
    #JWT decorador va aquí, 
    def get(self, user_id):        
        user=db.session.query(UserModel).get_or_404(user_id)
        return user.to_json_complete()
 #       user_id = int(user_id)
 #       user = USERS.get(user_id)
 #       if user:
 #           return user, 200 # 200 OK
 #       return {"message": "User ID not found"}, 404 # 404 NOT FOUND    
# Se utiliza un decorador acá, para validar los roles
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
        page =1 
        per_page=10

        users = db.session.query(UserModel)
        if request.args.get('page'):
            page=int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page=int(request.args.get('per_page'))
        
        #Buscamos por direccion:
        if request.args.get('address'):
            users=users.filter(UserModel.address.like("%"+request.args.get('address')+"%"))
        
        #Buscamos usuarios por rol:
        if request.args.get('role'):
            users=users.filter(UserModel.role.like(request.args.get('role')))
        #Filtramos por cantidad de órdenes:
        if request.args.get('nrOrders'):
            users=users.outerjoin(UserModel.orders).group_by(UserModel.id).having(func.count(OrderModel.id)>= int(request.args.get('nrOrders')))
        
        users = users.paginate(page=page, per_page=per_page, error_out=False)
        return jsonify({'users':[user.to_json() for user in users],'total': users.total,'pages':users.pages,'page':page})
#        return USERS, 200
    
    def post(self):
#No devolver al crear la contraseña en texto plano
        orders_ids = request.get_json().get('orders')
        user = UserModel.from_json(request.get_json())
        if orders_ids:
            orders = OrderModel.query.filter(OrderModel.id.in_(orders_ids)).all()
            user.orders.extend(orders)
            
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201
        #Pide la data para agregar la info nueva a users
        
        #data = request.get_json()
        #new_id = max(USERS.keys())+1
        #USERS[new_id] = data
        #return {'message': 'User created successfully','product_id':new_id}, 201
