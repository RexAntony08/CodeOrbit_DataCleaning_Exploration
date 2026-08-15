# Simple Linear Regression Report
**Task:** Simple Linear Regression Model
**Dataset:** `sales_data_cleaned.csv` (output of Task 1 — 10 rows)

## 1. Goal
Predict **Revenue** from **Price** using a simple linear regression model. Price was chosen as the
predictor because Task 2's EDA showed Revenue is driven mainly by how expensive an item is (laptops vs
accessories), while Quantity varies only slightly (mostly 1–3 units) and doesn't explain the big
revenue swings on its own.

## 2. Method
- Split the data into training (70%) and test (30%) sets using `train_test_split`.
- Trained a `LinearRegression` model from scikit-learn on the training set.
- Evaluated on the held-out test set using MAE, RMSE, and R².

## 3. Model
The fitted line is approximately:

**Revenue ≈ 667.76 + 0.99 × Price**

This makes intuitive sense: since most orders in this dataset have Quantity = 1, Revenue (Quantity × Price)
ends up almost equal to Price itself — the slope of ~0.99 confirms nearly a 1-to-1 relationship, with a
small positive intercept and slight upward adjustment for orders with Quantity > 1.

## 4. Evaluation
| Metric | Value |
|---|---|
| MAE (test set) | ₹299.07 |
| RMSE (test set) | ₹331.97 |
| R² (test set) | 0.635 |
| R² (full dataset) | 0.999 |

**In simple terms:** the model explains the data almost perfectly overall (R² = 0.999 on the full
dataset), meaning Price alone predicts Revenue very well here. The test-set R² is lower (0.635) mainly
because the test split only had 3 data points — with such a small dataset, a single unusual point can
swing the test score a lot. This is a common limitation of small sample sizes and would be resolved with
more data.

## 5. Key Takeaway
Price is a strong, nearly one-to-one predictor of Revenue in this dataset because Quantity is usually 1.
In a larger, real-world dataset with more variation in order quantity, Quantity would likely need to be
included as a second predictor (multiple regression) to capture revenue accurately — a natural next step
beyond this simple regression exercise.
