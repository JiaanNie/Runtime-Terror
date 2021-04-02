"""
Original code created by Kaggle user 'thanisornsr'
Code found on Kaggle.com, acessed Mar. 1 2021

Modifications by Allan Wambold
    - adjusted model to use Runtime Terror's dataset & csv files
    - adjusted model to use pre-trained weights (Imagenet)
    - added line to re-compile loaded model with new learning rate
"""

import numpy as np
import pandas as pd 
import os

from scipy import stats
import cv2
import glob
from keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dense
from tensorflow.keras import Model
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.models import load_model, Model
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.optimizers import Adam

import tensorflow as tf
import tensorflow.keras.layers as L
from collections import Counter

current_dir = os.path.dirname(os.path.realpath(__file__)) 

train_df=pd.read_csv(current_dir + '/../images_v2/train/train.csv') #edited - Allan Wambold Mar. 1, 2021
print(train_df.head())

landmark_counts=pd.value_counts(train_df["landmark_id"])
landmark_counts=landmark_counts.reset_index()
landmark_counts.rename(columns={"index":'landmark_ids','landmark_id':'count'},inplace=True)
landmark_counts

train_img_name = glob.glob('/../images_v2/train/*/*/*/*')

train_df["filename"] = train_df.id.str[0]+"/"+train_df.id.str[1]+"/"+train_df.id.str[2]+"/"+train_df.id+".jpg"
train_df["label"] = train_df.landmark_id.astype(str)
print(train_df.head(3))

n_class = len(np.unique(train_df.landmark_id.values))
print(n_class)

val_ratio = 0.2 
batch_size = 128

gen = ImageDataGenerator(validation_split=val_ratio)

train_gen = gen.flow_from_dataframe(
    train_df,
    directory="../images_v2/train/",
    x_col="filename",
    y_col="label",
    weight_col=None,
    target_size=(256, 256),
    color_mode="rgb",
    classes=None,
    class_mode="categorical",
    batch_size=batch_size,
    shuffle=True,
    seed = 44,
    subset="training",
    interpolation="nearest",
    validate_filenames=False)
    
val_gen = gen.flow_from_dataframe(
    train_df,
    directory="../images_v2/train/",
    x_col="filename",
    y_col="label",
    weight_col=None,
    target_size=(256, 256),
    color_mode="rgb",
    classes=None,
    class_mode="categorical",
    batch_size=batch_size,
    shuffle=True,
    seed = 44,
    subset="validation",
    interpolation="nearest",
    validate_filenames=False)
    
    
def my_model(input_shape,nclass,dropout, learning_rate = 0.001):
    base_model = MobileNetV2(weights = "imagenet", include_top = False)
    
    model_input = L.Input(input_shape)
    x = base_model(model_input)
    x = L.GlobalAveragePooling2D()(x)
    
    y = L.Dense(512,activation='relu')(x)
    y = L.Dropout(dropout)(y)
    y = L.Dense(512,activation='relu')(y)
    y = L.Dropout(dropout)(y)
    
    y_h = L.Dense(nclass, activation = 'softmax', name = 'Id')(y)
    
    model = Model(inputs=model_input, outputs= y_h)
    
    optimizer = Adam(learning_rate=learning_rate)
    
    model.compile(loss='categorical_crossentropy', optimizer = optimizer, metrics='accuracy')
    
    return model
model = my_model(input_shape = (224,224,3), nclass = n_class, dropout = 0.4)

model.summary()


model = load_model("best_model_weights_3.h5")
#model.compile(loss='categorical_crossentropy', optimizer = Adam(learning_rate = 0.0001), metrics = 'accuracy')

epochs = 50
train_steps = int(len(train_df)*(1-val_ratio))//batch_size
val_steps = int(len(train_df)*val_ratio)//batch_size

early_stopping = EarlyStopping(monitor='val_loss', mode='min',patience=6)
model_checkpoint = ModelCheckpoint("best_model_weights_4.h5", monitor='loss', save_best_only=True, verbose=1)
history = model.fit_generator(train_gen, steps_per_epoch=train_steps, epochs=epochs,validation_data=val_gen, validation_steps=val_steps, callbacks=[model_checkpoint, early_stopping])
model.save("last_model_3.h5")

