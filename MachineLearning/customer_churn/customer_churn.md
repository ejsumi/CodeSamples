# Customer Churn Prediction (Random Forest)

## Background
A telecom company wants to predict whether a customer will churn (leave the service) based on their demographics, account details, and service usage patterns.

## Dataset
- File: `customer_churn.csv`
- Columns:
  - `CustomerID`: Unique customer identifier
  - `Gender`: Male or Female
  - `SeniorCitizen`: 0 or 1
  - `Tenure`: Number of months the customer has been with the company
  - `MonthlyCharges`: Monthly bill amount
  - `TotalCharges`: Total amount charged to date
  - `ContractType`: Month-to-Month, One Year, Two Year
  - `InternetService`: DSL, Fiber Optic, No
  - `PaymentMethod`: Credit Card, Electronic Check, etc.
  - `Churn`: 1 (churned) or 0 (retained) — target variable

## Task
- Load and explore the dataset
- Drop `CustomerID` column
- Handle missing values (mode for categorical, median for numerical)
- Encode categorical columns using `LabelEncoder`
- Reserve the last 3 rows for prediction
- Scale numerical features using `StandardScaler`
- Split data into training (70%) and testing (30%) sets
- Train a **Random Forest Classifier** (`n_estimators=175`, `max_depth=6`)
- Evaluate with accuracy and precision scores
- Predict churn for the last 3 customers

## Constraints
- Use `scikit-learn`'s `RandomForestClassifier`
- Use `pandas` for data manipulation
- Use `StandardScaler` for feature scaling
- Use `LabelEncoder` for categorical encoding
