import pandas as pd

class Training:
    def __init__(self, csv):
        self.training = pd.read_csv("training.csv").to_dict(orient="records")

    def get_all(self):
        return self.training
