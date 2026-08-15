import pandas as pd

# read data
df = pd.read_csv('sales_analysis.csv', dayfirst=True)

#  Total sales per manager (unsorted)
total_sales = df.groupby('sales_manager')['sale_amount'].sum()
print(total_sales)

#  Get sorted amounts (descending) as a plain array
sorted_amounts = total_sales.sort_values(ascending=False).values
print(sorted_amounts)

# Get managers in the order they FIRST appeared in the file
first_appearance_order = df['sales_manager'].drop_duplicates().tolist()
print(first_appearance_order)

#  Map sorted amounts to first-appearance order
result = pd.DataFrame({
    'sales_manager': first_appearance_order,
    'total_sales': sorted_amounts
})
# format as currencyresult['total_sales'] = result['total_sales'].apply(lambda x: f"${x:,.0f}")
print(result)