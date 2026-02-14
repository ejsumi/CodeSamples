import pandas as pd
import numpy as np

df = pd.read_csv('campaign_executions.csv')

df1 = df.groupby('marketing_manager', as_index=False).agg(
    total_campaigns = ('campaign_id', 'count'),
    total_budget_spent = ('campaign_budget','sum'),
    total_revenue_generated = ('revenue_generated','sum'),
    total_impressions = ('impressions','sum'),
    total_clicks = ('clicks','sum'),
    total_conversions = ('conversions','sum')
)

df1['roi_percentage'] = ((df1['total_revenue_generated'] - df1['total_budget_spent']) / df1['total_budget_spent'])*100

df1['roi_percentage'] = df1['roi_percentage'].apply(lambda x: f'{x:.1f}%')
df1['avg_click_through_rate'] = (df1['total_clicks'] / df1['total_impressions'] )*100
df1['avg_click_through_rate'] = df1['avg_click_through_rate'].apply(lambda x: f'{x:.1f}%')
df1['avg_conversion_rate'] = (df1['total_conversions'] / df1['total_clicks'])*100
df1['avg_conversion_rate'] = df1['avg_conversion_rate'].apply(lambda x: f'{x:.1f}%')
df1['cost_per_conversion'] = df1['total_budget_spent'] / df1['total_conversions']

df1 = df1[['marketing_manager', 'total_campaigns', 'total_budget_spent', 'roi_percentage', 'total_revenue_generated', 'total_impressions', 'total_clicks', 'total_conversions', 'avg_click_through_rate', 'avg_conversion_rate', 'cost_per_conversion']]

print(df1.info())
print(df1.head())