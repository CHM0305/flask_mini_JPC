from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
<<<<<<< HEAD
from app.models import Question,db
=======
from config import db
from app.models import Question
>>>>>>> d9031b5f32baf3354385d65704abf2ae35567a00

question_blp = Blueprint('Question', 'question', url_prefix='/question')
questions_blp = Blueprint('Questions', 'questions', url_prefix='/questions')

@question_blp.route('/')
<<<<<<< HEAD
class QuestionCreate(MethodView):
    #질문 생성
    def post(self):
        data = request.json   
        if not data or 'title' not in data or 'is_active' not in data or 'sqe' not in data:
            return jsonify({'msg': 'Invalid input data'}), 400     
        
        new_question = Question(
            title = data['title'],
            is_active = data['is_active'],
            sqe = data['sqe'],
            image_id = data['image_id']
                )
=======
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
>>>>>>> d9031b5f32baf3354385d65704abf2ae35567a00
        db.session.add(new_question)
        db.session.commit()
        return jsonify({"message": "Question created successfully"}), 201
        
    #질문 조회
    def get(self):
        questions = Question.query.all()
        return jsonify ([question.to_dict() for question in questions]), 200

#특정 질문 가져오기
@questions_blp.route('/<int:question_id>')
class QuestionResource(MethodView):
    def get(self, question_id):
        question = Question.query.get_or_404(question_id)
        return jsonify(question.to_dict()), 200

# 질문 개수 확인
@question_blp.route('/count')
class QuestionCount(MethodView):   
    def get(self):
        questions = Question.query.all()
        return jsonify({"total": len(questions)}) 


