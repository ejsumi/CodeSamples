# Student Study Location Prediction (KNN Classifier)

## Background
A university library wants to predict where students will choose to study based on their year of study, preferred study time, group size, and study purpose. You have 200 students' study location preferences to build your prediction model.

## Dataset
- File: `knn_student1.csv`
- Rows: 200
- Columns:
  - `student_id`: Unique student identifier
  - `year_of_study`: Freshman, Sophomore, Junior, Senior
  - `study_time`: Morning, Afternoon, Evening, Late_Night
  - `group_size`: Solo, Pair, Small_Group, Large_Group
  - `study_purpose`: Exam_Prep, Assignment, Reading, Project
  - `location`: Library, Cafe, Dorm, Study_Hall, Outdoor — target variable

## Task
- Load and explore the dataset
- Perform one-hot encoding on categorical variables
- Prepare the data:
  - Features (X): `year_of_study`, `study_time`, `group_size`, `study_purpose`
  - Target (y): `location`
- Split into training (65%) and testing (35%) sets
- Train a **KNN Classifier** model (try k = 3, 5, 7, 9, 11)
- Evaluate model accuracy for different k values
- Predict location for: **Senior, Evening, Small_Group, Project**

## Constraints
- Use `scikit-learn`'s `KNeighborsClassifier`
- Use `pandas` for data manipulation
- Apply `pd.get_dummies` with `drop_first=True` for feature encoding
- Reindex prediction data to match training columns
