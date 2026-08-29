import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('customer_segments.csv')
#print(df_in.info())

# dataset split
#df_pred = df['customer_type'].isna()
df_train =df[df['customer_type'].notna()]

print(df.shape)


income_median = df_train['annual_income'].median()
df['annual_income'] = df['annual_income'].fillna(income_median)


df['age'] = df['age'].clip(upper=90)

df = pd.get_dummies(df, columns=['preferred_category'], drop_first=True)

df_pred = df[df['customer_type'].isna()].copy()
df_train = df[df['customer_type'].notna()].copy()

X = df_train.drop(columns=['customer_type'])
y = df_train['customer_type']
X_pred = df_pred.drop(columns=['customer_type'])

#X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
num_cols = ['annual_income','spending_score','age','membership_years']

scaler = StandardScaler()
X[num_cols] = scaler.fit_transform(X[num_cols])
X_pred[num_cols] = scaler.transform(X_pred[num_cols])

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X,y)

pred = model.predict(X_pred)

print(pred.tolist())