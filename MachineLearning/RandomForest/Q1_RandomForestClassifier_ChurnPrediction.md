# Coding Question 1 — Customer Churn Prediction (Classification)

## Scenario
A telecom company wants to predict whether a customer will **churn** (leave the
service). You are given historical customer data in `churn_train.csv`.

**The last 2 rows of the CSV have a blank/`NaN` value in the `churn`
column — these are the rows you must predict.** All other rows have a known
`churn` label and should be used to train your model.

Your code will also be run against hidden datasets with the same schema
(same columns, same idea of blank target rows at the end, possibly a
different number of blank rows) — so **do not hardcode row counts, indices,
or the number "2"**. Always detect the rows to predict by checking which
rows have a missing target value, not by position.

## Dataset Columns
| Column | Type | Description |
|---|---|---|
| age | int | Customer age |
| tenure_months | int | Months the customer has stayed |
| monthly_charges | float | Monthly bill amount (**contains missing values and outliers**) |
| total_charges | float | Total amount billed till date (**contains missing values**) |
| num_support_calls | int | Number of support calls made |
| contract_type | categorical | `Month-to-Month`, `One-Year`, `Two-Year` |
| churn | int (target) | 0 = stayed, 1 = churned |

## Preprocessing Requirements (must follow exactly — auto-graded)
1. **Missing values**: Impute missing values in `monthly_charges` and
   `total_charges` using the **median** of each respective column.
2. **Outliers**: Treat outliers in `monthly_charges` using the **IQR method**:
   - `Q1` = 25th percentile, `Q3` = 75th percentile, `IQR = Q3 - Q1`
   - Lower bound = `Q1 - 1.5 * IQR`, Upper bound = `Q3 + 1.5 * IQR`
   - **Clip** (cap) values outside these bounds to the bound value (do not drop rows).
3. **Encoding**: **Label encode** `contract_type` (map each category to an
   integer). Fit the mapping on `train_df` only, then apply the same mapping
   to `test_df`. 

   ```python
   def encode_column(train_df, test_df, col):
       categories = train_df[col].unique()
       mapping = {cat: i for i, cat in enumerate(categories)}
       train_df[col] = train_df[col].map(mapping)
       # unseen category in test set -> -1 instead of crashing
       test_df[col] = test_df[col].map(mapping).fillna(-1).astype(int)
       return train_df, test_df
   ```



## Model Requirements
Train a **`sklearn.ensemble.RandomForestClassifier`** with these exact
hyperparameters (grading checks predictions, so parameters must match):

```python
RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)
```


## Provided File
- `churn_train.csv` (182 rows total: 180 labeled rows + **2 rows at the end
  with `churn` left blank**, to be predicted) — use this to build and
  sanity-check your pipeline locally before submitting.
