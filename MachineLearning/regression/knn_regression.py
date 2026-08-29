import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor

df = pd.read_csv('employee_dataset.csv')

eid = df.tail(3)['EmployeeID'].copy()

df = df.drop(columns=['EmployeeID', 'Education','Salary', 'Attrition'])
df_pred = df.tail(3).copy()
df1 = df.iloc[:-3]


df = df1[df1['PerformanceRating'].notna()]

df['Age'] = df['Age'].fillna(df['Age'].mean())
df_pred['Age'] = df_pred['Age'].fillna(df['Age'].mean())
df['DistanceFromHome_km'] = df['DistanceFromHome_km'].fillna(df['DistanceFromHome_km'].median())
df_pred['DistanceFromHome_km'] = df_pred['DistanceFromHome_km'].fillna(df['DistanceFromHome_km'].median())

df = pd.get_dummies(df, columns=['Department'], drop_first=True)
df_pred = pd.get_dummies(df_pred, columns=['Department'], drop_first=True )

num_cols = ['Age', 'YearsAtCompany', 'DistanceFromHome_km','MonthlyWorkingHours']
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])
df_pred[num_cols] = scaler.transform(df_pred[num_cols])

X = df.drop(columns=['PerformanceRating'])
y = df['PerformanceRating']
X_pred = df_pred.drop(columns=['PerformanceRating'])
X_pred = X_pred.reindex(columns=X.columns, fill_value=0)

model = KNeighborsRegressor(n_neighbors=5)
model.fit(X,y)

y_pred = model.predict(X_pred)
y_fin = y_pred.round().astype(int)
final = pd.DataFrame({'EmployeeID':eid, 'Predicted_PerformanceRating':y_fin})
print(final)