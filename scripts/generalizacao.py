import pandas as pd

class Generalizacao:
    def __init__(self, data):
        self.data = data
        self.df_anon = None
        self.df_mask = None

    def load_data(self):
        try:
            self.df_anon = pd.read_csv('data/titanic_anonimizado.csv')
            self.df_mask = pd.read_csv('data/titanic_masked.csv')

            
            
        except FileNotFoundError:
            print('File not found.')
    
    def merge_data(self):
        merged = pd.DataFrame()

        merged['PassengerId'] = self.df_mask['PassengerId']
        merged['Survived'] = self.df_anon['Survived']
        merged['Pclass'] = self.df_anon['Pclass']
        merged['Name'] = self.df_anon['Name_Hash']
        merged['Age'] = self.df_anon['Age']
        merged['SibSp'] = self.df_anon['SibSp']
        merged['Parch'] = self.df_anon['Parch']
        merged['Ticket'] = self.df_mask['Ticket']
        merged['Fare'] = self.df_anon['Fare']
        merged['Cabin'] = self.df_mask['Cabin']

        return merged

    
