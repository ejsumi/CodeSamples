import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix

# Load and explore the dataset
df = pd.read_csv('customer_churn.csv')
print(df.head())

# Drop CustomerID column as it is not a useful feature
df = df.drop(columns=['CustomerID'])

# Handle missing values: mode for categorical, median for numerical
target_col = 'Churn'

for col in df.columns:
    if col != target_col:  # fix: 'not in' on a string checks substring match, not column identity
        if df[col].dtype == 'object':
            df[col].fillna(df[col].mode()[0],inplace=True)
        else:
            df[col].fillna(df[col].median(),inplace=True)

#print(df['Gender'].value_counts())

# Encode categorical columns to numeric using LabelEncoder
catg_cols = ['Gender','ContractType','InternetService','PaymentMethod']
#df = pd.get_dummies(df,columns=catg_cols, drop_first=True)
encoder = LabelEncoder()
for col in catg_cols:
    df[col] = encoder.fit_transform(df[col])

# Reserve last 3 rows for prediction, rest for training
df_pred = df.tail(3).copy()
df = df.iloc[:-3].copy()

# Scale numerical columns using StandardScaler
scaler = StandardScaler()
num_cols = ['Tenure','MonthlyCharges', 'TotalCharges']
df[num_cols] = scaler.fit_transform(df[num_cols])

# Apply the same scaler to prediction rows
df_pred[num_cols] = scaler.transform(df_pred[num_cols])

# Separate features and target
X= df.drop(columns = target_col)
y = df[target_col]

# Split data into 70% train and 30% test sets
X_train, X_test,y_train,y_test = train_test_split(X,y, test_size=0.3, random_state=42)

# Train Random Forest Classifier and predict on test set
model = RandomForestClassifier(n_estimators = 175,max_depth = 6,random_state = 42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Predict churn for the last 3 reserved customers
X_pred = df_pred.drop(columns=['Churn'])
churn_pred = model.predict(X_pred)

# Evaluate model with accuracy and precision scores
print("accuracy",round(accuracy_score(y_test,y_pred),3))
print("precison",round(precision_score(y_test,y_pred),3))

print(churn_pred)
