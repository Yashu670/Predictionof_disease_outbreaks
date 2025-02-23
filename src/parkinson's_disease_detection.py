

import pandas as pd
import numpy as np

parkinson_data = pd.read_csv("/content/parkinsons.data")

parkinson_data.head()

parkinson_data.tail()

parkinson_data.shape

parkinson_data.info()

parkinson_data.isnull().sum()

parkinson_data.duplicated().sum()

parkinson_data.describe()

parkinson_data['status'].value_counts()

X = parkinson_data.drop(columns=['name','status'],axis=1)
Y = parkinson_data['status']

print(X)

print(Y)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)

print(X.shape, X_train.shape, X_test.shape)

parkinson_data.head()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn import svm
model = svm.SVC(kernel='linear')
model.fit(X_train,Y_train)

from sklearn.metrics import accuracy_score
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train,X_train_prediction)
print(f"Training accuracy score : {training_data_accuracy}")

X_test_prediction = model.predict(X_test)
testing_data_accuracy = accuracy_score(Y_test, X_test_prediction)
print(f"Testing accuracy score : {testing_data_accuracy}")

input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)

# changing input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the data
std_data = scaler.transform(input_data_reshaped)

prediction = model.predict(std_data)
print(prediction)


if (prediction[0] == 0):
  print("The Person does not have Parkinsons Disease")

else:
  print("The Person has Parkinsons")

import pickle
filename = 'parkinsons_model.sav'
pickle.dump(model, open(filename, 'wb'))
# loading the saved model
loaded_model = pickle.load(open('parkinsons_model.sav', 'rb'))