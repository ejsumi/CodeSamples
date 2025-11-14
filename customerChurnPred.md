# Customer churn prediction

You are given a dataset customer_churn.csv containing the following columns:
```
CustomerID, Gender, SeniorCitizen, Tenure, MonthlyCharges, TotalCharges,
ContractType, InternetService, PaymentMethod, Churn
```

Note: The dataset contains last 3 rows where the target column Churn is missing, which is to be predicted.

## Tasks
1. Load the dataset and drop identifier column CustomerID.
2. Convert categorical columns (Gender, ContractType, InternetService, PaymentMethod) using label encoding or one-hot encoding.
3. Handle missing values:
   * Numeric → fill with median
   * Categorical → fill with most frequent value
4. Define Churn as the target variable and the remaining fields as features.
5. Split the data into training (70%) and testing (30%) sets.
6. Build a Random Forest Classifier using:
   * n_estimators = 150
   * max_depth = 10
   * random_state = 42
7. Train the model and predict values for the missing set.
8. Print the churn value for the last 3 rows
