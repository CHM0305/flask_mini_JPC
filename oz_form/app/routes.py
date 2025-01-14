from flask import Blueprint, jsonify, request
from .views import users, questions, choices, answers, images
from app.views import answers,choices,images,questions,users
# 블루프린트 정의
api = Blueprint("api", __name__)

us_blp=users.user_blp
ans_blp=answers.answer_blp
qu_blp=questions.question_blp
im_blp=images.image_blp
ch_blp=choices.choice_blp

# 사용자 관련 라우트
@us_blp.route("/users", methods=["GET"])
def get_users():
    user_list = users.get_all_users()
    return jsonify([user.to_dict() for user in user_list]), 200

@us_blp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({"error": "User not found"}), 404

@us_blp.route("/users", methods=["POST"])
def create_user():
    data = request.json
    try:
        new_user = users.create_user(data)
        return jsonify(new_user.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# 질문 관련 라우트
@qu_blp.route("/questions", methods=["GET"])
def get_questions():
    question_list = questions.get_all_questions()
    return jsonify([question.to_dict() for question in question_list]), 200

@qu_blp.route("/questions/<int:question_id>", methods=["GET"])
def get_question(question_id):
    question = questions.get_question_by_id(question_id)
    if question:
        return jsonify(question.to_dict()), 200
    return jsonify({"error": "Question not found"}), 404

@qu_blp.route("/questions", methods=["POST"])
def create_question():
    data = request.json
    try:
        new_question = questions.create_question(data)
        return jsonify(new_question.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# 선택지 관련 라우트
@ch_blp.route("/choices", methods=["GET"])
def get_choices():
    choice_list = choices.get_all_choices()
    return jsonify([choice.to_dict() for choice in choice_list]), 200

@ch_blp.route("/choices/<int:choice_id>", methods=["GET"])
def get_choice(choice_id):
    choice = choices.get_choice_by_id(choice_id)
    if choice:
        return jsonify(choice.to_dict()), 200
    return jsonify({"error": "Choice not found"}), 404

@ch_blp.route("/choices", methods=["POST"])
def create_choice():
    data = request.json
    try:
        new_choice = choices.create_choice(data)
        return jsonify(new_choice.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# 답변 관련 라우트
@ans_blp.route("/answers", methods=["GET"])
def get_answers():
    answer_list = answers.get_all_answers()
    return jsonify([answer.to_dict() for answer in answer_list]), 200

@ans_blp.route("/answers/<int:answer_id>", methods=["GET"])
def get_answer(answer_id):
    answer = answers.get_answer_by_id(answer_id)
    if answer:
        return jsonify(answer.to_dict()), 200
    return jsonify({"error": "Answer not found"}), 404

@ans_blp.route("/answers", methods=["POST"])
def create_answer():
    data = request.json
    try:
        new_answer = answers.create_answer(data)
        return jsonify(new_answer.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# 이미지 관련 라우트
@im_blp.route("/images", methods=["GET"])
def get_images():
    image_list = images.get_all_images()
    return jsonify([image.to_dict() for image in image_list]), 200

@im_blp.route("/images/<int:image_id>", methods=["GET"])
def get_image(image_id):
    image = images.get_image_by_id(image_id)
    if image:
        return jsonify(image.to_dict()), 200
    return jsonify({"error": "Image not found"}), 404

@im_blp.route("/images", methods=["POST"])
def create_image():
    data = request.json
    try:
        new_image = images.create_image(data)
        return jsonify(new_image.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
