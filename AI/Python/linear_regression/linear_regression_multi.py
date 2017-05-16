import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def feature_scaling(x):
    x_norm = x
    x_mean = np.zeros(x.shape[1])
    x_std = np.zeros(x.shape[1])
    for i in range(0, len(x_mean)):
        x_mean[i] = np.mean(x[:, i])
        x_std[i] = np.std(x[:, i])
        x_norm[:, i] = (x_norm[:, i] - x_mean[i]) / x_std[i]
    return x_norm, x_mean, x_std

def compute_cost(x, y, theta):
    m = len(x)
    cost = 1 / (2 * m) * np.sum((np.dot(x, theta) - y) * (np.dot(x, theta) - y))
    return cost

def gradient_descent(x, y, theta, alpha, iteration, method='gds'):
    m = len(x)
    J_history = np.zeros((iteration, 1))
    if method == 'gds':
        print('calculating theta using gradient descent method')
        for iter in range(0, iteration):
            theta_prime = np.zeros(len(theta))
            for i in range(0, m):
                for j in range(0, len(theta)):
                    theta_prime[j] += (np.dot(x[i], theta) - y[i]) * x[i][j]

            for j in range(0, len(theta)):
                theta[j] -= alpha * (1 / m) * theta_prime[j]

            J_history[iter] = compute_cost(x, y, theta)
            print("iteration = %d, J(theta) = %.4f" % (iter, J_history[iter]))
    else:
        print('calculating theta using normal equation method')
        XTX = np.dot(x.T, x)
        XTX = np.linalg.inv(XTX)
        XTX = np.dot(XTX, x.T)
        theta = np.dot(XTX, y)

    return theta, J_history

names = ['house size', 'bed rooms', 'profit']
data = pd.read_csv('ex1data2.txt', sep=',', names=names)
# convert dataframe to numpy array
data = data.values.astype(float)
x = data[:, 0:2]
y = data[:, 2]
alpha = 0.02
num_iters = 400
# scaling data to get better result
x_norm, x_mean, x_std = feature_scaling(x)
# add a column of ones to x
x_norm = np.c_[np.ones(len(x_norm)), x_norm]
theta, J_history = gradient_descent(x_norm, y, [0, 0, 0], alpha, num_iters)
print("theta obtain by gds method: ", theta)
theta, J_history = gradient_descent(x_norm, y, [0, 0, 0], alpha, num_iters, method='equ')
print("theta obtain by normal equation method: ", theta)
# plt.figure()
# plt.plot(np.arange(0, len(J_history)), J_history, '-')
# plt.show()