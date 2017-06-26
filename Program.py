from Classifier import Classifier
from FeatureExtraction import FeatureExtraction
from TextProcessing import TextProcessing

ratio = 0.7

def main():
    tp = TextProcessing()
    tp.read_data(["data/Youtube01-Psy.csv",
                  "data/Youtube02-KatyPerry.csv",
                  "data/Youtube03-LMFAO.csv",
                  "data/Youtube04-Eminem.csv",
                  "data/Youtube05-Shakira.csv"])

    training_data = tp.comments[:int(len(tp.comments) * ratio)]
    training_labels = tp.labels[:int(len(tp.labels) * ratio)]
    test_data = tp.comments[int(len(tp.comments) * ratio):]
    test_labels = tp.labels[int(len(tp.labels) * ratio):]

    fe = FeatureExtraction(training_data)

    features = fe.extract_all()

    clf = Classifier(fe)

    clf.train(features, training_labels)
    print(clf.test(test_data, test_labels))

    comment = tp.process_comment("Like comment and http://www.google.com subscribe")

    print(clf.predict(fe.extract(comment)))
    print (fe.vectorizer.vocabulary_)
    print (len(fe.vectorizer.vocabulary_))


if __name__ == "__main__":
    main()
