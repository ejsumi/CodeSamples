import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Load and explore the dataset
df = pd.read_csv('knn_student1.csv')
print(df.head())
print(df.info())

# Separate features and target, drop student_id
X = df.drop(columns=['student_id','location'])
y = df['location']

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

# Build prediction row for: Senior, Evening, Small_Group, Project
dfp = pd.DataFrame({'year_of_study':['Senior'],
                     'study_time': ['Evening'],
                     'group_size':['Small_Group'],
                     'study_purpose':['Project']})

# Encode and align prediction row columns to match training data
dfp_en = pd.get_dummies(dfp,drop_first=True)
dfp_en = dfp_en.reindex(columns=X_en.columns,fill_value=0)

# Predict and extract location with highest score
y_pred = knn.predict(dfp_en)
pred = y_en.columns[y_pred.argmax()]
print("Predicted Location : ",pred )
