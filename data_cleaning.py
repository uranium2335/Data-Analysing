# the process of fixing/removing
# incomplete, incorrect or irelivent data
# about 75% of work is done with pandas is data cleaning

import pandas as pd

df = pd.read_csv("C:/Users/chido/OneDrive/Desktop/pokemon.csv")

# just removes/drops colums that are listed 
# df = df.drop(columns=["Legendary", "Sp. Atk", "Sp. Def" ,"Total", "#", "Generation"])

# removes/drops any rows with a N/A or Nan 
df = df.dropna(subset=["Type 2"])

# replaces any N/A with somthing or ur choosing
# df= df.fillna({"Type 2": "None"})

# fix inconsistan values
# df["Type 1"] = df["Type 1"].replace({"Grass": "GRASS", 
#                                      "Fire": "FIREBALL", 
#                                      "Water": "WATER"})

# changes it to lower or changes data type
# df["Name"] = df["Name"].str.lower()

# remove duplicated
# df = df.drop_duplicates()

print(df)