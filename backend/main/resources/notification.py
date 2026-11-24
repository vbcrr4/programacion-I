from flask_restful import Resource
from flask import request,jsonify
from main.models import (NotificationModel)
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import role_required

# Recurso /notifications/<id>: operaciones sobre una notificación concreta.
class Notification(Resource):
    # PENDIENTE: con optional=True también responde sin token, y NotificationModel no define
    # to_json_complete, por lo que fallaría si el usuario consulta su propia notificación.
    @jwt_required(optional=True)
    def get(self,notification_id):
        notification = db.session.query(NotificationModel).get_or_404(notification_id)
        current_identity = get_jwt_identity()
        if current_identity == str(notification.user_id):
            return notification.to_json_complete()
        else: return notification.to_json() 
        
    # PENDIENTE: el rol 'Users' no existe (los roles son Admin, Empleado y Client),
    # por lo que en la práctica solo Admin puede borrar.
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
    
# Recurso /notifications: listado (solo Admin, con filtros y paginación) y creación.
class Notification_List(Resource):    
    @role_required(roles = ["Admin"])
    def get(self):
        page = 1
        per_page = 10

        notifications = db.session.query(NotificationModel)

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        # Filtros opcionales por query string: user_id, created_at y status
        if request.args.get('user_id'):
            user_id = int(request.args.get('user_id'))
            notifications = notifications.filter(NotificationModel.user_id == user_id)
        if request.args.get('created_at'):
            created_at = request.args.get('created_at')
            notifications = notifications.filter(NotificationModel.created_at == created_at)
        if request.args.get('status'):
            status = request.args.get('status')
            notifications = notifications.filter(NotificationModel.status == status)
        
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