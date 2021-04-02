"""
This script was used to give the landmark classes new landmark_ids once the sub-set had been taken from the dataset
"""
import os
import pandas as pd

actual_path = os.path.dirname(os.path.abspath(__file__))

csv_path = 'C:/Users/Allan/Desktop/477 Model Files/csv' # path to csv files

train_csv = csv_path + '/train_reduced_v3.csv' # csv to be re-identified
new_train = csv_path + '/train_v4_reidentified.csv' #where to save train csv
new_label_name = csv_path + '/train_label_to_category_v3.csv' #where to save label name map
old_label_name = csv_path + '/train_label_to_category.csv'

print('loading csv files')
label_to_category_csv_file = pd.read_csv(old_label_name)
train_csv_file = pd.read_csv(train_csv)

train_csv_file = train_csv_file.sort_values(by=['landmark_id'])
current_landmark_ids = train_csv_file['landmark_id'].unique().tolist()
print(train_csv_file['landmark_id'].unique())
print(train_csv_file.head)

print(len(current_landmark_ids))

i = 0
for id in current_landmark_ids:
    train_csv_file.loc[train_csv_file['landmark_id'] == id, 'landmark_id'] = i
    label_to_category_csv_file.loc[label_to_category_csv_file['landmark_id'] == id, 'landmark_id'] = i
    i+=1
    if i % 25 == 0:
        print(i, '/', len(current_landmark_ids))

train_csv_file = train_csv_file.sample(frac=1) # shuffle dataframe because it was sorted above
train_csv_file.to_csv(new_train, index=False)
label_to_category_csv_file.to_csv(new_label_name, index=False)

