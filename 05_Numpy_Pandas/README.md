# NumPy & Pandas Practice

A collection of exercises covering NumPy array operations and Pandas data manipulation — the core toolkit for data cleaning and analysis work.

## What's Inside

### `numpy_basics.py`
- Array creation and vectorized operations (element-wise math without loops)
- Broadcasting — applying operations across arrays of different shapes
- Boolean indexing and filtering (`array[array > threshold]`)
- Multi-condition filtering with `&` / `|`
- `np.where()` for vectorized conditional logic
- Aggregations across axes (`axis=0` vs `axis=1`) on 2D arrays

### `pandas_basics.py`
- Creating Series and DataFrames
- Reading and inspecting data (`.head()`, `.info()`, `.describe()`)
- Column selection and row filtering
- Boolean-based row selection (equivalent to SQL `WHERE`)

### `data_cleaning.py`
- Detecting missing values (`.isnull().sum()`)
- Handling missing data — `fillna()` with mean/default values vs `dropna()`
- Identifying and removing duplicate rows (`drop_duplicates()`)
- End-to-end cleaning of a messy, real-world-style dataset

## Why This Matters

Data cleaning is one of the most common real-world data tasks — messy CSVs with missing values, duplicates, and inconsistent formatting are the norm, not the exception. These exercises build the foundation for handling that kind of data reliably, whether for analysis, freelance data-cleaning work, or as a preprocessing step before machine learning.

## Tech Stack

- Python
- NumPy
- Pandas

## Part of

These exercises are part of a structured Python → AI Engineering learning roadmap