import pandas as pd

class DataCleaning:
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        self.data.drop_duplicates(inplace=True)
        
        self.data['Age'].fillna(self.data['Age'].median(), inplace=True)
        self.data['Age'] = self.data['Age'].astype(int)

        self.data['Embarked'].fillna('Desconhecido', inplace=True)
        self.data['Cabin'].fillna('Desconhecido', inplace=True)

        return self.data
    
    def save_clean_data(self):
        self.data.to_csv('data/titanic_clean.csv', index=False)

    def get_clean_data(self):
        try:
            df = pd.read_csv('data/titanic_clean.csv')
            return df
        except FileNotFoundError:
            print('File not found.')