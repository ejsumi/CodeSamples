# Question 3 — K-Nearest Neighbors: Customer Segment Classification
 
## Dataset
`customer_segments.csv` — 170 rows, 6 columns.
 
| Column | Type | Description |
|---|---|---|
| annual_income | numeric | Annual income — **contains missing values** |
| spending_score | numeric | Spending score (1–100) |
| age | numeric | Customer age — **contains one outlier** |
| membership_years | numeric | Years as a member |
| preferred_category | categorical | `Electronics`, `Fashion`, `Grocery` |
| customer_type | categorical (target) | `Bronze`, `Silver`, `Gold` — **missing for the last 3 rows** |
 
## Task
Train a K-Nearest Neighbors classifier to predict `customer_type` for the last 3 rows of the dataset, using the remaining 167 rows as training data.
 
## Required steps
 
1. **Load** `customer_segments.csv`. Split into training rows (`customer_type` not null) and prediction rows (last 3 rows, `customer_type` null).
2. **Handle missing values** (compute fill value on the training set only, apply to both):
   - `annual_income`: fill missing values with the **median** of the training set.
3. **Handle the outlier**:
   - `age` contains at least one unrealistic value. Cap (clip) all values in `age` at an upper bound of **90**.
4. **Encode categorical columns**:
   - One-hot encode `preferred_category` using `pandas.get_dummies(..., drop_first=True)`.
   - Apply encoding consistently so training and prediction sets end up with identical columns.
5. **Scale features**:
   - KNN is distance-based, so scaling is required. Fit `sklearn.preprocessing.StandardScaler()` on the training features only, then transform both training and prediction features using that same fitted scaler.
   - Do **not** scale the target column.
6. **Train the model**:
   - Use `sklearn.neighbors.KNeighborsClassifier(n_neighbors=5)` with all other parameters at default.
7. **Predict**:
   - Predict `customer_type` for the last 3 rows.
8. **Output**:
   - Print the predictions as a Python list of strings, e.g. `['Gold', 'Bronze', 'Bronze']`, in the same row order as they appear in the file.
## Optional metric
If asked, also report **accuracy** on an internal 80/20 split of the training data, rounded to 3 decimal places.
 
## Notes
- The order of operations matters: impute missing values and cap the outlier **before** scaling, and fit the scaler only on training data to avoid leakage.
- Your code will be re-run on larger hidden datasets with the same structure; derive the train/predict split dynamically from missing values in `customer_type`, not row counts.
 