
import pandas as pd
from sklearn.metrics import accuracy_score

diabetes_data = pd.read_csv("/content/diabetes.csv")

diabetes_data.head()

diabetes_data.tail()

diabetes_data.shape

diabetes_data.info()

diabetes_data.describe()

diabetes_data.isnull().sum()

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='Outcome',data=diabetes_data)

diabetes_data['Outcome'].value_counts()

diabetes_data.hist(bins=10,figsize=(10,10))
plt.show()

diabetes_data.columns

plt.figure(figsize=(15,12))
sns.set_style(style='whitegrid')
plt.subplot(3,3,1)
sns.boxplot(x='Glucose',data=data)
plt.subplot(3,3,2)
sns.boxplot(x='BloodPressure',data=data)
plt.subplot(3,3,3)
sns.boxplot(x='Insulin',data=data)
plt.subplot(3,3,4)
sns.boxplot(x='BMI',data=data)
plt.subplot(3,3,5)
sns.boxplot(x='Age',data=data)
plt.subplot(3,3,6)
sns.boxplot(x='SkinThickness',data=data)
plt.subplot(3,3,7)
sns.boxplot(x='Pregnancies',data=data)
plt.subplot(3,3,8)
sns.boxplot(x='DiabetesPedigreeFunction',data=data)

from pandas.plotting import scatter_matrix
scatter_matrix(diabetes_data,figsize=(20,20));

corrmat=diabetes_data.corr()
sns.heatmap(corrmat, annot=True)

diabetes_data.head()

X = diabetes_data.drop(columns='Outcome',axis=1)
Y = diabetes_data['Outcome']

print(X)

print(Y)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

X = standardized_data
Y = diabetes_data['Outcome']

print(X)
print(Y)

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

from sklearn import svm
classifier = svm.SVC(kernel='linear')

#training the support vector Machine Classifier
classifier.fit(X_train, Y_train)

X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy score of the training data : ', training_data_accuracy)

import numpy as np
input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

import pickle
filename = 'diabetes_model.sav'
pickle.dump(classifier,open(filename,'wb'))

loaded_model = pickle.load(open('diabetes_model.sav','rb'))