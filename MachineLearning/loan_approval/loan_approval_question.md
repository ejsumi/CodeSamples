# Loan Approval Prediction (Random Forest Classifier)

## Background
A bank wants to predict whether a loan application will be **approved** based on
applicant demographics, income, and loan details. The **last 2 rows** of the
dataset are reserved for prediction (their `Loan_Approved` value is missing).

## Dataset
- File: `loan_approval_data.csv`
- Rows: 200 (last 2 rows have a blank `Loan_Approved` value)
- Columns:
  - `Age`: Applicant's age (years)
  - `Gender`: `Male` / `Female`
  - `Married`: Marital status (`Yes` / `No`)
  - `Education`: `Graduate` / `Not Graduate`
  - `Self_Employed`: `Yes` / `No` — **contains missing values**
  - `ApplicantIncome`: Applicant's monthly income
  - `CoapplicantIncome`: Co-applicant's monthly income
  - `LoanAmount`: Requested loan amount (in thousands)
  - `Loan_Amount_Term`: Loan repayment term (in months)
  - `Credit_History`: Whether applicant has a valid credit history (`1` / `0`)
  - `Property_Area`: `Urban` / `Semiurban` / `Rural`
  - `Loan_Approved`: Target — whether the loan was approved (`Y` / `N`). Blank
    for the last 2 rows.

## Task
- Load and explore the dataset
- Handle missing values in `Self_Employed` using the **mode** of the column
  (most frequent category)
- Encode categorical columns (`Gender`, `Married`, `Education`, `Self_Employed`,
  `Property_Area`) using `LabelEncoder`
- Scale numerical columns (`ApplicantIncome`, `CoapplicantIncome`, `LoanAmount`,
  `Loan_Amount_Term`) using `StandardScaler`
- Reserve the last 2 rows (with missing `Loan_Approved`) for prediction; train on
  the rest
- Split the training data with **`test_size=0.2`**, `random_state=42`
- Train a **Random Forest Classifier** (`n_estimators=150`, `max_depth=10`,
  `random_state=42`)
- Evaluate using **accuracy score**
- Predict `Loan_Approved` for the last 2 rows and print the results

## Expected Deliverables
- Printed test-set accuracy score — no other metrics required
- Predicted `Loan_Approved` label (`Y` or `N`) for each of the last 2 rows

## Things to Watch Out For
- Fill missing values in `Self_Employed` using the mode computed **only from the
  training portion of the data** (i.e., excluding the last 2 rows, since those
  represent unseen prediction rows) to avoid leaking information.
- `LabelEncoder` should be **fit on the full set of known categories** before
  splitting off the last 2 rows, so the same encoding applies consistently to
  both training data and the rows you're predicting for.
- `Credit_History` is already numeric (`1`/`0`) — do not label-encode it, and
  note it is intentionally left out of the scaling list since it's a binary
  flag, not a continuous quantity.
- Since `Loan_Approved` is categorical (`Y`/`N`), this is a **classification**
  task — a Random Forest Classifier is the correct model, not a Regressor.
- Make sure the last 2 rows are excluded from `train_test_split` entirely (they
  have no valid target), not merely ignored during evaluation.
