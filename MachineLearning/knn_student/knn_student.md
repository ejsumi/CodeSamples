# Question
A university library wants to predict where a student will choose to study based on year of study, preferred study time, group size, and study purpose. The final row has an unknown study location to predict.

## Dataset
- File: `knn_student1.csv`
- Rows: 500 (the final `location` value is missing)
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
    - Features (X): year_of_study, study_time, group_size, study_purpose
    - Target (y): location
- Set aside the row with a missing `location`, then split the known rows into training (80%) and testing (20%) sets
- Train a KNN Classifier model (try k=3, 5, 7)
- Evaluate model accuracy for different k values
- Predict location for the row with the missing target
 

## Constraints
- Use scikit-learn's KNeighborsClassifier
- Use pandas for data manipulation
- Apply proper one-hot encoding techniques
- Use drop_first=True for feature encoding