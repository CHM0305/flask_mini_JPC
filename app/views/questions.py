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
        data = Question.query.all()
        questions_data=[question.to_dict() for question in data]
        return jsonify(questions_data)
    
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

# 질문 개수 확인
@question_blp.route('/count')
class QuestionCount(MethodView):   
    def get(self):
        questions = Question.query.all()
        return jsonify({"total": len(questions)}) 

#특정 질문 조회 수정 삭제
@question_blp.route('/<int:question_id>')
class QuestionResource(MethodView):
    
    #특정 질문 조회
    def get(self, question_id):
        question=Question.query.get_or_404(question_id)
        return jsonify(question.to_dict()),200
    
    #특정 질문 수정
    def put(self, question_id):
        question=Question.query.get(question_id)
        if not question:
            return jsonify({"error": f"Question with ID {question_id} not found"}), 404
        
        data=request.json
        question.title=data.get["title"],
        question.is_active=data.get["is_active", True],
        question.sqe=data.get["sqe"],
        question.image_id=data.get["image_id"] 
        db.session.commit()
        return jsonify({"message": "Question updated successfully"}), 200
    
    # 특정 질문 삭제
    def delete(self, question_id):
        question=Question.query.get(question_id)
        if not question:
            return jsonify({"error": f"Question with ID {question_id} not found"}), 404

        db.session.delete(question)
        db.session.commit()
        return jsonify({"message": "Question deleted successfully"}), 204



#특정 질문 조회 수정 삭제
@question_blp.route('/<int:question_id>')
class QuestionResource(MethodView):
    
    #특정 질문 조회
    def get(self, question_id):
        question=Question.query.get_or_404(question_id)
        return jsonify(question.to_dict()),200
    
    #특정 질문 수정
    def put(self, question_id):
        question=Question.query.get(question_id)
        if not question:
            return jsonify({"error": f"Question with ID {question_id} not found"}), 404
        
        data=request.json
        question.title=data.get["title"],
        question.is_active=data.get["is_active", True],
        question.sqe=data.get["sqe"],
        question.image_id=data.get["image_id"] 
        db.session.commit()
        return jsonify({"message": "Question updated successfully"}), 200
    
    # 특정 질문 삭제
    def delete(self, question_id):
        question=Question.query.get(question_id)
        if not question:
            return jsonify({"error": f"Question with ID {question_id} not found"}), 404

        db.session.delete(question)
        db.session.commit()
        return jsonify({"message": "Question deleted successfully"}), 204


