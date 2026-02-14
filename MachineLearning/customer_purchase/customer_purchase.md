# Customer Purchase Category Prediction (Logistic Regression)

## Background
An e-commerce company wants to predict what product category a customer will purchase based on their age group, membership tier, and shopping session time.

## Dataset
- File: `customer_purchase.csv`
- Rows: 151 (last row has missing target value)
- Columns:
  - `customer_id`: Unique customer identifier
  - `age_group`: Teen, Young_Adult, Adult, Senior
  - `membership`: Bronze, Silver, Gold, Platinum
  - `session_time`: Short, Medium, Long
  - `category`: Electronics, Clothing, Books, Home, Sports, Beauty — **MISSING for last row**

## Task
- Load and explore the dataset
- Perform one-hot encoding on categorical variables
- Prepare the data:
  - Features (X): `age_group`, `membership`, `session_time`
  - Target (y): `category`
- Split into training (80%) and testing (20%) sets from rows 1–150
- Train a **Logistic Regression** model
- Predict the category for row 151 (the last row with missing target)

> Row 151 features: Adult, Gold, Long

## Note
Row 151 has all features but the `category` column is empty (NaN). This is the value you need to predict.

## Constraints
- Use `scikit-learn`'s `LogisticRegression`
- Use `pandas` for data manipulation
- Apply proper one-hot encoding techniques
