from flask_restful import Resource
from flask import request,jsonify
from main.models import (RatingModel,UserModel,ProductModel)
from sqlalchemy import func, desc
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import role_required

class Rating(Resource):
    @jwt_required()
    def get(self,rating_id):
        rating = db.session.query(RatingModel).get_or_404(rating_id)
        return rating.to_json()
    

    @role_required(roles = ["Admin","Users"])
    def delete(self,rating_id):
        role = get_jwt().get('role')
        rating = db.session.query(RatingModel).get_or_404(rating_id)
        if role == 'Users' and rating.user_id != get_jwt_identity():
            return 'No tiene permisos para eliminar este recurso', 403
        
        db.session.delete(rating)
        db.session.commit()
        return rating.to_json(), 200  
    
 
    @role_required(roles = ["Users"])
    def put(self,rating_id):
        rating = db.session.query(RatingModel).get_or_404(rating_id)
        current_identity = get_jwt_identity()
        if current_identity == rating.user_id:

            data = request.get_json().items()
            for key, value in data:
                setattr(rating, key, value)
            db.session.add(rating)
            db.session.commit()
            return rating.to_json(), 201
        else: 
            return 'No tienes permisos para modificar este rating', 403

class RatingList(Resource):
    @role_required(roles = ["Admin"])
    def get(self):
        page =1 
        per_page=10
        rating = db.session.query(RatingModel)
        if request.args.get('page'):
            page=int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page=int(request.args.get('per_page'))
        #Filtrado por usuario id
        if request.args.get('user_id'):
            rating=rating.filter(RatingModel.user_id.like(request.args.get('user_id')))
        #Filtrado por producto
        product_id = request.args.get('product_id')
        if product_id:
            product_id = RatingModel.query.get_or_404(product_id)
            rating=rating.filter(RatingModel.product_id.like(request.args.get('product_id')))

        date = request.args.get('asc','desc')
        if date:
        #filtrado por creacion, mas nuevo
            if date.lower() == 'asc':
                rating=rating.order_by(RatingModel.created_at.asc())
        #filtrado por creacion, mas viejo
            elif date.lower() == 'desc':
                rating=rating.order_by(RatingModel.created_at.desc())

            
        
        #Filtrado por rating
        rating = rating.paginate(page=page, per_page=per_page, error_out=False)
        return jsonify({'rating':[rating.to_json() for rating in rating],
                        'total':rating.total,
                        'pages':rating.pages,
                        'page':page})
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        rating = RatingModel.from_json(request.get_json())
        rating.user_id = user_id
        db.session.add(rating)
        db.session.commit()
        return rating.to_json(), 201