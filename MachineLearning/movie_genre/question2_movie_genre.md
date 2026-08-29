# Question 2: Predict Next Day's Movie Genre (Logistic Regression)

## Problem Statement

A household has been logging which genre of movie they watched each day, along
with the date and day of the week. Using a **Logistic Regression classification
model**, predict the genre for the final logged day, whose genre is missing,
based on its day of the week.

## Dataset

File: `movie_genre_data.csv`
Rows: 150 (the final `genre_watched` value is missing)

| Column | Description |
|---|---|
| `date` | Date in `DD-MM-YYYY` format |
| `day_of_week` | Day name (`Monday` ... `Sunday`) |
| `genre_watched` | Genre watched that day (`Action`, `Comedy`, `Drama`, `Horror`) |

## Tasks

1. Load the CSV and parse `date` correctly using `format='%d-%m-%Y'`. Sort the
   data chronologically (it should already be sorted, but verify).
2. Set aside the row where `genre_watched` is missing. Train only on rows with a
   known genre, then predict the missing final row.
3. One-hot encode `day_of_week` as the input feature (use all 7 possible days as
   categories, even if one doesn't appear in a given split, to avoid
   train/test column mismatches).
4. Keep the target genre labels as strings; `LogisticRegression` accepts string
   class labels directly.
5. Split into train/test sets. Since this is sequential "predict the next day"
   data, use `shuffle=False` in `train_test_split`.
6. Train a **LogisticRegression** model with `max_iter=1000`.
7. Evaluate using **accuracy** or **precision** (`average='macro'` if using
   precision, since there are 4 classes).
8. Use the trained model to predict the genre for the row set aside in step 2 and
   print the predicted label.

## Expected Deliverables

- Printed test-set accuracy (or macro precision) score — no other metrics required
- Final predicted genre label for the last row (row 150)

## Things to Watch Out For

- This is a **multi-class** classification problem (4 genres), not binary — don't
  assume binary metrics defaults will work without specifying `average=`.
- Do not include the row with the missing target in `train_test_split` or
   `.fit()`; a classifier cannot train on `NaN` labels.
- One-hot encode the full `day_of_week` column before setting aside the prediction
   row so its features use exactly the same columns as the training rows.
