import pandas as pd
import secrets

class Generalizacao:
    def __init__(self):
        self.df_anon = None
        self.df_mask = None
        self.merged = pd.DataFrame()

    def load_data(self):
        try:
            self.df_anon = pd.read_csv('data/titanic_anonimizado.csv')
            self.df_mask = pd.read_csv('data/titanic_masked.csv')

        except FileNotFoundError:
            print('File not found.')
    
    def merge_data(self):
        self.merged['PassengerId'] = self.df_mask['PassengerId']
        self.merged['Survived'] = self.df_anon['Survived']
        self.merged['Pclass'] = self.df_anon['Pclass']
        self.merged['Name'] = self.df_anon['Name_Hash']
        self.merged['Age'] = self.df_anon['Age'].astype(object)
        self.merged['NrFamiliares'] = self.df_anon['SibSp'] + self.df_anon['Parch']
        self.merged['Ticket'] = self.df_mask['Ticket']
        self.merged['Fare'] = self.df_anon['Fare']
        self.merged['Cabin'] = self.df_mask['Cabin']

    def gen_age(self):

        for age in self.merged['Age']:
            if int(age) < 18:
                self.merged['Age'] = self.merged['Age'].replace(age, 'Menor')
            elif int(age) < 60:
                self.merged['Age'] = self.merged['Age'].replace(age, 'Adulto')
            else:
                self.merged['Age'] = self.merged['Age'].replace(age, 'Senior')

    def gen_classe(self):
        token_map: dict[int, str] = {}
        classes = [1, 2, 3]

        for element in classes:
            if element not in token_map:
                token_map[element] = secrets.token_hex(2)
        

        for e in self.merged['Pclass']:
            self.merged['Pclass'] = self.merged['Pclass'].replace(e, token_map[e])

    def gen_fam(self):

        for fam in self.merged['NrFamiliares']:
            if int(fam) == 0:
                self.merged['NrFamiliares'] = self.merged['NrFamiliares'].replace(fam, 'Sem familiares')
            elif int(fam) < 4:
                self.merged['NrFamiliares'] = self.merged['NrFamiliares'].replace(fam, 'Pequena')
            else:
                self.merged['NrFamiliares'] = self.merged['NrFamiliares'].replace(fam, 'Grande')

    def gen_fare(self):

        for e in self.merged['Fare']:
            if float(e) < 100:
                self.merged['Fare'] = self.merged['Fare'].replace(e, 'menos que $100')
            elif float(e) < 200:
                self.merged['Fare'] = self.merged['Fare'].replace(e, '$100-$200')
            elif float(e) < 300:
                self.merged['Fare'] = self.merged['Fare'].replace(e, '$200-$300')
            elif float(e) < 400:
                self.merged['Fare'] = self.merged['Fare'].replace(e, '$300-$400')
            else:
                self.merged['Fare'] = self.merged['Fare'].replace(e, '$500+')

    def save(self):
        self.merged.to_csv('data/titanic_tratado.csv', index=False)

    def generalizar(self):
        self.merge_data()
        self.gen_age()
        self.gen_fam()
        self.gen_classe()
        self.gen_fare()
        self.save()

        return self.merged