# Car Sales Data Analysis - Practice Questions

## Dataset Information

**Dataset Name:** `car_sales.csv`

**Total Rows:** 475

**Columns:**
- `SaleID`: Unique sale identifier
- `VIN`: Vehicle Identification Number
- `Make`: Car manufacturer (Toyota, Honda, Ford, BMW, Tesla, etc.)
- `Model`: Car model name
- `SaleDate`: Date of sale (MM-DD-YYYY)
- `SalePrice`: Sale price of the vehicle
- `DealerFee`: Additional dealer fees
- `SalespersonID`: ID of the salesperson
- `Location`: Dealership location (city)
- `PaymentMethod`: Payment type (Cash, Finance, Lease)

---

## Question 1: Location-Based Sales Analysis

**Objective:** Analyze car sales performance across different dealership locations for 2023.

### Tasks:

1. **Drop unnecessary columns:** Remove `SaleID`, `VIN`, and `SalespersonID`.

2. **Create a new column:** Compute a new column `TotalRevenue` = `SalePrice + DealerFee`.

3. **Filter condition:** Keep only transactions from the year 2023.

4. **Create a conditional field:** Add a new column `SaleType`:
   - `"Premium Sale"` if `SalePrice >= 45000`
   - `"Standard Sale"` otherwise.

5. **Aggregation and sorting:**
   - Group the dataset by `Location`.
   - Compute:
     - `TotalSales` = count of sales
     - `TotalRevenue` = sum of `TotalRevenue`
     - `PremiumSales` = count of `"Premium Sale"` transactions
     - `AvgSalePrice` = mean of `SalePrice`
   - Sort the results in descending order of `TotalRevenue` and select the top 10 locations.

6. **Final dataset:** Print a DataFrame with the following 6 columns:
   - `Location`
   - `TotalSales`
   - `TotalRevenue`
   - `PremiumSales`
   - `AvgSalePrice`
   - `RevenuePerSale` = `TotalRevenue / TotalSales`

---

## Question 2: Brand Performance Analysis Across Years

**Objective:** Analyze car brand performance trends over multiple years, focusing on financed and leased vehicles.

### Tasks:

1. **Drop unnecessary columns:** Remove `SaleID`, `VIN`, `Model`, and `SalespersonID`.

2. **Extract year from date:** Create a new column `SaleYear` by extracting the year from `SaleDate`.

3. **Create a new column:** Compute a new column `NetProfit` = `DealerFee * 0.6` (assuming 60% of dealer fee is profit).

4. **Filter condition:** Keep only sales where `PaymentMethod` is either `"Finance"` or `"Lease"`.

5. **Create multiple conditional fields:**
   - Add a column `PriceRange`:
     - `"Economy"` if `SalePrice < 30000`
     - `"Mid-Range"` if `30000 <= SalePrice < 50000`
     - `"Luxury"` if `SalePrice >= 50000`
   - Add a column `TimeOfYear`:
     - `"Q1"` if month is 1-3
     - `"Q2"` if month is 4-6
     - `"Q3"` if month is 7-9
     - `"Q4"` if month is 10-12

6. **Aggregation and sorting:**
   - Group the dataset by `Make` and `SaleYear`.
   - Compute:
     - `UnitsSold` = count of sales
     - `TotalRevenue` = sum of `SalePrice`
     - `TotalProfit` = sum of `NetProfit`
     - `LuxuryCount` = count of `"Luxury"` price range sales
     - `FinanceCount` = count of sales where `PaymentMethod` is `"Finance"`
   - Sort the results first by `SaleYear` (ascending), then by `TotalRevenue` (descending).
   - Select the top 15 combinations.

7. **Final dataset:** Print a DataFrame with the following 7 columns:
   - `Make`
   - `SaleYear`
   - `UnitsSold`
   - `TotalRevenue`
   - `TotalProfit`
   - `LuxuryCount`
   - `AvgRevenuePerUnit` = `TotalRevenue / UnitsSold`

---
