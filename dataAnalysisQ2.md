#  Question: Quarterly Sales & Performance Analysis

---
You are given a DataFrame **`electronics_sales`** containing transactional sales data for an electronics retailer. Using pandas, perform the following tasks and print the final output.
Columns:
InvoiceID, SaleDate, CustomerID, Region, ProductCategory, Quantity, UnitPrice, DiscountPercent, TotalAmount


## **Tasks**

### 1. Create new computed fields

Add the following new columns:

 - NetUnitPrice = UnitPrice * (1 - DiscountPercent/100)

 - ComputedTotal = Quantity * NetUnitPrice

* **ValueBand**
  Assign each transaction a value label:
   Based on ComputedTotal:

   - “High Value” if ComputedTotal >= 1500

   - “Medium Value” if 500 <= ComputedTotal < 1500

   - “Low Value” if ComputedTotal < 500

* **Quarter** 
  Create a new column to capture the Quarter as Q1, Q2, Q3 and Q4
---

### 2. Apply filtering

Filter the dataset so that it includes only:

* Transactions belonging to the year **2023**
* Rows where **Quantity > 0**
* Only records from the regions: **South, West, and North**

---

### 3. Group the data

Group the filtered data by **Quarter** and **ProductCategory**.
For each group, calculate:

* **TotalQuantity** – total units sold
* **TotalSales** – sum of ComputedTotal
* **NumTransactions** – number of records in the group
* **HighValueOrders** – count of rows labeled as “High Value”

---

### 4. Sorting

Sort the grouped results:

1. First by **Quarter** in ascending order
2. Then by **TotalSales** in descending order within each quarter

---

### 5. Final Output Format

Print a DataFrame that contains **only** these columns in the order below:

1. **Quarter**
2. **ProductCategory**
3. **TotalQuantity**
4. **TotalSales** (rounded to 2 decimals)
5. **NumTransactions**
6. **HighValueOrders**

---
