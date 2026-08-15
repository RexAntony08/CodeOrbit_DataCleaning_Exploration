# Data Cleaning & Exploration Report
**Task:** Data Cleaning & Exploration with Pandas
**Dataset:** Sample sales dataset (`sales_data.csv`) — 12 rows, 6 columns

## 1. Loading the Data
Loaded the CSV using `pandas.read_csv()`. Initial inspection with `.shape`, `.dtypes`, and `.isnull().sum()`
showed 12 rows, one duplicate order, and missing values in 4 different columns.

## 2. Issues Found
- **Duplicates:** OrderID `108` appeared twice (identical row).
- **Missing values:** one missing entry each in `Product`, `Quantity`, `Price`, and `Customer_Age`.
- **Incorrect data type:** `Quantity` was stored as mixed text/number (e.g., `"1"` as a string) instead of a clean integer column.
- **Invalid outlier:** one `Customer_Age` value was `150`, which is not a realistic age and was treated as bad data.

## 3. Cleaning Steps Applied
1. Dropped the duplicate order (kept the first occurrence).
2. Converted `Quantity` to numeric using `pd.to_numeric(..., errors='coerce')`, then filled the missing value with the column median.
3. Filled missing `Price` values using the median price for that same product (a laptop's missing price is estimated from other laptop prices, not the overall average).
4. Replaced the invalid age (150) with a missing value, then filled all missing ages with the median age.
5. Dropped the one row with a missing `Product` name, since the product is the core identifier of a sales record.
6. Converted `Purchase_Date` to a proper datetime type and cast `Quantity`/`Customer_Age` to integers.

**Result:** 12 rows → 10 clean rows, 0 missing values remaining.

## 4. Basic Statistics (after cleaning)
| Metric | Quantity | Price (₹) | Customer_Age |
|---|---|---|---|
| Mean | 1.50 | 19,880 | 31.9 |
| Median | 1.00 | 8,500 | 30.5 |
| Min | 1 | 450 | 22 |
| Max | 3 | 55,000 | 45 |

**Product value counts:** Laptop (3), Mouse (2), Keyboard (2), Monitor (2), Headphones (1)

## 5. Key Takeaway
The dataset had typical real-world messiness: duplicate records, missing values, and a mixed-type column.
Filling missing prices by product group (rather than a flat average) kept estimates realistic, since a
missing laptop price shouldn't be replaced by the average of cheap accessories. The cleaned dataset is now
ready for further analysis such as EDA or building a regression model.
