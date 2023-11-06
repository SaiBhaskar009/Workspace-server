from flask import request, json, jsonify
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from models.user_model import User
from schemas.user_schema import user
from default_settings import db 
import datetime
from blueprints import blp
from extensions.BCRYPT import bcrypt

class User_auth(Resource):
    

    @blp.route('/login', methods=['POST'])
    def login_user():

        data = request.get_json()
        username = data['username']
        password = data['password']

        post = User.query.filter_by(name=username).first()

        expires = datetime.timedelta(minutes=60)

        if post and bcrypt.check_password_hash(post.password,password):
           access_token = create_access_token(identity=username, expires_delta=expires)
           return jsonify({'access_token': access_token})
        else:
           return jsonify({'message': 'Invalid credentials'}), 401



    @blp.route('/create_admin', methods=['POST'])
    def create_admin(): 
            name = request.json['name']
            password = request.json['password']
            

            admin_user = User(name=name,  password=password, type='admin')
            admin_user.password = bcrypt.generate_password_hash(admin_user.password).decode('utf8')
            db.session.add(admin_user)
            db.session.commit()
            return jsonify("Admin Created Successfully")
        


    
    
