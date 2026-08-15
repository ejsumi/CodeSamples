import pandas as pd
import numpy as np

#read data
df = pd.read_csv('electronics_sales.csv')

# drop identifier columns and invalid quantity rows
df = df.drop(columns=['InvoiceID','CustomerID'])
df = df[df['Quantity']>0]

# derive net price and computed total per sale
df['NetUnitPrice'] = df['UnitPrice'] - (1-(df['DiscountPercent']/100))
df['ComputedTotal'] = df['Quantity']*df['NetUnitPrice']

# derive value band from computed total
conditions = [(df['ComputedTotal']>=1500.00),(df['ComputedTotal'].between(500,1500)),(df['ComputedTotal']<500.00)]
values = ['High Value','Medium Value','Low Value']
df['ValueBand'] = np.select(conditions, values, default='Unknown')

# derive quarter and year from sale date
df['date'] = pd.to_datetime(df['SaleDate'])
df['Quarter'] = 'Q' + df['date'].dt.quarter.astype(str)
df['Year'] = df['date'].dt.year

# filter to 2023 and target regions
df = df.drop(columns=['date','SaleDate'])
df = df[df['Year'] ==2023]
df = df[df['Region'].isin(['South','West', 'North'])]

# aggregate by quarter and product category
df = df.groupby(['Quarter','ProductCategory']).agg(
    TotalQuantity = ('Quantity','sum'),
    TotalSales = ('ComputedTotal','sum'),
    NumTransactions = ('Quarter','count'),
    HighValueTran =('ValueBand',lambda x :(x == 'High Value').sum())
)
# sort by quarter then total sales descending
df = df.sort_values(by=['Quarter','TotalSales'],ascending=[False,False])

print(df)