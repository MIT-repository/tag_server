# -*- coding: utf-8 -*-
import random
import string
import os
import sys
import glob
import operator

from .model import createModel
from .datasetTools import getDataset
from .datasetTools import getDataset_predict
from .config import slicesPath
from .config import slicesPath_predict
from .config import batchSize
from .config import filesPerGenre, predict_genre
from .config import nbEpoch
from .config import validationRatio, testRatio
from .config import sliceSize


from .songToData import createSlicesFromAudio
from .songToData import createSlicesFromAudio_predict


print("--------------------------")
print("| ** Config ** ")
print("| Validation ratio: {}".format(validationRatio))
print("| Test ratio: {}".format(testRatio))
print("| Slices per genre: {}".format(filesPerGenre))
print("| Slice size: {}".format(sliceSize))
print("--------------------------")


#List genres
genres = os.listdir(slicesPath)
print("genres",genres)
genres = [filename for filename in genres if os.path.isdir(slicesPath+filename)]
nbClasses = len(genres)
base_path = os.path.dirname(os.path.abspath( __file__ ))

#Create model 
model = createModel(nbClasses, sliceSize)

spect_files = glob.glob('prediction/*.png')
images = []
model.load(base_path+'/musicDNN.tflearn')

def predict():
    #load a dataset
    createSlicesFromAudio_predict()
    predict_X, predict_y = getDataset_predict(filesPerGenre, genres, sliceSize)
#Load weights
    #model.load('tag/DeepAudioClassification/musicDNN.tflearn')

    countArray = [0,0,0,0,0,0,0,0,0,0]
    genreCountDict = dict(zip(genres,countArray))

    i = 0
    prediction = model.predict([predict_X[i]])
    maxIndex, maxValue = max(enumerate(prediction[0]), key=operator.itemgetter(1))


    tempValue = genreCountDict[genres[maxIndex]]
    tempValue = tempValue + 1
    genreCountDict[genres[maxIndex]] = tempValue
    predictedGenre = max(genreCountDict.items(), key=operator.itemgetter(1))[0]
    #return predict_genre
    return predictedGenre

def test():
    return "test"
