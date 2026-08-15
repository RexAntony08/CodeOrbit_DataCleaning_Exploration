import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# Step 1: Load the cleaned dataset from Task 1
df = pd.read_csv('sales_data_cleaned.csv', parse_dates=['Purchase_Date'])
print("=== DATA OVERVIEW ===")
print(df.head())
print("\nShape:", df.shape)

# Step 2: Quick stats recap
print("\n=== SUMMARY STATS ===")
print(df.describe(include='all'))

# --- VISUAL 1: Histogram - distribution of Customer_Age ---
plt.figure(figsize=(6, 4))
sns.histplot(df['Customer_Age'], bins=6, kde=True, color='steelblue')
plt.title('Distribution of Customer Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('hist_customer_age.png', dpi=120)
plt.close()

# --- VISUAL 2: Bar chart - total revenue by product ---
df['Revenue'] = df['Quantity'] * df['Price']
revenue_by_product = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

plt.figure(figsize=(6, 4))
sns.barplot(x=revenue_by_product.index, y=revenue_by_product.values, hue=revenue_by_product.index, palette='viridis', legend=False)
plt.title('Total Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue (₹)')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('bar_revenue_by_product.png', dpi=120)
plt.close()

# --- VISUAL 3: Scatter plot - Price vs Customer_Age ---
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='Customer_Age', y='Price', hue='Product', s=100)
plt.title('Price vs Customer Age')
plt.xlabel('Customer Age')
plt.ylabel('Price (₹)')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=8)
plt.tight_layout()
plt.savefig('scatter_price_vs_age.png', dpi=120)
plt.close()

# --- VISUAL 4 (bonus): Sales trend over time ---
plt.figure(figsize=(6, 4))
daily_revenue = df.groupby('Purchase_Date')['Revenue'].sum()
daily_revenue.plot(marker='o', color='darkorange')
plt.title('Revenue Over Time')
plt.xlabel('Purchase Date')
plt.ylabel('Revenue (₹)')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('trend_revenue_over_time.png', dpi=120)
plt.close()

print("\nAll charts saved as PNG files.")

# Step 3: Print some pattern observations
print("\n=== KEY OBSERVATIONS ===")
print("Revenue by product:\n", revenue_by_product)
print("\nAverage price per product:\n", df.groupby('Product')['Price'].mean().sort_values(ascending=False))
print("\nCorrelation between Age and Price:", df['Customer_Age'].corr(df['Price']))
