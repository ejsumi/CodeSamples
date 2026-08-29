import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv('house_price_train.csv')

train = df.iloc[:-2]

df['area_sqft'] = df['area_sqft'].fillna(train['area_sqft'].median())
df['distance_to_city_km'] = df['distance_to_city_km'].fillna(train['distance_to_city_km'].median())

Q1 = df['area_sqft'].quantile(.25)
Q3 = df['area_sqft'].quantile(.75)

IQR = Q3-Q1
df['area_sqft'] = df['area_sqft'].clip(lower=Q1-1.5*IQR, upper=Q3+1.5*IQR)

df = pd.get_dummies(df, columns=['location_type'], drop_first=True)

df_train = df.iloc[:-2].copy()
df_pred = df.tail(2).copy()

X = df_train.drop(columns=['price'])
y = df_train['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=150, max_depth=8, random_state=42)
model.fit(X_train, y_train)

X_pred= df_pred.drop(columns=['price'])
X_pred = X_pred.reindex(columns=X.columns, fill_value=0)

y_pred = model.predict(X_pred)
print(y_pred.round(2))


