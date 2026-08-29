import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


df = pd.read_csv('employee_dataset.csv')

eid = df.tail(3)['EmployeeID'].copy()
df = df.drop(columns=['EmployeeID','Salary','PerformanceRating'])
df_train = df.iloc[:-3]

df['Age']= df['Age'].fillna(df_train['Age'].mean())
df['DistanceFromHome_km'] = df['DistanceFromHome_km'].fillna(df_train['DistanceFromHome_km'].mean())

df['MonthlyWorkingHours'] = df['MonthlyWorkingHours'].clip(upper=250)

df = pd.get_dummies(df, columns=['Department'], drop_first=True)
df['Education'] = df['Education'].map({"High School": 0, "Bachelors": 1, "Masters": 2, "PhD": 3})
df['Attrition'] = df['Attrition'].map({"Yes":1, "No":0})

df_train = df.iloc[:-3]
df_pred = df.tail(3).copy()

X = df_train.drop(columns = ['Attrition'])
y = df_train['Attrition']
X_pred = df_pred.drop(columns = ['Attrition'])


model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X, y)

y_pred = model.predict(X_pred)
#print(df.info())
final_result = [f"[{int(eid)}: {'Yes' if attrition==1 else 'No'}]" for eid, attrition in zip(eid.values, y_pred)]

print("[" + "," .join(final_result)+ "]")


