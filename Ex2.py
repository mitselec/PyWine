"""
Exercise 2

Next, we will inspect the dataset and perform some mild data cleaning.
"""

data.head()
numeric_data = data.drop("color", axis =1)
