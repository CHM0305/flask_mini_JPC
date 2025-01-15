from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from app.models import Answer,db

answer_blp = Blueprint('Answer', 'answer', url_prefix='/answer')

# 응답 저장
@answer_blp.route('/')
class AnswerCreate(MethodView):
    def post(self):
        data = request.json
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
    