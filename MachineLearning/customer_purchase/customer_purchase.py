import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load and explore the dataset
df = pd.read_csv('customer_purchase.csv')
print(df.head())
print(df.info())

# Separate last row (row 151) for prediction, drop customer_id
pred_row = df.iloc[-1:].copy()
df = df.iloc[:-1].copy()
df = df.drop(columns=['customer_id'])

# Separate features and target from training data (rows 1-150)
X = df[['age_group','membership','session_time']]
y = df['category']

# One-hot encode features and align prediction row to match training columns
X_en = pd.get_dummies(X)
pred_features = pred_row[['age_group','membership','session_time']]
pred_en = pd.get_dummies(pred_features)
pred_en = pred_en.reindex(columns=X_en.columns, fill_value=0)

# Split into 80% train and 20% test sets
X_train, X_test, y_train, y_test = train_test_split(X_en, y, test_size=0.2, random_state=42)

# Train Logistic Regression model and evaluate accuracy
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, y_pred), 3))

# Predict purchase category for row 151
predicted_category = model.predict(pred_en)
pred_row = pred_row.copy()
pred_row['category'] = predicted_category[0]
print(pred_row.iloc[0])
