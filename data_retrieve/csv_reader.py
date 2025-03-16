import csv

class CSVReader:
    def __init__(self, file_path):

        self.file_path = file_path

    def read_csv(self):
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

        return reader