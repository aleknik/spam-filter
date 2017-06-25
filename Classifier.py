from sklearn import svm


class Classifier:
    def __init__(self, vectorizer):
        self.vectorizer = vectorizer
        self.clf = svm.SVC()

    def train(self, features, labels):
        self.clf.fit(features, labels)

    def predict(self, feature):
        return self.clf.predict(feature)

    def test(self, data, labels):
        right = 0
        wrong = 0
        for row, label in zip(data, labels):
            predicted = self.predict(self.vectorizer.extract(row))
            if predicted == label:
                right += 1
            else:
                wrong += 1

        return float(right)/(right + wrong)
