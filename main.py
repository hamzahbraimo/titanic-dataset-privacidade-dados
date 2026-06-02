import pandas as pd

from scripts.data_cleaning import DataCleaning

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

    except FileNotFoundError:
        print('FIle not found')

if __name__ == "__main__":
    main()