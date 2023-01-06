

class NumberInfo:
    def __init__(self):
        self.info = {}
        self.raw_data = open('NumberInfos.txt').read().split("\n")
        self.split_data()

    def split_data(self):
        for i in range(len(self.raw_data)):
            part1, part2 = self.raw_data[i].split("=")
            self.info[part1] = part2

    def get_data(self, number):
        output = self.info[str(number)]
        return output
