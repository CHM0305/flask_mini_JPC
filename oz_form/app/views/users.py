from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from models import User

user_blp = Blueprint('users', 'users', url_prefix='/users', description='Operations on users')

@user_blp.route('/')
class UserList(MethodView):
    def get(self):
        users = User.query.all()
        user_data = [user.to_dict() for user in users]
        return jsonify(user_data)

    def post(self):
        user_data = request.json
        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created"}), 201