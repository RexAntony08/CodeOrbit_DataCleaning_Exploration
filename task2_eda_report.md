# Exploratory Data Analysis (EDA) Report
**Task:** Exploratory Data Analysis
**Dataset:** `sales_data_cleaned.csv` (output of Task 1 — 10 rows, 6 columns)

## 1. Approach
Loaded the cleaned dataset and used pandas + matplotlib/seaborn to visualize the distribution of
customer age, revenue by product, and the relationship between customer age and price paid. A time-based
revenue trend chart was also included as a bonus view.

## 2. Visualizations

**Histogram — Customer Age Distribution** (`hist_customer_age.png`)
Most customers fall between 27–34 years old, with a smaller spread of older customers up to 45.
The distribution is right-skewed (a longer tail toward older ages).

**Bar Chart — Total Revenue by Product** (`bar_revenue_by_product.png`)
Laptops dominate total revenue (~₹163,500), far ahead of Monitors (~₹30,000). Headphones, Keyboards,
and Mice contribute comparatively little, since they're low-priced items even though some sold multiple units.

**Scatter Plot — Price vs Customer Age** (`scatter_price_vs_age.png`)
Two visible clusters: younger customers (ages 27–34) tend to buy higher-priced items like Laptops,
while older customers (40–45) cluster around mid-priced Monitors. Low-cost accessories (Mouse, Keyboard,
Headphones) are spread across a wider age range.

**Bonus — Revenue Over Time** (`trend_revenue_over_time.png`)
Revenue spikes on days when a laptop was sold (Jan 5, Jan 8, Jan 12) and stays low on days with only
accessory sales, showing that big-ticket items drive most day-to-day revenue swings.

## 3. Key Findings
- **Laptops are the clear revenue driver** despite being only 3 of 10 orders — high price per unit matters more than order volume here.
- **Age and price show a weak negative correlation (-0.12)** — essentially no strong linear relationship, but the scatter plot reveals a more useful non-linear pattern: younger buyers lean toward laptops, older buyers lean toward monitors.
- **No major outliers remain** after Task 1's cleaning — the age and price ranges all look reasonable now.
- With only 10 rows, these are directional patterns from a small sample, not statistically robust conclusions — but they're exactly the kind of insight EDA is meant to surface before deeper modeling.
