import pandas as pd
import matplotlib.pyplot as plt
from NumberInfo import NumberInfo


class DataAnalyse:
    def __init__(self):
        self.data_df = pd.read_csv("data.csv")
        self.number_info_object = NumberInfo()
        self.labels_pretty = list(self.number_info_object.info.values())
        self.frequency = {}

    def get_frequency(self):
        labels = self.data_df.iloc[:, 1].tolist()

        for element in labels:
            if element not in self.frequency:
                self.frequency[element] = 1
            else:
                self.frequency[element] += 1

    def show_diagramm(self):
        values = list(self.frequency.values())
        plt.bar(self.labels_pretty, values)
        plt.show()


if __name__ == "__main__":
    number_info_object = DataAnalyse()
    number_info_object.get_frequency()
    number_info_object.show_diagramm()
