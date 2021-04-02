"""
This script is used to reduce the number of landmarks in the training csv file to remove landmarks that don't appear often enough for training
This version does not assume label numbers
"""

import os
import pandas as pd

new_csv = 'C:/Users/Allan/Desktop/477 model files/csv/train_reduced_v3.csv'
old_csv = 'C:/Users/Allan/Desktop/477 model files/csv/train_v3_reidentified.csv'

old_df = pd.read_csv(old_csv)

# find the landmark_ids with the most occurances
n = 1000
most_common_ids = old_df['landmark_id'].value_counts()[:n].index.tolist()
print(most_common_ids)

print("creating list of all possible ids")
to_remove = old_df['landmark_id'].unique().tolist()


print('removing wanted ids from list of unwanted ids')
for id in most_common_ids:
    to_remove.remove(id)

print('removing unwanted rows from dataframe')
i = 0
for id in to_remove:
    old_df = old_df[old_df.landmark_id != id]
    
    if i % 100 == 0:
        print(i, 'ids removed')
        #print(old_df.head)
    i+=1

old_df.to_csv(new_csv, index=False)
