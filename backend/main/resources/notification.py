from flask_restful import Resource
from flask import request,jsonify
from main.models import (NotificationModel)
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import role_required

class Notification(Resource):
    @jwt_required(optional=True)
    def get(self,notification_id):
        notification = db.session.query(NotificationModel).get_or_404(notification_id)
        current_identity = get_jwt_identity()
        if current_identity == notification.user_id:
            return notification.to_json_complete()
        else: return notification.to_json() 
        
    @role_required(roles = ["Admin","Users"])
    def delete(self,notification_id):

        notification = db.session.query(NotificationModel).get_or_404(notification_id)
        role = get_jwt().get('role')
        if role == 'Users' and notification.user_id != get_jwt_identity():
            return 'No tiene permisos para eliminar este recurso', 403
        db.session.delete(notification)
        db.session.commit()
        return notification.to_json(), 200  
    
    @role_required(roles = ["Admin"])
    def put(self,notification_id):
        notification = db.session.query(NotificationModel).get_or_404(notification_id)
        data = request.get_json().items()
        for key, value in data:
            setattr(notification, key, value)
        db.session.add(notification)
        db.session.commit()
        return notification.to_json(), 201
    
class Notification_List(Resource):    
    @role_required(roles = ["Admin"])
    def get(self):
        page = 1
        per_page = 10

        notifications = db.session.query(NotificationModel)

        #paginacion
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        #filtro por id usuario
        if request.args.get('user_id'):
            user_id = int(request.args.get('user_id'))
            notifications = notifications.filter(NotificationModel.user_id == user_id)
        #filtro por fecha de creacion
        if request.args.get('created_at'):
            created_at = request.args.get('created_at')
            notifications = notifications.filter(NotificationModel.created_at == created_at)
        #filtro por estado
        if request.args.get('status'):
            status = request.args.get('status')
            notifications = notifications.filter(NotificationModel.status == status)
        
        #fin filtros
        notifications = notifications.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'notifications': [notification.to_json() for notification in notifications.items],
                        'total' : notifications.total,
                         'pages' : notifications.pages,
                         'page' : page
        })
    

    @role_required(roles=["Admin"])
    def post(self):
        notification = NotificationModel.from_json(request.get_json())
        db.session.add(notification)
        db.session.commit()
        return notification.to_json(), 201