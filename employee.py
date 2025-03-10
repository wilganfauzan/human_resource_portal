import pandas as pd

class Employee:
    def __init__(self, csv):
        self.employees = pd.read_csv("employees.csv").to_dict(orient="records")

    def get_all(self):
        return self.employees
