from flask_restful import Resource
from flask import request,jsonify
from .. import db
from main.models import (UserModel, OrderModel)
from sqlalchemy import func, desc
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import role_required



class User(Resource):
    #JWT decorador va aquí,
    @jwt_required()
    def get(self, user_id):        
        user=db.session.query(UserModel).get_or_404(user_id)
        current_identity = get_jwt_identity()
        if current_identity == user.id:
            return user.to_json_complete()
        else: return user.to_json()
        
    @role_required(roles = ["Admin","Client","Empleado"])
    def delete(self, user_id):
        
        user = db.session.query(UserModel).get_or_404(user_id)
        role = get_jwt().get('role')
        if role == 'Client' and user.id != get_jwt_identity():
            return 'No tiene permisos para eliminar este recurso', 403
        elif role == 'Client' and user.id == get_jwt_identity():
            user.is_active = False #Desactiva el usuario
            return 'Usuario desactivado', 200
        
        db.session.delete(user)
        db.session.commit()
        return user.to_json(), 200
#        if user_id in USERS:
#            del USERS[user_id]
#            return {"message": "User deleted successfully"}, 200
#        return {"message": "User ID not found for deletion"}, 404
    @jwt_required()
    def put(self, user_id):
        user = db.session.query(UserModel).get_or_404(user_id)
        claims = get_jwt()
        role = claims.get('role')
        current_identity = get_jwt_identity()

        # Allow Admin/Empleado to edit any user, but Client can only edit self
        if role in ['Admin', 'Empleado'] or str(current_identity) == str(user.id):
            data = request.get_json().items()
            for key, value in data:
                # Prevent non-admins from changing roles
                if key == 'role' and role != 'Admin':
                    continue
                setattr(user, key, value)
            db.session.add(user)
            db.session.commit()
            return user.to_json(), 201
        else:
            return 'No tiene permisos para modificar este usuario', 403
    

class UserList(Resource):
    @role_required(roles = ["Admin", "Empleado"])
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
        number_of_orders= request.args.get('nrOrders')
        if number_of_orders:
            users=users.outerjoin(UserModel.orders).group_by(UserModel.id).having(func.count(OrderModel.id)>= int(number_of_orders))
        
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
