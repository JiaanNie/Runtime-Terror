from flask_restful import Api, Resource
from flask import request, Response, send_file, jsonify
from db.models import *
from datetime import datetime
import requests as python_requests
import os
import config
from werkzeug.utils import secure_filename
from collections import defaultdict
import shutil
from zipfile import ZipFile
import base64
import random
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.models import Sequential, save_model, load_model
import numpy as np
from PIL import Image as pil_image
from google.cloud import vision
import io
import time
import uuid
# import panda as pd
#UPLOAD_FOLDER = 'D:\\University\\ENSE400\\Runtime-Terror\\Backend\\UploadImages'
UPLOAD_FOLDER = config.ImageStoragePath()
# model = load_model(config.MLModelPath() + "model.h5")
# data = pd.read_csv(config.MLModelPath()+ "label_name.csv")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
class Image(Resource):
    def post(self):
        user_uuid = request.headers["user"]
        class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']
        uploaded_image = request.files['img']
        if uploaded_image == None:
            return "No image uploaded", 400
        # self.label = request.form["label"]
        ## save the image to the folder
        file_name = secure_filename(uploaded_image.filename)
        time_uploaded = datetime.now().strftime("%Y%m%d%H%M%S")
        new_file_name  = time_uploaded + file_name
        mime_type = uploaded_image.mimetype
        path  = os.path.join(UPLOAD_FOLDER, new_file_name)
        uploaded_image.save(path)
        im = np.array(pil_image.open(path))
        print(im.shape)
        if im.shape == (224,224,3):
            im = np.expand_dims(im, axis=0)
            prediction = model.predict(im)
            index =np.argmax(prediction)
            self.label = class_names[index]
        self.label = self.detect_landmarks(path)
        print(self.label)
        new_image = ImageEntry(
            label = self.label,
            mime_type = mime_type,
            file_name = new_file_name,
            image_path = path,
            favorite = False,
            user_id = user_uuid
        )
        db.session.add(new_image)
        db.session.commit()
    def detect_landmarks(self, path):
        client = vision.ImageAnnotatorClient()
        with io.open(path, 'rb') as image_file:
            content = image_file.read()
        image = vision.Image(content=content)
        response = client.landmark_detection(image=image)
        if not response:
            return None
        else:
            return response.landmark_annotations[0].description


    def get(self):
        list_of_ids = []
        user_uuid = request.headers["user"]
        imgs  = ImageEntry.query.filter_by(user_id=user_uuid).all()
        for img in imgs:
            details = {}
            details["id"] = img.id
            details["favorite"] = img.favorite
            list_of_ids.append(details)
        return jsonify(list_of_ids)

class FetchImageByID(Resource):
    def get(self, image_id):
        print(image_id)
        img = ImageEntry.query.filter_by(id=image_id).first()
        print(img.image_path)
        data = open(img.image_path, "rb").read()
        bytes = bytearray(data)
        return Response(bytes, mimetype=img.mime_type)

class FetchLabel(Resource):
    def get(self):
        user_uuid = request.headers["user"]
        result = []
        labels = ImageEntry.query.filter_by(user_id=user_uuid).with_entities(ImageEntry.label).distinct().all()
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
        user_uuid = request.headers["user"]
        text = request.json['text']
        result = ImageEntry.query.filter_by(user_id=user_uuid).filter(ImageEntry.file_name.like("%"+ text + "%")).all()
        result += ImageEntry.query.filter_by(user_id=user_uuid).filter(ImageEntry.mime_type.like("%"+ text + "%")).all()
        result += ImageEntry.query.filter_by(user_id=user_uuid).filter(ImageEntry.label.like("%"+ text + "%")).all()
        for img in result:
            ids.append(img.id)
        return jsonify(ids)

class FilterLabel(Resource):
    def get(self):
        filterd_ids = []
        param = request.args.to_dict()
        label = param["filter_by"]
        user_uuid = request.headers["user"]
        imgs = ImageEntry.query.filter_by(user_id=user_uuid).filter_by(label=label).all()
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
        user_uuid = request.headers["user"]
        imgs = ImageEntry.query.filter_by(user_id=user_uuid).filter_by(favorite=True).all()
        for img in imgs:
            details = {}
            details["id"] = img.id
            details["favorite"] = img.favorite
            favorite_ids.append(details)
        return jsonify(favorite_ids)

class FetchPlaceDetails(Resource):
    def get(self):
        list_of_name = ["Eiffel Tower", "Great Wall of China", "Leaning Tower of Pisa", "Pyramid of Giza", "Sydney Opera House in Australia", "Statue of Liberty in the USA", "Taj Mahal in India"]
        index = random.randint(0,6)
        google_api_key = config.GetGooglePlaceAPIKey()
        input = list_of_name[index]
        place_detail = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key={}'
        res = python_requests.get(place_detail.format(input, google_api_key))
        res = res.json()['candidates'][0]
        print(res['name'])
        photo_reference = res['photos'][0]['photo_reference']
        location = res['geometry']['location']
        response = {
            'photo_reference': photo_reference,
            'name': res['name'],
            'location': location
        }
        return jsonify(response)

class Login(Resource):
    def post(self):
        email = request.json['email']
        password = request.json['password']
        print(email, password)
        q = User.query.filter((User.email==email) & (User.password==password)).first()
        if q is not None:
            return q.uuid
        else:
            return 404, "invaild account"

class Register(Resource):
    def post(self):
        email = request.json['email']
        password = request.json['password']
        q = User.query.filter_by(email=email).first()
        if q is None:
            new_user = User(
                uuid= uuid.uuid1(),
                email=email,
                password=password
            )
            db.session.add(new_user)
            db.session.commit()
        else:
            return 409, "Account already exits!"
