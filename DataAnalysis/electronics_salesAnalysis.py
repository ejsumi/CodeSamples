import pandas as pd
import numpy as np

#read data
df = pd.read_csv('electronics_sales.csv')

df = df.drop(columns=['InvoiceID','CustomerID'])
df = df[df['Quantity']>0]

df['NetUnitPrice'] = df['UnitPrice'] - (1-(df['DiscountPercent']/100))
df['ComputedTotal'] = df['Quantity']*df['NetUnitPrice']

conditions = [(df['ComputedTotal']>=1500.00),(df['ComputedTotal'].between(500,1500)),(df['ComputedTotal']<500.00)]
values = ['High Value','Medium Value','Low Value']
df['ValueBand'] = np.select(conditions, values, default='Unknown')

df['date'] = pd.to_datetime(df['SaleDate'])
df['Quarter'] = 'Q' + df['date'].dt.quarter.astype(str)
df['Year'] = df['date'].dt.year

df = df.drop(columns=['date','SaleDate'])
df = df[df['Year'] ==2023]
df = df[df['Region'].isin(['South','West', 'North'])]

df = df.groupby(['Quarter','ProductCategory']).agg(
    TotalQuantity = ('Quantity','sum'),
    TotalSales = ('ComputedTotal','sum'),
    NumTransactions = ('Quarter','count'),
    HighValueTran =('ValueBand',lambda x :(x == 'High Value').sum())
)
df = df.sort_values(by=['Quarter','TotalSales'],ascending=[False,False])
print(df)
#print(df.describe())