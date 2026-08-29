import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, accuracy_score

#read data
df = pd.read_csv('laptop_data.csv')
print(df.describe())

target_col = 'Price'

# Create categorical col array
catg_cols = ['Brand','Processor','Operating_System','Graphics_Card']

# Fill missing values: mode for categorical, median for numerical
for col in df.columns:
    if col != target_col:  # fix: 'not in' on a string checks substring match, not column identity
        if df[col].dtype == 'object':
            df[col].fillna(df[col].mode()[0], inplace=True)
        else:
            df[col].fillna(df[col].median(),inplace=True)

# Detect outliers in RAM_GB using IQR and compute bounds
Q1 = df['RAM_GB'].quantile(.25)
Q3 = df['RAM_GB'].quantile(.75)

IQR = Q3 - Q1

lower = Q1-1.5*IQR
upper = Q3+1.5*IQR

# Filter out rows outside the IQR bounds
df1 = df[(df['RAM_GB']>=lower) & (df['RAM_GB']<=upper)]
df = df1

# to see the difference
print(df1.describe())

# Encode categorical columns to numeric using LabelEncoder
for col in catg_cols:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])

# Define numerical columns to scale
num_cols = ['RAM_GB','Storage_GB','Screen_Size','Weight_kg']  # fix: Operating_System is a label-encoded category, not a continuous value to scale

# Scale numerical columns using StandardScaler
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

#split the data
# Reserve last 5 rows for prediction, rest for training
pred = df.tail(5).copy()
data = df.iloc[:-5].copy()

# Separate features and target
X= data.drop(target_col,axis=1)
y = data['Price']

#train the model
# Split training data into train and test sets (25% test)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25, random_state=42)

# Train Random Forest Regressor and predict on test set
model = RandomForestRegressor(n_estimators=175, max_depth=12, random_state=42)
model.fit(X_train, y_train)
y_ml = model.predict(X_test)

# Predict prices for the last 5 reserved laptops
X_target = pred.drop(target_col,axis=1)
y_target = model.predict(X_target)

# Evaluate model and print predicted prices
print("r2_score:",round(r2_score(y_test,y_ml),3))
print("MAE:", round(mean_absolute_error(y_test,y_ml),3))
print (y_target.round(3))
