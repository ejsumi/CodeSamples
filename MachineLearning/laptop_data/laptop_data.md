# Laptop Price Prediction (Random Forest Regressor)

## Background
A laptop retailer wants to predict the price of laptops based on hardware specifications and software configuration. The last 5 rows of the dataset are reserved for prediction.

## Dataset
- File: `laptop_data.csv`
- Columns:
  - `Brand`: Laptop manufacturer
  - `Processor`: CPU type (e.g., Intel i9, Apple M1)
  - `RAM_GB`: RAM in gigabytes
  - `Storage_GB`: Storage capacity in GB
  - `Screen_Size`: Display size in inches
  - `Graphics_Card`: GPU model
  - `Weight_kg`: Laptop weight in kg
  - `Operating_System`: OS installed (e.g., Windows 10, macOS)
  - `Price`: Laptop price — target variable

## Task
- Load and explore the dataset
- Handle missing values (mode for categorical, median for numerical)
- Detect and filter outliers in `RAM_GB` using IQR method
- Encode categorical columns (`Brand`, `Processor`, `Operating_System`, `Graphics_Card`) using `LabelEncoder`
- Scale numerical columns (`RAM_GB`, `Storage_GB`, `Screen_Size`, `Weight_kg`, `Operating_System`) using `StandardScaler`
- Reserve the last 5 rows for prediction; train on the rest
- Split training data with 25% test
- Train a **Random Forest Regressor** (`n_estimators=175`, `max_depth=12`)
- Evaluate using R² score
- Predict prices for the last 5 laptops


