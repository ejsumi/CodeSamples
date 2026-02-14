import pandas as pd

df = pd.read_csv('employee_data.csv')

#print(df.info())
#print(df.iloc[[5,10,15]])
print(df.iloc[0:5]['salary'])
print(df.iloc[12,[1,2]])
print(df[['employee_name','department']].iloc[12])