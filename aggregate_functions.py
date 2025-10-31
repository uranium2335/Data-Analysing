# aggrogate functions = reduce a set of values into a single summaried value
#                       used to summaries and analyze data
#                       often used with grouby() function

import pandas as pd

df = pd.read_csv("C:/Users/chido/OneDrive/Desktop/pokemon.csv", index_col="Name")

# gettiing thigs that are numbers only
# value = df.mean(numeric_only=True)

# value = df.sum(numeric_only=True)
# value = df.min(numeric_only=True)
# value = df.max(numeric_only=True)
# value = df.mean(numeric_only=True)
# value = df.median(numeric_only=True)
value = df.mode(numeric_only=True)

print(value)

# just counts how many valid things are in each column
other = df.count()
print(other)

print("----------------------------------------------------------")
#only applied to a column

# value = df["HP"].sum()
# value = df["Attack"].min()
# value = df["Defense"].max()
# value = df["Sp. Atk"].mean()
# value = df["Speed"].median()

# print(value)

print("----------------------------------------------------------")

group = df.groupby("Speed") # groups everything with the same speed
print(group["Attack"].count())# then in all the groups it will look at their attack and then how many are in each group(sum)