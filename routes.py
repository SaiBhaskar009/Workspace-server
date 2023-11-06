from resources.user_login import User_auth
from resources.users_views import User_requirements
from flask_restful import Api

def Create_routes(app):

    api = Api(app)

    api.add_resource(User_auth, '/users', methods=['GET','POST'])
    api.add_resource(User_requirements, '/users', methods=['GET','POST'])



    return api.init_app(app)