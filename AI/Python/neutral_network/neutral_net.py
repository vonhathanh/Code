import numpy as np
from scipy.io import loadmat
from ml_utils import *


# read data and weight from mat file
data = loadmat('ex3data1.mat')
weight = loadmat('ex3weights.mat')

# conver data to numpy array
# shape: X = 5000x400 y = 5000x1 theta1 = 25x401 theta2 = 10x26
X = data['X']
Y = data['y']
theta1 = weight['Theta1']
theta2 = weight['Theta2']

num_labels = 10
rows = len(X)

# insert a column of ones at the beginning of training examples, X.shape = 5000x401
X = np.insert(X, 0, values=np.ones(rows), axis=1)
# calculate z1, it should have shape 5000x25
Z1 = X.dot(theta1.T)
# insert a column of ones at the beginning of Z1, Z1.shape = 5000x26
Z1 = np.insert(sigmoid(Z1), 0, values=np.ones(len(Z1)), axis=1)
# calculate z2, it should have shape 5000x10
Z2 = Z1.dot(theta2.T)
# calculate the output
optimal_theta = sigmoid(Z2)
# create array of the index with the maximum probability
h_argmax = np.argmax(optimal_theta, axis=1)
# because our array was zero-indexed we need to add one for the true label prediction
h_argmax = h_argmax + 1

correct = [1 if a == b else 0 for (a, b) in zip(h_argmax, Y)]
accuracy = (sum(map(int, correct)) / float(len(correct)))
print ('accuracy = {0}%'.format(accuracy * 100))