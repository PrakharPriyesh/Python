#import library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing dataset
dataset = pd.read_excel('ESD.xlsx')
X = dataset.iloc[:,0:32].values
y = dataset.iloc[:,32].values
"""
#Encoding the data
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
#lencoder = LabelEncoder()
#y = lencoder.fit_transform(y)
oencoder = OneHotEncoder(categorical_features = 'all')
y = y.reshape(366,1)
y = oencoder.fit_transform(y).toarray()
"""
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split , cross_val_score
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler(with_std = 1)
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel ='linear', random_state = 0 )
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
accuracy = classifier.score(X_test,y_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)