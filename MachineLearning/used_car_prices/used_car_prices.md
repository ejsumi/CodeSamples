# Used Car Price Prediction (Regression — Multi-Model Comparison)

## Background
A used car marketplace wants to predict the resale price of cars based on brand, age, fuel type, transmission, mileage, engine specs, and ownership history. The last 8 rows of the dataset are reserved for prediction.

## Dataset
- File: `used_car_prices.csv`
- Columns:
  - `Car_ID`: Unique car identifier (dropped)
  - `Brand`: Car manufacturer
  - `Model`: Car model (dropped)
  - `Year`: Manufacturing year
  - `Fuel_Type`: Petrol, Diesel, CNG, etc.
  - `Transmission`: Manual or Automatic
  - `Kilometers_Driven`: Total km driven
  - `Owner_Type`: First, Second, Third, etc.
  - `Mileage_kmpl`: Fuel efficiency
  - `Engine_CC`: Engine displacement in CC
  - `Power_bhp`: Engine power in bhp
  - `Seats`: Number of seats
  - `Price`: Resale price in lakhs — target variable

## Task
- Load and explore the dataset
- Drop `Car_ID` and `Model` columns
- Handle missing values (mode for categorical, median for numerical)
- Encode categorical columns (`Brand`, `Fuel_Type`, `Transmission`, `Owner_Type`) using `LabelEncoder`
- Engineer a new feature: `Car_Age = 2024 - Year`
- Scale numerical features (`Kilometers_Driven`, `Mileage_kmpl`, `Engine_CC`, `Power_bhp`, `Car_Age`) using `StandardScaler`
- Reserve last 8 rows for prediction; train on the rest
- Split training data into 75% train / 25% test
- Train and compare four regression models:
  - **Random Forest Regressor** (`n_estimators=200`, `max_depth=12`)
  - **K-Nearest Neighbors Regressor** (`n_neighbors=7`)
  - **Decision Tree Regressor** (`max_depth=10`)
  - **Support Vector Regressor** (`kernel=rbf`, `C=100`, `gamma=0.1`)
- Evaluate each model using R² score, MAE, and RMSE
- Predict prices for the last 8 cars using all four models

## Constraints
- Use `scikit-learn` for all models and metrics
- Use `LabelEncoder` for categorical encoding
- Use `StandardScaler` for numerical scaling
- Use `pandas` and `numpy` for data manipulation
