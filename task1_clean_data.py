import pandas as pd
import numpy as np

# Step 1: Load the dataset
df = pd.read_csv('sales_data.csv')
print("=== ORIGINAL DATA ===")
print(df)
print("\nShape:", df.shape)
print("\nData types:\n", df.dtypes)

# Step 2: Check for missing values
print("\n=== MISSING VALUES (before cleaning) ===")
print(df.isnull().sum())

# Step 3: Check for duplicates
print("\n=== DUPLICATE ROWS (before cleaning) ===")
print("Number of duplicate OrderIDs:", df.duplicated(subset=['OrderID']).sum())

# --- CLEANING STEPS ---

# 3a. Remove duplicate rows (based on OrderID, keep first occurrence)
df = df.drop_duplicates(subset=['OrderID'], keep='first')

# 3b. Fix incorrect data type: Quantity should be numeric, not mixed text/number
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

# 3c. Handle missing values
# Quantity: fill missing with median quantity
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())

# Price: fill missing with median price of that Product
df['Price'] = df.groupby('Product')['Price'].transform(lambda x: x.fillna(x.median()))
df['Price'] = df['Price'].fillna(df['Price'].median())  # fallback if group had no other value

# Customer_Age: fill missing with median age
df['Customer_Age'] = df['Customer_Age'].fillna(df['Customer_Age'].median())

# Fix incorrect/outlier value: age of 150 is impossible, treat as missing then fill with median
df.loc[df['Customer_Age'] > 100, 'Customer_Age'] = np.nan
df['Customer_Age'] = df['Customer_Age'].fillna(df['Customer_Age'].median())

# Product: drop row where Product name itself is missing (core identifier missing)
df = df.dropna(subset=['Product'])

# 3d. Fix data types
df['Quantity'] = df['Quantity'].astype(int)
df['Customer_Age'] = df['Customer_Age'].astype(int)
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'])

# Step 4: Basic statistics
print("\n=== CLEANED DATA ===")
print(df)

print("\n=== MISSING VALUES (after cleaning) ===")
print(df.isnull().sum())

print("\n=== BASIC STATISTICS ===")
print(df[['Quantity', 'Price', 'Customer_Age']].describe())

print("\n=== Mean Price:", df['Price'].mean())
print("Median Price:", df['Price'].median())
print("\nValue counts for Product:")
print(df['Product'].value_counts())

# Save cleaned dataset
df.to_csv('sales_data_cleaned.csv', index=False)
print("\nCleaned dataset saved as sales_data_cleaned.csv")
