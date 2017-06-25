from Classifier import Classifier
from FeatureExtraction import FeatureExtraction
from TextProcessing import TextProcessing


def main():
    tp = TextProcessing()
    tp.read_data(["data/Youtube01-Psy.csv",
                  "data/Youtube02-KatyPerry.csv",
                  "data/Youtube03-LMFAO.csv",
                  "data/Youtube04-Eminem.csv",
                  "data/Youtube05-Shakira.csv"])

    training_data = tp.data[:int(len(tp.data) * 0.7)]
    training_labels = tp.labels[:int(len(tp.labels) * 0.7)]
    test_data = tp.data[int(len(tp.data) * 0.7):]
    test_labels = tp.labels[int(len(tp.labels) * 0.7):]

    fe = FeatureExtraction(training_data)

    features = fe.extract_all()

    clf = Classifier(fe)

    clf.train(features, training_labels)
    print(clf.test(test_data, test_labels))

    print(clf.predict(fe.extract("like comment and subscribe")))


if __name__ == "__main__":
    main()
