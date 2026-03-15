import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load and explore the dataset
df = pd.read_csv('CodeSamples\MachineLearning\dish_pred\dish_pred.csv')
print(df.info())
print(df.head())

# One-hot encode features and target variable
X = pd.get_dummies(df[['meal_type','season','weather']])
y = pd.get_dummies(df['main_course'])
dish_classes = y.columns  # Store the dish names

# Split into 80% train and 20% test sets
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train,y_train)

# Build prediction row and align columns to match training data
data = pd.DataFrame({'meal_type': ['Dinner'], 'season': ['Winter'], 'weather': ['Snowy']})
data_encoded = pd.get_dummies(data)
data_enc = data_encoded.reindex(columns=X.columns, fill_value=0)

# Predict and extract dish with highest score
prediction = model.predict(data_enc)
predicted_dish = y.columns[np.argmax(prediction[0])]
print(f"Predicted main_course for Dinner, Winter, Snowy: {predicted_dish}")
