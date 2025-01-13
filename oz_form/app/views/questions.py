from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from models import Question

question_blp = Blueprint('Questions', 'question', url_prefix='/question')

@question_blp.route('/')
class Question_list(MethodView):
    #질문조회
    def get_question(self):
        questions = Question.query.all()
        return jsonify ([{
                "id": question.id,
                "title": question.title,
                "is_active": self.is_active,
                "sqe": self.sqe,
                "image": question.image.to_dict() if self.image else None,
                "created_at": question.created_at.isoformat(),
                "updated_at": question.updated_at.isoformat(),
            }for question in questions
            ])
    #질문 생성
    def add_question(self):
        data = request.json        
        new_question = Question()
        db.session.add(new_question)
        db.session.commit()
        return jsonify({"message": "Question created successfully"}), 201


