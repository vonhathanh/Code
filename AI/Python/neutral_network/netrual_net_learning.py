from ml_utils import *
from scipy.io import loadmat
from sklearn.preprocessing import OneHotEncoder
from matplotlib import pyplot as plt
import scipy.misc as msc
import matplotlib.cm as cm
import random
import math
from scipy.optimize import minimize
import pickle

def getDatumImg(row):
    """
    Function that is handed a single np array with shape 1x400,
    crates an image object from it, and returns it
    """
    size = math.floor(math.sqrt(row.shape[1]))
    width, height = size, size
    square = row[0,1:].reshape(width,height)
    return square.T

def displayData(X, indices_to_display=None):
    """
    Function that picks 100 random rows from X, creates a 20x20 image from each,
    then stitches them together into a 10x10 grid of images, and shows it.
    """
    width = round(np.sqrt(X.shape[1]))
    height = X.shape[1] / width
    m, n = X.shape
    nrows = math.floor(np.sqrt(m))
    ncols = math.ceil(m / nrows)

    if not indices_to_display:
        indices_to_display = random.sample(range(X.shape[0]), nrows * ncols)

    big_picture = np.zeros((height * nrows, width * ncols))

    irow, icol = 0, 0
    for idx in indices_to_display:
        if icol == ncols:
            irow += 1
            icol = 0
        iimg = getDatumImg(X[idx].flatten())
        big_picture[irow * height:irow * height + iimg.shape[0], icol * width:icol * width + iimg.shape[1]] = iimg
        icol += 1
    fig = plt.figure(figsize=(6, 6))
    img = msc.toimage(big_picture)
    plt.imshow(img, cmap=cm.Greys_r)
    plt.show()

def forward_propagate(X, theta1, theta2):
    m = X.shape[0]
    a1 = np.insert(X, 0, np.ones(m), axis=1)
    z2 = np.dot(a1, theta1.T)
    a2 = np.insert(sigmoid(z2), 0, np.ones(m), axis=1)
    z3 = a2.dot(theta2.T)
    h = sigmoid(z3)
    return a1, z2, a2, z3, h

def cost_function(params, X, Y, input_size, hidden_size, num_labels, learning_rate):
    m = X.shape[0]
    theta1 = np.reshape(params[:hidden_size * (input_size + 1)], (hidden_size, input_size + 1))
    theta2 = np.reshape(params[hidden_size * (input_size + 1):], (num_labels, hidden_size + 1))

    a1, z2, a2, z3, h = forward_propagate(X, theta1, theta2)

    j = 0
    for i in range(m):
        left = np.dot(-Y[i], np.log(h[i]))
        right = np.dot(1 - Y[i], np.log(1 - h[i]))
        j += left - right

    j /= m
    j += (float(learning_rate) / (2 * m)) * (np.sum(np.power(theta1[:, 1:], 2)) + np.sum(np.power(theta2[:, 1:], 2)))

    return j

def back_propagation(params, X, Y, input_size, hidden_size, num_labels, learning_rate):
    m = X.shape[0]
    X = np.matrix(X)
    Y = np.matrix(Y)

    theta1 = np.matrix(np.reshape(params[:hidden_size * (input_size + 1)], (hidden_size, input_size + 1)))
    theta2 = np.matrix(np.reshape(params[hidden_size * (input_size + 1):], (num_labels, hidden_size + 1)))

    delta1 = np.zeros(theta1.shape)  # (25, 401)
    delta2 = np.zeros(theta2.shape)  # (10, 26)

    a1, z2, a2, z3, h = forward_propagate(X, theta1, theta2)
    for i in range(m):
        a1t = a1[i]  # (1, 401)
        z2t = z2[i]  # (1, 25)
        a2t = a2[i]  # (1, 26)
        ht = h[i]  # (1, 10)
        yt = Y[i]  # (1, 10)
        # step 1
        d3t = ht - yt  # (1, 10)
        # step 2
        z2t = np.insert(z2t, 0, values=np.ones(1))  # (1, 26)
        d2t = np.multiply((theta2.T * d3t.T).T, sigmoid_gradient(z2t))  # (1, 26)

        delta1 = delta1 + (d2t[:, 1:]).T * a1t
        delta2 = delta2 + d3t.T * a2t

    delta1[:, 0] = delta1[:, 0] / m
    delta1[:, 1:] = delta1[:, 1:] / m + learning_rate / m * theta1[:, 1:]
    delta2[:, 0] = delta2[:, 0] / m
    delta2[:, 1:] = delta2[:, 1:] / m + learning_rate / m * theta2[:, 1:]

    grad = np.concatenate((np.ravel(delta1), np.ravel(delta2)))
    return grad

def compute_numerical_grad(params, X, Y, input_layer_size, hidden_layer_size, num_labels, learning_rate):
    m = len(params)
    numgrad = np.zeros(m)
    perturb = np.zeros(m)
    e = 0.0001
    for i in range(m):
        perturb[i] = e
        loss1 = cost_function(params - perturb, X, Y, input_layer_size, hidden_layer_size, num_labels, learning_rate)
        loss2 = cost_function(params + perturb, X, Y, input_layer_size, hidden_layer_size, num_labels, learning_rate)
        numgrad[i] = (loss2 - loss1) / (2 * e)
        perturb[i] = 0
    return numgrad

def gradient_checking_nn(learning_rate):
    input_layer_size = 3
    hidden_layer_size = 5
    num_labels = 3
    m = 5

    theta1 = debug_init_weight(input_layer_size, hidden_layer_size)
    theta2 = debug_init_weight(hidden_layer_size, num_labels)
    params = np.r_[theta1.flatten(), theta2.flatten()]

    X = debug_init_weight(input_layer_size - 1, m)
    Y = np.matrix(1 + np.mod(range(0, m), num_labels))
    Y = Y.T
    encoder = OneHotEncoder(sparse=False)
    y_onehot = encoder.fit_transform(Y)

    grad = back_propagation(params, X, y_onehot, input_layer_size, hidden_layer_size, num_labels, learning_rate)
    numgrad = compute_numerical_grad(params, X, y_onehot, input_layer_size, hidden_layer_size, num_labels, learning_rate)
    diff = np.linalg.norm(numgrad - grad, 2) / np.linalg.norm(numgrad + grad, 2)
    print(diff)


data = loadmat('ex3data1.mat')
params = loadmat('ex3weights.mat')
theta1 = params['Theta1']
theta2 = params['Theta2']

params = np.r_[theta1.flatten(), theta2.flatten()]
X = data['X']
Y = data['y']

encoder = OneHotEncoder(sparse=False)
y_onehot = encoder.fit_transform(Y)

input_size = 400
hidden_size = 25
num_labels = 10
learning_rate = 1

X = np.insert(X,0,1,axis=1)
theta1 = np.load('theta1.dat')
theta2 = np.load('theta2.dat')
displayData(theta1)
# gradient_checking_nn(1)
# params = (np.random.random(size=hidden_size * (input_size + 1) + num_labels * (hidden_size + 1)) - 0.5) * 0.25
# cost = cost_function(params, X, y_onehot, input_size, hidden_size, num_labels, learning_rate)
# grad = back_propagation(params, X, y_onehot, input_size, hidden_size, num_labels, learning_rate)
# fmin = minimize(cost_function,x0=params,
#                 args=(X, y_onehot, input_size, hidden_size, num_labels, learning_rate),
#                 method='TNC',
#                 jac=back_propagation,
#                 options={'maxiter':250})
# print(fmin)

# theta1 = np.matrix(np.reshape(fmin.x[:hidden_size * (input_size + 1)], (hidden_size, (input_size + 1))))
# theta2 = np.matrix(np.reshape(fmin.x[hidden_size * (input_size + 1):], (num_labels, (hidden_size + 1))))

# theta1 = np.load('theta1.dat')
# theta2 = np.load('theta2.dat')
# a1, z2, a2, z3, h = forward_propagate(X, theta1, theta2)
# y_pred = np.array(np.argmax(h, axis=1) + 1)
#
# correct = [1 if a == b else 0 for (a, b) in zip(y_pred, Y)]
# accuracy = (sum(map(int, correct)) / float(len(correct)))
# print('accuracy = {0}%'.format(accuracy * 100))
