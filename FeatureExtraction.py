from sklearn.feature_extraction.text import CountVectorizer

from TextProcessing import TextProcessing


class FeatureExtraction:
    def __init__(self, data):
        self.vectorizer = CountVectorizer(lowercase=True, analyzer="word", ngram_range=(1, 3),
                                          min_df=25)
        self.data = data

    def extract_all(self):
        return self.vectorizer.fit_transform(self.data)

    def extract(self, comment):
        return self.vectorizer.transform([comment])


if __name__ == "__main__":
    tp = TextProcessing()
    # tp.read_data(["data/Youtube01-Psy.csv",
    #               "data/Youtube02-KatyPerry.csv",
    #               "data/Youtube03-LMFAO.csv",
    #               "data/Youtube04-Eminem.csv",
    #               "data/Youtube05-Shakira.csv"])

    tp.read_data(["data/test.csv"])

    fe = FeatureExtraction(tp.data)
