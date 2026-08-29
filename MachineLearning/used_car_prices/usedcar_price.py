import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Load and explore the dataset
df = pd.read_csv('used_car_prices.csv')
print(df.head())

# Drop Car_ID and Model columns as they are not useful features
target_col = 'Price'
df = df.drop(columns = ['Car_ID','Model'])

# Handle missing values: mode for categorical, median for numerical
for col in df.columns:
    if col != target_col:  # fix: 'not in' on a string checks substring match, not column identity
        if df[col].dtype =='object':
            df[col].fillna(df[col].mode()[0],inplace=True)
        else:
            df[col].fillna(df[col].median(), inplace=True)

# Encode categorical columns to numeric using LabelEncoder
catg_col = ['Brand', 'Fuel_Type','Transmission','Owner_Type']
for col in catg_col:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])

# Engineer new feature: Car_Age from manufacturing year
df['Car_Age'] = 2024 - df['Year']

# Scale numerical columns using StandardScaler
num_cols = ['Kilometers_Driven', 'Mileage_kmpl', 'Engine_CC', 'Power_bhp', 'Car_Age']
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

# Reserve last 8 rows for prediction, rest for training
df_final = df.iloc[:-8].copy()
df_pred = df.tail(8).copy()

# Separate features and target
X = df_final.drop(columns = ['Price'])
y = df_final["Price"]

# Split training data into 75% train and 25% test sets
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25,random_state=42)

X_target = df_pred.drop(columns=['Price'])

# --- Random Forest Regressor ---
model = RandomForestRegressor(n_estimators = 200, max_depth = 12, random_state = 42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_target = model.predict(X_target)
print("Random Forest Regressor Performance:")
print(np.round(y_target,3))
print("R2 Score:", round(r2_score(y_test,y_pred),3))
print("MAE:", round(mean_absolute_error(y_test,y_pred),3))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test,y_pred)),3))

# --- K-Nearest Neighbors Regressor ---
knn_model = KNeighborsRegressor(n_neighbors=7)
knn_model.fit(X_train, y_train)
y_pred_knn = knn_model.predict(X_test)
y_target_knn = knn_model.predict(X_target)
print("\nKNN Regressor Performance:")
print(y_target_knn)
print("R2 Score:", r2_score(y_test, y_pred_knn))
print("MAE:", mean_absolute_error(y_test, y_pred_knn))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_knn)))

# --- Decision Tree Regressor ---
dt_model = DecisionTreeRegressor(max_depth=10, random_state=42)
dt_model.fit(X_train, y_train)
y_pred_dt = dt_model.predict(X_test)
y_target_dt = dt_model.predict(X_target)
print("\nDecision Tree Regressor Performance:")
print(y_target_dt)
print("R2 Score:", r2_score(y_test, y_pred_dt))
print("MAE:", mean_absolute_error(y_test, y_pred_dt))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_dt)))

# --- Support Vector Regressor ---
svr_model = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1)
svr_model.fit(X_train, y_train)
y_pred_svr = svr_model.predict(X_test)
y_target_svr = svr_model.predict(X_target)
print("\nSupport Vector Regressor Performance:")
print(y_target_svr)
print("R2 Score:", r2_score(y_test, y_pred_svr))
print("MAE:", mean_absolute_error(y_test, y_pred_svr))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_svr)))
