import pandas as pd

# used to read .csv files
df = pd.read_csv("C:/Users/chido/OneDrive/Desktop/pokemon.csv")
print(df)

# used to print .json files
df1 = pd.read_json("C:/Users/chido/OneDrive/Desktop/pokemon.json")
print(df1)