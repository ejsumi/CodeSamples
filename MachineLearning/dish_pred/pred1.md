# Restaurant Main Course Prediction

## Background
A restaurant wants to predict what main course customers will order based on the meal type, season, and weather conditions. You have 200 days of historical order data to build your prediction model.

## 
Dataset

File: restaurant_orders.csv
Rows: 200
Columns:

date: Date in YYYY-MM-DD format
meal_type: Breakfast, Lunch, or Dinner
season: Spring, Summer, Fall, or Winter
weather: Sunny, Rainy, Cloudy, or Snowy
main_course: Pasta, Burger, Steak, Salad, Pizza, Sushi, or Tacos



Your Task

Load and explore the dataset
Perform one-hot encoding on the categorical variables
Prepare the data for modeling:

Use meal_type, season, and weather as features (X)
Use main_course as the target variable (y)


Split the data into training (80%) and testing (20%) sets
Train a Linear Regression model
Predict the main course for: Dinner, Winter, Snowy