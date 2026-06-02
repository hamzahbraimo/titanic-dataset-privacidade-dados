import pandas as pd

try:
    df = pd.read_csv('data/titanic.csv')
except FileNotFoundError:
    print("File not found.")

print(df.head())
print()
print(df.info())
print()
print(df.isnull().sum())