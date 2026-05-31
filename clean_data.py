import pandas as pd

df = pd.read_csv("data.csv")

duplicate_count = df.duplicated().sum()

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df = df.drop_duplicates()

df["City"] = df["City"].str.title()

total_records = len(df)

report = f"""
DATA CLEANING REPORT
--------------------
Total Records: {total_records}
Duplicates Removed: {duplicate_count}
"""

print(report)