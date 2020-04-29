# -*- coding: utf-8 -*-
"""Copy of Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10melUutsRkmHfzy1LJUCSo6yyCa3CEGs
"""

# Commented out IPython magic to ensure Python compatibility.
import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import os
from PIL import Image
import pathlib
import csv 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import keras
from keras import layers
from keras import layers
import keras
from keras.models import Sequential
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('dataset.csv')
data.head()

data = data.drop(['filename'],axis=1)

data.head()

genre_list = data.iloc[:, -1]

genre_list

data.head()

encoder = LabelEncoder()
y = encoder.fit_transform(genre_list)
y

data.iloc[:, :-1]

scaler = StandardScaler()
X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype = float))

X

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

X_train.shape

X_test.shape

y_train

y_train.shape

y_test.shape

model = Sequential()
model.add(layers.Dense(256, activation='relu', input_shape=(X_train.shape[1],)))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model

model.summary()

"""# New Section"""

classifier = model.fit(X_train,
                    y_train,
                    epochs=100,
                    batch_size=128)

prediction = model.predict_classes(X_test)
prediction

from sklearn.metrics import confusion_matrix,classification_report
from sklearn import metrics

metrics.accuracy_score(y_test,prediction)

print (classification_report(y_test,prediction))

