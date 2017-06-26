import csv
import random
import re

delimiters = ['\n', ' ', ',', '.', '?', '!', ':']


class TextProcessing:
    def __init__(self):
        self.comments = []
        self.labels = []
        self.all_data = []

    def read_data(self, paths):
        for path in paths:
            with open(path, 'rb') as csv_file:
                reader = csv.reader(csv_file)
                next(reader, None)
                for row in reader:
                    self.process_row(row)

        random.Random(5).shuffle(self.all_data)
        for data in self.all_data:
            self.comments.append(data[0])
            self.labels.append(data[1])

    def process_row(self, row):
        comment = self.process_comment(row[3])
        self.all_data.append([comment, row[4]])

    def process_comment(self, comment):
        comment = comment.lower()
        new_comment = re.sub(r"http\S+", 'link_url', comment).strip()
        return new_comment


if __name__ == "__main__":
    tp = TextProcessing()
    tp.read_data(["data/Youtube01-Psy.csv",
                  "data/Youtube02-KatyPerry.csv",
                  "data/Youtube03-LMFAO.csv",
                  "data/Youtube04-Eminem.csv",
                  "data/Youtube05-Shakira.csv"])

    print(tp.data)
    print(tp.labels)
