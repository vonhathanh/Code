import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_gradient(x):
    return np.multiply(sigmoid(x), (1 - sigmoid(x)))

def rand_init_weights(lin, lout):
    epsilon = 0.12
    w = np.random.random((lout, 1 + lin)) * 2 * epsilon - epsilon
    return w

def debug_init_weight(lin, lout):
    w = np.zeros((lout, lin + 1))
    w = np.reshape(np.sin(range(0,lout * (lin + 1))), w.shape)
    return w

def thresh_hold(x):
    if x > 0.5:
        return 1
    return 0

def predict(theta, X):
    p = sigmoid(X.dot(theta))
    p = [thresh_hold(i) for i in p]
    return p
