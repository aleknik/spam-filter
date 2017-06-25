import csv


class TextProcessing():
    def __init__(self):
        self.data = []
        self.labels = []

    def readData(self, paths):
        for path in paths:
            with open(path, 'rb') as csv_file:
                reader = csv.reader(csv_file)
                next(reader, None)
                for row in reader:
                    print(row)


if __name__ == "__main__":
    tp = TextProcessing()
    tp.readData(["data/Youtube01-Psy.csv",
                 "data/Youtube02-KatyPerry.csv",
                 "data/Youtube03-LMFAO.csv",
                 "data/Youtube04-Eminem.csv",
                 "data/Youtube05-Shakira.csv"])
