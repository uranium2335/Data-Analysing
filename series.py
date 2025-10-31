import pandas as pd

data = [100, 102, 104, 200 ,202]

series = pd.Series(data, index = ["a","b","c","d","e"])

# loc for location by label
print(series.loc["c"])

print("-----------")

# iloc for intiger location
print(series.iloc[0])

print("-----------")

# getting data ranges
print(series[series >= 200])

print("-----------")

# created a dictionary
cal = {"day 1": 1750, 
       "day 2": 2100, 
       "day 3": 1700
       }

series = pd.Series(cal)


print(series)