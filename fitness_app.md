# Fitness App Usage Analysis

You have a DataFrame `fitness_data` with these columns: `SessionID`, `SessionDate`, `UserID`, `WorkoutType`, `Duration`, `CaloriesBurned`, `HeartRate`, `SubscriptionPlan`, `AppVersion`

## Write Python (pandas) code to perform the following tasks:

1. **Remove columns**: Drop `SessionID`, `UserID`, `HeartRate`, and `AppVersion` from the dataset.

2. **Create new column**: Create a column `BurnRate` calculated as:
```
   BurnRate = CaloriesBurned / Duration
(Calories burned per minute)
```

3. Add conditional column: Create a column IntensityLevel based on BurnRate:
```
"High Intensity" if BurnRate >= 10
"Moderate Intensity" if 5 <= BurnRate < 10
"Low Intensity" if BurnRate < 5
```

4. Filter data: Keep only sessions where:
```
SessionDate is from the year 2024
Duration >= 10 (minimum 10 minutes)
SubscriptionPlan is "Premium" or "Pro"
```

5. Group and aggregate: Group by WorkoutType and calculate:
```
TotalSessions: Count of sessions
AvgDuration: Average of Duration
TotalCalories: Sum of CaloriesBurned
AvgBurnRate: Average of BurnRate
HighIntensityCount: Count of sessions with IntensityLevel == "High Intensity"
```

6. Sort: Sort by TotalCalories in descending order and select top 10 workout types.

### Final output: 

Print a DataFrame with columns: 
|WorkoutType | TotalSessions | AvgDuration | TotalCalories | HighIntensityCount | AvgBurnRate|
|------------|---------------|-------------|---------------|--------------------|------------|
|            |               |             |               |                    |            |


Round AvgDuration, TotalCalories, and AvgBurnRate to 2 decimal places.
