# Titanic Dataset — Exploratory Data Analysis

An end-to-end EDA pipeline on the classic Titanic dataset — covering data loading, cleaning, statistical analysis, and visualization.

## Problem Statement

Given raw, real-world passenger data from the Titanic (with missing values and mixed data types), clean the dataset and explore what factors — specifically gender and passenger class — were associated with survival.

## What This Project Covers

- **Data Loading** — reading a CSV dataset directly from a remote source
- **Data Cleaning**
  - Filling missing `Age` values with the median (robust to outliers)
  - Dropping the `Cabin` column entirely (77%+ missing — too sparse to be usable)
  - Filling missing `Embarked` values with the mode (most common value)
- **Statistical Analysis**
  - Survival rate by gender, using `groupby()` on a binary (0/1) column to directly compute percentages
  - Survival rate by passenger class
- **Visualization**
  - Bar chart comparing survival rate across genders
  - Histogram showing age distribution, split by gender

## Key Findings

- Survival rate was substantially higher among female passengers than male passengers
- Survival rate decreased with passenger class (1st class passengers had a notably higher survival rate than 3rd class)

## Tech Stack

- Python
- Pandas
- Matplotlib
- Seaborn

## How to Run

```bash
python titanic_eda.py
```

The script prints cleaning/analysis results to the console and displays two charts (survival by gender, age distribution by gender).

## What I Learned

This project reinforced a practical, decision-driven approach to data cleaning — different missing-value strategies (fill vs. drop, mean vs. median vs. mode) depending on how much data is missing and what the column represents. It also highlighted a useful Pandas pattern: taking the `.mean()` of a binary column to directly compute a rate/percentage without extra calculation steps.
