import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('umbrella/umbrella_data.csv')

#print(df.head())
#print(df.info())

X_in = df.drop(columns=['date','bought_umbrella'])
y = df['bought_umbrella']

#print(X.head())

X_en = pd.get_dummies(X_in, columns=['rained_today'], drop_first=True)

# fix: derive the forecast row from the missing target, not a hardcoded iloc[-1]/iloc[:-1] split
train_mask = y.notna()
num_cols = ['temperature', 'humidity']
scaler = StandardScaler()
X_en.loc[train_mask, num_cols] = scaler.fit_transform(X_en.loc[train_mask, num_cols])
X_en.loc[~train_mask, num_cols] = scaler.transform(X_en.loc[~train_mask, num_cols])

X_tar = X_en[~train_mask]
X = X_en[train_mask]
y = y[train_mask]

#print(X.info())

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, shuffle=False)

model = LogisticRegression(max_iter = 1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy :", accuracy_score(y_test, y_pred) )

y_tar = model.predict(X_tar)

print("prediction:", y_tar[0])