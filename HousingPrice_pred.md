# Predicting House Prices Using Random Forest Regression

You are given a dataset housing_data.csv with the following columns:

Area, Bedrooms, Bathrooms, Stories, Parking, Furnishing, Mainroad, Guestroom, Price

Tasks

- Load and inspect the dataset.

- Handle categorical features like Furnishing, Mainroad, and Guestroom using one-hot or label encoding.

- Treat missing values, if any, by imputing suitable replacements.

- Define Price as the target variable and the rest as predictors.

- Split the data into training (70%) and testing (30%) sets.

- Build a Random Forest Regressor with the following parameters:
```
n_estimators = 200

max_depth = 10

random_state = 0
```

- Train the model and predict on the test data.