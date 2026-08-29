import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('employee_dataset.csv')

employee_ids = df.tail(3)['EmployeeID'].copy()

# drop columns
df = df.drop(columns=['EmployeeID','PerformanceRating','Attrition'])

#missing values update
df_train = df.iloc[:-3]
df['Age'] = df['Age'].fillna(df_train['Age'].mean())
df['DistanceFromHome_km'] = df['DistanceFromHome_km'].fillna(df_train['DistanceFromHome_km'].median())

# cap outliers
df['MonthlyWorkingHours'] = df['MonthlyWorkingHours'].clip(upper=250)

#encoding categorical columns
df = pd.get_dummies(df, columns = ['Department'], drop_first=True)

df['Education'] = df['Education'].map({"High School": 0, "Bachelors": 1, "Masters": 2, "PhD": 3})
#print(df.info()) 

df_train = df.iloc[:-3]
df_pred = df.tail(3).copy()

X = df_train.drop(columns=['Salary'])
y = df_train['Salary']

model = LinearRegression()
model.fit(X,y)

X_pred = df_pred.drop(columns=['Salary'])

y_final = model.predict(X_pred)

y_pred = model.predict(X)

#final_result = pd.DataFrame({
#	'EmployeeID': employee_ids,
#	'PredictedSalary': y_final.round(2)
#})

final_result = [
    f"[{int(employee_id)}: {int(round(predicted_salary))}]"
    for employee_id, predicted_salary in zip(employee_ids.values, y_final)
]



print("[" +",".join(final_result) + "]")
print("R2_score: ",round(r2_score(y, y_pred),2))