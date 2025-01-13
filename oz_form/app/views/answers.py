from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from models import Choices, Answer, User

answer_blp = Blueprint('Answer', 'answer', url_prefix='/answer')

@answer_blp.route('/')
class AnswerList(MethodView):
    #  선택지 저장
    def post(self):
        data = request.json
        new_answer = Answer(choice_id=data.get("choice_id"), user_id=data.get("user_id"))
        db.session.add(new_answer)
        db.session.commit()
        return jsonify({"message": "answer saved successfully"}), 201