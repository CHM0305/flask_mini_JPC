from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from app.models import User

user_blp = Blueprint('users', 'users',description='Operations on users', url_prefix='/signup')
#아이디 전체 조회
@user_blp.route('/')
class UserList(MethodView):
    def post(self):
        user_data = request.json
        # 새로운 사용자 생성
        new_user = User(
            name=user_data["name"],
            age=user_data["age"],
            email=user_data["email"],
            gender=user_data["gender"]
        )
        #뉴 사용자 이름과, 원래 있던 사용자의 이름이 같으면 오류를
        existing_user = User.query.filter_by(email=new_user.email).first()
        if existing_user:
            return jsonify({"error": "이미 존재하는 계정 입니다."}), 400
        db.session.add(new_user)
        db.session.commit()
        # 회원 가입 축하 메세지
        return jsonify({"message" :"User님 회원가입을 축하합니다.",
                        "user_id" : new_user.id}), 201

    def get(self):
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])
    



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
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        user.gender = data.get('gender', user.gender)
        user.age = data.get('age', user.age)
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