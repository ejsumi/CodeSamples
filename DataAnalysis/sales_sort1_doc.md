# Sales Manager Ranking Scenario

## Business Question
**Rank Sales Managers by total revenue, while preserving each manager's first-appearance order from the source file as the row label, so the leaderboard can be cross-referenced back to the original transaction log.**

---

## Input Data Structure

### Sales Transactions Table
**Dataset file:** `sales_analysis.csv`

Each row represents a single sale transaction with the following columns:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| transaction_id | Integer | Unique identifier for each sale |
| salesperson_name | String | Name of the salesperson who made the sale |
| sales_manager | String | Name of the manager overseeing this salesperson |
| region | String | Geographic region (North, South, East, West) |
| sale_amount | Decimal | Revenue generated from the sale (in USD) |
| sale_date | Date (DD-MM-YYYY) | Date when the sale was completed |
| product_category | String | Category of product sold |

### Sample Input Data (First 2 rows)

| transaction_id | salesperson_name | sales_manager | region | sale_amount | sale_date | product_category |
|----------------|------------------|---------------|--------|-------------|-----------|------------------|
| 1001 | Alice Johnson | Sarah Williams | North | 24,567 | 15-01-2024 | Software |
| 1002 | David Lee | Michael Chen | South | 18,234 | 08-01-2024 | Hardware |

---

## Expected Output Structure

| Column Name | Calculation Method | Description |
|-------------|-------------------|-------------|
| sales_manager | GROUP BY, first-appearance order | Name of the Sales Manager, listed in original file order |
| total_sales | SUM, sorted descending | Total sales amount for that manager, formatted as currency |

---

## Analysis Requirements

1. **Aggregation Level**: Group all transactions by `sales_manager` and sum `sale_amount`
2. **Sorting for Values**: Sort the summed totals descending
3. **Row Labels**: Keep `sales_manager` in the order each manager first appears in the file — do not sort the labels themselves
4. **Combine**: Map the sorted totals onto the first-appearance-ordered manager list
5. **Formatting**: Display `total_sales` as currency with `$` and comma separators

---

## Business Use Cases

This view helps answer:
- What is each manager's total revenue, at a glance, without re-sorting the leaderboard every time the file is re-read?
- How do the ranked totals compare against the order managers appear in operational reports?
