from flask_restful import Api, Resource
from flask import request, Response, send_file
from db.models import *
from datetime import datetime
import os
import config
from werkzeug.utils import secure_filename
#UPLOAD_FOLDER = 'D:\\University\\ENSE400\\Runtime-Terror\\Backend\\UploadImages'
UPLOAD_FOLDER = config.ImageStoragePath()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
class Image(Resource):
    def post(self):
        uploaded_image = request.files['img']
        if uploaded_image == None:
            return "No image uploaded", 400

        ## save the image to the folder
        file_name = secure_filename(uploaded_image.filename)
        time_uploaded = datetime.now().strftime("%Y%m%d%H%M%S")
        new_file_name  = time_uploaded + file_name
        mime_type = uploaded_image.mimetype
        path  = os.path.join(UPLOAD_FOLDER, new_file_name)
        uploaded_image.save(path)


        new_image = ImageEntry(
            label = "test",
            mime_type = mime_type,
            file_name = new_file_name,
            image_path = path
        )
        db.session.add(new_image)
        db.session.commit()

    def get(self, image_id):
        img  = ImageEntry.query.filter_by(id=image_id).first()
        return send_file(img.image_path, mimetype=img.mime_type)
