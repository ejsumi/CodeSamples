# Regression Practice — 3 Questions (Single Dataset)

**Dataset file:** `employee_dataset.csv`
**Rows:** 180 (EmployeeID 1001–1180)

**Columns**

| Column | Type | Notes |
|---|---|---|
| EmployeeID | int | identifier only — never use as a feature |
| Age | float | has missing values |
| Department | categorical | Sales / IT / HR / Finance / Marketing |
| Education | categorical | High School / Bachelors / Masters / PhD |
| YearsAtCompany | float | |
| DistanceFromHome_km | float | has missing values |
| MonthlyWorkingHours | float | has outliers |
| PerformanceRating | float | 1–5 scale, has missing values |
| Salary | float | has outliers |
| Attrition | categorical | Yes / No |

**Important — the last 3 rows (EmployeeID 1178, 1179, 1180)** have `Salary`, `Attrition`, and `PerformanceRating` left blank on purpose. These 3 rows are your **prediction set**. Every question below uses all other rows (EmployeeID 1001–1177) as the **training set** — do **not** use `train_test_split`, and do **not** shuffle the data. This keeps everyone's answer identical.

---

## Question 1 — Linear Regression: Predict Salary

Build a **Linear Regression** model (`sklearn.linear_model.LinearRegression`, default parameters) to predict `Salary`.

**Features to use (in this order):** `Age`, `Department`, `Education`, `YearsAtCompany`, `DistanceFromHome_km`, `MonthlyWorkingHours`

**Steps to follow exactly:**
1. Drop `EmployeeID`, `PerformanceRating`, and `Attrition` — do not use them.
2. **Missing values:**
   - `Age`: fill missing values with the **mean** of the `Age` column (computed on the training rows, i.e., EmployeeID 1001–1177).
   - `DistanceFromHome_km`: fill missing values with the **median** of the `DistanceFromHome_km` column (computed on the training rows).
3. **Outlier handling:** In `MonthlyWorkingHours`, any value **greater than 250** is an outlier. Cap all such values to exactly **250** (do not remove the rows).
4. **Encoding:**
   - `Department`: one-hot encode using `pd.get_dummies(df['Department'], drop_first=True)`.
   - `Education`: ordinal-encode using this exact mapping: `{"High School": 0, "Bachelors": 1, "Masters": 2, "PhD": 3}`.
5. Train the model on EmployeeID 1001–1177 (rows where `Salary` is not null).
6. Predict `Salary` for EmployeeID **1178, 1179, 1180**.
7. Also report the **R² score** computed on the training data itself (round to 2 decimal places).

**Output format:** Print the 3 predictions as a **table** with two columns — `EmployeeID` and `Predicted_Salary` (rounded to the nearest integer). Print the R² score as a single separate line: `Training R2: <value>`.

---

## Question 2 — Logistic Regression: Predict Attrition

Build a **Logistic Regression** model (`sklearn.linear_model.LogisticRegression(max_iter=1000, random_state=42)`) to predict `Attrition` (Yes/No).

**Features to use (in this order):** `Age`, `Department`, `Education`, `YearsAtCompany`, `DistanceFromHome_km`, `MonthlyWorkingHours`

**Steps to follow exactly:**
1. Drop `EmployeeID`, `Salary`, and `PerformanceRating` — do not use them. (`Salary` is left blank for the same 3 prediction rows in Question 1, so it cannot be used as a feature here.)
2. **Missing values:**
   - `Age`: fill missing values with the **mean** of the `Age` column (training rows only).
   - `DistanceFromHome_km`: fill missing values with the **mean** of the `DistanceFromHome_km` column (training rows only).
3. **Outlier handling:** In `MonthlyWorkingHours`, any value **greater than 250** is an outlier. Cap all such values to exactly **250** (do not remove the rows).
4. **Encoding:**
   - `Department`: one-hot encode using `pd.get_dummies(df['Department'], drop_first=True)`.
   - `Education`: ordinal-encode using this exact mapping: `{"High School": 0, "Bachelors": 1, "Masters": 2, "PhD": 3}`.
   - Target `Attrition`: encode `"Yes"` → `1`, `"No"` → `0`.
5. Train the model on EmployeeID 1001–1177 (rows where `Attrition` is not null).
6. Predict `Attrition` for EmployeeID **1178, 1179, 1180**.
7. Also report the **Accuracy** computed on the training data itself (round to 2 decimal places).

**Output format:** Print the 3 predictions as a **list** of the form `[EmployeeID: Attrition]`, e.g. `[1178: Yes, 1179: No, 1180: Yes]`, using the original `Yes`/`No` labels (not 1/0). Print the accuracy as a single separate line: `Training Accuracy: <value>`.

---

## Question 3 — K-Nearest Neighbors Regressor: Predict PerformanceRating

Build a **KNN Regressor** (`sklearn.neighbors.KNeighborsRegressor(n_neighbors=5)`) to predict `PerformanceRating`.

**Features to use (in this order):** `Age`, `Department`, `YearsAtCompany`, `DistanceFromHome_km`, `MonthlyWorkingHours`

**Steps to follow exactly:**
1. Drop `EmployeeID`, `Education`, and `Salary` — do not use them. (`Salary` is left blank for the same 3 prediction rows in Question 1, so it cannot be used as a feature here.)
2. Start from EmployeeID 1001–1177 only (the last 3 rows are the prediction set and must not be part of the training pool). Within this training pool, some rows also have `PerformanceRating` missing (this is separate from the 3 held-out rows) — **drop those rows entirely** before training (do not fill the target column).
3. **Missing values (on the remaining training rows, and on the 3 prediction rows):**
   - `Age`: fill missing values with the **mean** of the `Age` column (computed on the training rows only, after the drop in step 2).
   - `DistanceFromHome_km`: fill missing values with the **median** of the `DistanceFromHome_km` column (computed on the training rows only, after the drop in step 2).
4. **Outlier handling:** In `MonthlyWorkingHours`, any value **greater than 250** is an outlier. Cap all such values to exactly **250**.
5. **Encoding:** `Department` — one-hot encode using `pd.get_dummies(df['Department'], drop_first=True)`.
6. **Feature scaling:** Scale all numeric features using `sklearn.preprocessing.StandardScaler` — fit the scaler on the training rows only, then transform both training and prediction rows with it.
7. Train the model on the cleaned training rows from step 2–3.
8. Predict `PerformanceRating` for EmployeeID **1178, 1179, 1180**, and round each prediction to the **nearest whole number** (since ratings are on a 1–5 integer scale).

**Output format:** Print the 3 predictions as a **table** with two columns — `EmployeeID` and `Predicted_PerformanceRating`. No metric is required for this question.

---

### General notes for all 3 questions
- Do not use `train_test_split` or any random splitting — train on all rows with a non-null target, predict on the 3 specified rows.
- Do not generate any plots or charts.
- Follow the missing-value and outlier instructions exactly as written for that question (they differ slightly between questions).
- Round numeric outputs as instructed in each question so answers are directly comparable.
