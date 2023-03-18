import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from os import path 


# This File will be for the machine learning portion of the the program
filename = "mlTrain.txt"

if path.isfile(filename):
    with open(filename, "r") as data:
        sampleData = list(data.read())
    print("File exists and contains the following content:")
    print(sampleData)
else:
    print("File does not exist.")
    quit()

input("Press Enter")

exerciseLabels = [
    'abductorLegRaises',
    'barbellSquats',
    'bicepCurls',
    'singleArmBicepCurls',
    'deltoidArmRaises',
    'singleArmDeltoidRaises',
    'frontLatRaises',
    'singleArmFrontLatRaises',
    'gobletSquats',
    'shoulderPress',
    'singleArmShoulderPress'
]

# Define the target range of each exercise
exerciseRanges = {
    'abductorLegRaises': [(0, 135), (0, 150), (130, 155), (170, 180)],
    'barbellSquats': [(30, 90), (75, 150), (0, 135), (0, 135)],
    'bicepCurls': [(0, 30), (0, 90), (160, 180), (160, 180)],
    'singleArmBicepCurls': [(0, 30), (0, 90), (160, 180), (160, 180)],
    'deltoidArmRaises': [(75, 135), (160, 180), (160, 180), (160, 180)],
    'singleArmDeltoidRaises': [(75, 135), (160, 180), (160, 180), (160, 180)],
    'frontLatRaises': [(75, 135), (160, 180), (160, 180), (160, 180)],
    'singleArmFrontLatRaises': [(75, 135), (160, 180), (160, 180), (160, 180)],
    'gobletSquats': [(0, 20), (0, 45), (0, 135), (0, 135)],
    'shoulderPress': [(80, 180), (80, 180), (160, 180), (160, 180)],
    'singleArmShoulderPress': [(80, 180), (80, 180), (160, 180), (160, 180)]
}

# Define the model with different activation functions and optimizers
def createModel(activationFn, optimizer):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation=activationFn, input_shape=(34,)),
        tf.keras.layers.Dense(64, activation=activationFn),
        tf.keras.layers.Dense(32, activation=activationFn),
        tf.keras.layers.Dense(len(exerciseLabels), activation='softmax')
    ])
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Load the models with different activation functions and optimizers
sigmoidOptimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
sigmoidModel = createModel(tf.keras.activations.sigmoid, sigmoidOptimizer)
sigmoidModel.load_weights('sigmoidModelWeights.h5')

#reluOptimizer = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)
#reluModel = createModel(tf.keras.activations.relu, reluOptimizer)
#reluModel.load_weights('reluModelWeights.h5')

#leakyReluOptimizer = tf.keras.optimizers.RMSprop(learning_rate=0.001)
#leakyReluModel = createModel(tf.keras.layers.LeakyReLU(alpha=0.1), leakyReluOptimizer)
#leakyReluModel.load_weights('leakyReluMmodelWeights.h5')

# Define the function to preprocess the input data
def preprocessInput(angles, keyLocations, isRepetition):
    anglesArray = np.array(angles).flatten()
    keyLocationsArray = np.array(keyLocations).flatten()
    isRepetitionArray = np.array([isRepetition])
    inputArray = np.concatenate((anglesArray, keyLocationsArray, isRepetitionArray))
    inputArray = np.expand_dims(inputArray, axis=0)
    return inputArray

# Define the function to check if angles fall within a range
def isWithinRange(angles, targetRange):
    for angle, tRange in zip(angles, targetRange):
        if angle < tRange[0] or angle > tRange[1]:
            return False
    return True

# Modify the predict_exercise function to use the target ranges
def predictExercise(model, angles, keyLocations, isRepetition):
    inputData = preprocessInput(angles, keyLocations, isRepetition)
    prediction = model.predict(inputData)
    for i, exercisePrediction in enumerate(prediction[0]):
        if exercisePrediction > 0.5:
            exerciseName = exerciseLabels[i]
            if exerciseName in exerciseRanges and isWithinRange(angles, exerciseRanges[exerciseName]):
                return exerciseName
    return "unknown"


exList = []
for data in sampleData:
    exList.append(predictExercise(sigmoidModel, data[0], data[1], data[2]))

print(exList)



## Load the dataset
#data = [ [[], []], [], bool] # example data in new format

## Preprocess the data
#X = []
#y = []
#for sample in data:
#    angles = sample[0]
#    keyLocations = sample[1]
#    isRepetition = sample[2]
#    X.append(preprocessInput(angles, keyLocations, isRepetition))
#    y.append(isRepetition)
#X = np.concatenate(X, axis=0)
#y = np.array(y)

## Convert the output data to categorical format
#y = tf.keras.utils.to_categorical(y)

## Split the data into training and testing sets
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

## Define the model with different activation functions and optimizers
#def createModel(activationFn, optimizer):
#    model = tf.keras.Sequential([
#        tf.keras.layers.Dense(128, activation=activationFn, input_shape=(34,)),
#        tf.keras.layers.Dense(64, activation=activationFn),
#        tf.keras.layers.Dense(32, activation=activationFn),
#        tf.keras.layers.Dense(len(labelEncoder.classes_), activation='softmax')
#    ])
#    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
#    return model

## Train the model and evaluate on the test set
#activations = ['relu', 'sigmoid', 'tanh']
#optimizers = ['adam', 'sgd', 'rmsprop']
#for activation in activations:
#    for optimizer in optimizers:
#        print(f'Training model with activation={activation} and optimizer={optimizer}...')
#        model = createModel(activation, optimizer)
#        model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)
#        loss, acc = model.evaluate(X_test, y_test, verbose=0)
#        print(f'Test set accuracy: {acc}')