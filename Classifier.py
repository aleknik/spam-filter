from sklearn import svm
from sklearn.neural_network import MLPClassifier
import time


class SVMClassifier:
    def __init__(self):
        self.clf = svm.SVC(kernel="linear")

    def train(self, features, labels):
        start = time.time()
        self.clf.fit(features, labels)
        end = time.time()
        print("SVM training time: %f" % (end - start))

    def predict(self, feature):
        return self.clf.predict(feature)


class NNClassifier:
    def __init__(self):
        self.clf = MLPClassifier(hidden_layer_sizes=(15,), max_iter=1000, activation="logistic")

    def train(self, features, labels):
        start = time.time()
        self.clf.fit(features, labels)
        end = time.time()
        print("SVM training time: %f" % (end - start))


    def predict(self, feature):
        return self.clf.predict(feature)
