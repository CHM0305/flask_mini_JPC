from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from app.models import Answer

answer_blp = Blueprint('Answer', 'answer', description="Operations on answer", url_prefix='/submit')

@answer_blp.route('/',methods=['POST'])
class AnswerPost(MethodView):
    def post(self):
        data=request.json
        
        for answer in data:
            user_id=answer.get("userId")
            choice_id=answer.get("choiceId")
            #존재한지 안한지 확인
            if not user_id or choice_id:
                return{"message":"Not Found user_id or choice_id"}
            
            #검사 후 데이터 존재시 답변 정보를 저장한다.
            new_answer=Answer(user_id=user_id,choice_id=choice_id)
            db.session.add(new_answer)
            db.session.commit()
            return {
                    "message":"User: 1's answers Success Create"
                    },201
        
@answer_blp.route('/')
class AnswerList(MethodView):
    # 모든 답변 조회 - 사용자들이 어떤 답변들을 했는지 통계적으로 알기 위함 
    def get(self):
        datas =Answer.query.all()
        answer_data = [data.to_dict() for data in datas]
        return jsonify(answer_data)

@answer_blp.route('/<int:user_id>/<int:choice_id>')
    # 특정 답변 조회
class AnswerGet(MethodView):
    def get(self, user_id, choice_id):
        answers = Answer.query.filter_by(user_id=user_id,choice_id=choice_id).all()
        if not answers:
            return{"massage":"No found data"}
        return [answer.to_dict() for answer in answers]

