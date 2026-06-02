import pandas as pd

class Data_Cleaning:
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        self.data.drop_duplicates(inplace=True)
        self.data.fillna(method='ffill', inplace=True)
        return self.data