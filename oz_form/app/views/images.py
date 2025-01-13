from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from models import Image

image_blp = Blueprint('Images', 'images', description='Operations on images', url_prefix='/images')

#이미지 조회 및 생성
@image_blp.route('/')
class ImageList(MethodView):
    #이미지 조회
    def get(self):
        images = Image.query.all()
        return jsonify([
            {
                "id": image.id,
                "url": image.url,
                "type": image.type.value if hasattr(image.type, "value") else image.type,
                "created_at": image.created_at.isoformat(),
                "updated_at": image.updated_at.isoformat(),
            } for image in images
        ])
    #이미지 생성
    def post(self):
        data = request.json
        new_image = Image(url=data['url'], type=data['type'])
        db.session.add(new_image)
        db.session.commit()
        return jsonify({"message": "Image created successfully"}), 201

#특정 이미지 조회 후 삭제, 수정
@image_blp.route('/<int:image_id>')
class ImageResource(MethodView):
    #특정 이미지 조회
    def get(self, image_id):
        image = Image.query.get_or_404(image_id)
        return jsonify({
            "id": image.id,
            "url": image.url,
            "type": image.type.value if hasattr(image.type, "value") else image.type,
            "created_at": image.created_at.isoformat(),
            "updated_at": image.updated_at.isoformat(),
        })
    #특정 이미지 수정
    def put(self, image_id):
        image = Image.query.get_or_404(image_id)
        data = request.json
        image.url = data['url']
        image.type = data['type']
        db.session.commit()
        return jsonify({"message": "Image updated successfully"})
    #특정 이미지 삭제
    def delete(self, image_id):
        image = Image.query.get_or_404(image_id)
        db.session.delete(image)
        db.session.commit()
        return jsonify({"message": "Image deleted successfully"})
