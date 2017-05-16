import numpy as np
from matplotlib import pyplot as plt
from scipy.io import loadmat
from ml_utils import *
import scipy.optimize as op

def plot_data():
    plt.figure(figsize=(8, 5))
    plt.ylabel('water flowing out of the dam(y)')
    plt.xlabel('change in water level(x)')
    plt.plot(X[:, 1], y, 'rx')

def plot_straight_line(X, theta):
    plot_data()
    plt.plot(X[:, 1], np.dot(X, theta).flatten(), '--')

def plot_learning_curve(error_train, error_val):
    m = len(error_train)
    plt.figure()
    plt.xlabel('Number of training examples')
    plt.ylabel('Error')
    plt.title('Learning curve for linear regression')
    plt.plot(range(m), error_train, label='Train')
    plt.plot(range(m), error_val, label='cross validation')
    plt.legend()

def cost_function(theta, X, y, learning_rate):
    m = len(X)
    theta = np.matrix(theta.reshape((X.shape[1], 1)))
    X = np.matrix(X)
    y = np.matrix(y)

    h = np.dot(X, theta)
    left = np.sum(np.power(h - y, 2))
    right = np.sum(np.power(theta[1:], 2))

    J = 1.0 / (2 * m) * left + float(learning_rate) / (2 * m) * right
    return J

def gradient(theta, X, y, learning_rate):
    m = len(X)
    theta = np.matrix(theta.reshape((X.shape[1], 1)))
    X = np.matrix(X)
    y = np.matrix(y)

    h = np.dot(X, theta)
    grad = 1.0 / m * np.dot(X.T, h - y)
    grad[1:] += learning_rate / m * theta[1:]

    return grad.flatten()

def learning_curve(X, y, Xval, yval, learning_rate, poly=False):
    m = len(X)

    error_train = np.zeros((m - 1, 1))
    error_val = np.zeros((m - 1, 1))
    theta = np.ones((X.shape[1], 1))

    for i in range(2, m + 1):
        Xi = X[0:i, :]
        yi = y[0:i]
        if poly:
            Xi = poly_feartures(Xi, 8)
            Xi, Xi_mean, Xi_std = fearture_normalize(Xi)
            Xi = np.insert(Xi, 0, 1, axis=1)
            theta = np.ones((Xi.shape[1], 1))
        result = op.minimize(cost_function, x0=theta, args=(Xi, yi, learning_rate), method='TNC', jac=gradient)
        optimal_theta = result.x

        error_train[i - 2] = cost_function(optimal_theta, Xi, yi, learning_rate)
        error_val[i - 2] = cost_function(optimal_theta, Xval, yval, learning_rate)

    return error_train, error_val

def poly_feartures(X, p):
    m = len(X)
    Xpoly = np.zeros((m, p))
    for i in range(1, p + 1):
        Xpoly[:, i - 1] = np.power(X[:, 1], i)

    return Xpoly

def fearture_normalize(X):
    Xnorm = X.copy()
    Xmean = np.mean(X, axis=0)
    Xstd = np.std(X, axis=0, ddof=1)

    Xnorm -= Xmean
    Xnorm /= Xstd

    return Xnorm, Xmean, Xstd

def train_linear_reg(X, y, learning_rate):
    theta = np.ones((X.shape[1], 1))
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)

    result = op.minimize(cost_function, x0=theta, args=(X, y, learning_rate), method='TNC', jac=gradient)
    optimal_theta = result.x
    return optimal_theta

def plot_fit(minx, maxx, theta, means, stds, p):
    n_points_to_plot = 50
    xvals = np.linspace(minx - 15, maxx + 25, n_points_to_plot)
    xmat = np.ones((n_points_to_plot, 1))

    xmat = np.insert(xmat, 1, xvals.T, axis=1)
    xmat = poly_feartures(xmat, len(theta) - 1)
    # This is undoing feature normalization
    xmat -= means
    xmat /= stds
    xmat = np.insert(xmat, 0, 1, axis=1)

    plot_data()
    plt.plot(xvals, np.dot(xmat, theta), 'b--')

data = loadmat('ex5data1.mat')
X, y = data['X'], data['y']
Xval, yval = data['Xval'], data['yval']
Xtest, ytest = data['Xtest'], data['ytest']

X = np.insert(X, 0, 1, axis=1)
Xval = np.insert(Xval, 0, 1, axis=1)
Xtest = np.insert(Xtest, 0, 1, axis=1)

learning_rate = 1.0
p = 8

Xpoly = poly_feartures(X, p)
Xnorm, Xmean, Xstd = fearture_normalize(Xpoly)
Xnorm = np.insert(Xnorm, 0, 1, axis=1)

Xval_poly = poly_feartures(Xval, p)
Xval_norm, Xval_mean, Xval_std = fearture_normalize(Xval_poly)
Xval_norm = np.insert(Xval_norm, 0, 1, axis=1)

error_train, error_val = learning_curve(X, y, Xval_norm, yval, learning_rate, poly=True)
plot_learning_curve(error_train, error_val)

# error_train, error_val = learning_curve(X, y, Xval, yval, learning_rate)
# plot_learning_curve(error_train, error_val)
# plot_fit(min(X.flatten()), max(X.flatten()), theta, Xmean, Xstd, p)
plt.show()
