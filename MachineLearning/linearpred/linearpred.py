import pandas as pd
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error

# Load the dataset
df = pd.read_csv('LinearPred1.csv')

# Determine the next date and compute its weekday name
last_date = pd.to_datetime(df['date'].iloc[-1])
next_date = last_date + timedelta(days=1)
tomorrow_weekday = next_date.strftime('%A')  # e.g., "Tuesday"

print(f"Last date: {last_date.date()}")
print(f"Next date: {next_date.date()}")
print(tomorrow_weekday)

# One-hot encode weekday (drop_first=True) and target flavor
X = pd.get_dummies(df['weekday'],drop_first=True)
y = pd.get_dummies(df['flavor'])

# Encode prediction row and align columns to match training data
tomorrow_en = pd.get_dummies([tomorrow_weekday],drop_first=True)
tomorrow_en = tomorrow_en.reindex(columns=X.columns, fill_value=0)

# Split into 70% train and 30% test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
#print("mse:", mse)
accuracy = accuracy_score(y_test.values.argmax(axis=1), y_pred.argmax(axis=1))
#print(f"Model Accuracy: {accuracy:.2%}")

#print("Accuracy score:", round(accuracy,2))

# Predict next day's flavor and pick the class with highest score
pred = model.predict(tomorrow_en)
predicted_flavor = y.columns[pred.argmax()]  # fix: .replace('flavor_', '') was a no-op since get_dummies used no prefix
print(f"Next day flavor: {predicted_flavor}")
