Task 1: Data Cleaning & Exploration with Pandas
Dataset: Sample sales dataset (sales_data.csv) — 12 rows, 6 columns
1. Loading the Data
Loaded the CSV using pandas' read_csv(). Initial inspection showed 12 rows, one duplicate order, and missing values across 4 different columns.
2. Issues Found
Duplicates: OrderID 108 appeared twice (identical row)
Missing values: one missing entry each in Product, Quantity, Price, and Customer_Age
Incorrect data type: Quantity was stored as mixed text/number instead of a clean integer column
Invalid outlier: one Customer_Age value was 150, which isn't a realistic age
3. Cleaning Steps Applied
Dropped the duplicate order (kept the first occurrence)
Converted Quantity to numeric, then filled the missing value with the column median
Filled missing Price values using the median price for that same product
Replaced the invalid age (150) with a missing value, then filled all missing ages with the median age
Dropped the one row with a missing Product name, since it's the core identifier
Converted Purchase_Date to a proper datetime type and cast Quantity/Customer_Age to integers
Result: 12 rows became 10 clean rows, with 0 missing values remaining.
4. Basic Statistics (after cleaning)
Quantity — mean 1.50, median 1.00, min 1, max 3
Price (₹) — mean 19,880, median 8,500, min 450, max 55,000
Customer_Age — mean 31.9, median 30.5, min 22, max 45
Product value counts: Laptop (3), Mouse (2), Keyboard (2), Monitor (2), Headphones (1)
5. Key Takeaway
The dataset had typical real-world messiness: duplicate records, missing values, and a mixed-type column. Filling missing prices by product group kept estimates realistic, since a missing laptop price shouldn't be replaced by the average of cheap accessories. The cleaned dataset is now ready for further analysis.
