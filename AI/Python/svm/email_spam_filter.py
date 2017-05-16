import nltk as nltk
import numpy as np
from scipy.io import loadmat
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from stemming.porter2 import stem
import re


def get_vocal_list(reverse=False):
    vocab_dict = {}

    with open('vocab.txt') as f:
        if reverse:
            for line in f:
                (val, key) = line.split()
                vocab_dict[int(val)] = key
        else:
            for line in f:
                (val, key) = line.split()
                vocab_dict[key] = int(val)

    return vocab_dict

def pre_process(raw_email):
    email = raw_email.lower()
    email = re.sub('<[^<>]+>', ' ', email)
    email = re.sub('[0-9]+', 'number', email)
    email = re.sub('(http|https)://[^\s]*', 'httpaddr', email)
    email = re.sub('[^\s]+@[^\s]+', 'emailaddr', email)
    email = re.sub('[$]+', 'dollar', email)

    return email

def email_to_token(raw_email):
    email = pre_process(raw_email)
    stemmer = nltk.stem.porter.PorterStemmer()
    tokens = re.split('[ \@\$\/\#\.\-\:\&\*\+\=\[\]\?\!\(\)\{\}\,\'\"\>\_\<\;\%]', email)
    token_list = []

    for token in tokens:
        token = re.sub('[^a-zA-Z0-9]', '', token)
        stemmed = stemmer.stem(token)
        if not len(token):
            continue
        token_list.append(stemmed)

    return token_list

def email_to_indice(raw_email, vocab_dict):
    tokens = email_to_token(raw_email)
    index_list = [vocab_dict[token] for token in tokens if token in vocab_dict]

    return index_list

def extract_features(raw_email, vocab_dict):
    indices = email_to_indice(raw_email, vocab_dict)
    fearure_vec = np.zeros(len(vocab_dict))

    for index in indices:
        fearure_vec[index] = 1

    return fearure_vec

# vocab_dict = get_vocal_list()
# raw_email = open('emailSample1.txt','r').read()
#
# feature_vec = extract_features(raw_email, vocab_dict)

train_mat = loadmat('spamTrain.mat')
test_mat = loadmat('spamTest.mat')

X = train_mat['X']
y = train_mat['y']
XTest = test_mat['Xtest']
YTest = test_mat['ytest']

C = 0.1
gauss_svm = svm.SVC(C=C, kernel='linear')

gauss_svm.fit(X, y.flatten())

vocab_dict = get_vocal_list(True)
sorted_indices = np.argsort(gauss_svm.coef_, axis=None)[::-1]
print([vocab_dict[x] for x in sorted_indices[:15]])
# print(gauss_svm.score(XTest, YTest.flatten()))

