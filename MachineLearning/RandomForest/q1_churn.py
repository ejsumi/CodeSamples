import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


df = pd.read_csv('churn_train.csv')

train = df.iloc[:-2]

df['monthly_charges'] = df['monthly_charges'].fillna(train['monthly_charges'].median())
df['total_charges'] = df['total_charges'].fillna(train['total_charges'].median())

Q1 = train['monthly_charges'].quantile(.25)
Q3 = train['monthly_charges'].quantile(.75)

IQR = Q3-Q1

df['monthly_charges'] = df['monthly_charges'].clip(lower = Q1-1.5*IQR, upper = Q3+ 1.5*IQR)

df_pred = df.tail(2).copy()
df_train = df.iloc[:-2].copy()

encoder = LabelEncoder()
df_train['contract_type'] = encoder.fit_transform(df_train['contract_type'])
df_pred['contract_type'] = encoder.transform(df_pred['contract_type'])


X = df_train.drop(columns=['churn'])
y = df_train['churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100,max_depth=5, random_state=42)
model.fit(X_train, y_train)

X_pred = df_pred.drop(columns=['churn'])

y_pred = model.predict(X_pred)

y_pred = ['Stayed' if x == 0 else 'Churned' for x in y_pred]
#print(df_pred.info())
print(y_pred)