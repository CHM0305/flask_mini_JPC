from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from app.models import Question

question_blp = Blueprint('Questions', 'question', url_prefix='/question')

@question_blp.route('/')
class QuestionList(MethodView):
    # 질문 조회
    def get(self):
        questions = Question.query.all() or []
        if not questions:
            return jsonify({"error": "No questions found"}), 404  # 질문이 없을 때 처리

        return jsonify([{
            "id": question.id,
            "title": question.title,
            "is_active": question.is_active,
            "sqe": question.sqe,
            "image": question.image.to_dict() if question.image else None,
            "created_at": question.created_at.isoformat(),
            "updated_at": question.updated_at.isoformat(),
        } for question in questions]), 200

    # 질문 생성
    def post(self):
        data = request.json

        # 필수 데이터 확인
        if not data.get("title"):
            return jsonify({"error": "The 'title' field is required"}), 400

        # 새로운 질문 생성
        new_question = Question(
            title=data.get("title"),
            is_active=data.get("is_active", True),
            sqe=data.get("sqe"),
            image_id=data.get("image_id")  # 이미지 연결 필드가 있다면 사용
        )
        db.session.add(new_question)
        db.session.commit()
        return jsonify({"message": "Question created successfully"}), 201

