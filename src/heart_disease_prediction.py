
import pandas as pd

# loading the data
heart_disease_data = pd.read_csv("/content/heart_disease_data.csv")

heart_disease_data.head()

heart_disease_data.tail()

heart_disease_data.shape

heart_disease_data.info()

heart_disease_data.isnull().sum()

heart_disease_data.describe()

heart_disease_data['target'].value_counts()

X = heart_disease_data.drop(columns='target', axis=1)
Y = heart_disease_data['target']

print(X)

print(Y)

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

# training the LogisticRegression model with Training data
model.fit(X_train, Y_train)

from sklearn.metrics import accuracy_score
X_training_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_training_prediction,Y_train)

print(f"Trainig accuracy score is : {training_data_accuracy}")

X_test_prediction = model.predict(X_test)
testing_data_accuarcy = accuracy_score(X_test_prediction,Y_test)

print(f"Testing accuracy score : {testing_data_accuarcy}")

# @title
import numpy as np
input_data = (63,1,3,145,233,1,0,150,0,2.3,0,0,1)
input_data_to_array = np.asarray(input_data)
input_data_reshaped = input_data_to_array.reshape(1,-1)
prediction = model.predict(input_data_reshaped)
print(prediction)
if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')

import pickle
filename = 'heart_disease_model.sav'
pickle.dump(model, open(filename, 'wb'))
# loading the saved model
loaded_model = pickle.load(open('heart_disease_model.sav', 'rb'))