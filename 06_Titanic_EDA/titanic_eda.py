# Titanic Dataset - Exploratory Data Analysis (EDA)

# A complete data cleaning and analysis pipeline

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD DATA
data = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)

# Initial inspection (uncomment to explore the raw data)
# print(data.head())
# print(data.info())
# print(data.describe())
# print(data.shape)

# 2. CLEAN DATA
# Age: fill missing values with the median (robust to outliers)
data["Age"] = data["Age"].fillna(data["Age"].median())

# Cabin: drop the entire column : over 687 missing values (77%+ of the data)
data = data.drop("Cabin", axis=1)

# Embarked: only 2 missing values : safe to fill with the most common port (mode)
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])

# Confirm no missing values remain
print("Missing values after cleaning:")
print(data.isnull().sum())
print()

# 3. ANALYZE : SURVIVAL RATES

# Survival rate by gender (%)
print("Survival rate by gender (%):")
print(data.groupby("Sex")["Survived"].mean() * 100)
print()

# Survival rate by passenger class (%)
print("Survival rate by passenger class (%):")
print(data.groupby("Pclass")["Survived"].mean() * 100)
print()

# 4. VISUALIZE

# Survival rate by gender : bar chart
sns.barplot(x="Sex", y="Survived", data=data)
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")
plt.show()

# Age distribution, split by gender : histogram
sns.histplot(data=data, x="Age", bins=20, hue="Sex")
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()