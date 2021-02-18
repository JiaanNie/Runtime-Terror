from flask_restful import Api, Resource
from flask import request, Response, send_file, jsonify
from db.models import *
from datetime import datetime
import os
import config
from werkzeug.utils import secure_filename
from collections import defaultdict
import shutil
from zipfile import ZipFile
import base64
#UPLOAD_FOLDER = 'D:\\University\\ENSE400\\Runtime-Terror\\Backend\\UploadImages'
UPLOAD_FOLDER = config.ImageStoragePath()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
class Image(Resource):
    def post(self):
        uploaded_image = request.files['img']
        print(uploaded_image)
        label = request.form["label"]
        if uploaded_image == None:
            return "No image uploaded", 400

        print(dir(uploaded_image))
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
            image_path = path,
            favorite = False
        )
        db.session.add(new_image)
        db.session.commit()

    def get(self):
        list_of_ids = []
        imgs  = ImageEntry.query.all()
        for img in imgs:
            details = {}
            details["id"] = img.id
            details["favorite"] = img.favorite
            list_of_ids.append(details)
        return jsonify(list_of_ids)

class FetchImageByID(Resource):
    def get(self, image_id):
        img = ImageEntry.query.filter_by(id=image_id).first()
        print(img.image_path)
        data = open(img.image_path, "rb").read()
        bytes = bytearray(data)
        return Response(bytes, mimetype=img.mime_type)

class FetchLabel(Resource):
    def get(self):
        result = []
        labels = ImageEntry.query.with_entities(ImageEntry.label).distinct().all()
        for lable in labels:
            result.append(lable[0])
        return result


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
                    shutil.copy(file.image_path, target_path)
                    #print("moving file over")
                except:
                    print(file.image_path, file.id, "image no longer exist")
        file_paths = []
        for root, dirs, files in os.walk(base_path):
            for file in files:
                path =  os.path.join(root, file)
                print(path)
                file_paths.append(path)
        with ZipFile('result.zip','w') as zip:
            for file in file_paths:
                zip.write(file)
        return send_file('result.zip', attachment_filename='capsule.zip', as_attachment=True, cache_timeout=0)

class Search(Resource):
    def post(self):
        ids = []
        text = request.json['text']
        # searchable_columns = ['file_name', 'mime_type', 'label']
        # for column in searchable_columns:
        #     result = ImageEntry.query.filter_by(getattr(ImageEntry, column).ilike("%"+text+"")).all()
        #     if result != []:
        #         query = query + result
        result = ImageEntry.query.filter(ImageEntry.file_name.like("%"+ text + "%")).all()
        result += ImageEntry.query.filter(ImageEntry.mime_type.like("%"+ text + "%")).all()
        result += ImageEntry.query.filter(ImageEntry.label.like("%"+ text + "%")).all()
        for img in result:
            ids.append(img.id)
        return jsonify(ids)

class FilterLabel(Resource):
    def get(self):
        filterd_ids = []
        param = request.args.to_dict()
        label = param["filter_by"]
        imgs = ImageEntry.query.filter_by(label=label).all()
        for img in imgs:
            details = {}
            details["id"] = img.id
            details["favorite"] = img.favorite
            filterd_ids.append(details)
        return jsonify(filterd_ids)

class ToggleFavorite(Resource):
    def put(self, image_id):
        img = ImageEntry.query.filter_by(id=image_id).first()
        img.favorite = not img.favorite
        db.session.add(img)
        db.session.commit()

class FetchFavoriteImages(Resource):
    def get(self):
        favorite_ids = []
        imgs = ImageEntry.query.filter_by(favorite=True).all()
        for img in imgs:
            details = {}
            details["id"] = img.id
            details["favorite"] = img.favorite
            favorite_ids.append(details)
        return jsonify(favorite_ids)
