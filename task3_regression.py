import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Load cleaned dataset
df = pd.read_csv('sales_data_cleaned.csv')
df['Revenue'] = df['Quantity'] * df['Price']

print("=== DATA ===")
print(df[['Product', 'Quantity', 'Price', 'Revenue']])

# Step 2: Build a simple linear regression model
# Predicting Revenue from Price (X = Price, y = Revenue)
# Price is a much stronger driver of Revenue here than Quantity, since most
# orders have Quantity=1 and Revenue is dominated by how expensive the item is.
X = df[['Price']]
y = df['Revenue']

# With only 10 rows, use a small test split just to demonstrate train/evaluate workflow
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Step 3: Evaluate
y_pred_test = model.predict(X_test)
y_pred_all = model.predict(X)

print("\n=== MODEL PARAMETERS ===")
print(f"Intercept: {model.intercept_:.2f}")
print(f"Coefficient (slope) for Price: {model.coef_[0]:.2f}")

print("\n=== EVALUATION (on test set) ===")
print(f"MAE:  {mean_absolute_error(y_test, y_pred_test):.2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_test)):.2f}")
print(f"R² (test):  {r2_score(y_test, y_pred_test):.3f}")

r2_all = r2_score(y, y_pred_all)
print(f"R² (full dataset): {r2_all:.3f}")

# Step 4: Visualize regression line vs actual data
plt.figure(figsize=(6, 4))
plt.scatter(X, y, color='steelblue', s=80, label='Actual data')
x_line = np.linspace(X['Price'].min(), X['Price'].max(), 100).reshape(-1, 1)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, color='darkorange', linewidth=2, label='Regression line')
plt.xlabel('Price (₹)')
plt.ylabel('Revenue (₹)')
plt.title('Simple Linear Regression: Price vs Revenue')
plt.legend()
plt.tight_layout()
plt.savefig('regression_plot.png', dpi=120)
plt.close()

print("\nRegression plot saved as regression_plot.png")
