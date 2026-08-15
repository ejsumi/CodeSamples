import pandas as pd
import numpy as np

#read data
df = pd.read_csv('sales_analysis.csv')

# aggregate team-level metrics per manager
dfmgr = df.groupby('sales_manager',as_index=False, sort=False).agg(
    region=('region','first'),
    team_size=('salesperson_name','nunique'),
    total_transactions=('sale_amount','count'),
    total_revenue=('sale_amount','sum'),
    average_deal_size=('sale_amount', 'mean')
)

# aggregate individual totals per manager/salesperson pair
dftsales = df.groupby(['sales_manager','salesperson_name'],as_index=False).agg(
    top_performer_sales = ('sale_amount','sum')
)

# rank individuals within each manager and keep the top performer
dftper = dftsales.sort_values(
    ['sales_manager','top_performer_sales'], ascending=[True, False]).groupby('sales_manager').first()

# merge team summary with top performer
final = dfmgr.merge(dftper,on='sales_manager',how='left').rename(columns={'salesperson_name':'top_performer'})
# sort by total revenue descending
final = final.sort_values('total_revenue', ascending=False).reset_index(drop=True)

#print(dfmgr.info())
#print(dftsales)
#print(dftper.info())
#print(dfmgr)
print(final)