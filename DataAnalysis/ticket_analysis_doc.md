# Customer Support Performance Analysis Scenario

## Business Question
**Analyze customer support ticket resolution performance by aggregating individual agent tickets to show each Team Lead's group performance, including total tickets resolved, average resolution time, customer satisfaction scores, and agent productivity metrics.**

---

## Input Data Structure

### Support Tickets Table
Each row represents a single support ticket with the following columns:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| ticket_id | Integer | Unique identifier for each support ticket |
| support_agent | String | Name of the agent who handled the ticket |
| team_lead | String | Name of the team lead supervising this agent |
| department | String | Support department (Technical, Billing, General, Product) |
| resolution_time_hours | Decimal | Time taken to resolve ticket (in hours) |
| ticket_date | Date | Date when ticket was created |
| priority_level | String | Urgency level (Low, Medium, High, Critical) |
| customer_satisfaction | Integer | Customer rating 1-5 (5 being highest) |
| ticket_category | String | Type of issue (Bug, Question, Feature Request, Complaint) |

### Sample Input Data (First 10 rows)

| ticket_id | support_agent | team_lead | department | resolution_time_hours | ticket_date | priority_level | customer_satisfaction | ticket_category |
|-----------|---------------|-----------|------------|---------------------|-------------|----------------|---------------------|-----------------|
| T1001 | Sarah Chen | Amanda Rodriguez | Technical | 3.5 | 2024-01-05 | High | 5 | Bug |
| T1002 | Sarah Chen | Amanda Rodriguez | Technical | 2.2 | 2024-01-08 | Medium | 4 | Question |
| T1003 | Mike Johnson | Amanda Rodriguez | Technical | 5.8 | 2024-01-12 | Critical | 3 | Bug |
| T1004 | Lisa Park | Amanda Rodriguez | Technical | 1.5 | 2024-01-15 | Low | 5 | Question |
| T1005 | David Kumar | Brian Foster | Billing | 4.2 | 2024-01-07 | Medium | 4 | Complaint |
| T1006 | David Kumar | Brian Foster | Billing | 2.8 | 2024-01-10 | High | 5 | Question |
| T1007 | Emily Watson | Brian Foster | Billing | 6.5 | 2024-01-14 | Critical | 2 | Complaint |
| T1008 | Carlos Martinez | Brian Foster | Billing | 3.1 | 2024-01-18 | Medium | 4 | Question |
| T1009 | Jennifer Lee | Claire Thompson | General | 1.8 | 2024-01-06 | Low | 5 | Question |
| T1010 | Jennifer Lee | Claire Thompson | General | 4.5 | 2024-01-11 | High | 4 | Feature Request |

---

## Expected Output Structure

### Aggregated Support Metrics by Team Lead

The output should aggregate all tickets to the Team Lead level with these columns:

| Column Name | Calculation Method | Description |
|-------------|-------------------|-------------|
| team_lead | GROUP BY | Name of the Team Lead |
| department | FIRST or MODE | Primary department managed |
| team_size | COUNT DISTINCT | Number of unique support agents under this lead |
| total_tickets_resolved | COUNT | Total number of tickets handled |
| avg_resolution_time | AVG | Average resolution time in hours |
| avg_satisfaction_score | AVG | Average customer satisfaction rating |
| critical_tickets_handled | COUNT WHERE | Number of critical priority tickets |
| top_performer | MAX BY | Agent with most tickets resolved |
| top_performer_tickets | COUNT | Total tickets resolved by top performer |
| satisfaction_rate_4plus | PERCENTAGE | Percentage of tickets rated 4 or 5 |

### Sample Expected Output

| team_lead | department | team_size | total_tickets_resolved | avg_resolution_time | avg_satisfaction_score | critical_tickets_handled | top_performer | top_performer_tickets | satisfaction_rate_4plus |
|-----------|------------|-----------|----------------------|-------------------|----------------------|------------------------|---------------|---------------------|----------------------|
| Amanda Rodriguez | Technical | 3 | 62 | 3.8 | 4.2 | 18 | Sarah Chen | 25 | 78.4% |
| Brian Foster | Billing | 3 | 58 | 4.1 | 3.9 | 15 | David Kumar | 22 | 72.1% |
| Claire Thompson | General | 3 | 54 | 2.9 | 4.5 | 8 | Jennifer Lee | 21 | 87.0% |
| Daniel Park | Product | 3 | 48 | 5.2 | 3.7 | 12 | Rachel Green | 19 | 68.8% |

---

## Analysis Requirements

1. **Aggregation Level**: Group all individual support tickets by Team Lead
2. **Time Period**: Q1 2024 (January - March)
3. **Metrics to Calculate**:
   - Average resolution time across all tickets per team lead
   - Average customer satisfaction score per team lead
   - Count of critical priority tickets per team lead
   - Percentage of tickets with satisfaction score of 4 or higher
   - Identify the most productive agent (most tickets resolved) within each team
4. **Filtering**: Exclude any tickets still open or unresolved
5. **Sorting**: Order results by avg_satisfaction_score descending
6. **Formatting**: 
   - Times should be displayed in hours with 1 decimal place
   - Satisfaction scores with 1 decimal place
   - Percentages with 1 decimal place

---

## Business Use Cases

This aggregated view helps answer:
- Which Team Lead's group has the highest customer satisfaction?
- Which teams are resolving tickets fastest vs slowest?
- How does handling critical tickets impact overall satisfaction scores?
- Who are the top performing agents within each team?
- Which departments need additional training or resources?
- How does team size correlate with resolution efficiency?

---

## Additional Analysis Questions

Once you have the aggregated data, you can explore:
1. **Trend Analysis**: How does performance change month-over-month?
2. **Priority Distribution**: Which teams handle more critical vs low priority tickets?
3. **Category Analysis**: Which ticket categories take longest to resolve?
4. **Satisfaction Drivers**: What factors most influence customer satisfaction ratings?
5. **Resource Allocation**: Should agents be redistributed between teams?