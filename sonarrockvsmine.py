# -*- coding: utf-8 -*-
"""SonarRockVSMine.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B7gwdqD1-9DeNwCDEwLlP4Z_t_uJJkbp

Import The Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data collection and Data Processing"""

#loading the dataset to a pandas dataframe
sonar_data = pd.read_csv('C:\Machine_Learning\Project\P1\sonar.csv', header=None)

sonar_data.head()

#Number of Rows and Columns
sonar_data.shape

sonar_data.describe()            #statistical measures of the data

sonar_data[60].value_counts()

"""M----> Mine
R----> Rock
"""

sonar_data.groupby(60).mean()

#seperating data and labels
x = sonar_data.drop(columns = 60, axis =1)
y = sonar_data[60]

print(x)
print(y)

"""Training and Test Data"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size =0.1, stratify=y, random_state=1)

print(x.shape , x_train.shape, x_test.shape)

"""Model Training --> Logistic regression"""

model = LogisticRegression()

# training the Logistic Regression model with training data
model.fit(x_train, y_train)

"""Model Evaluation"""

#accuracy on training data
x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)

print('Accuracy on training data:', training_data_accuracy)

#accuracy on test data
x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)

print('Accuracy on test data:', test_data_accuracy)

"""Making A predictive system"""

input_data = (0.0262,0.0582,0.1099,0.1083,0.0974,0.2280,0.2431,0.3771,0.5598,0.6194,0.6333,0.7060,0.5544,0.5320,0.6479,0.6931,0.6759,0.7551,0.8929,0.8619,0.7974,0.6737,0.4293,0.3648,0.5331,0.2413,0.5070,0.8533,0.6036,0.8514,0.8512,0.5045,0.1862,0.2709,0.4232,0.3043,0.6116,0.6756,0.5375,0.4719,0.4647,0.2587,0.2129,0.2222,0.2111,0.0176,0.1348,0.0744,0.0130,0.0106,0.0033,0.0232,0.0166,0.0095,0.0180,0.0244,0.0316,0.0164,0.0095,0.0078)
#changing the input data to a numpy array

input_data_as_numpy_array = np.asarray(input_data)


#reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]=='R'):
  print('Object is the Rock')
else:
  print('Object is the mine')

