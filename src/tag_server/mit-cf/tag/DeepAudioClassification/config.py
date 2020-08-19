#Define paths for file
import os
master_path = os.path.dirname(os.path.abspath( __file__ ))
#master_path = '/root/Music-Collaboration-Platform-Mit/src/tag_server/mit-cf/tag/DeepAudioClassification/'
spectrogramsPath = master_path+"/Data/Spectrograms/"
slicesPath = master_path+"/Data/Slices/"
datasetPath = master_path+"/Data/Dataset/"
rawDataPath = master_path+"/Data/Raw/"
predict_genre = "Pop"

spectrogramsPath_predict = master_path+"/Prediction/Spectrograms/"
slicesPath_predict = master_path+"/Prediction/Slices/"
datasetPath_predict = master_path+"/Prediction/Dataset/"
rawDataPath_predict = master_path+"/Prediction/Raw/"

#Spectrogram resolution
pixelPerSecond = 50

#Slice parameters
sliceSize = 128

#Dataset parameters
filesPerGenre = 1000
validationRatio = 0.3
testRatio = 0.1

#Model parameters
batchSize = 128
learningRate = 0.001
nbEpoch = 20
