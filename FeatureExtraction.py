from sklearn.feature_extraction.text import CountVectorizer

from TextProcessing import TextProcessing


class FeatureExtraction:
    def __init__(self, data):
        self.bigram_vectorizer = CountVectorizer(ngram_range=(1,2),
                                                 token_pattern=r'\b\w+\b', min_df=1)
        self.data = data

    def extract(self):
        self.bigram_vectorizer.fit_transform(self.data)
        x = self.bigram_vectorizer.get_feature_names()
        print(x)


if __name__ == "__main__":
    tp = TextProcessing()
    tp.read_data(["data/Youtube01-Psy.csv",
                  "data/Youtube02-KatyPerry.csv",
                  "data/Youtube03-LMFAO.csv",
                  "data/Youtube04-Eminem.csv",
                  "data/Youtube05-Shakira.csv"])
    fe = FeatureExtraction(tp.data)

    fe.extract()
