"""
This script was used to scrape the label names using the provided urls to the Wikimedia pages where the images are found.
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

startIndex = 0

labels = 'C:/Users/Allan/Desktop/Final csv/train_label_to_category.csv' #load location
label_csv = pd.read_csv(labels)


labels = 'C:/Users/Allan/Desktop/Final csv/train_label_names.csv' #save location
try:
    save_label_csv = pd.read_csv(labels)
    label_names = save_label_csv['name'].tolist()
    print(len(label_names))
except:
    print("label names empty, creating from new")
    startIndex = 0
    label_names = []
    

print("CSV loaded")
i = 0

label_urls = label_csv['category']
print(label_urls.size, 'labels to scrape.')
landmark_ids = label_csv['landmark_id']
exception = False

for url in label_urls[startIndex:]:
    attempts = 0
    while attempts < 3:
        try:            
            html_content = requests.get(url).text
            attempts = 10
        except:
            print("url:", url, "failed with", requests.get(url))
            attempts += 1
            
    if attempts == 3:
        exception = True
        break
        
    soup = BeautifulSoup(html_content, 'lxml')
    title = str(soup.find('title'))
    label_names.append(title[16:-28])
    
    i+=1
    if i%250 == 0:
        print(i, "names scraped")
        print("Saving progress")
        data = {'name': label_names} 
        df = df = pd.DataFrame(data) 
        df.to_csv(labels, index=False)
        print("Save complete")

if not exception:
    print("names loaded, saving to CSV")  

    label_csv['name'] = label_names
    label_csv.to_csv('C:/Users/Allan/Desktop/Final csv/label_names.csv', index=False)