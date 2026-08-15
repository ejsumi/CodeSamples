# Electronics Sales Analysis Scenario

## Business Question
**Analyze 2023 electronics sales in the South, West, and North regions by cleaning transaction-level data, deriving a value band per sale, and aggregating results by quarter and product category to show total quantity sold, total sales, transaction volume, and high-value transaction counts.**

---

## Input Data Structure

### Electronics Sales Table
**Dataset file:** `electronics_sales.csv`

Each row represents a single electronics sale transaction with the following columns:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| InvoiceID | String | Unique identifier for each sale invoice |
| SaleDate | Date (DD-MM-YYYY) | Date the sale occurred |
| CustomerID | String | Unique identifier for the customer |
| Region | String | Geographic region (East, West, North, South, Central) |
| ProductCategory | String | Category of electronics sold (TVs, Smartphones, Speakers, Gaming Consoles, etc.) |
| Quantity | Integer | Number of units sold |
| UnitPrice | Decimal | List price per unit (in USD) |
| DiscountPercent | Integer | Discount applied to the sale (0–100) |
| TotalAmount | Decimal | Recorded total for the invoice (pre-discount reference value) |

### Sample Input Data (First 5 rows)

| InvoiceID | SaleDate | CustomerID | Region | ProductCategory | Quantity | UnitPrice | DiscountPercent | TotalAmount |
|-----------|----------|-----------|--------|------------------|----------|-----------|-----------------|-------------|
| INV00001 | 15-12-2023 | CUST6390 | East | TVs | 7 | 1782.08 | 0 | 12474.56 |
| INV00002 | 10-04-2023 | CUST9322 | Central | Smartphones | 6 | 300.93 | 20 | 1805.58 |
| INV00003 | 10-11-2023 | CUST7396 | West | Speakers | 10 | 132.67 | 20 | 1326.70 |
| INV00004 | 24-06-2023 | CUST4005 | East | Gaming Consoles | 5 | 313.94 | 5 | 1569.70 |
| INV00005 | 16-06-2023 | CUST6393 | West | Speakers | 4 | 369.79 | 0 | 1479.16 |

---

## Expected Output Structure

### Aggregated Sales by Quarter and Product Category

| Column Name | Calculation Method | Description |
|-------------|-------------------|-------------|
| Quarter | GROUP BY | Calendar quarter of the sale (Q1–Q4) |
| ProductCategory | GROUP BY | Category of electronics sold |
| TotalQuantity | SUM | Total units sold in the group |
| TotalSales | SUM | Total computed sales value in the group |
| NumTransactions | COUNT | Total number of transactions in the group |
| HighValueTran | COUNT WHERE | Number of transactions classified as `High Value` |

---

## Analysis Requirements

1. **Cleanup**: Drop `InvoiceID` and `CustomerID` (not needed for aggregation); keep only rows with `Quantity > 0`
2. **Derived Fields**:
   - `NetUnitPrice` = unit price adjusted for discount
   - `ComputedTotal` = `Quantity` × `NetUnitPrice`
   - `ValueBand` = `High Value` (≥ 1500), `Medium Value` (500–1500), `Low Value` (< 500), based on `ComputedTotal`
3. **Time Fields**: Parse `SaleDate` and derive `Quarter` and `Year`
4. **Filtering**: Restrict to `Year == 2023` and `Region` in South, West, North
5. **Aggregation Level**: Group by `Quarter` and `ProductCategory`
6. **Sorting**: Order results by `Quarter` descending, then `TotalSales` descending

---

## Business Use Cases

This aggregated view helps answer:
- Which product categories drive the most revenue each quarter?
- How many high-value transactions occur per category?
- Are certain regions and quarters underperforming in unit volume vs. revenue?
