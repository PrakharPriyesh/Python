# Classification template
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('1.csv')
dataset = dataset.sort_values(['0.1'], ascending = [True])
dataset_1= dataset[(dataset['0.1'] < 2)]
dataset_2= dataset[(dataset['0.1'] > 2)]
dataset_1 = dataset_1.append(dataset_2, ignore_index=True)
dataset = dataset_1
X = dataset.iloc[:,1:4].values
y = dataset.iloc[:,4].values
