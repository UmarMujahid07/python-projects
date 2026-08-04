# real world data is messy
# in this, we will handle missing values, use of groupby, combining 2 datasets

import numpy as np
import pandas as pd

data = {
    "Name" : ["Umar","Umar","Ali","Hamza","Zain"],
    "Age" : [21,21, np.nan, 20, 19], # nan is "Not a Number"
    "City" : ["Multan","Multan","Lahore",np.nan,"Karachi"]
}
df = pd.DataFrame(data)
print(df)

print(df.isnull()) # True False grid for each cell
print(df.isnull().sum()) # count null of each column

# handling missing values
# approach a - remove whole row
cleaned_data = df.dropna()
print(cleaned_data)
# we can lose more data by this

# fill nan by replacing
df["Age"] = df["Age"].fillna(df["Age"].mean()) # fill with average age
df["City"] = df["City"].fillna("Unknown") # fill with Unknown
print(df)

# finding and removing duplicate rows
print(df.duplicated()) # -> True where duplcate exists
df_unique = df.drop_duplicates()
print(df_unique)

# Groupby - summarize data in categories
data1 = {
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [80000, 60000, 95000, 70000, 65000]
}
df = pd.DataFrame(data1)
print(df.groupby("Department")["Salary"].mean())
# multiple aggregations together
print(df.groupby("Department")["Salary"].agg(["mean","count","max"]))

# merging 2 DataFrames
employees = pd.DataFrame({
    "id":[1,2,3],
    "name":["Ahmad","Ali","Bilal"],
    "dept_id":[1,2,1]
})

departments = pd.DataFrame({
    "dept_id": [1, 2],
    "dept_name": ["IT", "HR"]
})

merged = pd.merge(employees,departments, on="dept_id")
print(merged)

# daily task

data = {
    "Name": ["Umar", "Ali", "Sara", "Umar", "Zain"],
    "Age": [21, np.nan, 20, 21, 19],
    "City": ["Multan", "Lahore", np.nan, "Multan", "Karachi"],
    "Salary": [50000, 60000, 55000, 50000, 45000]
}
df = pd.DataFrame(data)
print(f"Missing values count: \n{df.isnull().sum()}")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["City"] = df["City"].fillna("Unknown")

df = df.drop_duplicates()
print(df)