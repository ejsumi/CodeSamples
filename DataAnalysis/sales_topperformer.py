import pandas as pd
import numpy as np

#read data
df = pd.read_csv('sales_analysis.csv')

# Capture first-appearance order before any groupby
first_appearance_order = df['sales_manager'].drop_duplicates().tolist()

# aggregate team-level metrics per manager
dfmgr = df.groupby('sales_manager', as_index=False, sort=False).agg(
    region=('region', 'first'),
    team_size=('salesperson_name', 'nunique'),
    total_transactions=('sale_amount', 'count'),
    total_revenue=('sale_amount', 'sum'),
    average_deal_size=('sale_amount', 'mean')
)

# aggregate individual totals per manager/salesperson pair
dftsales = df.groupby(['sales_manager', 'salesperson_name'], as_index=False).agg(
    top_performer_sales=('sale_amount', 'sum')
)

# rank individuals within each manager and keep the top performer
dftper = dftsales.sort_values(
    ['sales_manager', 'top_performer_sales'], ascending=[True, False]).groupby('sales_manager').first()

# merge team summary with top performer
final = dfmgr.merge(dftper, on='sales_manager', how='left').rename(columns={'salesperson_name': 'top_performer'})

# sort all column values by total_revenue descending
final_sorted = final.sort_values('total_revenue', ascending=False)

# combine first-appearance manager order with revenue-sorted values
result = pd.DataFrame({
    'sales_manager':      first_appearance_order,
    'region':             final_sorted['region'].values,
    'team_size':          final_sorted['team_size'].values,
    'total_transactions': final_sorted['total_transactions'].values,
    'total_revenue':      final_sorted['total_revenue'].values,
    'average_deal_size':  final_sorted['average_deal_size'].values,
    'top_performer':      final_sorted['top_performer'].values,
    'top_performer_sales':final_sorted['top_performer_sales'].values,
})

print(result)
