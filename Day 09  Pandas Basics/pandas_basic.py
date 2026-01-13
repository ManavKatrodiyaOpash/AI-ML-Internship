import pandas as pd

data = {
    "Name" : ["Manav","two","three","four","five","six","seven","eight","nine","ten"],
    "Age" : [21,15,23,22,19,17,14,15,19,17],
    "City" : ["Surat","London","Paris","Surat","Los Santos","Vice city","Surat","Vice city","Liberty city","Liberty city"]
}

df = pd.DataFrame(data)
print(df)

df2 = pd.read_csv("data.csv")
print(df2)

print(df.head())
print(df.tail())
print(df.describe())
print(df.info())

print("\n\n")
print(df["Name"].value_counts())
print(df["Age"].value_counts())
print(df["City"].value_counts())

print("\n\n")
print(df[df["Age"]>20])
df.sort_values(by="Age", ascending=False)
print(df.sort_values(by="Age", ascending=False))