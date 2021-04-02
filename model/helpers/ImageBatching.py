import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from PIL import Image


class ImageHandler(object):
    def __init__(self, BatchSize, ImagePaths, LabelPath, ImageShape = None, label_name = '/train.csv'):
        self.batchSize = BatchSize
        self.imagePaths = ImagePaths
        self.labelPath = LabelPath
        self.batchNumber = 0
        self.imageShape = ImageShape
        self.labels = None
        self.label_name = label_name
        if self.batchSize < 1:
            print("Warning, invalid batch size will result in the image handler not performing correctly. Batch size set to 100.")
            self.batchSize = 100
        if not self.imageShape:
            print("image shape not provided, images will be returned in their original shape. This does not guarantee all images are of the same shape.")
        elif len(self.imageShape) != 2 and len(self.imageShape) != 3 and self.imageShape != None:
            print("invalid image shape, setting shape to None.")
            self.imageShape = None
            
    def resetBatchNum(self):
        self.batchNumber = 0
    
    def getNextBatch(self):
        print("Retrieving Batch:", self.batchNumber)
        batch = self.getImageBatch()
        self.batchNumber += 1
        return batch
        
    #This does not fully sort labels, it re-organizes them into a dictionary using the first 3 characters of the IDs (this corresponds to images in the same directory)
    def sortLabels(self):
        numImages = 0
        file = open(self.labelPath + '/train.csv')
        label_file = csv.reader(file, delimiter=",")
        label_file = list(label_file)
        length = len(label_file)
        train_len = int(length * 0.8)
        test_len = int(length * 0.2)
        print("total length of image labels:", length)
        print("total number of training images:", train_len)
        print("total number of test images:", test_len)
        if self.label_name == '/train.csv':
            label_file = label_file[1:train_len]
        else:
            label_file = label_file[train_len:]
        self.labels = {}
        print("length of label file after split:", len(label_file))
        for label in label_file:
            numImages += 1
            labelIdentifier = label[0][0:3]
            if not labelIdentifier in self.labels:
                self.labels[labelIdentifier] = []   
            self.labels[labelIdentifier].append(label)
        print("number of images:",numImages)    
        
        
    """
     The images being used in our project are stored in a file strcuture:
     
     base directory/
                ....0/
                    ....0/
                        ....0/
                            ....images here
                            1/
                            .
                            .
                            .
                            f/
                        1/
                        .
                        .
                        .
                        f/
                    1/
                    .
                    .
                    .
                    f/
    example of accessing an image: 
        base/2/3/d/imageName.jpg
    """    
    # This method takes a given batch number, batch size, and image location path
    # and uses them to load a batch of images for use in training the model.
    # This method should not be called directly, instead use 'getNextBatch()' to get the next image batch
    # and 'resetBatchNum()' to reset the current batch number to 0
    def getImageBatch(self):
        currentImageNum = self.batchNumber * self.batchSize # the number of images that have already been put into batches
        numImagesProcessed = 0 # used to track how many images have been in the previous directories while filling current batch
        
        batchImages = []
        batchLabels = np.array([])
      
        if not self.labels: #labels have not been sorted yet
            print("Labels have not yet been initialized, loading and organizing labels now...")
            self.sortLabels()
            print("finished sorting labels.")
        # the dataset is large, this is to handle the case that there are multiple storage devices holding the images
        imagePaths = self.imagePaths
        if not type(imagePaths) == list: 
            imagePaths = [imagePaths]
            
        for path in imagePaths:
            
            for dir_level_one in os.listdir(path):
                dirOne = path + '/' + dir_level_one
                if os.path.isdir(dirOne): # base folder contains files, and directories; we only want the directories

                    for dir_level_two in os.listdir(dirOne):
                        dirTwo = dirOne + '/' + dir_level_two
                    
                        for dir_level_three in os.listdir(dirTwo):
                            dirThree = dirTwo + '/' + dir_level_three
                            
                            images = os.listdir(dirThree)
                            if currentImageNum < len(images) + numImagesProcessed: 
                                startImage = 0
                                if currentImageNum - numImagesProcessed >= 0:
                                    startImage = currentImageNum - numImagesProcessed
                                for image in images[startImage:]:
                                        # load the images into the batch
                                        #im = Image.open(dirThree + '/' + image)
                                        #if self.imageShape: # image shape has been provided, re-shape before adding to batch
                                        #    im = im.resize((self.imageShape[0], self.imageShape[1]))                                         
                                        #im = np.asarray(im)
                                        #batchImages.append(im)  
                                        # load the label into the batch
                                        imageID = os.path.splitext(image)[0] #drop the file ext.
                                        for label in self.labels[imageID[0:3]]:
                                            if label[0] == imageID:
                                                im = Image.open(dirThree + '/' + image)
                                                if self.imageShape:
                                                    im = im.resize((self.imageShape[0], self.imageShape[1]))
                                                im = np.asarray(im)
                                                batchLabels = np.append(batchLabels, int(label[2]))
                                                batchImages.append(im)
                                                break
                                        if len(batchImages) == self.batchSize: #batch is full
                                            batchLabels = np.vstack(batchLabels)
                                            return (np.array(batchImages), batchLabels)
                                        
                            numImagesProcessed += len(images)
        return (batchImages, batchLabels) # will return either a tuple of images/labels
                           # This should only be reached if there are not enough images to make another full batch
    
    """
    This method does not run in default notebooks, the test has been ran locally without the use of the jupyter 
    local server to ensure the tests pass.
    
    To improve on this function, one could set multiple batch sizes to ensure the batching system works as intended under all
    circumstances.
    
    In order to test the getImageBatch function, the function to be tested is modified to load and return the image IDs 
    rather than the image data itself. This is done to reduce the memory and time used to test the logic involved.
    """
    def TEST_getImageBatch(self, imagePaths):
        # start by gettin a list of all the images:
        EVERY_IMAGE = []
        print("Retrieving image IDs...")
        for path in imagePaths:
            for dir_level_one in os.listdir(path):
                    dirOne = path + '/' + dir_level_one
                    if os.path.isdir(dirOne): #base folder contains files as well as directories, we only want the directories

                        for dir_level_two in os.listdir(dirOne):
                            dirTwo = dirOne + '/' + dir_level_two

                            for dir_level_three in os.listdir(dirTwo):
                                dirThree = dirTwo + '/' + dir_level_three

                                for image in os.listdir(dirThree):
                                            EVERY_IMAGE.append(image)
        print("Finished getting all image IDs, ", len(EVERY_IMAGE), "found.")
        print()
        
        
         # next start retrieving batches and comparing the returned images to the list of images we just populated.
        print("Testing batch function.....")
        batchSize = 20000
        batchNumber = 0     
        imageBatch = self.getImageBatch(batchNumber, batchSize, imagePaths)#used this to start the while loop, images loaded from
        # this particular line are not used in the test below.
        
        while (len(imageBatch) != 0):
            expectedBatch = EVERY_IMAGE[batchNumber * batchSize : batchNumber * batchSize + batchSize]        
            imageBatch = self.getImageBatch(batchNumber, batchSize, imagePaths)
            if(imageBatch != expectedBatch):
                print("Test failed on batch number:", batchNumber)
                print("Length of expected values:", len(expectedBatch))
                print("Length of batched  values:", len(imageBatch))
                print("First Image id of expected values:", expectedBatch[0])
                print("First Image id of  batched values:", imageBatch[0])
                print("Last Image id of expected values:", expectedBatch[len(expectedBatch) - 1])
                print("Last Image id of  batched values:", imageBatch[len(imageBatch) - 1])
                
                break
            elif batchNumber % 10 == 0:
                print("batch:", batchNumber, "passed.")
            batchNumber += 1
                                       


