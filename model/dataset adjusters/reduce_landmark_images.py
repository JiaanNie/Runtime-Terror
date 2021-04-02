"""
This script was used to reduce the number of images that belonged to a specific landmark
- The original dataset was VERY unbalanced and so to reduce the natural bias in the model, some landmarks needed to be reduced.
"""
import os
import pandas as pd

actual_path = os.path.dirname(os.path.abspath(__file__))

csv_path = 'C:/Users/Allan/Desktop/477 Model Files/train_v2_reidentified.csv'

current_image_path = actual_path + '../images/train/'
desired_image_path = actual_path + '../images/temp/'

csv_file = pd.read_csv(csv_path)

most_common_ids = csv_file['landmark_id'].value_counts().index.tolist()
id_to_reduce = most_common_ids[0]

path = desired_image_path + '/train/'

to_reduce = csv_file.loc[csv_file['landmark_id'] == 4]
remove_length = to_reduce['id'].size
to_reduce = to_reduce[:int(remove_length * 0.9)]
print(csv_file.head)
print(int(remove_length * 0.9))
i = 0
for id in to_reduce['id']:
    d1 = id[0]
    d2 = id[1]
    d3 = id[2]
    dir = d1 + '/' + d2 + '/' + d3 + '/'
    if not os.path.exists(path + dir):
        os.makedirs(path + dir)
    os.replace(current_image_path + dir + id + '.jpg', path + dir + id + '.jpg')
    csv_file = csv_file[csv_file.id != id]
    i+=1
    if i%500 == 0:
        print(i, 'images moved')

csv_file.to_csv(current_image_path + 'train.csv', index=False)

