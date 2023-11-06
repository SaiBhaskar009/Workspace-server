from flask import request, json , jsonify
from extensions.BCRYPT import bcrypt
from flask_restful import Resource
from models.user_model import User
from schemas.user_schema import user, users, User_Schema
from default_settings import db 
from blueprints import blp
from flask_jwt_extended import get_jwt_identity, jwt_required



class User_requirements(Resource):

    def hashed_password(password):
        return bcrypt.generate_password_hash(password)

    @blp.route('/adduser', methods=['POST'])
    @jwt_required()
    def adduser():

        current_user = get_jwt_identity()
        check_user = User.query.filter_by(name=current_user).first()

        if check_user.type != 'admin':
            return jsonify("Unauthorized, Not an Admin")

        if request.method == 'POST':
            name = request.json['name'],
            password = request.json['password']
           
            new_user = User(name=name, password=password, user_type='user')
            new_user.password = bcrypt.generate_password_hash(new_user.password).decode('utf8')
            db.session.add(new_user)
            db.session.commit()
            result = user.dump(new_user)
            return jsonify(result)       
    
    @blp.route('/getallusers', methods=['GET'])
    @jwt_required()
    def getallusers():

        current_user = get_jwt_identity()
        check_user = User.query.filter_by(name=current_user).first()

        if check_user.user_type == 'admin':
    
            posts = User.query.filter_by(type='user').all()
            result = users.dump(posts)
            return jsonify(result)
        else:
            return jsonify({"Error Not Authorised"})
    

    @blp.route('/getuser', methods=['GET'])
    @jwt_required()
    def getuser():

        current_user = get_jwt_identity()

        get_user = User.query.filter_by(name=current_user).first()

        result = user.dump(get_user)
        return jsonify(result)

    @blp.route('/deleteuser/<yash_id>', methods=['DELETE'])
    def delete_user(yash_id):

        getting_user = User.query.filter_by(yash_id=yash_id).first()
        db.session.delete(getting_user)
        db.session.commit()
        return jsonify("User Deleted")
    
    


    
    

    

        

    
