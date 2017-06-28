from sklearn.feature_extraction.text import CountVectorizer

from TextProcessing import TextProcessing


class FeatureExtraction:
    def __init__(self):
        self.vectorizer = CountVectorizer(lowercase=True, analyzer="word", ngram_range=(1, 3),
                                          min_df=0.05)

    def fit(self, data):
        return self.vectorizer.fit(data)

    def extract(self, data):
        return self.vectorizer.transform(data)
