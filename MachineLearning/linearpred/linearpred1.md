# Ice Cream Flavor Prediction (Linear Regression)

## Background
A shop wants to predict what ice cream flavor will be most popular the next day based on the day of the week. You have 100 days of sales history to build your prediction model.

## Dataset
- File: `linearpred1.csv`
- Rows: 100
- Columns:
  - `date`: Date in DD-MM-YYYY format
  - `weekday`: Day of the week (Monday to Sunday)
  - `flavor`: The top-selling flavor for that day — target variable

## Task
- Load the dataset
- Determine the next date after the last entry and compute its weekday
- Perform one-hot encoding on `weekday` (drop first)
- One-hot encode the target `flavor`
- Split into training (70%) and testing (30%) sets
- Train a **Linear Regression** model
- Predict the most likely flavor for the next day

## Constraints
- Use `scikit-learn`'s `LinearRegression`
- Use `pandas` for data manipulation
- Use `pd.get_dummies` with `drop_first=True` for weekday encoding
- Reindex prediction row to match training columns
