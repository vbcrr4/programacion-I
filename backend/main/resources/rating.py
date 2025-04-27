from flask_restful import Resource
from flask import request,jsonify
from main.models import (RatingModel)
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
        rating = db.session.query(RatingModel).all()
        return jsonify([rating.to_json() for rating in rating])
    
    def post(self):
        rating = RatingModel.from_json(request.get_json())
        db.session.add(rating)
        db.session.commit()
        return rating.to_json(), 201