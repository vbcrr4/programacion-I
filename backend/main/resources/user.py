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
        # get_jwt_identify() devuelve String, por eso se compara contra str(user.id)

        if role == 'Client' and str(user.id) != get_jwt_identity():
            return "No tenes permisos para eliminar este recurso", 403
        elif role == 'Client':
            user.is_active = False #Desactivar el usuario
            db.session.commit()
            return "Usuario desactivado", 200


        
        
        db.session.delete(user)
        db.session.commit()
        return user.to_json(), 200
    @jwt_required()
    def put(self, user_id):
        user = db.session.query(UserModel).get_or_404(user_id)
        claims = get_jwt()
        role = claims.get('role')
        is_self = str(get_jwt_identity()) == str(user.id)

        # Allow Admin/Empleado to edit any user, but Client can only edit self
        if role in ['Admin', 'Empleado'] or is_self:
            data = request.get_json().items()
            for key, value in request.get_json().items():
                if key in ['name','cellphone','email','address']:
                    setattr(user,key,value)
                elif key == 'password' and (is_self or role == 'Admin'):
                    user.plain_password = value # el setter hashea
                elif key == 'is_active' and role in ['Admin','Empleado']:
                    user.is_active = value
                elif key == 'role' and role == 'Admin':
                    user.role = value
            db.session.add(user)
            db.session.commit()
            return user.to_json(), 201
        else:
            return 'No tenes permisos para modificar este usuario ', 403
                
            
    

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
        
        #Buscamos por nombre:
        if request.args.get('name'):
            users=users.filter(UserModel.name.like("%"+request.args.get('name')+"%"))

        #Buscamos por direccion:
        if request.args.get('address'):
            users=users.filter(UserModel.address.like("%"+request.args.get('address')+"%"))
        #Filtramos por email
        if request.args.get('email'):
            users=users.filter(UserModel.email.like("%"+request.args.get('email')+"%"))
        #Vericamos si el usuario esta desactivado
        if request.args.get('is_active'):
            users=users.filter(UserModel.is_active == 0)

        #Buscamos usuarios por rol:
        if request.args.get('role'):
            users=users.filter(UserModel.role.like(request.args.get('role')))
        #Filtramos por cantidad de órdenes:
        number_of_orders= request.args.get('nrOrders')
        if number_of_orders:
            users=users.outerjoin(UserModel.orders).group_by(UserModel.id).having(func.count(OrderModel.id)>= int(number_of_orders))
        
        users = users.paginate(page=page, per_page=per_page, error_out=False)
        return jsonify({'users':[user.to_json() for user in users],'total': users.total,'pages':users.pages,'page':page})
    
    @role_required(roles = ["Admin"])
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
        
