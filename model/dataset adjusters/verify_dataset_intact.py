"""
This script is used to verify that the dataset is still intact after any modifications.
It will verify that all images are in the correct directory, all images have a label, and all labels have images.
- Each test will generate a CSV file to store the ID's of any images/labels that fail the tests.
- If no CSVs are generated, then all tests passed.
"""

from PIL import Image
import os
import pandas as pd

imagePath1 = 'E:/477_reduced/train'
CSVPath = 'E:/477_reduced/train/train.csv'
"""
imagePath1 = 'E:/477_reduced/test'
CSVPath = 'E:/477_reduced/test/test.csv'
"""

#dirname = os.path.dirname(__file__)
#imagePath1 = os.path.join(dirname, '/train')
#CSVPath = imagePath1
print(imagePath1)
# this iterates through all the image directories and ensures all the images contained within them are where they are supposed to be
# images are sorted by id where the first 3 characters are the sub directory (eg image 01701adf5 will be located in 0/1/7/)
def ensureImagesInCorrectFolder(path1, csvPath):
    paths = [path1]
    for path in paths:
        print("Processing path:", path)
        for dir_level_one in os.listdir(path):
            dirOne = path + '\\' + dir_level_one
            if os.path.isdir(dirOne):
                for dir_level_two in os.listdir(dirOne):
                    dirTwo = dirOne + '\\' + dir_level_two
                    for dir_level_three in os.listdir(dirTwo):
                        dirThree = dirTwo + '\\' + dir_level_three
                        #print("Checking images in", dirThree)
                        for image in os.listdir(dirThree):                           
                            if dir_level_one+dir_level_two+dir_level_three != image[0:3]:
                                print("misplaced image found:", image, "is being added to the mis-located_images csv file.")
                                out = pd.DataFrame({'imageID' : [image], 'found in' : [dirThree]})  
                                try:
                                    IncorrectImages = pd.read_csv(csvPath + '\\mis-located_images.csv')
                                except:
                                    IncorrectImages = pd.DataFrame()
                                IncorrectImages = IncorrectImages.append(out)
                                IncorrectImages.to_csv(csvPath + '\\mis-located_images.csv',index=False) 

                            


#iterates through all images and ensures each image has a label corresponding to it.
def checkImagesAgainstLabels(path1, csvPath):

    print("loading label csv file")
    labels = pd.read_csv(path1 + '\\train.csv')
    print("labels loaded")
    
    organizedLabels = {}
    for label in labels['id']:
        labelIdentifier = label[0:3]
        if not labelIdentifier in organizedLabels:
            organizedLabels[labelIdentifier] = []   
        organizedLabels[labelIdentifier].append(label)
        
        
    #print(labels.head)
    #print(labels.info)
    missingCSV = csvPath + '\\ImagesWithoutLabels.csv'

    paths = [path1]
    for path in paths:
        print("image path:", path)
        for dir_level_one in os.listdir(path):
            dirOne = path + '\\' + dir_level_one
            if os.path.isdir(dirOne):
                for dir_level_two in os.listdir(dirOne):
                    dirTwo = dirOne + '\\' + dir_level_two
                    print("Checking images in", dirTwo)
                    dirTwo_listdir = os.listdir(dirTwo)                    
                    i = 0
                    for dir_level_three in dirTwo_listdir:
                        i+=1
                        #print("working on", i, "/", len(dirTwo_listdir))
                        dirThree = dirTwo + '\\' + dir_level_three
                        for image in os.listdir(dirThree):
                            image = os.path.splitext(image)[0] #remove file ext.
                            idFound = False
                            imageIdentifier = image[0:3]
                            for label in organizedLabels[imageIdentifier]:
                                if label == image:
                                    idFound = True
                                    break
                            if not idFound:
                                print("Image", image,"does not have a label.")
                                out = pd.DataFrame({'imageID' : [image]})  
                                try:
                                    noLabel = pd.read_csv(csvPath + '\\ImagesWithoutLabels.csv')
                                except:
                                    noLabel = pd.DataFrame() 
                                noLabel = noLabel.append(out)
                                noLabel.to_csv(csvPath + '\\ImagesWithoutLabels.csv', index=False)


          
#iterates through all labels and ensures each label has an image corresponding to it.
def checkLabelsAgainstImages(path1, csvPath):
    print("loading label csv file")
    labels = pd.read_csv(path1 + '\\train.csv')
    print("labels loaded")
    totalLength = len(labels['id'])
    i = 0
    for label in labels['id']:
        i+=1
        if i%25000 == 0:
            percentDone = (i / totalLength) * 100
            print(percentDone, '%')
        dirOne = label[0:1]
        dirTwo = label[1:2]
        dirThree = label[2:3]
        imageFound = False
        for path in [path1]:
            imageDirectory = path + '\\' + dirOne + '\\' + dirTwo + '\\' + dirThree
            try:
                for image in os.listdir(imageDirectory):
                    image = os.path.splitext(image)[0] #remove file ext.
                    if image == label:
                        imageFound = True
                        break
                if imageFound:
                    break
            except:
                pass
        if not imageFound:
            print("image not found for label", label)
            try:
                noImage = pd.read_csv(csvPath + '\\LabelsWithoutImages.csv')
            except:
                noImage = pd.DataFrame() 
            out = pd.DataFrame({'imageID' : [label]})  
            noImage = noImage.append(out)
            noImage.to_csv(csvPath + '\\LabelsWithoutImages.csv', index=False)
            
#ensureImagesInCorrectFolder(imagePath1, CSVPath)
#checkImagesAgainstLabels(imagePath1, CSVPath)
checkLabelsAgainstImages(imagePath1, CSVPath)







