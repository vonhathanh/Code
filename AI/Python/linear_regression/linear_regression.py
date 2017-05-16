import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# J(theta) = 1/(2m) * sum(predict[i] - actual[i])^2 for i from 0 to m-1
def compute_cost(x, y, theta):
    m = len(x)
    cost = 0.0
    for i in range(0, m):
        hx = np.dot(x[i], theta)
        cost += (hx - y[i]) * (hx - y[i])
    cost /= 2 * m
    return cost

def gradientDescent(x, y, theta, alpha, iteration):
    m = len(x)
    J_history = np.zeros((iteration, 1))

    for iter in range(0, iteration):
        theta_prime = [0, 0]
        for i in range(0, m):
            theta_prime[0] += (np.dot(x[i], theta) - y[i]) * x[i][0]
            theta_prime[1] += (np.dot(x[i], theta) - y[i]) * x[i][1]

        theta[0] -= alpha * (1 / m) * theta_prime[0]
        theta[1] -= alpha * (1 / m) * theta_prime[1]
        J_history[iter] = compute_cost(x, y, theta)
        print("iteration = %d, J(theta) = %.4f" % (iter, J_history[iter]))

    return theta, J_history

# read data from file
names = ['profit', 'population']
data = pd.read_csv('ex1data1.txt', sep=',', names=names)
# convert dataframe to numpy array
data = data.values
x = data[:, 0]
y = data[:, 1]
m = len(x)
iteration = 1500
alpha = 0.01
# add a column of ones to x
x = np.c_[np.ones(m), x]
# calculate cost
theta, J_history = gradientDescent(x, y, [0, 0], alpha, iteration)
print(theta)
predict1 = np.dot([1, 3.5], theta)
predict2 = np.dot([1, 7], theta)
print('for population  = 35000, we predict a profit of ', predict1 * 10000)
print('for population  = 70000, we predict a profit of ', predict2 * 10000)

theta0_vals = np.linspace(-10, 10, 100)
theta1_vals = np.linspace(-1, 4, 100)
J_vals = np.zeros((len(theta0_vals), len(theta1_vals)))
#X, Y = np.meshgrid(theta0_vals, theta1_vals)

for i in range(0, len(theta0_vals)):
    for j in range(0, len(theta1_vals)):
        t = [theta0_vals[i], theta1_vals[j]]
        J_vals[i, j] = compute_cost(x, y, t)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(theta0_vals, theta1_vals, J_vals, color='b')
plt.figure()
plt.contour(theta0_vals, theta1_vals, J_vals, np.logspace(-2, 3, 20))

plt.show()

# plt.xlabel('Population of city in 10,000')
# plt.ylabel('Profit in $10,000')
# plt.plot(x[:, 1], y, 'rx')
# plt.plot(x[:, 1], x*theta, '-')
#plt.show()
