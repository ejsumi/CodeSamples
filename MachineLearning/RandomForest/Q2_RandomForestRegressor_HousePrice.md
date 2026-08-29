# Coding Question 2 — House Price Prediction (Regression)

## Scenario
A real-estate firm wants to estimate house **price** from property features.
You are given `house_price_train.csv`.

**The last 2 rows of the CSV have a blank/`NaN` value in the `price`
column — these are the rows you must predict.** All other rows have a known
`price` and should be used to train your model.



## Dataset Columns
| Column | Type | Description |
|---|---|---|
| area_sqft | float | Built-up area in sq. ft (**contains missing values and outliers**) |
| bedrooms | int | Number of bedrooms |
| bathrooms | int | Number of bathrooms |
| age_years | int | Age of the property in years |
| distance_to_city_km | float | Distance from city center (**contains missing values**) |
| location_type | categorical | `Urban`, `Suburban`, `Rural` |
| price | float (target) | Sale price |

## Preprocessing Requirements (must follow exactly — auto-graded)
1. **Missing values**: Impute missing values in `area_sqft` and
   `distance_to_city_km` using the **median** of each respective column
   (computed on the training data).
2. **Outliers**: Apply the **IQR method** to `area_sqft` on the *feature*
   side:
   - `Q1` = 25th percentile, `Q3` = 75th percentile, `IQR = Q3 - Q1`
   - Lower bound = `Q1 - 1.5 * IQR`, Upper bound = `Q3 + 1.5 * IQR`
   - **Clip** values outside these bounds (do not drop rows).
   - Note: `price` itself may also contain extreme outliers in the training
     data — you may clip them the same way when *training*, but never clip
     or alter the target in the test set (you don't have it).
3. **Encoding**: One-hot encode `location_type` using
   `pd.get_dummies(..., drop_first=True)`.
4. Do **not** scale/standardize features.

## Model Requirements
Train a **`sklearn.ensemble.RandomForestRegressor`** with these exact
hyperparameters:

```python
RandomForestRegressor(
    n_estimators=150,
    max_depth=8,
    random_state=42
)
```

- Use `train_test_split(X, y, test_size=0.2, random_state=42)` only for your
  own local validation.

## Function Signature (what the grader calls)
Write your solution as a single function that takes the **full dataframe**
(training rows + the blank-target rows to predict, all together, exactly as
read from the CSV):

```python
def predict_price(df: pd.DataFrame):
    """
    df: the FULL dataframe as read from CSV — includes both labeled rows
        (price is a number) and one or more rows where price is NaN.
    returns: a 1-D array / list / pd.Series containing ONLY the predicted
             prices for the rows where price was NaN, in the same order
             they appear in df.
    """
    # 1. split df into train_df (price.notna()) and predict_df (price.isna())
    # 2. compute median/IQR bounds on train_df ONLY, apply the same fitted
    #    values to transform predict_df (never touch/clip price in predict_df —
    #    it's NaN and isn't used for training)
    # 3. one-hot encode location_type on both; reindex predict_df's dummy
    #    columns to match train_df's columns (fill missing dummy cols with 0)
    # 4. fit RandomForestRegressor as specified above on train_df
    # 5. return predictions for predict_df only
    ...
```

Usage the grader will follow:
```python
df = pd.read_csv("hidden_dataset.csv")
predictions = predict_price(df)
# predictions should have one value per row where price was NaN
```

> ⚠️ Common exam trap: forgetting to `reindex` the test set's one-hot
> columns to match the train set's columns (e.g. if a `location_type` value
> is missing in the test split) will cause a shape mismatch at predict time.

## Evaluation
The grader will call `predict_price` on hidden datasets (same structure:
labeled rows + blank-target rows at the end) and score your predictions for
the blank rows using **RMSE** (or R²) against the true prices it holds back.
Exact threshold not disclosed.

## Provided File
- `house_price_train.csv` (202 rows total: 200 labeled rows + **2 rows at
  the end with `price` left blank**, to be predicted) — use this to build
  and sanity-check your pipeline locally before submitting.
