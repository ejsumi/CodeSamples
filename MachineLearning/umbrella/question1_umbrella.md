# Umbrella Purchase Prediction (Logistic Regression)

## Background
A retail store wants to predict whether a customer will buy an umbrella based on daily weather conditions. The historical rows have known outcomes; the final forecast row has a missing outcome to predict.

## Dataset
- File: `umbrella_data.csv`
- Rows: 151 (150 historical rows plus one forecast row with missing `bought_umbrella`)
- Columns:
  - `date`: Date in `DD-MM-YYYY` format — parse with `format='%d-%m-%Y'`
  - `temperature`: Recorded temperature (°C)
  - `humidity`: Recorded humidity (%)
  - `rained_today`: Whether it rained (`Yes` / `No`)
  - `bought_umbrella`: Whether an umbrella was bought (`Yes` / `No`) - target variable, missing for the forecast row

## Task
- Load and parse the CSV
- Encode `rained_today` (`Yes`/`No` → 1/0, or one-hot encode)
- Scale `temperature` and `humidity` using `StandardScaler` — fit on training data only
- Split with 20% test, `shuffle=False` (sequential daily data)
- Train a **Logistic Regression** model (`max_iter=1000`)
- Evaluate using accuracy score
- Predict `bought_umbrella` for the forecast row already present in the CSV and print the result:

| Feature | Value |
|---|---|
| `temperature` | 21.5 |
| `humidity` | 78.0 |
| `rained_today` | `Yes` |
