from flask_restful import Api, Resource
from flask import request, Response, send_file
from db.models import *
from datetime import datetime
import os
import config
from werkzeug.utils import secure_filename
from collections import defaultdict
import shutil
from zipfile import ZipFile
#UPLOAD_FOLDER = 'D:\\University\\ENSE400\\Runtime-Terror\\Backend\\UploadImages'
UPLOAD_FOLDER = config.ImageStoragePath()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
class Image(Resource):
    def post(self):
        uploaded_image = request.files['img']
        label = request.form["label"]
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
            label = label,
            mime_type = mime_type,
            file_name = new_file_name,
            image_path = path
        )
        db.session.add(new_image)
        db.session.commit()

    def get(self, image_id):
        img  = ImageEntry.query.filter_by(id=image_id).first()
        return send_file(img.image_path, mimetype=img.mime_type)

class SorteImage(Resource):
    def get(self):
        base_path = config.SortedImagesBasePath()
        access_right = 0o755
        sorted_imgs = defaultdict(list)
        imgs = ImageEntry.query.all()
        for img in imgs:
            sorted_imgs[img.label].append(img)
        for label in sorted_imgs.keys():
            target_path  = base_path+"\\"+label
            try:
                os.mkdir(target_path, access_right)
            except:
                print("folder already exist")
            for file in sorted_imgs[label]:
                try:
                    ## use the copy function for testing after everything is working use the move function
                    #shutil.copy(file.image_path, target_path)
                    print("moving file over")
                except:
                    print(file.image_path, file.id, "image no longer exist")
        file_paths = []
        for root, dirs, files in os.walk(base_path):
            for file in files:
                path =  os.path.join(root, file)
                print(path)
                file_paths.append(path)
        with ZipFile(base_path+'\\result.zip','w') as zip:
            for file in file_paths:
                zip.write(file)
        return send_file(base_path+'\\result.zip', attachment_filename='capsule.zip', as_attachment=True)
