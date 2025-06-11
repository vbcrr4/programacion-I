from flask import request,jsonify
from flask_jwt_extended import get_jwt,create_access_token,get_jwt_identity,set_access_cookies,verify_jwt_in_request
from datetime import datetime,timedelta

def refresh_check():
    if request.endpoint in ['auth.login', 'auth.refresh','auth.register']:
        return None

    try:
        verify_jwt_in_request(optional=True)
        jwt_data = get_jwt()
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now()
        target_timestamp = datetime.timestamp(now+timedelta(minutes=3))
        print('HOLA SOY UN TESTEO DEL REFRESH')

        if jwt_data and target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = {'id':jwt_data['id'],
                    'email':jwt_data['email'],
                    'access_token':access_token
                    }
            response = jsonify(data)
            set_access_cookies(response, access_token)
            return response, 200
        
    except Exception as error:
        return jsonify({
            "error": str(error),
            "msg": "Error in refresh token"
        }), 500
    