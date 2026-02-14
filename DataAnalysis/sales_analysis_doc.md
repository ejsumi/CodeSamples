# Sales Performance Analysis Scenario

## Business Question
**Analyze quarterly sales performance by aggregating individual salesperson transactions to show each Sales Manager's team performance, including total revenue, average deal size, number of transactions, and team size.**

---

## Input Data Structure

### Sales Transactions Table
Each row represents a single sale transaction with the following columns:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| transaction_id | Integer | Unique identifier for each sale |
| salesperson_name | String | Name of the salesperson who made the sale |
| sales_manager | String | Name of the manager overseeing this salesperson |
| region | String | Geographic region (North, South, East, West) |
| sale_amount | Decimal | Revenue generated from the sale (in USD) |
| sale_date | Date | Date when the sale was completed |
| product_category | String | Category of product sold |

### Sample Input Data (First 10 rows)

| transaction_id | salesperson_name | sales_manager | region | sale_amount | sale_date | product_category |
|----------------|------------------|---------------|--------|-------------|-----------|------------------|
| 1001 | Alice Johnson | Sarah Williams | North | 12,500 | 2024-01-15 | Software |
| 1002 | Alice Johnson | Sarah Williams | North | 8,300 | 2024-01-22 | Hardware |
| 1003 | Bob Smith | Sarah Williams | North | 15,700 | 2024-01-18 | Software |
| 1004 | Carol Davis | Sarah Williams | North | 9,200 | 2024-02-05 | Services |
| 1005 | David Lee | Michael Chen | South | 22,000 | 2024-01-20 | Enterprise |
| 1006 | David Lee | Michael Chen | South | 18,500 | 2024-02-14 | Enterprise |
| 1007 | Emma Wilson | Michael Chen | South | 11,200 | 2024-01-25 | Software |
| 1008 | Frank Martinez | Michael Chen | South | 14,800 | 2024-02-10 | Hardware |
| 1009 | Grace Taylor | Robert Brown | East | 10,500 | 2024-01-12 | Services |
| 1010 | Henry Anderson | Robert Brown | East | 16,900 | 2024-01-28 | Software |

---

## Expected Output Structure

### Aggregated Sales by Manager Table

The output should aggregate all transactions to the Sales Manager level with these columns:

| Column Name | Calculation Method | Description |
|-------------|-------------------|-------------|
| sales_manager | GROUP BY | Name of the Sales Manager |
| region | FIRST or MODE | Primary region managed |
| team_size | COUNT DISTINCT | Number of unique salespeople under this manager |
| total_transactions | COUNT | Total number of sales transactions |
| total_revenue | SUM | Total sales amount across all transactions |
| average_deal_size | AVG | Average sale amount per transaction |
| top_performer | MAX BY | Salesperson with highest individual sales |
| top_performer_sales | SUM | Total sales by the top performer |

### Sample Expected Output

| sales_manager | region | team_size | total_transactions | total_revenue | average_deal_size | top_performer | top_performer_sales |
|---------------|--------|-----------|-------------------|---------------|-------------------|---------------|-------------------|
| Sarah Williams | North | 3 | 24 | $315,400 | $13,142 | Bob Smith | $127,600 |
| Michael Chen | South | 3 | 28 | $428,700 | $15,311 | David Lee | $165,200 |
| Robert Brown | East | 3 | 22 | $287,900 | $13,086 | Henry Anderson | $108,300 |
| Jennifer Lopez | West | 3 | 26 | $392,100 | $15,081 | Karen White | $145,800 |

---

## Analysis Requirements

1. **Aggregation Level**: Group all individual sales transactions by Sales Manager
2. **Time Period**: Q1 2024 (January - March)
3. **Metrics to Calculate**:
   - Sum of all sales amounts per manager
   - Count of unique salespeople per manager
   - Count of total transactions per manager
   - Average transaction value per manager
   - Identify top performing salesperson within each team
4. **Sorting**: Order results by total_revenue descending
5. **Formatting**: Currency values should be displayed with $ and comma separators

---

## Business Use Cases

This aggregated view helps answer:
- Which Sales Manager's team is generating the most revenue?
- Which teams have the highest average deal sizes?
- How does team size correlate with overall performance?
- Who are the top individual performers within each team?
- Which regions are performing best overall?