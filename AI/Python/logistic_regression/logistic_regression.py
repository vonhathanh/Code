import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as op
from ml_utils import *


def gradient(theta, X, Y):
    m = len(Y)
    h = sigmoid(np.dot(X, theta))
    grad = 1 / m * (np.dot(X.T, h - Y))
    return grad

def costFunction(theta, X, Y):
    m = len(Y)
    h = sigmoid(np.dot(X, theta))
    J = 1 / m * (np.dot(-Y.T, np.log(h)) - np.dot((1 - Y).T, np.log(1 - h)))
    #grad = 1 / m * (np.dot(X.T, h - Y))
    return J


def plotDecicionBoundary(theta, X, Y):
    if X.shape[1] <= 3:
        plot_x = np.array([min(X[:, 0] - 2), max(X[:, 1]) + 2])
        print(plot_x)
        print(theta[1])
        print(theta[1] * plot_x)
        print(theta[1] * plot_x + theta[0])
        plot_y = (-1./theta[2]) * (theta[1] * plot_x + theta[0])
        plt.plot(plot_x, plot_y)
        plt.axis([30, 100, 30, 100])

names = ['exam1 score', 'exam2 score', 'predict']
data = pd.read_csv('ex2data1.txt', sep=',', names=names)
data = data.values
m = len(data)
X = data[:, 0:2]
X = np.c_[np.ones(m), X]
Y = data[:, 2]
test_theta = np.zeros(3)

# here is an alternative way to find the optimal theta
#optimal_theta = op.fmin_bfgs(costFunction, test_theta, fprime=gradient, args=(X, Y))
result = op.minimize(costFunction, x0 = test_theta, args=(X, Y), method='TNC', jac=gradient)
optimal_theta = result.x
prob = sigmoid(np.dot(optimal_theta, np.array([1, 45, 85])))
print("for a student with scores 45 and 85 we predict an admission probability of %f"%(prob))
pred = predict(optimal_theta, X)
a = np.where(pred == Y)[0]
print(len(a)/len(Y) * 100)
pos = np.where(data[:, 2] == 1)
neg = np.where(data[:, 2] == 0)
admitted = plt.plot(data[pos, 0], data[pos, 1], 'k+', label="admitted")
notadmitted = plt.plot(data[neg, 0], data[neg, 1], 'yo', label="not admitted")
plt.xlabel('exam1 score')
plt.ylabel('exam2 score')
plotDecicionBoundary(optimal_theta, X, Y)
# #plt.legend(handles=[admitted, notadmitted])
# plt.show()
