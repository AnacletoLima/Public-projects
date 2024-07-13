import csv


class Index:
    def __init__(self):
        self.index = 0

    def find_index(self, input_answer):
        o = open('50_states.csv', 'r')
        my_data = csv.reader(o)
        self.index = 0
        for row in my_data:
            if row[0] == input_answer:
                return self.index
            else:
                self.index += 1
