import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


df = pd.read_csv('house_prices.csv')
#print(df.info())


# WRONG: computes stats on full df including prediction rows (data leakage)
#df['bathrooms'] = df['bathrooms'].fillna(df['bathrooms'].mode()[0])
#df['distance_to_city_km'] = df['distance_to_city_km'].fillna(df['distance_to_city_km'].median())

# CORRECT: compute imputation values on training rows only, then apply to full df
train_mask = df['price_lakhs'].notna()
print("train_mask", train_mask.shape)
bath_mode = df.loc[train_mask, 'bathrooms'].mode()[0]
dist_median = df.loc[train_mask, 'distance_to_city_km'].median()
df['bathrooms'] = df['bathrooms'].fillna(bath_mode)
df['distance_to_city_km'] = df['distance_to_city_km'].fillna(dist_median)

df['age_years'] = df['age_years'].clip(upper=100)

#snippets for reference
#df['area_sqft'] = df['area_sqft'].clip(lower=150)
#df['area_sqft'] = df['area_sqft'].clip(lower=150, upper=5000) 

#conditions = [
#    (df['age_years'] >= 85) & (df['age_years'] <= 94),
#    df['age_years'] >= 95
#]
#choices = [90, 95]
#df['age_years'] = np.select(conditions, choices, default=df['age_years'])

df = pd.get_dummies(df,columns=['locality','furnishing'], drop_first=True )

# WRONG: hardcodes row count (iloc[:-2] / tail(2))
# X= df.iloc[:-2].drop(columns='price_lakhs')
# y = df['price_lakhs'].iloc[:-2]
# df_pred = df.tail(2).copy()

# CORRECT: derive split from which rows have price_lakhs missing
train_df = df[df['price_lakhs'].notna()]
pred_df  = df[df['price_lakhs'].isna()]

X = train_df.drop(columns='price_lakhs')
y = train_df['price_lakhs']
X_pred = pred_df.drop(columns='price_lakhs')

# Optional: 80/20 split for internal MAE check only
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# WRONG: trains on 80% split only instead of all training rows
# model = LinearRegression()
# model.fit(X_train, y_train)

# CORRECT: fit on all training rows for final prediction
model = LinearRegression()
model.fit(X, y)

# WRONG: prints raw numpy array without rounding
# print(y_pred)

# CORRECT: round to 2 decimal places and print as Python list
import numpy as np
y_pred = model.predict(X_pred)
print(list(np.round(y_pred, 2)))