import matplotlib.pyplot as plt
from ml_utils import *
from scipy.io import loadmat
from scipy.optimize import minimize

def gradient(theta, X, y, lamda):
    m = len(X)
    h = sigmoid(X.dot(theta))
    out = np.zeros(len(theta))
    sumdelta = h - y
    out[0] = 1 / m * (np.dot(sumdelta.T, X[:, 0]))
    XR = X[:, 1:]
    thetaR = theta[1:]
    hx = np.dot(XR.T, sumdelta)
    hy = (lamda / m * thetaR).flatten()
    out[1:] = (1 / m * hx + hy)
    return out

def cost_function_reg(theta, X, y, lamda):
    m = len(X)
    h = sigmoid(X.dot(theta))
    thetaR = theta[1:]
    J = (1.0 / m) * ((-y.T.dot(np.log(h))) - ((1 - y.T).dot(np.log(1.0 - h)))) \
        + (lamda / (2.0 * m)) * (thetaR.T.dot(thetaR))
    return J

def one_vs_all(X, y, num_labels, learning_rate):
    rows = X.shape[0]
    params = X.shape[1]

    # k X (n + 1) array for the parameters of each of the k classifiers
    all_theta = np.zeros((num_labels, params + 1))

    # insert a column of ones at the beginning for the intercept term
    X = np.insert(X, 0, values=np.ones(rows), axis=1)

    # labels are 1-indexed instead of 0-indexed
    for i in range(1, num_labels + 1):
        theta = np.zeros(params + 1)
        y_i = np.array([1 if label == i else 0 for label in y])
        #y_i = np.reshape(y_i, (rows, 1))

        # minimize the objective function
        fmin = minimize(fun=cost_function_reg, x0=theta, args=(X, y_i, learning_rate), method='TNC', jac=gradient)
        all_theta[i - 1, :] = fmin.x

    return all_theta

def predict_all(X, all_theta):
    rows = X.shape[0]

    # same as before, insert ones to match the shape
    X = np.insert(X, 0, values=np.ones(rows), axis=1)

    # convert to matrices
    X = np.matrix(X)
    all_theta = np.matrix(all_theta)

    # compute the class probability for each class on each training instance
    h = sigmoid(X * all_theta.T)

    # create array of the index with the maximum probability
    h_argmax = np.argmax(h, axis=1)

    # because our array was zero-indexed we need to add one for the true label prediction
    h_argmax = h_argmax + 1

    return h_argmax

data = loadmat('ex3data1.mat')
X = data['X']
Y = data['y']
num_labels = 10
learning_rate = 1
optimal_theta = one_vs_all(X, Y, num_labels, learning_rate)
y_pred = predict_all(data['X'], optimal_theta)
correct = [1 if a == b else 0 for (a, b) in zip(y_pred, data['y'])]
accuracy = (sum(map(int, correct)) / float(len(correct)))
print ('accuracy = {0}%'.format(accuracy * 100))