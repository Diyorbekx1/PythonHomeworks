homework1

import pandas as pd
import numpy as np

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)


df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)


print("First 3 rows:")


mean_age = df['age'].mean()
print("\nMean age:", mean_age)

print("\nName and City:")
print(df[['first_name', 'City']])


df['Salary'] = np.random.randint(40000,  size=len(df))

print("\nSummary statistics:")
print(df.describe(include='all'))

homework2

import pandas as pd


data = { 'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]}
sales_and_expenses = pd.DataFrame(data)


print("Maximum sales:", sales_and_expenses['Sales'].max())
print("Maximum expenses:", sales_and_expenses['Expenses'].max())


print("Minimum sales:", sales_and_expenses['Sales'].min())
print("Minimum expenses:", sales_and_expenses['Expenses'].min())

print("Average sales:", sales_and_expenses['Sales'].mean())
print("Average expenses:", sales_and_expenses['Expenses'].mean())


homework3
import pandas as pd

data = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]}
expenses = pd.DataFrame(data)

expenses = expenses.set_index('Category')


print("Maximum per category:\n", expenses.max(axis=1))
print("\nMinimum per category:\n", expenses.min(axis=1))
print("\nAverage per category:\n", expenses.mean(axis=1))


