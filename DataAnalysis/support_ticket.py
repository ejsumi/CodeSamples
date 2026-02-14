import pandas as pd

df = pd.read_csv('support_tickets.csv')

dft = df.groupby('team_lead').agg(
    department = ('department', lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0]),
    team_size = ('support_agent', 'nunique'),
    total_tickets_resolved = ('ticket_id','count'),
    avg_resolution_time = ('resolution_time_hours','mean'),
    avg_customer_score = ('customer_satisfaction', 'mean'),
    count_critical_tickets = ('priority_level', lambda x:( x=='Critical').sum())
)
print(dft.head())
#print(df.tail())