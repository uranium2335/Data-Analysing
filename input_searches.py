import pandas as pd

df = pd.read_csv("C:/Users/chido/OneDrive/Desktop/pokemon.csv", index_col="Name")

pokemon = input("enter pokemon name: ")

try:
    print(df.loc[pokemon])

except KeyError:
    print(f"{pokemon} not in pokedex")