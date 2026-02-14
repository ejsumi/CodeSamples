# Student Course Selection Prediction (Random Forest)

## Background
A university wants to predict which elective course students will choose based on their major, GPA range, semester, and previous course completion.

## Dataset
- File: `student_course.csv`
- Rows: 201 (last row has missing target value)
- Columns:
  - `student_id`: Unique student identifier
  - `major`: Engineering, Business, Arts, Science
  - `gpa_range`: Low, Medium, High
  - `semester`: Fall, Spring, Summer
  - `completed_courses`: Few, Moderate, Many
  - `elective`: DataScience, WebDev, AI, CloudComputing, Cybersecurity, GameDev — **MISSING for last row**

## Task
- Load and explore the dataset
- Perform one-hot encoding on categorical variables
- Prepare the data:
  - Features (X): `major`, `gpa_range`, `semester`, `completed_courses`
  - Target (y): `elective`
- Split into training (80%) and testing (20%) sets from rows 1–200
- Train a **Random Forest Classifier** model (`n_estimators=75`, `max_depth=5`)
- Predict the elective for row 201 (the last row with missing target)

> Row 201 features: Engineering, High, Fall, Many

## Note
Row 201 has all features but the `elective` column is empty (NaN). This is the value you need to predict.

## Constraints
- Use `scikit-learn`'s `RandomForestClassifier`
- Use `pandas` for data manipulation
- Apply `pd.get_dummies` with `drop_first=True` for feature encoding
- Reindex prediction data to match training columns
