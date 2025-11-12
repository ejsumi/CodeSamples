# Used Car Price Prediction
You are given a dataset used_car_prices.csv containing details of used cars listed for sale. The goal is to predict the selling price of used cars.
## Dataset Columns:

| Feature           | Description                                         |
|--------------------|-----------------------------------------------------|
| Car_ID             | Unique car identifier                               |
| Brand              | Car manufacturer (Maruti, Hyundai, Honda, etc.)     |
| Model              | Car model name                                      |
| Year               | Year of manufacture                                 |
| Fuel_Type          | Petrol / Diesel / CNG / Electric                    |
| Transmission       | Manual / Automatic                                  |
| Kilometers_Driven  | Total kilometers driven                             |
| Owner_Type         | First / Second / Third / Fourth & Above             |
| Mileage_kmpl       | Mileage in km per liter                             |
| Engine_CC          | Engine capacity in CC                               |
| Power_bhp          | Power in bhp                                        |
| Seats              | Number of seats                                     |
| Price              | Target variable: Selling price in ₹ (Lakhs)         |


## Task Instructions:

- Load the dataset and perform exploratory data analysis (check shape, data types, summary statistics).
Handle missing values appropriately:

- For numerical columns: use median imputation
- For categorical columns: use mode imputation

- Encode categorical variables:

 Use Label Encoding for Fuel_Type, Transmission, Owner_Type
 Use One-Hot Encoding for Brand (if number of unique brands ≤ 15)


- Create a new feature Car_Age by subtracting Year from current year (2024).

- Normalize the following numerical features using StandardScaler:
```
Kilometers_Driven, Mileage_kmpl, Engine_CC, Power_bhp, Car_Age
```
- Split the dataset into training and test sets with a 75-25 ratio (use random_state=42).
- Train a Random Forest Regressor with these parameters:
```
n_estimators = 200
max_depth = 15
min_samples_split = 5
min_samples_leaf = 2
random_state = 42
```

### Evaluate the model using:

R² Score (for both training and test sets)
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
Mean Absolute Percentage Error (MAPE)


### Predict the Price for the last 8 rows in the dataset.
- Display the predicted prices along with the actual features (Car_ID, Brand, Model, Year) for these 8 cars.


