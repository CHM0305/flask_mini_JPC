from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from models import Choices, Answer, User

choice_blp = Blueprint('Choices', 'choice', url_prefix='/choices')

@choice_blp.route('/')
class Choices_list(MethodView):
    #선택지 조회
    def get_choices(self):
        choices = Choices.query.all()
        return jsonify ([{
                "id": self.id,
                "content": self.content,
                "is_active": self.is_active,
                "sqe": self.sqe,
                "question_id": self.question_id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()
            }for choice in choices
            ])
    #선택지 생성
    def add_choices(self):
                data = request.json
                new_choices = Choices()
                db.session.add(new_choices)
                db.session.commit()
                return jsonify({"message": "Choices created successfully"}), 201

    #응답 저장
    def answer():    
        new_answer = Answer(choice_id=Choices.id, user_id=User.id)
        db.session.add(new_answer)
        db.session.commit()
