# Question
A university library wants to predict where students will choose to study based on their year of study, preferred study time, group size, and study purpose. You have 200 students' study location preferences to build your prediction model.

## Dataset
- File: study_location.csv
- Rows: 200
**Columns:**
- student_id: Unique student identifier
- year_of_study: Freshman, Sophomore, Junior, Senior
- study_time: Morning, Afternoon, Evening, Late_Night
- group_size: Solo, Pair, Small_Group, Large_Group
- study_purpose: Exam_Prep, Assignment, Reading, Project
- location: Library, Cafe, Dorm, Study_Hall, Outdoor

## Task
- Load and explore the dataset
- Perform one-hot encoding on categorical variables
- Prepare the data:
    - Features (X): year_of_study, study_time, group_size, study_purpose
    - Target (y): location
- Split into training (80%) and testing (20%) sets
- Train a KNN Classifier model (try k=3, 5, 7)
- Evaluate model accuracy for different k values
- Predict location for last row
 

## Constraints
- Use scikit-learn's KNeighborsClassifier
- Use pandas for data manipulation
- Apply proper one-hot encoding techniques
- Use drop_first=True for feature encoding