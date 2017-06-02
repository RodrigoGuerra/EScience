import service.user as service
import bson.json_util as json


class Users(Resource):
    def __init__(self):
        pass

    def get(self):
        users = service.get_users()
        return users, 200

    def post(self):
        user = request.get_json()
        service.create_user(user)
        return json.object_hook(user), 201


class User(Resource):
    def __init__(self):
        pass

    def put(self, user_id):
        user = request.get_json()
        new_user = service.update_user(user_id, user)
        if new_user is None:
            return {'message': 'Resource not found'}, 404
        else:
            return new_user, 200

    def delete(self, user_id):
        deleted = service.delete_user(user_id)
        if deleted is None:
            return {'message': 'Resource not found'}, 404
        else:
            return None, 204
