import pandas as pd

from scripts.anonimizacao import DataAnonymization
from scripts.data_cleaning import DataCleaning
from scripts.generalizacao import Generalizacao
from scripts.pseudo_mask import PseudoMask

def main():
    path = 'data/titanic.csv'

    try:
        df = pd.read_csv(path)

        dc = DataCleaning(df)
        clean = dc.clean_data()

        print(clean.head())
        print()
        print(clean.info())
        print()
        print(clean.isnull().sum())

        dc.save_clean_data()
        pm = PseudoMask()
        
        pm.mask_data()
        
        a = DataAnonymization(df)
        
        a.anonimizar()

        g = Generalizacao()
        g.load_data()
        merged = g.generalizar()

        print(merged.tail(50))

    except FileNotFoundError:
        print('File not found')

if __name__ == "__main__":
    main()