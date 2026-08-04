# numpy handles only one data type best like all numbers or all strings
# pandas can handle different data types, null values in a table (dataframe)

# series : Pandas 1D building block
import pandas as pd
# ages = pd.Series([21,22,20,19]) # will show lables(index) as 0,1,2,3
ages = pd.Series([21,22,20,19], index = ["Umar","Ali","Hamza","Arham"])
print(ages)

# DataFrame : Pandas 2D building block
# it is a table - whole spreadsheet

data = {
    # each key is a column
    # each value list is a row
    "Name" : ["Umar","Ali","Hamza"],
    "Age": [21,18,19],
    "City": ["Multan","Lahore","Karachi"]
}
df = pd.DataFrame(data)
print(df)

# making dataframe from csv file
df = pd.read_excel("olympics-data.xlsx")
print(df.head()) # first 5 rows
print(df.tail()) # last 5 rows
print(df.shape) # rows,columns
print(df.columns) # list of column names
print(df.info()) # show data types, missing values summary
print(df.describe()) # mean, mode, med of numeric columns

print(df["name"]) # returns 'name' column -> returns a series 1D []
print(df[["name", "born_city"]]) # returns a DataFrame -2D [[]]

tallest = df[df["height_cm"] >= 190]
print(tallest)

# Practice
data = {
    "Name" : ["Umar","Ali","Hamza","Zain"],
    "Age" : [21, 23, 18, 19],
    "Marks" : [85,60,92,45]
}
df = pd.DataFrame(data)
print(df.describe())

good_students = df[df['Marks']>60]
print(good_students[['Name','Marks']])
# print(df[['Name','Marks']])
