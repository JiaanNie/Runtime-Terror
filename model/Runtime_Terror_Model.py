"""
This model was roughly translated and inspired by the model described in the paper: 'Is object localization for free? –
Weakly-supervised learning with convolutional neural networks'
By M. Oquab, et.al.

Paper found at: https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Oquab_Is_Object_Localization_2015_CVPR_paper.pdf
accessed Feb. 2021
Lua/Torch code found at: https://www.di.ens.fr/willow/research/weakcnn/
accessed Feb. 2021
"""

import tensorflow as tf
from tensorflow.keras import models, layers, datasets
from tensorflow.keras.optimizers import Adam
import os
import pandas as pd
import numpy as np

from ImageBatching import ImageHandler

current_path = os.path.dirname(os.path.realpath(__file__))

train_image_paths = [current_path + '/train']
train_label_path = current_path + '/train'
test_image_paths = [current_path + '/train']
test_label_path = current_path + '/train'

numClasses = 1000
input_shape = (256,256,3)
training_batch_size = 128
testing_batch_size = int(training_batch_size * 0.0285)

train_image_handler = ImageHandler(training_batch_size, train_image_paths, train_label_path, input_shape)
test_image_handler = ImageHandler(testing_batch_size, test_image_paths, test_label_path, input_shape, label_name = '/test.csv')

"""
Feature Extractor translated into python and tensorflow.
Base code found in featureextractor.lua
Things to check added via inline comments
This makes up the first part of the model.
"""
model = models.Sequential()

model.add(layers.Conv2D(96, 11, 4, activation = 'relu', padding = 'same', input_shape = input_shape))
model.add(layers.MaxPool2D(pool_size=(3, 3), strides=(2,2), padding='valid', data_format=None))
model.add(layers.Conv2D(256, 5, 1, activation = 'relu', padding = 'same'))
model.add(layers.MaxPool2D(pool_size=(3, 3), strides=(2,2), padding='valid', data_format=None))
#model.add(layers.Conv2D(384, 3, 1, activation = 'relu', padding = 'same'))
model.add(layers.Conv2D(384, 3, 1, activation = 'relu', padding = 'same')) 
model.add(layers.Conv2D(256, 3, 1, activation = 'relu', padding = 'same')) 
model.add(layers.MaxPool2D(pool_size=(3, 3), strides=(2,2), padding='valid', data_format=None))
#model.add(layers.Conv2D(6144, 6, 1, activation = 'relu', padding = 'same')) 
model.add(layers.Conv2D(6144, 1, 1, activation = 'relu', padding = 'valid'))

model.summary()

"""
Adaptation Layers
Base code found in post-train.lua
"""
#added to see what happens
model.add(layers.GlobalAveragePooling2D())
model.add(layers.Dense(512))
model.add(layers.Dropout(0.4))
##################################
#model.add(layers.Conv2D(2048, 3, 1, activation = 'relu', padding = 'valid'))
#model.add(layers.Conv2D(1024, 3, 1, padding = 'valid'))
#model.add(layers.GlobalMaxPool2D())
model.add(layers.Dense(numClasses))
model.summary()


model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

num_images = 0
(train_images, train_labels) = train_image_handler.getNextBatch()
while len(train_images) > 0:
    (test_images, test_labels) = test_image_handler.getNextBatch()
    try:
        print("first_image:", train_images[0].filename)
        print("first label:", train_labels[0])
    except:
        pass
    history = model.fit(train_images, train_labels, epochs=25, validation_data=(test_images, test_labels))
    model.save('LandmarkRecognitionModel.h5')

    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
    (train_images, train_labels) = train_image_handler.getNextBatch()
    
print("accuracy:", text_acc)


