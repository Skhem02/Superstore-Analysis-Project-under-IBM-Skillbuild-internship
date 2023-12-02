# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("SampleSuperstore.csv")

# Display the first 5 rows of the DataFrame
df.head()

# Drop the "Postal Code" column (returns a new DataFrame, doesn't modify the original)
df.drop(columns="Postal Code")

# Drop the "Postal Code" column in-place (modifies the original DataFrame)
df.drop(columns="Postal Code", inplace=True)

# Display the first 5 rows of the DataFrame after dropping the "Postal Code" column
df.head()

# Print unique values in certain columns to understand categorical aspects of the data
print(df["Ship Mode"].unique())
print(df["Segment"].unique())
print(df["Country"].unique())
print(df["Category"].unique())
print(df["City"].unique())
print(df["State"].unique())
print(df["Region"].unique())
print(df["Sub-Category"].unique())
print(df["Sales"].unique())
print(df["Quantity"].unique())
print(df["Discount"].unique())
print(df["Profit"].unique())

# Generate descriptive statistics of the DataFrame
df.describe()

# Print a concise summary of the DataFrame
df.info()

# Count the number of missing values in each column
df.isna().sum()

# Generate bar charts and pie charts for data analysis
df.groupby("Region")["Profit"].sum().plot.bar()
df.groupby("Region")["Profit"].sum().plot.bar()
df.groupby("Region")["Sales"].sum().plot.pie(autopct="%1.0f%%")
df.groupby("Region")["Profit"].sum().plot.pie(autopct="%1.0f%%")
df.groupby("Segment")["Sales"].sum().plot.bar()
df.groupby("Segment")["Profit"].sum().plot.bar()
df.groupby("Category")["Sales"].sum().plot.bar()
df.groupby("Category")["Profit"].sum().plot.bar()
df.groupby("Category")["Sales"].sum().plot.pie(autopct="%1.0f%%")
df.groupby("Category")["Profit"].sum().plot.pie(autopct="%1.0f%%")
df.groupby("State")["Sales"].sum().plot.bar()
df.groupby("State")["Profit"].sum().plot.bar()
