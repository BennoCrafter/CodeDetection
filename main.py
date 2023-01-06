from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
import pandas as pd
from NumberInfo import NumberInfo


class Predict:
    def __init__(self):
        self.number_info_object = NumberInfo()
        self.data_df = pd.read_csv("data.csv")
        self.from_txt_file = True
        # read data from dataframe
        self.code_snippets = self.data_df.iloc[:, 0].tolist()
        self.labels = self.data_df.iloc[:, 1].tolist()

    def do_math(self):
        # Use a CountVectorizer to convert the text samples into numerical feature vectors
        self.vectorizer = CountVectorizer()
        X = self.vectorizer.fit_transform(self.code_snippets)
        # Train a LinearSVC classifier on the feature vectors
        self.classifier = LinearSVC()
        self.classifier.fit(X, self.labels)

    def get_output(self, user_input, txt):
        if txt:
            self.txt(user_input=user_input)
        else:
            new_sample_vector = self.vectorizer.transform([user_input])
            prediction = self.classifier.predict(new_sample_vector)
            prediction = self.number_info_object.get_data(number=prediction[0])
            print("I guess its a:", prediction)

    def txt(self, user_input):
        predict_input = open(user_input).read().split("\n")
        new_file = []
        pos = 1
        for element in predict_input:
            if not element:
                print("In line", pos, "is a free line")
                new_file.append("")
                pos += 1
            else:
                new_sample_vector = self.vectorizer.transform([element])
                prediction = self.classifier.predict(new_sample_vector)
                prediction = self.number_info_object.get_data(number=prediction[0])
                print("In line", pos, "is a", prediction)
                i = predict_input[pos - 1] + " #" + prediction
                new_file.append(i)
                pos += 1
        # write into file
        with open("predicted_code.py", "w") as f:
            for item in new_file:
                f.write(item + "\n")


if __name__ == "__main__":
    predictor = Predict()
    predictor.do_math()
    if predictor.from_txt_file:
        predictor.get_output(user_input=input("Whats the file path?:"), txt=True)
    else:
        predictor.get_output(user_input=input("What do you want to check?:"), txt=False)
