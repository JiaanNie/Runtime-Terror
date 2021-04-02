"""
The purpose of this script is to move images from one directory to another
- Will split the dataset into test & training batches at a ratio of 80:20
- This was used to reduce the dataset into a sub-set by creating a csv of the images that we wanted to keep
  and using that csv here to move the images into a new location
"""

import os
import pandas as pd

actual_path = os.path.dirname(os.path.abspath(__file__))

csv_path = 'C:/Users/Allan/Desktop/477 Model Files/train_v2.csv'

current_image_path = 'E:/477/train/'
desired_image_path = 'E:/477_reduced'

csv_file = pd.read_csv(csv_path)

print(len(csv_file['landmark_id'].unique().tolist()))


csv_len = len(csv_file['landmark_id'].tolist())
print(csv_len)
train = csv_file.iloc[:int(0.8*csv_len)]
test = csv_file.iloc[int(0.8*csv_len):]

print(train.head)
print(test.head)


path = desired_image_path + '/train/'
train.to_csv(path+'train.csv', index=False)

i = 0
for id in train['id']:
    d1 = id[0]
    d2 = id[1]
    d3 = id[2]
    dir = d1 + '/' + d2 + '/' + d3 + '/'
    #print('move', current_image_path + dir + id + '.jpg to', desired_image_path + dir + id + '.jpg')
    if not os.path.exists(path + dir):
        os.makedirs(path + dir)
    os.replace(current_image_path + dir + id + '.jpg', path + dir + id + '.jpg')
    i+=1
    if i%500 == 0:
        print(i, 'images moved')

path = desired_image_path + '/test/'
test.to_csv(path+'test.csv', index=False)

i = 0
for id in test['id']:
    d1 = id[0]
    d2 = id[1]
    d3 = id[2]
    dir = d1 + '/' + d2 + '/' + d3 + '/'
    #print('move', current_image_path + dir + id + '.jpg to', desired_image_path + dir + id + '.jpg')
    if not os.path.exists(path + dir):
        os.makedirs(path + dir)
    os.replace(current_image_path + dir + id + '.jpg', path + dir + id + '.jpg')
    i+=1
    if i%500 == 0:
        print(i, 'images moved')
