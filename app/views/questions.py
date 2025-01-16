from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from app.models import Question,Choices

question_blp = Blueprint('Questions', 'question', url_prefix='/question')

@question_blp.route('/')
class QuestionList(MethodView):
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
        return jsonify({"message": f"{new_question.title} Question created successfully"}), 201
        # 질문 조회
    def get(self):
        questions = Question.query.all()
        return jsonify([question.to_dict() for question in questions])
    



#특정 질문 조회 수정 삭제
@question_blp.route('/<int:question_id>')
class QuestionResource(MethodView):
    #특정 질문 조회
    def get(self, question_id):
        question=Question.query.get_or_404(question_id)
        return jsonify(
        {
        "question":{
        "id": question.id,
        "title": question.title,
        "image": {"url":question.image.url if question.image else None},
            }
        })
#특정 질문 삭제 수정을 같이 두면 안될듯. 사이트에 전체적으로 오류날듟?

# 질문 개수 확인
@question_blp.route('/count')
class QuestionCount(MethodView):   
    def get(self):
        questions = Question.query.all()
        return jsonify({"total": len(questions)}) 


