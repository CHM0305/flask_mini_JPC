from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from app.models import Choices, db

choices_blp = Blueprint('Choices', 'choices', url_prefix='/choices')

@choices_blp.route('/')
#선택지 생성
def add_choices(self):
    data = request.json
    new_choices = Choices(
        content = data['content'],
        is_active = data['is_active'],
        sqe = data['sqe'],
        question_id = data['question_id']
    )
    db.session.add(new_choices)
    db.session.commit()
    return jsonify({"message": "Choices created successfully"}), 201
#선택지 조회
def get_choices(self):
    choices = Choices.query.all()
    return jsonify ([choice.to_dict() for choice in choices])

# 선택지 가져오기
@choices_blp.route('/<int:question_id>')
def get(self, question_id):
        choices = Choices.query.get_or_404(question_id)
        return jsonify([choice.to_dict() for choice in choices])
    



