from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from app.models import Image

# 블루프린트 설정
image_blp = Blueprint(
    "Images", "images", description="Operations on images", url_prefix="/images"
)

@image_blp.route("/")
class ImageList(MethodView):
    # 전체 이미지 조회
    def get(self):
        """
        Get a list of all images.
        """
        images = Image.query.all() or []
        return jsonify(
            [
                {
                    "id": image.id,
                    "url": image.url,
                    "type": image.type.value
                    if hasattr(image.type, "value")
                    else image.type,
                    "created_at": image.created_at.isoformat(),
                    "updated_at": image.updated_at.isoformat(),
                }
                for image in images
            ]
        ), 200

    # 새로운 이미지 생성
    def post(self):
        """
        Create a new image.
        """
        data = request.json

        # 필수 데이터 확인
        if not data.get("url") or not data.get("type"):
            return jsonify({"error": "The 'url' and 'type' fields are required"}), 400

        new_image = Image(url=data["url"], type=data["type"])
        db.session.add(new_image)
        db.session.commit()

        return jsonify({"message": "Image created successfully"}), 201


@image_blp.route("/<int:image_id>")
class ImageResource(MethodView):
    # 특정 이미지 상세 조회
    def get(self, image_id):
        """
        Get details of a specific image by ID.
        """
        image = Image.query.get(image_id)
        if not image:
            return jsonify({"error": f"Image with ID {image_id} not found"}), 404

        return jsonify(
            {
                "id": image.id,
                "url": image.url,
                "type": image.type.value
                if hasattr(image.type, "value")
                else image.type,
                "created_at": image.created_at.isoformat(),
                "updated_at": image.updated_at.isoformat(),
            }
        )

    # 특정 이미지 수정
    def put(self, image_id):
        """
        Update details of a specific image by ID.
        """
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
        """
        Delete a specific image by ID.
        """
        image = Image.query.get(image_id)
        if not image:
            return jsonify({"error": f"Image with ID {image_id} not found"}), 404

        db.session.delete(image)
        db.session.commit()
<<<<<<< HEAD
        return jsonify({"message": "Image deleted successfully"}), 204
=======
        return jsonify({"message": "Image deleted successfully"}), 204
>>>>>>> d9031b5f32baf3354385d65704abf2ae35567a00
