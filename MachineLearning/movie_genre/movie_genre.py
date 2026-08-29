import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv(r'movie_genre\movie_genre_data.csv')
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
df = df.sort_values('date').reset_index(drop=True)

# fix: last row's genre_watched is already NaN (the row to predict) - it must not be trained on
X_full = pd.get_dummies(df['day_of_week'], drop_first=True)
train_mask = df['genre_watched'].notna()
X = X_full[train_mask]
y = df.loc[train_mask, 'genre_watched']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# fix: the row needing a prediction is the existing NaN row itself, not a computed future date
X_target = X_full[~train_mask]
target_date = df.loc[~train_mask, 'date'].iloc[0]
print("Predicting for:", target_date.strftime('%d-%m-%Y'), "| Weekday:", df.loc[~train_mask, 'day_of_week'].iloc[0])

pred_genre = model.predict(X_target)
print("Predicted genre:", pred_genre[0])