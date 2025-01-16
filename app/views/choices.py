from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from app.models import Choices, db

choices_blp = Blueprint('Choices', 'choices',description="Operations on Choices", url_prefix='/choice')

@choices_blp.route('/')
#선택지 생성
class ChoicesList(MethodView):
    def post(self):
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
    def get(self):
        choices = Choices.query.all()
        return jsonify ([choice.to_dict() for choice in choices])

# 선택지 가져오기
@choices_blp.route('/<int:question_id>')
class ChoiceResource(MethodView):
    def get(self, question_id):
            #선택지에 맞는 아이디 값을 설정해줘야하니 아이디에 맞는 값이 필요함 filter_by
            #choices = Choices.query.get_or_404(question_id) <- 아이디 값에 맞는 모든 것을 불러올 수 없음.
            choices = Choices.query.filter_by(question_id=question_id).all()
            return jsonify({
                            "choices":[
                                {"id": choices.id, "content": "옵션 1", "is_active": choices.is_active},
                                {"id": choices.id, "content": "옵션 2", "is_active": choices.is_active},
                                {"id": choices.id, "content": "옵션 3", "is_active": choices.is_active},
                                {"id": choices.id, "content": "옵션 4", "is_active": choices.is_active},
                                {"id": choices.id, "content": "옵션 5", "is_active": choices.is_active}
                            ]
                        })
                
    def delete(self, question_id):
        # 특정 질문에 해당하는 선택지 삭제
        choices = Choices.query.filter_by(question_id=question_id).all()
        for choice in choices:
            db.session.delete(choice)
        db.session.commit()
        return jsonify({'msg': 'Successfully deleted choices'}), 200



