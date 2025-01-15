from flask import request, jsonify, session
from flask.views import MethodView
from flask_smorest import Blueprint
<<<<<<< HEAD
from app.models import Answer,db
=======
from config import db
from app.models import Choices, Answer, User
>>>>>>> d9031b5f32baf3354385d65704abf2ae35567a00

answer_blp = Blueprint('Answer', 'answer', url_prefix='/answer')

# 응답 저장
@answer_blp.route('/')
<<<<<<< HEAD
class AnswerCreate(MethodView):
=======
class AnswerList(MethodView):
    # 선택지 저장
>>>>>>> d9031b5f32baf3354385d65704abf2ae35567a00
    def post(self):
        # 세션에서 사용자 정보 확인
        if 'username' not in session:
            return jsonify({"error": "User must be logged in to save an answer"}), 401
        
        user_id = User.query.filter_by(username=session['username']).first().id

        data = request.json
<<<<<<< HEAD
        new_answer = Answer(choice_id=data["choice_id"], user_id=data["user_id"])
        db.session.add(new_answer)
        db.session.commit()
        return jsonify({[answer for answer in new_answer]}), 201

# 답변 조회    
@answer_blp.route('/<int:user_id>/<int:choice_id>')
class AnswerGet(MethodView):
    def get(self,user_id, choice_id):
        answers = Answer.query.filter_by(user_id=user_id, choice_id=choice_id).all()
        if not answers:
            return {"msg":"No Found Data"}
        return [answer.to_dict() for answer in answers]
    
=======
        
        # 필수 데이터 확인
        if not data.get("choice_id") or not data.get("user_id"):
            return jsonify({"error": "choice_id and user_id are required"}), 400

        # 선택지와 사용자 확인
        choice = Choices.query.get(data["choice_id"])
        user = User.query.get(data["user_id"])

        if not choice:
            return jsonify({"error": f"Choice with ID {data['choice_id']} not found"}), 404

        if not user:
            return jsonify({"error": f"User with ID {data['user_id']} not found"}), 404

        # 새로운 답변 저장
        new_answer = Answer(choice_id=data["choice_id"], user_id=data["user_id"])
        db.session.add(new_answer)
        db.session.commit()

        return jsonify({"message": "Answer saved successfully"}), 201
>>>>>>> d9031b5f32baf3354385d65704abf2ae35567a00
