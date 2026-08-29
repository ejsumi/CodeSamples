# Question 1 — Linear Regression: House Price Prediction

## Dataset
`house_prices.csv` — 180 rows, 8 columns.

| Column | Type | Description |
|---|---|---|
| area_sqft | numeric | Built-up area in sq. ft. |
| bedrooms | numeric (int) | Number of bedrooms |
| bathrooms | numeric (float) | Number of bathrooms — **contains missing values** |
| locality | categorical | `Downtown`, `Suburb`, `Rural` |
| age_years | numeric | Age of the property in years — **contains one outlier** |
| furnishing | categorical | `Furnished`, `Semi-Furnished`, `Unfurnished` |
| distance_to_city_km | numeric | Distance to city center in km — **contains missing values** |
| price_lakhs | numeric (target) | Price of the house in ₹ lakhs — **missing for the last 2 rows** |

## Task
Train a model to predict `price_lakhs` for the last 2 rows of the dataset (where the value is blank), using the remaining 178 rows as training data.

## Required steps

1. **Load** `house_prices.csv`. Split it into a training set (rows where `price_lakhs` is not null) and a prediction set (the last 2 rows, where `price_lakhs` is null).

2. **Handle missing values** (fit/compute imputation values on the training set only, then apply to both train and predict sets):
   - `distance_to_city_km`: fill missing values with the **median** of the training set.
   - `bathrooms`: fill missing values with the **mode** of the training set.

3. **Handle the outlier**:
   - `age_years` contains at least one unrealistic value. Cap (clip) all values in `age_years` at an upper bound of **100** (i.e., any value above 100 becomes 100).

4. **Encode categorical columns**:
   - One-hot encode `locality` and `furnishing` using `pandas.get_dummies(..., drop_first=True)`.
   - Apply encoding consistently across both the training and prediction sets (concatenate before encoding, or fit encoding categories on the combined column set, so both sets end up with identical columns).

5. **Train the model**:
   - Use `sklearn.linear_model.LinearRegression()` with default parameters. Do not scale the features (not required for this model).

6. **Predict**:
   - Predict `price_lakhs` for the last 2 rows.
   - Round predictions to **2 decimal places**.

7. **Output**:
   - Print the predictions as a Python list, e.g. `[110.38, 105.05]`, in the same row order as they appear in the file.

## Optional metric
If asked, also report **MAE (Mean Absolute Error)** on a simple train-internal check (e.g., hold out 20% of the training rows, fit on the rest, and report MAE on that internal holdout) — this is secondary; the main grading is on the predicted values above.

## Notes
- Your code will be re-run on larger hidden datasets with the same column names and structure, so do not hardcode row counts or specific column values — always derive the train/predict split from which rows have `price_lakhs` missing.
- Column names, encoding method, and missing-value strategy must match exactly as specified above to avoid mismatched predictions.
