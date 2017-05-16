from ml_utils import *
import pandas as pd
import scipy.optimize as op
import matplotlib.pyplot as plt

def predict(theta, X):
    p = sigmoid(X.dot(theta))
    p = [thresh_hold(i) for i in p]
    return p

def thresh_hold(x):
    if x > 0.5:
        return 1
    return 0

def sigmoid(x):
    t =  1 / (1 + np.exp(-x))
    return t.flatten()

# remember to check two array addition when one have (xx,) shape and other have (xx,1) shape
def gradient(theta, X, y, lamda):
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
    h = sigmoid(X.dot(theta))
    thetaR = theta[1:]
    J = (1.0 / m) * ((-y.T.dot(np.log(h))) - ((1 - y.T).dot(np.log(1.0 - h)))) \
        + (lamda / (2.0 * m)) * (thetaR.T.dot(thetaR))
    return J

def map_feature(X1, X2):
    X1.shape = (X1.size, 1)
    X2.shape = (X2.size, 1)
    degree = 6
    out = np.ones((len(X1), 1))
    for i in range(1, degree + 1):
        for j in range(i + 1):
            r = (X1 ** (i - j)) * (X2 ** j)
            out = np.append(out, r, axis=1)
    return out

names = ['test 1', 'test 2', 'predict']
data = pd.read_csv('ex2data2.txt', sep=',', names=names)
data = data.values

m = len(data)
X = data[:, 0:2]
# X = np.c_[np.ones(m), X]
Y = data[:, 2]
X = map_feature(X[:, 0], X[:, 1])
lamda = 1

test_theta = np.zeros(X.shape[1])
result = op.minimize(cost_function_reg, x0 = test_theta, args=(X, Y, lamda), method='TNC', jac=gradient)
optimal_theta = result.x

pred = predict(optimal_theta, X)
a = np.where(pred == Y)[0]
print(len(a)/len(Y))

pos = np.where(data[:, 2] == 1)
neg = np.where(data[:, 2] == 0)
admitted = plt.plot(data[pos, 0], data[pos, 1], 'k+')
notadmitted = plt.plot(data[neg, 0], data[neg, 1], 'yo')
plt.xlabel('test 1')
plt.ylabel('test 2')

u = np.linspace(-1, 1.5, 50)
v = np.linspace(-1, 1.5, 50)
z = np.zeros(shape=(len(u), len(v)))
for i in range(len(u)):
    for j in range(len(v)):
        z[i, j] = (map_feature(np.array(u[i]), np.array(v[j])).dot(np.array(optimal_theta)))

z = z.T
plt.contour(u, v, z)
plt.title('lambda = %f' % lamda)
plt.legend(['y = +', 'y = o', 'Decision boundary'])

plt.show()
