from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from app.models import Question,db

question_blp = Blueprint('Question', 'question', url_prefix='/question')
questions_blp = Blueprint('Questions', 'questions', url_prefix='/questions')

@question_blp.route('/')
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



