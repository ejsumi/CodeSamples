import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load and explore the dataset
df = pd.read_csv('student_course.csv')
print(df.head())

# Save last row (row 201) for prediction and drop student_id
lr = df.iloc[-1:].copy()
df = df.drop(columns=['student_id'])

# Extract prediction row features (no target) and training rows
test = df.iloc[-1:]
test = test.drop(columns=['elective'])
df = df.iloc[0:-1]

# Separate features and target from training data
X = df.drop(columns=['elective'])
y = df['elective']

# One-hot encode features and target; align prediction row to training columns
X_en = pd.get_dummies(X, drop_first=True)
y_en = pd.get_dummies(y)
test_en = pd.get_dummies(test, drop_first=True)
test_en = test_en.reindex(columns=X_en.columns,fill_value=0)

#print(X_en.info())
#print(test_en.info())

# Split into 80% train and 20% test sets
X_train, X_test, y_train, y_test = train_test_split(X_en, y_en, test_size=0.2, random_state=42)

# Train Random Forest Classifier
model = RandomForestClassifier(n_estimators = 75, max_depth= 5, random_state=42)
model.fit(X_train, y_train)

# Predict elective for row 201 and fill back into the saved row
pred = model.predict(test_en)
pred_course = y_en.columns[pred.argmax()]
lr.loc[lr.index[0], 'elective'] = pred_course
print(lr.iloc[0])
