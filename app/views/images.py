from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from app.models import Image

# 블루프린트 설정
image_blp = Blueprint(
    "Image", "image", description="Operations on Image", url_prefix="/image"
)

@image_blp.route('/')
class ImageList(MethodView):
    # 전체 이미지 조회
    def get(self):
        images = Image.query.all()
        images_data=[image.to_dict() for image in images]
        return jsonify(images_data)

    # 새로운 이미지 생성
    def post(self):
        image_data = request.json
        if not image_data.get("url") or not image_data.get("type"):
            return jsonify({"error": "The 'url' and 'type' fields are required"}), 400

        new_image = Image(url=image_data["url"], type=image_data["type"])
        db.session.add(new_image)
        db.session.commit()

        return jsonify({"message": "Image created successfully"}), 201


@image_blp.route('/<int:image_id>')
class ImageResource(MethodView):
    # 특정 이미지 상세 조회
    def get(self, image_id):
        image = Image.query.get_or_404(image_id)
        if not image:
            return jsonify({"error": f"Image with ID {image_id} not found"}), 404

        return jsonify(image.to_dict()),200

    # 특정 이미지 수정
    def put(self, image_id):
        image = Image.query.get(image_id)
        if not image:
            return jsonify({"error": f"Image with ID {image_id} not found"}), 404

        data = request.json
        image.url = data["url"]
        image.type = data["type"]
        db.session.commit()
        return jsonify({"message": "Image updated successfully"}), 200

    # 특정 이미지 삭제
    def delete(self, image_id):
        image = Image.query.get(image_id)
        if not image:
            return jsonify({"error": f"Image with ID {image_id} not found"}), 404

        db.session.delete(image)
        db.session.commit()
        return jsonify({"message": "Image deleted successfully"}), 204

#이미지 수정 조회/ 특정 이미지 수정 조회 삭제 완료
@image_blp.route('/main')
class ImageMain(MethodView):
    def get(self):
        main_img = Image.query.filter_by(type="main").first()

        if main_img is None:
            return jsonify({"msg":"No main image found"}), 404

        return jsonify({"image": main_img.url }),200
                