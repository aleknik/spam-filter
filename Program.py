from collections import Counter

from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

from Classifier import SVMClassifier, NNClassifier
from FeatureExtraction import FeatureExtraction
from TextProcessing import TextProcessing
from YoutubeApi import get_comments


def main():
    tp = TextProcessing()
    tp.read_data(["data/Youtube01-Psy.csv",
                  "data/Youtube02-KatyPerry.csv",
                  "data/Youtube03-LMFAO.csv",
                  "data/Youtube04-Eminem.csv",
                  "data/Youtube05-Shakira.csv"])

    print(len(tp.comments))
    training_data, test_data, training_labels, test_labels = train_test_split(tp.comments, tp.labels, train_size=0.7,
                                                                              random_state=7)
    fe = FeatureExtraction()
    fe.fit(training_data)

    clf_svm = SVMClassifier()
    clf_svm.train(fe.extract(training_data), training_labels)
    comment = tp.process_comment("Like comment and http://www.google.com subscribe")
    print(comment)
    print("SVM results:")
    print(classification_report(test_labels, clf_svm.predict(fe.extract(test_data))))
    print(confusion_matrix(test_labels, clf_svm.predict(fe.extract(test_data))))
    print(clf_svm.predict(fe.extract([comment])))

    clf_nn = NNClassifier()
    clf_nn.train(fe.extract(training_data), training_labels)
    comment = tp.process_comment("Like comment and http://www.google.com subscribe")
    print(comment)
    print("NN results:")
    print(classification_report(test_labels, clf_nn.predict(fe.extract(test_data))))
    print(confusion_matrix(test_labels, clf_nn.predict(fe.extract(test_data))))
    print(clf_nn.predict(fe.extract([comment])))

    print(fe.vectorizer.vocabulary_)
    print(len(fe.vectorizer.vocabulary_))

    api_comments = get_comments("XbGs_qK2PQA")
    predictions = clf_svm.predict(fe.extract(api_comments))
    print(Counter(predictions))

    for index, pred in enumerate(predictions):
        if pred == '1':
            print("INDEX " + str(index))
            print(api_comments[index])


if __name__ == "__main__":
    main()
