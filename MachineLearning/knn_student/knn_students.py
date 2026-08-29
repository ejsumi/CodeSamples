import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Load and explore the dataset
df = pd.read_csv('knn_student1.csv')
print(df.head())
print(df.info())

# Separate known rows from the row to predict, then drop student_id
train_mask = df['location'].notna()
X = df.loc[train_mask].drop(columns=['student_id','location'])
y = df.loc[train_mask, 'location']
X_target = df.loc[~train_mask].drop(columns=['student_id','location'])

# One-hot encode features (drop_first=True) and target
X_en = pd.get_dummies(X, drop_first=True)
y_en = pd.get_dummies(y)

# Split into 80% train and 20% test sets
X_train, X_test, y_train, y_test = train_test_split(X_en, y_en, test_size=0.20)

# Train and evaluate KNN for k=3, 5, 7 and print accuracy for each
k_values = [3,5,7]
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    accuracy = knn.score(X_test, y_test)
    print(f"Accuracy for k={k} is {accuracy:.2f}")

#knn model
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)

# Encode and align the missing-target row to match training data
dfp_en = pd.get_dummies(X_target,drop_first=True)
dfp_en = dfp_en.reindex(columns=X_en.columns,fill_value=0)

# Predict and extract location with highest score
y_pred = knn.predict(dfp_en)
pred = y_en.columns[y_pred.argmax()]
print("Predicted Location : ",pred )
