import numpy as np
from scipy.io import loadmat
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from stemming.porter2 import stem
import re

def gaussian_kernel(Xi, Xj, sigma):
    upterm = np.power(Xi - Xj, 2)
    degree = np.sum(upterm) / (2 * sigma * sigma)
    return np.exp(-degree)

def plot_boundary(linear_svm, xmin, xmax, ymin, ymax):
    xvals = np.linspace(xmin, xmax, 100)
    yvals = np.linspace(ymin, ymax, 100)
    zvals = np.zeros((len(xvals), len(yvals)))

    for i in range(len(xvals)):
        for j in range(len(yvals)):
            zvals[i][j] = float(linear_svm.predict(np.array([xvals[i], yvals[j]]).reshape((1, 2))))

    zvals = zvals.T

    plt.contour(xvals, yvals, zvals, [0])
    plt.title('decision boundary')

def select_best_params(X, y, Xval, yval):
    sigmas = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]
    Cs = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]
    best_pair = (0, 0)
    best_score = 0.0

    for i in range(len(Cs)):
        for j in range(len(sigmas)):

            gamma = np.power(sigmas[j], -2.)
            gauss_svm = svm.SVC(C=Cs[j], kernel='rbf', gamma=gamma)
            gauss_svm.fit(X, y.flatten())

            current_score = gauss_svm.score(Xval, yval.flatten())
            if current_score > best_score:
                best_score = current_score
                best_pair = (Cs[j], gamma)

    return best_pair[0], best_pair[1]

raw_data = loadmat('ex6data3.mat')
X = raw_data['X']
y = raw_data['y']
Xval = raw_data['Xval']
yval = raw_data['yval']
positive = np.where(y == 1)[0]
negative = np.where(y == 0)[0]
XPos = X[positive]
XNeg = X[negative]

C, sigma = select_best_params(X, y, Xval, yval)
# sigma = 0.1
# gamma = np.power(sigma, -2)

gauss_svm = svm.SVC(C=C, kernel='rbf', gamma=sigma)
gauss_svm.fit(X, y.flatten())


# mysvm = svm.SVC(C=100, kernel='linear')
# mysvm.fit(X, y.flatten())

plt.figure(figsize=(10, 6))
plt.plot(XPos[:, 0], XPos[:, 1], 'x', label='positive')
plt.plot(XNeg[:, 0], XNeg[:, 1], 'o', label='negative')
plt.legend()
plot_boundary(gauss_svm, -0.5, 0.3, -0.8, 0.6)
# plot_boundary(mysvm, 0, 4.5, 1.5, 5)
plt.show()
