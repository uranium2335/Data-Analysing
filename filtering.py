import pandas as pd

df = pd.read_csv("C:/Users/chido/OneDrive/Desktop/pokemon.csv", index_col="Name")

selected = df[(df["Legendary"] == True) & (df["Generation"] == 1)]

print(selected)