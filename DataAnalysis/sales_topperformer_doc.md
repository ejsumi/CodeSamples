# Sales Manager Team Performance with Top Performer Scenario

## Business Question
**Analyze quarterly sales performance by aggregating individual salesperson transactions to show each Sales Manager's team performance — including total revenue, average deal size, team size, and the single top-performing salesperson on each team — sorted by total revenue.**

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

### Aggregated Sales by Manager Table, with Top Performer

| Column Name | Calculation Method | Description |
|-------------|-------------------|-------------|
| sales_manager | GROUP BY, first-appearance order | Name of the Sales Manager |
| region | FIRST | Primary region managed |
| team_size | COUNT DISTINCT | Number of unique salespeople under this manager |
| total_transactions | COUNT | Total number of sales transactions |
| total_revenue | SUM | Total sales amount across all transactions |
| average_deal_size | AVG | Average sale amount per transaction |
| top_performer | MAX BY | Salesperson with the highest individual sales within the team |
| top_performer_sales | SUM | Total sales by the top performer |

---

## Analysis Requirements

1. **Aggregation Level 1**: Group all transactions by `sales_manager` to compute team-level metrics (region, team size, transactions, revenue, average deal size)
2. **Aggregation Level 2**: Group transactions by `sales_manager` and `salesperson_name` to compute each individual's total sales
3. **Identify Top Performer**: Within each manager's group, sort individuals by total sales descending and take the top row
4. **Combine**: Merge the manager-level summary with each manager's top performer
5. **Row Labels**: Keep `sales_manager` in first-appearance order from the source file; sort all other columns' values by `total_revenue` descending

---

## Business Use Cases

This aggregated view helps answer:
- Which Sales Manager's team is generating the most revenue?
- Who is the standout individual performer within each team?
- How does team size and average deal size vary across top-revenue teams?
