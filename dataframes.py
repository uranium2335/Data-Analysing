import pandas as pd

data = {
    "name":["spongebob","patrick","squidward"],
    "age":["18","19","25"]
}

df = pd.DataFrame(data, index=["Employee 1","Employee 2","Employee 3"])

print(df)

print("----------")

# add a new collum
df["job"] = ["cook" ,"N/A" ,"cashier"]

# add a new rows
new_rows = pd.DataFrame([{"name": "sandy", "age": 28, "job": "scientist"},
                        {"name": "eugene", "age": 60, "job": "manager"}], 
                       index=["Emoplyee 4", "employee 5"])
df = pd.concat([df, new_rows])

print(df)



# print(df.loc["Employee 1"])
# print(df.loc[2])