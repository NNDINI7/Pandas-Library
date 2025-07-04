# -*- coding: utf-8 -*-
"""panda exercise.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13opuv3EFEV2_tkhJ43No33xJnvCYFu-E
"""

import pandas as pd
import numpy as np

print("--- Intermediate Pandas Exercise ---")
print("Complete each task by writing the requested Pandas code.")
print("------------------------------------")

# Task 1: Basic Pandas Functions and Converting Arrays to DataFrames
print("\n--- Task 1: Basic Pandas Functions and Converting Arrays to DataFrames ---")
# 1.1 Create a Pandas Series named 's1_1' from a list of numbers [10, 20, 30, 40, 50].
# 1.2 Create a 3x4 NumPy array named 'np_array1_2' with random integers between 1 and 100.
# 1.3 Convert 'np_array1_2' into a Pandas DataFrame named 'df1_3' with columns 'A', 'B', 'C', 'D'.

# Your code for Task 1 here:
s1_1 = pd.Series([10, 20, 30, 40, 50])
np_array1_2 = np.random.randint(1, 101, size=(3, 4))
df1_3 = pd.DataFrame(np_array1_2, columns=['A', 'B', 'C', 'D'])
print(s1_1)
print(df1_3)
print(np_array1_2)


# Task 2: Synthetic Data Generation for Practice
print("\n--- Task 2: Synthetic Data Generation for Practice ---")
# Create a DataFrame named 'df_sales' with 100 rows and the following columns:
# - 'Date': A range of dates from '2023-01-01' to '2023-04-09' (inclusive).
# - 'Region': Randomly chosen from ['East', 'West', 'North', 'South'].
# - 'Product': Randomly chosen from ['Laptop', 'Mouse', 'Keyboard', 'Monitor'].
# - 'Sales': Random integers between 100 and 1000.
# - 'Quantity': Random integers between 1 and 10.
# - Introduce 5 random NaN values in the 'Sales' column and 3 random NaN values in the 'Quantity' column.

# Your code for Task 2 here:
df_sales_dict = {
    'Date': pd.date_range(start='2023-01-01', end='2023-04-09', periods=100),
    'Region': np.random.choice(['East', 'West', 'North', 'South'], size=100),
    'Product': np.random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor'], size=100),
    'Sales': np.random.randint(100, 1001, size=100),
    'Quantity': np.random.randint(1, 11, size=100)
}

df_sales = pd.DataFrame(df_sales_dict)

# Introduce NaN values
df_sales.loc[np.random.choice(df_sales.index, 5, replace=False), 'Sales'] = np.nan
df_sales.loc[np.random.choice(df_sales.index, 3, replace=False), 'Quantity'] = np.nan

print(df_sales.head())


# Task 3: Indexing and Slicing in DataFrames
print("Task 3: Indexing and Slicing in DataFrames:")
# Use 'df_sales' from Task 2.
# 3.1 Select only the 'Region' and 'Sales' columns. Store it in 'df3_1'.
# 3.2 Select rows where 'Product' is 'Laptop'. Store it in 'df3_2'.
# 3.3 Select rows where 'Region' is 'East' AND 'Sales' are greater than 500. Store it in 'df3_3'.
# 3.4 Select the 'Sales' value for the first entry where 'Product' is 'Monitor' (use .loc and .iloc). Store it in 'val3_4'.

# Your code for Task 3 here:
df3_1 = df_sales[['Region', 'Sales']]
df3_2 = df_sales[df_sales['Product'] == 'Laptop']
df3_3 = df_sales[(df_sales['Region'] == 'East') & (df_sales['Sales'] > 500)]
val3_4 = df_sales.loc[df_sales['Product'] == 'Monitor', 'Sales'].iloc[0]
print(df3_1.head())
print(df3_2.head())
print(df3_3.head())
print(val3_4)

# Task 4: Data Cleaning (Handling Missing Values)
print("\n--- Task 4: Data Cleaning (Handling Missing Values) ---")
# Use 'df_sales' from Task 2 (which should have NaNs).
# 4.1 Check how many missing values are in each column. Store the result in 'missing_counts4_1'.
# 4.2 Fill missing 'Sales' values with the mean of the 'Sales' column. Store the modified DataFrame in 'df4_2_filled'.
# 4.3 Drop rows that have any missing values in 'df_sales'. Store the result in 'df4_3_dropped'.

# Your code for Task 4 here:
missing_counts4_1 = df_sales.isnull().sum()
df4_2_filled = df_sales.copy()
df4_2_filled['Sales'].fillna(df_sales['Sales'].mean(), inplace=True)
df4_3_dropped = df_sales.dropna()
print(missing_counts4_1)
print(df4_2_filled.head())
print(df4_3_dropped.head())

# Task 5: Data Manipulation (Columns, Sorting, Grouping)
print("\n--- Task 5: Data Manipulation (Columns, Sorting, Grouping) ---")
# Use 'df_sales' (the original one with NaNs)
# 5.1 Create a new column 'Total_Revenue' which is 'Sales' * 'Quantity'.
#     (Be mindful of NaNs, the result should also be NaN where either Sales or Quantity is NaN).
# 5.2 Sort 'df_sales' by 'Date' in ascending order, then by 'Sales' in descending order. Store it in 'df5_2_sorted'.
# 5.3 Group 'df_sales' by 'Region' and calculate the sum of 'Sales' and 'Quantity' for each region.
#     Store the result in 'df5_3_grouped_region'.
# 5.4 Group 'df_sales' by 'Product' and find the average 'Sales' for each product.
#     Store the result in 'df5_4_grouped_product'.

# Your code for Task 5 here:
df_sales['Total_Revenue'] = df_sales['Sales'] * df_sales['Quantity']
print(df_sales[['Sales', 'Quantity', 'Total_Revenue']].head())
df5_2_sorted = df_sales.sort_values(by=['Date', 'Sales'], ascending=[True, False])
print(df5_2_sorted.head())
df5_3_grouped_region = df_sales.groupby('Region')[['Sales', 'Quantity']].sum()
print(df5_3_grouped_region)
df5_4_grouped_product = df_sales.groupby('Product')['Sales'].mean()
print(df5_4_grouped_product)

