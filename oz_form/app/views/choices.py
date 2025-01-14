from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from app.models import Choices, Answer, User

choice_blp = Blueprint('Choices', 'choice', url_prefix='/choices')

@choice_blp.route('/')
class ChoicesList(MethodView):
    # 선택지 조회
    def get(self):
        choices = Choices.query.all() or []
        return jsonify([{
            "id": choice.id,
            "content": choice.content,
            "is_active": choice.is_active,
            "sqe": choice.sqe,
            "question_id": choice.question_id,
            "created_at": choice.created_at.isoformat(),
            "updated_at": choice.updated_at.isoformat()
        } for choice in choices]), 200

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


@choice_blp.route('/answers', methods=['POST'])
def create_answer():
    data = request.json
    choice_id = data.get('choice_id')
    user_id = data.get('user_id')

    # 필수 데이터 확인
    if not choice_id or not user_id:
        return jsonify({"error": "choice_id and user_id are required"}), 400

    # 선택지와 사용자 유효성 확인
    choice = Choices.query.get(choice_id)
    user = User.query.get(user_id)

    if not choice:
        return jsonify({"error": f"Choice with ID {choice_id} not found"}), 404

    if not user:
        return jsonify({"error": f"User with ID {user_id} not found"}), 404

    # 새로운 답변 생성
    new_answer = Answer(choice_id=choice_id, user_id=user_id)
    db.session.add(new_answer)
    db.session.commit()

    return jsonify({"message": "Answer created successfully"}), 201
