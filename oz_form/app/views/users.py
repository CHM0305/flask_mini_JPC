from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from app.models import User

user_blp = Blueprint('users', 'users', url_prefix='/users', description='Operations on users')

@user_blp.route('/')
class UserList(MethodView):
    def get(self):
        data = User.query.all()
        users_data = [user.to_dict() for user in data]
        return jsonify(users_data)

    def post(self):
        user_data = request.json

        # 필수 데이터 확인
        if not user_data.get("name") or not user_data.get("email"):
            return jsonify({"error": "name, email are required"}), 400

        # 새로운 사용자 생성
        new_user = User(
            name=user_data.get("name"),
            age=user_data.get("age"),
            email=user_data.get("email"),
            gender=user_data.get("gender")
        )
        
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201

@user_blp.route('/<int:user_id>')
class UserResource(MethodView):
    #특정 아이디 조회
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict()),200
    #특정 아이디 수정
    def put(self, user_id):
        user=User.query.get(user_id)
        if not user:
            return jsonify({"error": f"User with ID {user_id} not found"}), 404

        data=request.json
        user.name=data.get["name"],
        user.age=data.get["age"],
        user.email=data.get["email"],
        user.gender=data.get["gender"]
        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200

    def delete(self, user_id):
        user=User.query.get(user_id)
        if not user:
            return jsonify({"error": f"User with ID {user_id} not found"}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 204

#아이디 생성, 조회 완료
#특정 아이디 조회 수정 삭제 완료