from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from app.models import User

user_blp = Blueprint('users', 'users', url_prefix='/users', description='Operations on users')

@user_blp.route('/')
class UserList(MethodView):
    def get(self):
        users = User.query.all()
        user_data = [user.to_dict() for user in users]
        return jsonify(user_data)

    def post(self):
        user_data = request.json

        # 필수 데이터 확인
        if not user_data.get("name") or not user_data.get("email"):
            return jsonify({"error": "Username, email are required"}), 400

        # 새로운 사용자 생성
        new_user = User(
            name=user_data.get("name"),
            email=user_data.get("email")
        )
        
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
