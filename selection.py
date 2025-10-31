import pandas as pd

# switches it so that Name becomes the index so it becoms search by name no number
df = pd.read_csv("C:/Users/chido/OneDrive/Desktop/pokemon.csv", index_col="Name")

# selection by column
# searches for the column called Name

# print(df[["Name","Type 1","Type 2"]])

# selection by rows/s

# print(df.loc["Mewtwo", ["Type 1", "Attack", "Defense"]])

# giving it a range of pokemon to print
# print(df.loc["Mewtwo":"Skiploom", ["Type 1", "Attack", "Defense"]])

# from:to:step  /   now its the columns from:to
print(df.iloc[0:11:2, 0:3])