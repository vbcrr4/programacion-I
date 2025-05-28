from flask_restful import Resource
from flask import request,jsonify
from main.models import (RatingModel,UserModel,ProductModel)
from sqlalchemy import func, desc
from .. import db

class Rating(Resource):
    def get(self,rating_id):
        rating = db.session.query(RatingModel).get_or_404(rating_id)
        return rating.to_json()
    
    def delete(self,rating_id):
        rating = db.session.query(RatingModel).get_or_404(rating_id)
        db.session.delete(rating)
        db.session.commit()
        return rating.to_json(), 200  
    
    def put(self,rating_id):
        rating = db.session.query(RatingModel).get_or_404(rating_id)
        data = request.get_json().items()
        for key, value in data:
            setattr(rating, key, value)
        db.session.add(rating)
        db.session.commit()
        return rating.to_json(), 201
    
class RatingList(Resource):
    def get(self):

        page =1 
        per_page=10
        rating = db.session.query(RatingModel)
        if request.args.get('page'):
            page=int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page=int(request.args.get('per_page'))
        #Filtrado por usuario
        if request.args.get('user_id'):
            rating=rating.filter(RatingModel.role.like(request.args.get('user_id')))
        #Filtrado por producto
        #if request.args.get('product'):
        #    rating=rating.filter(RatingModel.role.like(request.args.get('user_id')))
        
        #Filtrado por rating
        rating = rating.paginate(page=page, per_page=per_page, error_out=False)
        return jsonify([rating.to_json() for rating in rating])
    
    def post(self):
        rating = RatingModel.from_json(request.get_json())
        db.session.add(rating)
        db.session.commit()
        return rating.to_json(), 201