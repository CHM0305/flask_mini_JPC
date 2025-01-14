from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from app.models import Question
#이미지 모듈 불러오기
question_blp = Blueprint('Questions', 'question', url_prefix='/question')

@question_blp.route('/')
class QuestionList(MethodView):
    # 질문 조회
    def get(self):
        data = Question.query.all()
        questions_data=[question.to_dict() for question in data]
        return jsonify(questions_data)
    
    # 질문 생성
    def post(self):
        question_data = request.json

        # 필수 데이터 확인
        if not question_data.get("title"):
            return jsonify({"error": "The 'title' field is required"}), 400

        # 새로운 질문 생성
        new_question = Question(
            title=question_data.get("title"),
            is_active=question_data.get("is_active", True),
            sqe=question_data.get("sqe"),
            image_id=question_data.get("image_id")  # 이미지 연결 필드가 있다면 사용
        )
        db.session.add(new_question)
        db.session.commit()
        return jsonify({"message": "Question created successfully"}), 201


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


