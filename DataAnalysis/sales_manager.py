import pandas as pd
import numpy as np

#read data
df = pd.read_csv('sales_analysis.csv')

dfmgr = df.groupby('sales_manager',as_index=False).agg(
    region=('region','first'),
    team_size=('salesperson_name','nunique'),
    total_transactions=('sale_amount','count'),
    total_revenue=('sale_amount','sum'),
    average_deal_size=('sale_amount', 'mean')
)

dftsales = df.groupby(['sales_manager','salesperson_name'],as_index=False).agg(
    top_performer_sales = ('sale_amount','sum')
)

dftper = dftsales.sort_values(
    ['sales_manager','top_performer_sales'], ascending=[True, False]).groupby('sales_manager').first()

final = dfmgr.merge(dftper,on='sales_manager',how='left').rename(columns={'salesperson_name':'top_performer'})

#print(dfmgr.info())
print(dftsales)
#print(dftper.info())
print(dfmgr)
print(final)