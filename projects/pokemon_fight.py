import pandas as pd

df = pd.read_csv("C:/Users/chido/OneDrive/Desktop/pokemon.csv", index_col="Name")

df = df.drop(columns=["Type 1", "Type 2", "Total", "Sp. Atk", "Sp. Def", "Generation", "Legendary", "#"])

print("use CAP for first letter")
p1 = input("pick a pokemon: ")
p2 = input("pick a pokemon: ")

try:
    print(df.loc[p1])
except:
    print("this is not a pokemon")

try:
    print(df.loc[p2])
except:
    print("this is not a pokemon")

def HP():
    hp1 = int(df.loc[p1, "HP"])
    hp2 = int(df.loc[p2, "HP"])

    if hp1 > hp2:
        return f"{p1} wins"
    elif hp2 > hp1:
        return f"{p2} wins"
    else:
        return "its a tie"

def ATTACK():
    at1 = int(df.loc[p1, "Attack"]) 
    at2 = int(df.loc[p2, "Attack"]) 

    if at1 > at2:
        return f"{p1} wins"
    elif at2 > at1:
        return f"{p2} wins"
    else:
        return "its a tie"
    
def DEFENSE():
    df1 = int(df.loc[p1, "Defense"]) 
    df2 = int(df.loc[p2, "Defense"]) 

    if df1 > df2:
        return f"{p1} wins"
    elif df2 > df1:
        return f"{p2} wins"
    else:
        return "its a tie"
    
def SPEED():
    sd1 = int(df.loc[p1, "Speed"]) 
    sd2 = int(df.loc[p2, "Speed"]) 

    if sd1 > sd2:
        return f"{p1} wins"
    elif sd2 > sd1:
        return f"{p2} wins"
    else:
        return "its a tie"

results = []

results.append(HP())
results.append(ATTACK())
results.append(DEFENSE())
results.append(SPEED())

print(results)

win1 = sum(p1.lower() in result.lower() for result in results) # Loop through each item (stat outcome) in the results list
win2 = sum(p2.lower() in result.lower() for result in results) # Loop through each item (stat outcome) in the results list

if win1 > win2:
    print(f"{p1} wins")
elif win1 < win2:
    print(f"{p2} wins")
else:
    print("its a draw")