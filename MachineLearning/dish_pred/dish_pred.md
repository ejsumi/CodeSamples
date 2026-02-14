# Restaurant Main Course Prediction (Linear Regression)

## Background
A restaurant wants to predict what main course customers will order based on the meal type, season, and weather conditions. You have 200 days of historical order data to build your prediction model.

## Dataset
- File: `dish_pred.csv`
- Rows: 200
- Columns:
  - `date`: Date in YYYY-MM-DD format
  - `meal_type`: Breakfast, Lunch, or Dinner
  - `season`: Spring, Summer, Fall, or Winter
  - `weather`: Sunny, Rainy, Cloudy, or Snowy
  - `main_course`: Pasta, Burger, Steak, Salad, Pizza, Sushi, or Tacos — target variable

## Task
- Load and explore the dataset
- Perform one-hot encoding on the categorical variables
- Prepare the data for modeling:
  - Features (X): `meal_type`, `season`, `weather`
  - Target (y): `main_course`
- Split the data into training (80%) and testing (20%) sets
- Train a **Linear Regression** model
- Predict the main course for: **Dinner, Winter, Snowy**

## Constraints
- Use `scikit-learn`'s `LinearRegression`
- Use `pandas` for data manipulation
- Use `pd.get_dummies` for one-hot encoding
- Reindex prediction data to match training columns
