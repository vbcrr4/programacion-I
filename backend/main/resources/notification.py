from flask_restful import Resource
from flask import request,jsonify
from main.models import (NotificationModel)
from .. import db

class Notification(Resource):
    def get(self,rating_id):
        rating = db.session.query(NotificationModel).get_or_404(rating_id)
        return rating.to_json()
    
    def delete(self,rating_id):
        rating = db.session.query(NotificationModel).get_or_404(rating_id)
        db.session.delete(rating)
        db.session.commit()
        return rating.to_json(), 200  
    
    def put(self,rating_id):
        rating = db.session.query(NotificationModel).get_or_404(rating_id)
        data = request.get_json().items()
        for key, value in data:
            setattr(rating, key, value)
        db.session.add(rating)
        db.session.commit()
        return rating.to_json(), 201
    
class Notification_List(Resource):
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
    
    def post(self):
        rating = NotificationModel.from_json(request.get_json())
        db.session.add(rating)
        db.session.commit()
        return rating.to_json(), 201