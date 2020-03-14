#import library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing dataset
dataset = pd.read_excel('ESD.xlsx')
X = dataset.iloc[:,0:32].values
y = dataset.iloc[:,32].values

#Encoding the data
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
#lencoder = LabelEncoder()
#y = lencoder.fit_transform(y)
oencoder = OneHotEncoder(categorical_features = 'all')
y = y.reshape(366,1)
y = oencoder.fit_transform(y).toarray()

# Splitting the data set to training set and test set 
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Fitting Logistic Regression  to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski' ,p=2)
classifier.fit(X_train, y_train)


t = X_test[4,0:33]
t = t.reshape(1,32)
y_pred = classifier.predict(X_test)
z = classifier.score(X_test,y_test)

