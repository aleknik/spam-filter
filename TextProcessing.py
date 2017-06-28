import csv
import re

words = r"\b(the|a)\b"


class TextProcessing:
    def __init__(self):
        self.comments = []
        self.labels = []

    def read_data(self, paths):
        for path in paths:
            with open(path, 'r', encoding="utf-8") as csv_file:
                reader = csv.reader(csv_file)
                next(reader, None)
                for row in reader:
                    self.process_row(row)

    def process_row(self, row):
        comment = self.process_comment(row[3])
        self.comments.append(comment)
        self.labels.append(row[4])

    def process_comment(self, comment):
        comment = comment.lower()
        comment = re.sub(r"(http\S+)", 'link_url', comment).strip()
        comment = re.sub(words, "", comment).strip()
        return comment

    def print_spam(self):
        for index, label in enumerate(self.labels):
            if label == '1':
                print(self.comments[index])


if __name__ == "__main__":
    tp = TextProcessing()
    tp.read_data(["data/Youtube01-Psy.csv",
                  "data/Youtube02-KatyPerry.csv",
                  "data/Youtube03-LMFAO.csv",
                  "data/Youtube04-Eminem.csv",
                  "data/Youtube05-Shakira.csv"])

    print(tp.comments)
    print(tp.labels)
