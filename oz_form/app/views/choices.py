from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from app.models import Choices, Answer, User
#퀘스쳔 모듈
choice_blp = Blueprint('Choices', 'choice', url_prefix='/choices')

@choice_blp.route('/')
class ChoicesList(MethodView):
    # 선택지 조회
    def get(self):
        data = Choices.query.all()
        choice_data=[choice.to_dict() for choice in data]
        return jsonify(choice_data)
    
    # 선택지 생성
    def post(self):
        data = request.json
        # 필수 데이터 확인
        if not data.get('content') or not data.get('question_id'):
            return jsonify({"error": "content and question_id are required"}), 400

        # 새로운 선택지 생성
        new_choice = Choices(
            content=data.get('content'),
            is_active=data.get('is_active', True),
            sqe=data.get('sqe'),
            question_id=data.get('question_id')
        )
        db.session.add(new_choice)
        db.session.commit()
        return jsonify({"message": "Choice created successfully"}), 201


@choice_blp.route('/<int:questions_id>') # FK
class ChoicesRource(MethodView):
    #특정 선택지 조회
    def get(self,questions_id):
        choices = Choices.query.get_or_404(questions_id)
        return jsonify([choice.to_dict() for choice in choices])

